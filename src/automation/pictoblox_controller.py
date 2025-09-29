"""
PictoBlox Controller - Automation interface for PictoBlox desktop application
"""

import time
import subprocess
import pyautogui
import pygetwindow as gw
from typing import Optional, Tuple, Dict, Any, List
from dataclasses import dataclass
from pathlib import Path
import json

# Configure pyautogui for safety
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.1


@dataclass
class BlockPosition:
    """Represents a block's position and connection points"""
    x: int
    y: int
    width: int = 100
    height: int = 30
    
    @property
    def center(self) -> Tuple[int, int]:
        return (self.x + self.width // 2, self.y + self.height // 2)
    
    @property
    def top_connection(self) -> Tuple[int, int]:
        return (self.x + self.width // 2, self.y)
    
    @property
    def bottom_connection(self) -> Tuple[int, int]:
        return (self.x + self.width // 2, self.y + self.height)


class PictoBloxNotFoundError(Exception):
    """Raised when PictoBlox application cannot be found or controlled"""
    pass


class BlockPlacementError(Exception):
    """Raised when block placement or connection fails"""
    pass


class PictoBloxController:
    """Main controller for PictoBlox automation"""
    
    def __init__(self, pictoblox_path: Optional[str] = None):
        self.pictoblox_path = pictoblox_path
        self.window = None
        self.workspace_bounds = None
        self.block_palette_bounds = None
        self.placed_blocks: List[BlockPosition] = []
        
        # Load UI element templates for image recognition
        self.ui_templates = self._load_ui_templates()
    
    def _load_ui_templates(self) -> Dict[str, str]:
        """Load UI element templates for image recognition"""
        templates_dir = Path(__file__).parent / "ui_templates"
        templates = {}
        
        if templates_dir.exists():
            for template_file in templates_dir.glob("*.png"):
                templates[template_file.stem] = str(template_file)
        
        return templates
    
    def launch_pictoblox(self) -> bool:
        """Launch PictoBlox application and wait for it to be ready"""
        try:
            if self.pictoblox_path:
                subprocess.Popen([self.pictoblox_path])
            else:
                # Try common installation paths
                common_paths = [
                    r"C:\Program Files\PictoBlox\PictoBlox.exe",
                    r"C:\Program Files (x86)\PictoBlox\PictoBlox.exe",
                    r"C:\Users\{}\AppData\Local\PictoBlox\PictoBlox.exe".format(os.getenv('USERNAME'))
                ]
                
                for path in common_paths:
                    if Path(path).exists():
                        subprocess.Popen([path])
                        break
                else:
                    raise PictoBloxNotFoundError("PictoBlox executable not found")
            
            # Wait for PictoBlox to start
            time.sleep(3)
            return self.connect_to_pictoblox()
            
        except Exception as e:
            raise PictoBloxNotFoundError(f"Failed to launch PictoBlox: {e}")
    
    def connect_to_pictoblox(self) -> bool:
        """Connect to running PictoBlox window"""
        try:
            # Find PictoBlox window
            windows = gw.getWindowsWithTitle("PictoBlox")
            if not windows:
                # Try alternative window titles
                alt_titles = ["PictoBlox", "Scratch", "Block Programming"]
                for title in alt_titles:
                    windows = [w for w in gw.getAllWindows() if title.lower() in w.title.lower()]
                    if windows:
                        break
            
            if not windows:
                raise PictoBloxNotFoundError("PictoBlox window not found")
            
            self.window = windows[0]
            self.window.activate()
            time.sleep(1)
            
            # Detect workspace and palette areas
            self._detect_ui_areas()
            
            return True
            
        except Exception as e:
            raise PictoBloxNotFoundError(f"Failed to connect to PictoBlox: {e}")
    
    def _detect_ui_areas(self):
        """Detect workspace and block palette areas"""
        if not self.window:
            return
        
        # Get window bounds
        win_left, win_top = self.window.left, self.window.top
        win_width, win_height = self.window.width, self.window.height
        
        # Estimate areas based on typical PictoBlox layout
        # Block palette is typically on the left side
        palette_width = int(win_width * 0.25)  # ~25% of window width
        
        self.block_palette_bounds = {
            'left': win_left,
            'top': win_top + 100,  # Account for title bar and menu
            'width': palette_width,
            'height': win_height - 200
        }
        
        # Workspace is the main central area
        self.workspace_bounds = {
            'left': win_left + palette_width,
            'top': win_top + 100,
            'width': win_width - palette_width - 200,  # Leave space for sprite area
            'height': win_height - 200
        }
    
    def find_block_in_palette(self, block_name: str) -> Optional[Tuple[int, int]]:
        """Find a block in the block palette using image recognition"""
        if block_name in self.ui_templates:
            template_path = self.ui_templates[block_name]
            
            # Search within block palette area
            search_area = (
                self.block_palette_bounds['left'],
                self.block_palette_bounds['top'],
                self.block_palette_bounds['width'],
                self.block_palette_bounds['height']
            )
            
            try:
                location = pyautogui.locateOnScreen(template_path, region=search_area, confidence=0.8)
                if location:
                    return pyautogui.center(location)
            except pyautogui.ImageNotFoundException:
                pass
        
        return None
    
    def place_block(self, block_name: str, position: Optional[Tuple[int, int]] = None) -> BlockPosition:
        """Place a block from palette to workspace"""
        if not self.window:
            raise PictoBloxNotFoundError("Not connected to PictoBlox")
        
        # Find block in palette
        block_location = self.find_block_in_palette(block_name)
        if not block_location:
            raise BlockPlacementError(f"Block '{block_name}' not found in palette")
        
        # Calculate target position in workspace
        if position is None:
            # Auto-position: place below last block or at top-left of workspace
            if self.placed_blocks:
                last_block = self.placed_blocks[-1]
                target_x = last_block.x
                target_y = last_block.y + last_block.height + 10
            else:
                target_x = self.workspace_bounds['left'] + 50
                target_y = self.workspace_bounds['top'] + 50
        else:
            target_x, target_y = position
        
        # Drag block from palette to workspace
        try:
            pyautogui.drag(
                block_location[0], block_location[1],
                target_x, target_y,
                duration=0.5
            )
            
            # Create block position record
            block_pos = BlockPosition(target_x, target_y)
            self.placed_blocks.append(block_pos)
            
            time.sleep(0.5)  # Wait for block to settle
            return block_pos
            
        except Exception as e:
            raise BlockPlacementError(f"Failed to place block '{block_name}': {e}")
    
    def connect_blocks(self, source_block: BlockPosition, target_block: BlockPosition) -> bool:
        """Connect two blocks together"""
        try:
            # Drag from source bottom connection to target top connection
            pyautogui.drag(
                source_block.bottom_connection[0], source_block.bottom_connection[1],
                target_block.top_connection[0], target_block.top_connection[1],
                duration=0.3
            )
            
            time.sleep(0.3)
            return True
            
        except Exception as e:
            raise BlockPlacementError(f"Failed to connect blocks: {e}")
    
    def set_block_parameter(self, block: BlockPosition, parameter_name: str, value: Any) -> bool:
        """Set a parameter value for a block"""
        try:
            # Click on the block to select it
            pyautogui.click(block.center[0], block.center[1])
            time.sleep(0.2)
            
            # Look for parameter input field (this would need specific UI recognition)
            # For now, we'll use a simple approach of clicking and typing
            
            # Double-click to select parameter field
            pyautogui.doubleClick(block.center[0] + 30, block.center[1])  # Offset for parameter area
            time.sleep(0.1)
            
            # Type the new value
            pyautogui.typewrite(str(value))
            pyautogui.press('enter')
            
            return True
            
        except Exception as e:
            raise BlockPlacementError(f"Failed to set parameter '{parameter_name}' to '{value}': {e}")
    
    def create_simple_program(self, blocks_data: List[Dict[str, Any]]) -> bool:
        """Create a simple program from block data"""
        try:
            placed_blocks = []
            
            for i, block_data in enumerate(blocks_data):
                block_name = block_data.get('opcode', 'unknown')
                
                # Place the block
                block_pos = self.place_block(block_name)
                placed_blocks.append(block_pos)
                
                # Set parameters if any
                if 'inputs' in block_data and block_data['inputs']:
                    for param_name, param_value in block_data['inputs'].items():
                        self.set_block_parameter(block_pos, param_name, param_value)
                
                # Connect to previous block (except for the first block)
                if i > 0:
                    self.connect_blocks(placed_blocks[i-1], block_pos)
            
            return True
            
        except Exception as e:
            print(f"Failed to create program: {e}")
            return False
    
    def get_status(self) -> Dict[str, Any]:
        """Get current status of PictoBlox connection and automation"""
        return {
            'connected': self.window is not None,
            'window_title': self.window.title if self.window else None,
            'blocks_placed': len(self.placed_blocks),
            'workspace_detected': self.workspace_bounds is not None,
            'palette_detected': self.block_palette_bounds is not None
        }


# Example usage and testing
if __name__ == "__main__":
    controller = PictoBloxController()
    
    try:
        print("Connecting to PictoBlox...")
        if controller.connect_to_pictoblox():
            print("✓ Connected successfully")
            print("Status:", controller.get_status())
            
            # Example: Create a simple "move 10 steps" program
            program_blocks = [
                {
                    'opcode': 'event_whenflagclicked',
                    'category': 'events'
                },
                {
                    'opcode': 'motion_movesteps',
                    'category': 'motion',
                    'inputs': {'STEPS': 10}
                }
            ]
            
            print("Creating simple program...")
            if controller.create_simple_program(program_blocks):
                print("✓ Program created successfully")
            else:
                print("✗ Failed to create program")
        else:
            print("✗ Failed to connect to PictoBlox")
            
    except Exception as e:
        print(f"Error: {e}")
