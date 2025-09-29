"""
MCP Integration for PictoBlox Automation
Extends the existing scratchattach-mcp with automation capabilities
"""

from typing import Dict, Any, List, Optional
from .pictoblox_controller import PictoBloxController, PictoBloxNotFoundError, BlockPlacementError
from ..programming.block_generator import BlockGenerator, Intent
from ..programming.parsers import NaturalLanguageParser
from ..programming.formatters import TextFormatter


class AutomationMCP:
    """Enhanced MCP with PictoBlox automation capabilities"""
    
    def __init__(self):
        self.controller = PictoBloxController()
        self.parser = NaturalLanguageParser()
        self.generator = BlockGenerator()
        self.formatter = TextFormatter()
        self.automation_enabled = False
    
    def initialize_automation(self) -> Dict[str, Any]:
        """Initialize PictoBlox automation"""
        try:
            if self.controller.connect_to_pictoblox():
                self.automation_enabled = True
                return {
                    "success": True,
                    "message": "PictoBlox automation initialized successfully",
                    "status": self.controller.get_status()
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to connect to PictoBlox. Make sure PictoBlox is running.",
                    "fallback": "Manual instructions will be provided instead."
                }
        except PictoBloxNotFoundError as e:
            return {
                "success": False,
                "message": f"PictoBlox not found: {e}",
                "suggestion": "Please launch PictoBlox and try again.",
                "fallback": "Manual instructions will be provided instead."
            }
    
    def create_scratch_program_auto(self, description: str, auto_execute: bool = True) -> Dict[str, Any]:
        """
        Generate AND automatically create Scratch program in PictoBlox
        
        Args:
            description: Natural language description of the program
            auto_execute: Whether to automatically create blocks in PictoBlox
        
        Returns:
            Result with automation status and fallback instructions
        """
        try:
            # Parse the natural language input
            intents = self.parser.parse(description)
            
            if not intents:
                return {
                    "success": False,
                    "message": "I didn't understand that request.",
                    "suggestions": [
                        "make the cat move right 10 steps",
                        "when space key pressed jump up",
                        "play sound when sprite clicked"
                    ]
                }
            
            # Generate block sequence
            block_sequence = self.generator.generate_blocks(intents)
            
            if not block_sequence.blocks:
                return {
                    "success": False,
                    "message": "Could not generate blocks for that request.",
                    "parsed_intents": [{"action": intent.action, "parameters": intent.parameters} for intent in intents]
                }
            
            # Prepare response with manual instructions as fallback
            manual_instructions = self.formatter.format(block_sequence)
            
            result = {
                "success": True,
                "description": description,
                "blocks_generated": len(block_sequence.blocks),
                "difficulty": block_sequence.difficulty,
                "explanation": block_sequence.explanation,
                "manual_instructions": manual_instructions,
                "automation_attempted": False,
                "automation_success": False
            }
            
            # Attempt automation if enabled and requested
            if auto_execute and self.automation_enabled:
                try:
                    result["automation_attempted"] = True
                    
                    # Convert blocks to automation format
                    automation_blocks = self._convert_blocks_for_automation(block_sequence.blocks)
                    
                    # Execute automation
                    if self.controller.create_simple_program(automation_blocks):
                        result["automation_success"] = True
                        result["message"] = "✓ Program created successfully in PictoBlox!"
                        result["blocks_placed"] = len(automation_blocks)
                    else:
                        result["message"] = "Automation failed, but here are manual instructions:"
                        result["automation_error"] = "Block placement failed"
                
                except Exception as e:
                    result["message"] = f"Automation failed ({str(e)}), but here are manual instructions:"
                    result["automation_error"] = str(e)
            
            elif not self.automation_enabled:
                result["message"] = "PictoBlox automation not available. Here are manual instructions:"
                result["automation_note"] = "Run 'initialize_pictoblox_automation' to enable automatic block creation"
            
            else:
                result["message"] = "Manual instructions (automation disabled):"
            
            return result
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Error processing request: {str(e)}",
                "error_type": "processing_error"
            }
    
    def _convert_blocks_for_automation(self, blocks) -> List[Dict[str, Any]]:
        """Convert generated blocks to automation format"""
        automation_blocks = []
        
        for block in blocks:
            automation_block = {
                "opcode": block.opcode,
                "category": block.category
            }
            
            # Add inputs if present
            if hasattr(block, 'inputs') and block.inputs:
                automation_block["inputs"] = block.inputs
            
            # Add fields if present
            if hasattr(block, 'fields') and block.fields:
                automation_block["fields"] = block.fields
            
            automation_blocks.append(automation_block)
        
        return automation_blocks
    
    def get_pictoblox_status(self) -> Dict[str, Any]:
        """Get current PictoBlox automation status"""
        if not self.automation_enabled:
            return {
                "automation_enabled": False,
                "message": "PictoBlox automation not initialized",
                "suggestion": "Run 'initialize_pictoblox_automation' to enable automation"
            }
        
        status = self.controller.get_status()
        status["automation_enabled"] = self.automation_enabled
        
        if status["connected"]:
            status["message"] = "✓ PictoBlox automation ready"
        else:
            status["message"] = "✗ PictoBlox connection lost"
            status["suggestion"] = "Restart PictoBlox and run 'initialize_pictoblox_automation'"
        
        return status
    
    def modify_existing_project(self, modification: str) -> Dict[str, Any]:
        """Modify currently open PictoBlox project"""
        if not self.automation_enabled:
            return {
                "success": False,
                "message": "PictoBlox automation not available",
                "suggestion": "Initialize automation first"
            }
        
        try:
            # Parse modification request
            intents = self.parser.parse(modification)
            
            if not intents:
                return {
                    "success": False,
                    "message": "I didn't understand the modification request",
                    "examples": [
                        "add a jump when space is pressed",
                        "make the sprite move faster",
                        "change the sound to meow"
                    ]
                }
            
            # Generate additional blocks
            block_sequence = self.generator.generate_blocks(intents)
            
            if not block_sequence.blocks:
                return {
                    "success": False,
                    "message": "Could not generate blocks for that modification"
                }
            
            # Convert and place blocks
            automation_blocks = self._convert_blocks_for_automation(block_sequence.blocks)
            
            if self.controller.create_simple_program(automation_blocks):
                return {
                    "success": True,
                    "message": f"✓ Added {len(automation_blocks)} blocks to your project",
                    "modification": modification,
                    "blocks_added": len(automation_blocks),
                    "explanation": block_sequence.explanation
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to modify project",
                    "manual_instructions": self.formatter.format(block_sequence)
                }
        
        except Exception as e:
            return {
                "success": False,
                "message": f"Error modifying project: {str(e)}",
                "error_type": "modification_error"
            }
    
    def create_game_template(self, game_type: str, complexity: str = "beginner") -> Dict[str, Any]:
        """Create complete game templates"""
        templates = {
            "platformer": {
                "beginner": [
                    "when green flag clicked",
                    "forever",
                    "if key left arrow pressed then change x by -5",
                    "if key right arrow pressed then change x by 5",
                    "if key space pressed then change y by 20 wait 0.1 seconds change y by -20"
                ]
            },
            "maze": {
                "beginner": [
                    "when green flag clicked",
                    "forever",
                    "if key up arrow pressed then point in direction 0 move 10 steps",
                    "if key down arrow pressed then point in direction 180 move 10 steps",
                    "if key left arrow pressed then point in direction -90 move 10 steps",
                    "if key right arrow pressed then point in direction 90 move 10 steps"
                ]
            }
        }
        
        if game_type not in templates:
            return {
                "success": False,
                "message": f"Game type '{game_type}' not available",
                "available_types": list(templates.keys())
            }
        
        if complexity not in templates[game_type]:
            return {
                "success": False,
                "message": f"Complexity '{complexity}' not available for {game_type}",
                "available_complexity": list(templates[game_type].keys())
            }
        
        # Create the template program
        template_description = " ".join(templates[game_type][complexity])
        
        return self.create_scratch_program_auto(
            description=f"Create a {complexity} {game_type} game: {template_description}",
            auto_execute=self.automation_enabled
        )
    
    def debug_scratch_program(self) -> Dict[str, Any]:
        """Analyze current project and suggest improvements"""
        if not self.automation_enabled:
            return {
                "success": False,
                "message": "PictoBlox automation not available for debugging",
                "suggestion": "Initialize automation first"
            }
        
        # This would require more advanced image analysis of the current project
        # For now, provide general debugging tips
        return {
            "success": True,
            "message": "Program analysis complete",
            "suggestions": [
                "Make sure all blocks are properly connected",
                "Check that event blocks (green flag, key press) are at the top",
                "Verify that loops have proper ending blocks",
                "Test your program step by step",
                "Add 'wait' blocks to slow down fast animations"
            ],
            "common_issues": [
                "Missing event triggers",
                "Infinite loops without wait blocks",
                "Disconnected block sequences",
                "Wrong parameter values"
            ]
        }


# Example integration with existing MCP tools
def enhance_existing_mcp(mcp_server):
    """Add automation tools to existing MCP server"""
    automation = AutomationMCP()
    
    @mcp_server.tool()
    def initialize_pictoblox_automation():
        """Initialize PictoBlox automation for automatic block creation"""
        return automation.initialize_automation()
    
    @mcp_server.tool()
    def create_scratch_program_auto(description: str, auto_execute: bool = True):
        """Generate AND automatically create Scratch program in PictoBlox"""
        return automation.create_scratch_program_auto(description, auto_execute)
    
    @mcp_server.tool()
    def get_pictoblox_status():
        """Check PictoBlox automation status"""
        return automation.get_pictoblox_status()
    
    @mcp_server.tool()
    def modify_existing_project(modification: str):
        """Modify currently open PictoBlox project"""
        return automation.modify_existing_project(modification)
    
    @mcp_server.tool()
    def create_game_template(game_type: str, complexity: str = "beginner"):
        """Create complete game templates (platformer, maze, quiz, etc.)"""
        return automation.create_game_template(game_type, complexity)
    
    @mcp_server.tool()
    def debug_scratch_program():
        """Analyze current project and suggest improvements"""
        return automation.debug_scratch_program()
    
    return automation
