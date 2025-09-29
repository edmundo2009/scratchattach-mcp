# Product Requirements Document: Scratch Automation MCP

## Executive Summary

Build an enhanced version of scratchattach-mcp that can directly control PictoBlox (desktop Scratch-compatible software) to automatically create, modify, and execute Scratch programs based on natural language instructions.

## Vision Statement

Transform natural language descriptions into fully functional Scratch programs by combining our existing educational MCP with direct PictoBlox automation, creating a seamless "describe-to-code" experience for visual programming education.

## Current State Analysis

### ✅ What We Have (scratchattach-mcp v1.0)
- Natural language parsing to programming intents
- Comprehensive Scratch block knowledge base
- Block generation logic with proper parameters
- Educational explanations and concept teaching
- Multiple output formats (text, pictoblox, blocks)
- MCP server architecture working with rovodev CLI

### ❌ What's Missing
- Direct application control/automation
- Real-time project manipulation
- Visual feedback and verification
- Error handling for automation failures
- Project file management

## Product Goals

### Primary Goals
1. **Seamless Automation**: "Make the cat jump when space is pressed" → Automatically creates the blocks in PictoBlox
2. **Educational Enhancement**: Maintain teaching aspects while adding practical implementation
3. **Error Recovery**: Handle automation failures gracefully with fallback instructions
4. **Project Management**: Create, save, and manage PictoBlox projects programmatically

### Secondary Goals
1. **Advanced Patterns**: Support complex programming patterns (games, animations, interactions)
2. **Debugging Support**: Help identify and fix issues in existing projects
3. **Code Review**: Analyze existing PictoBlox projects and suggest improvements
4. **Template System**: Pre-built project templates for common use cases

## Technical Architecture

### Core Components

#### 1. Enhanced MCP Server (`scratchattach-mcp-auto`)
```
scratchattach-mcp-auto/
├── src/
│   ├── automation/          # NEW: PictoBlox automation
│   │   ├── pictoblox_controller.py
│   │   ├── block_placer.py
│   │   ├── project_manager.py
│   │   └── error_handler.py
│   ├── programming/         # EXISTING: Enhanced
│   │   ├── block_generator.py
│   │   ├── parsers.py
│   │   ├── formatters.py
│   │   └── pattern_engine.py  # NEW: Advanced patterns
│   ├── knowledge/           # EXISTING: Expanded
│   │   ├── scratch_blocks.json
│   │   ├── patterns.json
│   │   ├── pictoblox_mapping.json  # NEW
│   │   └── project_templates.json  # NEW
│   └── main.py             # EXISTING: Enhanced with automation
```

#### 2. PictoBlox Integration Layer
- **Application Control**: Launch, focus, and manage PictoBlox windows
- **UI Automation**: Interact with PictoBlox interface elements
- **Block Placement**: Drag, drop, and connect blocks programmatically
- **Project Operations**: New, open, save, export projects

#### 3. Enhanced Block Generation
- **Spatial Awareness**: Calculate block positions and connections
- **Dependency Resolution**: Ensure proper block ordering and nesting
- **Visual Layout**: Organize blocks for readability
- **Validation**: Verify created programs match intent

## Implementation Strategy

### Phase 1: Foundation (Weeks 1-2)
**Goal**: Basic PictoBlox automation capability

#### Deliverables:
1. **PictoBlox Controller**
   - Launch and detect PictoBlox application
   - Basic window management and focus control
   - Screenshot capture for verification

2. **Simple Block Placement**
   - Place individual blocks in workspace
   - Basic drag-and-drop automation
   - Connect two blocks together

3. **Enhanced MCP Tools**
   ```python
   @mcp.tool()
   def create_scratch_program_auto(description: str, auto_execute: bool = True):
       """Generate AND automatically create Scratch program in PictoBlox"""
   
   @mcp.tool()
   def get_pictoblox_status():
       """Check if PictoBlox is running and ready for automation"""
   ```

#### Technical Requirements:
- **Windows Automation**: Use `pyautogui`, `pygetwindow`, or `win32gui`
- **Image Recognition**: Template matching for UI elements
- **Error Handling**: Graceful fallback to instruction mode

### Phase 2: Advanced Automation (Weeks 3-4)
**Goal**: Complex program creation and management

#### Deliverables:
1. **Advanced Block Placement**
   - Handle nested structures (loops, conditionals)
   - Manage block parameters and dropdowns
   - Create complex block arrangements

2. **Project Management**
   - Create new projects with templates
   - Save and load projects programmatically
   - Export projects in various formats

3. **Pattern Implementation**
   - Game creation patterns (platformer, maze, etc.)
   - Animation sequences
   - Interactive story templates

#### Enhanced MCP Tools:
```python
@mcp.tool()
def create_game_template(game_type: str, complexity: str = "beginner"):
    """Create complete game templates (platformer, maze, quiz, etc.)"""

@mcp.tool()
def modify_existing_project(modification: str):
    """Modify currently open PictoBlox project"""

@mcp.tool()
def debug_scratch_program():
    """Analyze current project and suggest improvements"""
```

### Phase 3: Intelligence & Polish (Weeks 5-6)
**Goal**: Smart automation with error recovery

#### Deliverables:
1. **Smart Error Recovery**
   - Detect automation failures
   - Retry with different strategies
   - Fallback to manual instructions

2. **Visual Verification**
   - Screenshot analysis to verify block placement
   - Compare intended vs. actual program structure
   - Automatic correction of placement errors

3. **Advanced Features**
   - Multi-sprite project support
   - Custom block creation
   - Asset management (sounds, images)

## Technical Implementation Details

### PictoBlox Automation Approach

#### Option 1: UI Automation (Recommended)
```python
class PictoBloxController:
    def __init__(self):
        self.app = None
        self.window = None
        
    def launch_pictoblox(self):
        """Launch PictoBlox and wait for ready state"""
        
    def place_block(self, block_type: str, position: tuple):
        """Place a specific block at given coordinates"""
        
    def connect_blocks(self, source_block, target_block):
        """Connect two blocks together"""
        
    def set_block_parameter(self, block, parameter, value):
        """Set parameter value for a block"""
```

#### Option 2: PictoBlox API Integration (If Available)
- Research PictoBlox's extension/plugin system
- Direct API calls instead of UI automation
- More reliable but requires PictoBlox API documentation

### Block Mapping System
```json
{
  "motion_movesteps": {
    "pictoblox_location": {"category": "Motion", "position": 1},
    "ui_identifier": "move_steps_block.png",
    "parameters": {
      "STEPS": {"type": "number", "ui_element": "input_field"}
    },
    "connection_points": {
      "top": {"type": "hat", "offset": [0, -5]},
      "bottom": {"type": "stack", "offset": [0, 25]}
    }
  }
}
```

### Error Handling Strategy
```python
class AutomationError(Exception):
    """Base class for automation errors"""
    
class PictoBloxNotFoundError(AutomationError):
    """PictoBlox application not running"""
    
class BlockPlacementError(AutomationError):
    """Failed to place or connect blocks"""

def with_fallback(automation_func):
    """Decorator to provide manual instruction fallback"""
    def wrapper(*args, **kwargs):
        try:
            return automation_func(*args, **kwargs)
        except AutomationError as e:
            return generate_manual_instructions(*args, **kwargs)
    return wrapper
```

## Success Metrics

### Functional Metrics
- **Automation Success Rate**: >90% for basic programs, >75% for complex programs
- **Block Placement Accuracy**: >95% correct placement and connections
- **Error Recovery Rate**: >80% successful fallback to manual instructions

### User Experience Metrics
- **Time to Program**: <30 seconds for simple programs, <2 minutes for complex
- **User Satisfaction**: Maintain educational value while adding automation
- **Error Clarity**: Clear error messages and recovery suggestions

### Technical Metrics
- **Response Time**: <5 seconds for automation initiation
- **Resource Usage**: <100MB additional memory, <10% CPU during automation
- **Reliability**: <1% crash rate, graceful degradation on failures

## Risk Assessment & Mitigation

### High Risk
1. **PictoBlox UI Changes**: Updates could break automation
   - *Mitigation*: Version detection, multiple UI recognition methods
   
2. **Platform Compatibility**: Windows/Mac/Linux differences
   - *Mitigation*: Platform-specific automation modules

### Medium Risk
1. **Performance Issues**: Automation might be slow
   - *Mitigation*: Optimize image recognition, parallel operations
   
2. **Complex Program Failures**: Advanced patterns might fail
   - *Mitigation*: Incremental complexity, robust fallback system

### Low Risk
1. **User Adoption**: Users might prefer manual control
   - *Mitigation*: Make automation optional, maintain educational focus

## Future Enhancements (Post-MVP)

### Advanced Features
- **Multi-Application Support**: Scratch 3.0, mBlock, other visual programming tools
- **AI-Powered Debugging**: Analyze program behavior and suggest optimizations
- **Collaborative Features**: Share and modify projects through MCP
- **Voice Control**: "Hey Scratch, make the cat jump higher"

### Integration Opportunities
- **GitHub Integration**: Version control for Scratch projects
- **Educational Platforms**: Integration with classroom management systems
- **Assessment Tools**: Automatic grading of programming assignments

## Implementation Roadmap

### Immediate Next Steps (Week 1)
1. **Research PictoBlox**
   - Download and install PictoBlox
   - Analyze UI structure and automation possibilities
   - Test basic pyautogui interactions

2. **Create Proof of Concept**
   - Simple block placement automation
   - Basic "move cat left" automation demo
   - Integration with existing MCP structure

3. **Architecture Setup**
   - Create automation module structure
   - Design PictoBlox controller interface
   - Plan error handling strategy

### Development Priorities
1. **Core Automation** (Highest Priority)
   - PictoBlox detection and control
   - Basic block placement
   - Simple program creation

2. **Enhanced Integration** (High Priority)
   - Seamless MCP tool integration
   - Error handling and fallbacks
   - User feedback and status reporting

3. **Advanced Features** (Medium Priority)
   - Complex pattern support
   - Project management
   - Visual verification

## Conclusion

This PRD outlines a clear path to transform the existing scratchattach-mcp from an educational assistant into a powerful automation tool. By leveraging PictoBlox's desktop nature, we can create a seamless "natural language to working program" experience while maintaining the educational value that makes the current MCP valuable.

The phased approach ensures we build incrementally, validate each component, and maintain backward compatibility with the existing educational features. The result will be a unique tool that bridges the gap between natural language programming instruction and actual program creation.

**Key Success Factors:**
- Build on existing solid foundation
- Maintain educational value
- Provide reliable fallback options
- Focus on user experience and error recovery
- Incremental complexity with thorough testing
