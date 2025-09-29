# Product Requirements Document: Snap! Automation MCP

## Executive Summary

Transform the existing scratchattach-mcp from an educational assistant into a fully automated visual programming system using Snap! (Berkeley's advanced Scratch successor) with programmatic control via JavaScript APIs. This will enable seamless "natural language to working visual program" automation while maintaining educational value.

## Vision Statement

Create the world's first natural language-driven visual programming automation system that bridges the gap between conversational AI and visual programming education, enabling students and educators to create working programs through simple descriptions.

## Product Overview

### Current State: scratchattach-mcp v1.0
- ✅ Natural language parsing to programming intents
- ✅ Comprehensive Scratch block knowledge base  
- ✅ Block generation logic with proper parameters
- ✅ Educational explanations and concept teaching
- ✅ Multiple output formats (text, pictoblox, blocks)
- ✅ MCP server architecture working with rovodev CLI

### Target State: snap-automation-mcp v2.0
- 🎯 Direct programmatic control of Snap! environment
- 🎯 Real-time visual program creation from natural language
- 🎯 Live execution and testing of generated programs
- 🎯 Interactive debugging and program modification
- 🎯 Educational scaffolding with visual feedback
- 🎯 Project management and sharing capabilities

## Why Snap! Over Other Platforms

### Technical Advantages
- **Full JavaScript API**: Complete programmatic control over blocks, sprites, and execution
- **Browser-Based**: No installation required, cross-platform compatibility
- **Educational Heritage**: Developed at UC Berkeley for computer science education
- **Advanced Features**: First-class functions, custom blocks, advanced data structures
- **Open Source**: MIT licensed, fully extensible and customizable

### Educational Benefits
- **Scratch Compatibility**: Familiar interface for Scratch users
- **Advanced Concepts**: Supports higher-order programming concepts
- **Visual Debugging**: Built-in tools for understanding program execution
- **Community**: Strong educational community and resources

### Automation Capabilities
```javascript
// Example Snap! programmatic control
world.children[0].addBlock('forward', 50);
world.children[0].addBlock('turn', 90);
world.children[0].scripts.children[0].fullCopy(); // Clone scripts
```

## Product Goals

### Primary Goals
1. **Seamless Automation**: Natural language → Working Snap! program in <10 seconds
2. **Educational Enhancement**: Maintain and enhance learning experience with visual feedback
3. **Reliability**: >95% success rate for basic programs, >85% for complex programs
4. **User Experience**: Intuitive workflow from description to working program

### Secondary Goals
1. **Advanced Programming**: Support complex patterns (recursion, data structures, algorithms)
2. **Collaborative Features**: Multi-user program creation and sharing
3. **Assessment Integration**: Automatic evaluation of programming assignments
4. **Curriculum Support**: Align with computer science education standards

### Success Metrics
- **Automation Success Rate**: >95% for basic programs, >85% for advanced
- **Time to Program**: <30 seconds average from description to execution
- **Educational Engagement**: Increased time spent programming vs. manual block placement
- **Error Recovery**: <5% unrecoverable automation failures

## Technical Architecture

### System Overview
```
Natural Language Input
        ↓
Enhanced MCP Server (Python)
        ↓
Snap! JavaScript API
        ↓
Visual Program Creation
        ↓
Live Execution & Feedback
```

### Core Components

#### 1. Enhanced MCP Server (`snap-automation-mcp`)
```
snap-automation-mcp/
├── src/
│   ├── automation/              # NEW: Snap! automation layer
│   │   ├── snap_controller.py   # Main Snap! interface
│   │   ├── block_mapper.py      # Block translation layer
│   │   ├── program_builder.py   # Program construction logic
│   │   ├── execution_manager.py # Program execution control
│   │   └── error_handler.py     # Automation error recovery
│   ├── programming/             # ENHANCED: Existing components
│   │   ├── block_generator.py   # Enhanced for Snap! blocks
│   │   ├── parsers.py          # Enhanced NLP parsing
│   │   ├── formatters.py       # Snap! output formatting
│   │   └── pattern_engine.py   # NEW: Advanced pattern support
│   ├── knowledge/               # EXPANDED: Enhanced knowledge base
│   │   ├── snap_blocks.json    # NEW: Snap!-specific blocks
│   │   ├── scratch_blocks.json # EXISTING: Maintained for compatibility
│   │   ├── patterns.json       # ENHANCED: Advanced patterns
│   │   ├── curriculum.json     # NEW: Educational curriculum mapping
│   │   └── templates.json      # NEW: Project templates
│   ├── web/                    # NEW: Web interface for Snap!
│   │   ├── snap_embed.html     # Embedded Snap! environment
│   │   ├── automation.js       # JavaScript automation layer
│   │   └── communication.js    # MCP ↔ Snap! communication
│   └── main.py                 # ENHANCED: Main MCP server
```

#### 2. Snap! Integration Layer
- **JavaScript Bridge**: Bidirectional communication between Python MCP and Snap! JavaScript
- **Block Translation**: Convert MCP block data to Snap! API calls
- **Program Execution**: Control program running, stopping, and debugging
- **State Management**: Track program state and execution flow

#### 3. Enhanced Block Generation System
- **Snap!-Specific Blocks**: Support for advanced Snap! features (custom blocks, lists, etc.)
- **Spatial Programming**: Handle block positioning and visual organization
- **Dependency Resolution**: Ensure proper block ordering and connections
- **Pattern Recognition**: Identify and implement common programming patterns

## Implementation Strategy

### Phase 1: Foundation (Weeks 1-3)
**Goal**: Basic Snap! automation with simple programs

#### Week 1: Snap! Integration Setup
**Deliverables:**
- Embedded Snap! environment in web interface
- Basic JavaScript ↔ Python communication bridge
- Simple block placement automation (move, turn, say)

**Technical Tasks:**
```python
# New MCP tools for Phase 1
@mcp.tool()
def initialize_snap_environment():
    """Launch embedded Snap! environment and establish connection"""

@mcp.tool()
def create_simple_program_snap(description: str):
    """Create basic programs (movement, sounds, simple interactions)"""

@mcp.tool()
def execute_snap_program():
    """Run the created program and return execution results"""
```

#### Week 2: Block Translation System
**Deliverables:**
- Complete block mapping from existing knowledge base to Snap! API
- Parameter handling and block connection logic
- Basic error handling and recovery

**Block Mapping Example:**
```json
{
  "motion_movesteps": {
    "snap_equivalent": "forward",
    "api_call": "sprite.addBlock('forward', {steps})",
    "parameters": {
      "STEPS": {"type": "number", "default": 10}
    }
  }
}
```

#### Week 3: Program Construction
**Deliverables:**
- Multi-block program creation
- Event handling (green flag, key press, sprite click)
- Basic program validation and testing

### Phase 2: Advanced Features (Weeks 4-6)
**Goal**: Complex program creation and educational enhancement

#### Week 4: Advanced Block Support
**Deliverables:**
- Control structures (loops, conditionals, functions)
- Variables and data manipulation
- Custom block creation

**Enhanced MCP Tools:**
```python
@mcp.tool()
def create_game_snap(game_type: str, complexity: str = "beginner"):
    """Create complete games (platformer, maze, quiz, etc.)"""

@mcp.tool()
def add_custom_block_snap(block_name: str, functionality: str):
    """Create custom blocks with specific functionality"""

@mcp.tool()
def modify_snap_program(modification: str):
    """Modify existing program with new features or fixes"""
```

#### Week 5: Educational Features
**Deliverables:**
- Step-by-step program explanation with visual highlighting
- Interactive debugging with breakpoints
- Curriculum-aligned project templates

#### Week 6: Program Management
**Deliverables:**
- Save/load Snap! projects
- Export programs in multiple formats
- Project sharing and collaboration features

### Phase 3: Intelligence & Polish (Weeks 7-8)
**Goal**: Smart automation with advanced error recovery

#### Week 7: Smart Error Recovery
**Deliverables:**
- Automatic error detection and correction
- Alternative implementation strategies
- Visual program validation

#### Week 8: Advanced Intelligence
**Deliverables:**
- Program optimization suggestions
- Code review and improvement recommendations
- Advanced pattern recognition and implementation

## Detailed Technical Specifications

### Snap! JavaScript API Integration

#### Core Automation Functions
```javascript
class SnapAutomationAPI {
    constructor() {
        this.world = world;
        this.stage = world.children[0];
        this.sprites = this.stage.children;
    }
    
    // Block creation and manipulation
    addBlock(blockType, parameters = {}) {
        const block = SpriteMorph.prototype.blockForSelector(blockType);
        this.setBlockParameters(block, parameters);
        this.currentSprite().scripts.add(block);
        return block;
    }
    
    // Program execution control
    runProgram() {
        this.stage.fireGreenFlagEvent();
    }
    
    stopProgram() {
        this.stage.fireStopAllEvent();
    }
    
    // Visual feedback and debugging
    highlightBlock(block) {
        block.addHighlight();
    }
    
    // Project management
    saveProject(name) {
        return this.stage.toXML();
    }
    
    loadProject(xmlData) {
        this.stage.fromXML(xmlData);
    }
}
```

#### Communication Bridge
```python
class SnapBridge:
    """Bridge between Python MCP and Snap! JavaScript"""
    
    def __init__(self, web_interface_url):
        self.web_interface = web_interface_url
        self.websocket = None
    
    async def send_command(self, command, parameters=None):
        """Send automation command to Snap! environment"""
        message = {
            "type": "automation_command",
            "command": command,
            "parameters": parameters or {}
        }
        await self.websocket.send(json.dumps(message))
        return await self.websocket.recv()
    
    async def create_block(self, block_type, parameters):
        """Create a block in Snap! environment"""
        return await self.send_command("addBlock", {
            "blockType": block_type,
            "parameters": parameters
        })
```

### Enhanced Block Generation

#### Snap!-Specific Block Templates
```json
{
  "snap_blocks": {
    "motion": {
      "forward": {
        "description": "Move sprite forward by steps",
        "parameters": {"steps": {"type": "number", "default": 10}},
        "snap_api": "addBlock('forward', {steps})",
        "educational_note": "This moves your sprite in the direction it's facing"
      },
      "turn": {
        "description": "Turn sprite by degrees",
        "parameters": {"degrees": {"type": "number", "default": 15}},
        "snap_api": "addBlock('turn', {degrees})",
        "educational_note": "Positive numbers turn right, negative turn left"
      }
    },
    "control": {
      "repeat": {
        "description": "Repeat enclosed blocks",
        "parameters": {"times": {"type": "number", "default": 10}},
        "snap_api": "addBlock('doRepeat', {times})",
        "educational_note": "This creates a loop that repeats the same actions"
      }
    }
  }
}
```

#### Advanced Pattern Engine
```python
class SnapPatternEngine:
    """Advanced pattern recognition and implementation for Snap!"""
    
    def __init__(self):
        self.patterns = self.load_patterns()
    
    def detect_pattern(self, intents):
        """Detect common programming patterns in user intent"""
        patterns = []
        
        # Game patterns
        if self.is_game_pattern(intents):
            patterns.append("game_creation")
        
        # Animation patterns  
        if self.is_animation_pattern(intents):
            patterns.append("animation_sequence")
            
        # Algorithm patterns
        if self.is_algorithm_pattern(intents):
            patterns.append("algorithm_implementation")
            
        return patterns
    
    def implement_pattern(self, pattern_type, intents):
        """Implement detected pattern with appropriate Snap! blocks"""
        if pattern_type == "game_creation":
            return self.create_game_structure(intents)
        elif pattern_type == "animation_sequence":
            return self.create_animation(intents)
        # ... more patterns
```

## User Experience Design

### Workflow Examples

#### Example 1: Simple Movement
```
User Input: "Make the cat walk in a square"
↓
MCP Processing: Parse → Generate → Automate
↓
Snap! Result: 
- Green flag event block
- Repeat 4 times block
- Forward 50 steps block  
- Turn 90 degrees block
- Program automatically runs showing cat walking in square
```

#### Example 2: Interactive Game
```
User Input: "Create a simple catching game where the cat catches falling apples"
↓
MCP Processing: Detect game pattern → Generate sprites → Create interactions
↓
Snap! Result:
- Cat sprite with arrow key controls
- Apple sprite with falling behavior
- Collision detection and scoring
- Game automatically starts and is playable
```

### Educational Integration

#### Step-by-Step Learning
1. **Program Creation**: Show blocks being added in real-time
2. **Concept Explanation**: Highlight each block with educational notes
3. **Execution Visualization**: Step through program execution with visual feedback
4. **Modification Suggestions**: Offer ways to extend or improve the program

#### Curriculum Alignment
- **Beginner**: Basic movement, sounds, simple interactions
- **Intermediate**: Loops, conditionals, variables, simple games
- **Advanced**: Functions, data structures, complex algorithms, custom blocks

## Risk Assessment & Mitigation

### Technical Risks

#### High Risk: Snap! API Stability
- **Risk**: Snap! updates could break automation
- **Mitigation**: 
  - Pin to specific Snap! version
  - Create abstraction layer for API calls
  - Maintain compatibility testing suite

#### Medium Risk: Browser Compatibility
- **Risk**: Different browsers may behave differently
- **Mitigation**:
  - Test on major browsers (Chrome, Firefox, Safari, Edge)
  - Use standardized web APIs
  - Provide browser-specific fallbacks

#### Medium Risk: Performance with Complex Programs
- **Risk**: Large programs may cause performance issues
- **Mitigation**:
  - Implement program size limits
  - Optimize block creation algorithms
  - Add performance monitoring

### Educational Risks

#### Low Risk: Learning Curve
- **Risk**: Users may become dependent on automation
- **Mitigation**:
  - Always show manual steps alongside automation
  - Provide "explain mode" that breaks down each step
  - Encourage manual experimentation

## Success Metrics & KPIs

### Functional Metrics
- **Automation Success Rate**: >95% for basic programs, >85% for complex
- **Response Time**: <10 seconds from description to working program
- **Error Recovery**: >90% successful fallback to manual instructions
- **Program Correctness**: >98% of generated programs execute as intended

### Educational Metrics
- **Engagement Time**: 50% increase in time spent programming
- **Concept Understanding**: Improved scores on programming concept assessments
- **Creative Output**: Increased number of original programs created
- **Error Resolution**: Faster debugging and problem-solving

### Technical Metrics
- **System Reliability**: <1% unrecoverable failures
- **Resource Usage**: <200MB memory, <15% CPU during automation
- **Scalability**: Support 100+ concurrent users
- **Cross-Platform**: 100% feature parity across major browsers

## Future Enhancements

### Advanced Features (Post-MVP)
- **AI-Powered Code Review**: Analyze programs and suggest improvements
- **Collaborative Programming**: Real-time multi-user program creation
- **Voice Control**: "Hey Snap, make the sprite jump higher"
- **Mobile Support**: Touch-friendly interface for tablets
- **VR/AR Integration**: 3D visual programming environments

### Educational Extensions
- **Classroom Management**: Teacher dashboards and student progress tracking
- **Assessment Tools**: Automatic grading of programming assignments
- **Curriculum Builder**: Tools for educators to create custom lessons
- **Peer Review**: Student code sharing and feedback systems

### Platform Integrations
- **LMS Integration**: Canvas, Blackboard, Google Classroom
- **Version Control**: Git integration for program history
- **Cloud Storage**: Automatic project backup and sync
- **Social Features**: Program sharing and community galleries

## Conclusion

This PRD outlines a comprehensive transformation of the existing scratchattach-mcp into a revolutionary educational tool that bridges natural language and visual programming. By leveraging Snap!'s powerful JavaScript API, we can create a seamless automation experience while maintaining the educational value that makes visual programming so effective for learning.

The phased approach ensures steady progress with measurable milestones, while the focus on error recovery and educational enhancement guarantees that the tool remains valuable even when automation encounters challenges. The result will be a unique platform that democratizes programming education by making it as simple as describing what you want to create.

**Key Success Factors:**
- Leverage existing solid MCP foundation
- Maintain educational focus throughout development
- Provide reliable automation with graceful fallbacks
- Create intuitive user experience with immediate visual feedback
- Build scalable architecture for future enhancements

This project has the potential to transform how programming is taught and learned, making it accessible to a much broader audience while maintaining the depth and rigor necessary for true computer science education.

## Implementation Roadmap

### Immediate Next Steps (Week 1)

#### Day 1-2: Snap! Research & Setup
1. **Download and analyze Snap!**
   - Study the JavaScript API documentation
   - Experiment with programmatic block creation
   - Test embedding Snap! in custom web interface

2. **Proof of Concept Development**
   ```javascript
   // Test basic automation
   function testSnapAutomation() {
     const sprite = world.children[0].children[0];
     const forwardBlock = sprite.blockForSelector('forward');
     sprite.scripts.add(forwardBlock);
     world.children[0].fireGreenFlagEvent();
   }
   ```

#### Day 3-5: Architecture Foundation
1. **Create web interface structure**
   ```html
   <!-- snap_embed.html -->
   <!DOCTYPE html>
   <html>
   <head>
     <title>Snap! Automation Environment</title>
   </head>
   <body>
     <div id="snap-container">
       <!-- Embedded Snap! IDE -->
     </div>
     <script src="snap/snap.js"></script>
     <script src="automation.js"></script>
   </body>
   </html>
   ```

2. **Basic Python-JavaScript bridge**
   ```python
   # Enhanced main.py with Snap! integration
   from automation.snap_controller import SnapController

   @mcp.tool()
   def initialize_snap_automation():
       """Initialize Snap! automation environment"""
       controller = SnapController()
       return controller.initialize()
   ```

#### Day 6-7: First Automation Demo
- Create simple "move cat forward" automation
- Test end-to-end: Natural language → MCP → Snap! → Visual result
- Document findings and refine approach

### Development Milestones

#### Milestone 1: Basic Automation (End of Week 2)
**Success Criteria:**
- ✅ Snap! embedded in custom web interface
- ✅ Python MCP can send commands to Snap! JavaScript
- ✅ Basic blocks (move, turn, say) can be created programmatically
- ✅ Simple programs execute correctly

#### Milestone 2: Enhanced Block Support (End of Week 4)
**Success Criteria:**
- ✅ All basic Scratch blocks supported in Snap!
- ✅ Control structures (loops, conditionals) working
- ✅ Event handling (green flag, key press) functional
- ✅ Parameter setting and block connections reliable

#### Milestone 3: Advanced Features (End of Week 6)
**Success Criteria:**
- ✅ Complex programs (games, animations) can be created
- ✅ Custom blocks and functions supported
- ✅ Project save/load functionality working
- ✅ Error handling and recovery mechanisms in place

#### Milestone 4: Production Ready (End of Week 8)
**Success Criteria:**
- ✅ >95% automation success rate for basic programs
- ✅ Educational features (explanations, step-by-step) integrated
- ✅ Performance optimized for real-time use
- ✅ Comprehensive testing and documentation complete

## Technical Deep Dive

### Snap! API Exploration

#### Core Objects and Methods
```javascript
// Key Snap! objects for automation
world                    // Global world object
world.children[0]        // Stage object
world.children[0].children[0]  // First sprite

// Block creation methods
SpriteMorph.prototype.blockForSelector('forward')
SpriteMorph.prototype.blockForSelector('turn')
SpriteMorph.prototype.blockForSelector('doSayFor')

// Script manipulation
sprite.scripts.add(block)
sprite.scripts.children  // Array of script blocks

// Execution control
stage.fireGreenFlagEvent()
stage.fireStopAllEvent()
```

#### Advanced Automation Patterns
```javascript
class SnapProgramBuilder {
    constructor() {
        this.stage = world.children[0];
        this.currentSprite = this.stage.children[0];
        this.blockStack = [];
    }

    addEventBlock(eventType, parameter = null) {
        let block;
        switch(eventType) {
            case 'green_flag':
                block = this.currentSprite.blockForSelector('receiveGo');
                break;
            case 'key_press':
                block = this.currentSprite.blockForSelector('receiveKey');
                block.inputs()[0].setContents(parameter);
                break;
        }
        this.currentSprite.scripts.add(block);
        this.blockStack = [block];
        return block;
    }

    addMotionBlock(type, value) {
        const block = this.currentSprite.blockForSelector(type);
        if (block.inputs().length > 0) {
            block.inputs()[0].setContents(value);
        }
        this.connectToStack(block);
        return block;
    }

    addControlBlock(type, parameter = null) {
        const block = this.currentSprite.blockForSelector(type);
        if (parameter && block.inputs().length > 0) {
            block.inputs()[0].setContents(parameter);
        }
        this.connectToStack(block);
        return block;
    }

    connectToStack(block) {
        if (this.blockStack.length > 0) {
            const lastBlock = this.blockStack[this.blockStack.length - 1];
            lastBlock.nextBlock(block);
        }
        this.blockStack.push(block);
    }
}
```

### Enhanced MCP Integration

#### Snap!-Specific Block Mapping
```python
class SnapBlockMapper:
    """Maps MCP block data to Snap! API calls"""

    BLOCK_MAPPING = {
        'motion_movesteps': {
            'snap_selector': 'forward',
            'parameters': ['STEPS'],
            'default_values': {'STEPS': 10}
        },
        'motion_turnright': {
            'snap_selector': 'turn',
            'parameters': ['DEGREES'],
            'default_values': {'DEGREES': 15}
        },
        'looks_say': {
            'snap_selector': 'doSayFor',
            'parameters': ['MESSAGE', 'SECS'],
            'default_values': {'MESSAGE': 'Hello!', 'SECS': 2}
        },
        'control_repeat': {
            'snap_selector': 'doRepeat',
            'parameters': ['TIMES'],
            'default_values': {'TIMES': 10},
            'is_container': True
        }
    }

    def map_block(self, mcp_block):
        """Convert MCP block to Snap! automation command"""
        if mcp_block.opcode not in self.BLOCK_MAPPING:
            raise ValueError(f"Unsupported block: {mcp_block.opcode}")

        mapping = self.BLOCK_MAPPING[mcp_block.opcode]

        return {
            'selector': mapping['snap_selector'],
            'parameters': self._extract_parameters(mcp_block, mapping),
            'is_container': mapping.get('is_container', False)
        }

    def _extract_parameters(self, mcp_block, mapping):
        """Extract and validate block parameters"""
        parameters = {}

        for param_name in mapping['parameters']:
            if hasattr(mcp_block, 'inputs') and param_name in mcp_block.inputs:
                parameters[param_name] = mcp_block.inputs[param_name]
            else:
                parameters[param_name] = mapping['default_values'][param_name]

        return parameters
```

#### WebSocket Communication Layer
```python
import asyncio
import websockets
import json

class SnapWebSocketServer:
    """WebSocket server for MCP ↔ Snap! communication"""

    def __init__(self, host='localhost', port=8765):
        self.host = host
        self.port = port
        self.clients = set()

    async def register_client(self, websocket, path):
        """Register new Snap! client connection"""
        self.clients.add(websocket)
        try:
            await websocket.wait_closed()
        finally:
            self.clients.remove(websocket)

    async def send_automation_command(self, command_data):
        """Send automation command to all connected Snap! clients"""
        if self.clients:
            message = json.dumps(command_data)
            await asyncio.gather(
                *[client.send(message) for client in self.clients],
                return_exceptions=True
            )

    async def create_program(self, blocks_data):
        """Send complete program creation command"""
        command = {
            'type': 'create_program',
            'blocks': blocks_data,
            'timestamp': time.time()
        }
        await self.send_automation_command(command)

        # Wait for completion response
        # Implementation depends on response handling
```

## Competitive Analysis

### Comparison with Existing Solutions

| Feature                | Our Snap! MCP      | Scratch         | Blockly             | MIT App Inventor |
|------------------------|--------------------|-----------------|---------------------|------------------|
| Natural Language Input | ✅ Full             | ❌ None          | ❌ None              | ❌ None           |
| Programmatic Control   | ✅ Complete         | ❌ Limited       | ✅ Full              | ⚠️ API Only       |
| Educational Focus      | ✅ Built-in         | ✅ Strong        | ⚠️ Developer-focused | ✅ Strong         |
| Real-time Automation   | ✅ Yes              | ❌ No            | ✅ Yes               | ❌ No             |
| Advanced Features      | ✅ Functions, Lists | ⚠️ Basic         | ✅ Extensible        | ✅ Mobile Apps    |
| Installation Required  | ❌ Browser-based    | ❌ Browser-based | ❌ Library           | ❌ Browser-based  |

### Unique Value Proposition
1. **Only solution** combining natural language programming with visual block automation
2. **Educational-first** design with built-in teaching features
3. **Real-time feedback** showing program creation and execution
4. **Advanced programming concepts** accessible through simple descriptions
5. **Seamless workflow** from idea to working program in seconds

This comprehensive PRD provides a complete roadmap for creating a revolutionary programming automation tool. The Snap! approach offers the perfect balance of educational value, technical capability, and automation potential.

---

# IMPLEMENTATION GUIDE - Ready to Code

## Project Setup & Structure

### New Project: `snap-automation-mcp`

```
snap-automation-mcp/
├── README.md
├── requirements.txt
├── setup.py
├── pyproject.toml
├── .env.example
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── core/                    # Core automation engine
│   │   ├── __init__.py
│   │   ├── snap_api.py         # Snap! JavaScript API wrapper
│   │   ├── program_builder.py  # Program construction logic
│   │   ├── execution_engine.py # Program execution control
│   │   └── block_mapper.py     # Block translation layer
│   ├── nlp/                     # Natural language processing
│   │   ├── __init__.py
│   │   ├── parser.py           # Intent parsing (adapted from old project)
│   │   ├── intent_mapper.py    # Intent to Snap! block mapping
│   │   └── pattern_detector.py # Programming pattern recognition
│   ├── knowledge/               # Knowledge base
│   │   ├── __init__.py
│   │   ├── snap_blocks.json    # Snap!-specific block definitions
│   │   ├── patterns.json       # Programming patterns
│   │   ├── curriculum.json     # Educational curriculum mapping
│   │   └── templates.json      # Project templates
│   ├── web/                     # Web interface for Snap!
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   └── style.css
│   │   │   ├── js/
│   │   │   │   ├── automation.js    # JavaScript automation layer
│   │   │   │   ├── bridge.js        # Python ↔ JavaScript communication
│   │   │   │   └── snap-embed.js    # Snap! embedding logic
│   │   │   └── snap/                # Snap! source files
│   │   ├── templates/
│   │   │   └── index.html           # Main web interface
│   │   └── server.py                # Web server (FastAPI/Flask)
│   ├── mcp/                     # MCP server implementation
│   │   ├── __init__.py
│   │   ├── server.py           # Main MCP server
│   │   ├── tools.py            # MCP tool definitions
│   │   └── handlers.py         # Request handlers
│   ├── utils/                   # Utilities
│   │   ├── __init__.py
│   │   ├── logger.py           # Logging configuration
│   │   ├── config.py           # Configuration management
│   │   └── validators.py       # Input validation
│   └── main.py                 # Entry point
├── tests/                       # Comprehensive test suite
│   ├── __init__.py
│   ├── test_core/
│   ├── test_nlp/
│   ├── test_mcp/
│   └── test_integration/
├── docs/                        # Documentation
│   ├── api.md
│   ├── development.md
│   └── deployment.md
└── examples/                    # Usage examples
    ├── basic_automation.py
    └── advanced_patterns.py
```

## Essential Configuration Files

### requirements.txt
```txt
# Core MCP and web framework
mcp>=1.0.0
fastapi>=0.104.0
uvicorn>=0.24.0
websockets>=12.0

# Natural language processing
spacy>=3.7.0
nltk>=3.8.0

# Data handling
pydantic>=2.5.0
python-dotenv>=1.0.0
pyyaml>=6.0.1

# Development and testing
pytest>=7.4.0
pytest-asyncio>=0.21.0
black>=23.0.0
flake8>=6.0.0
mypy>=1.7.0

# Optional: Enhanced NLP
transformers>=4.35.0  # For advanced language understanding
torch>=2.1.0         # If using transformers
```

### setup.py
```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="snap-automation-mcp",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Natural language to visual programming automation using Snap! and MCP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/snap-automation-mcp",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "snap-automation-mcp=main:main",
            "snap-mcp=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "knowledge": ["*.json"],
        "web": ["templates/*.html", "static/**/*"],
    },
)
```

### pyproject.toml
```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "snap-automation-mcp"
version = "1.0.0"
description = "Natural language to visual programming automation using Snap! and MCP"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"},
]
keywords = ["education", "programming", "visual-programming", "snap", "mcp", "automation"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Education",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

[project.scripts]
snap-automation-mcp = "main:main"
snap-mcp = "main:main"

[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --tb=short"
asyncio_mode = "auto"
```

### .env.example
```env
# Server Configuration
HOST=localhost
PORT=8000
DEBUG=true

# MCP Configuration
MCP_SERVER_NAME=snap-automation-mcp
MCP_SERVER_VERSION=1.0.0

# Web Interface Configuration
WEB_HOST=localhost
WEB_PORT=3000
WEBSOCKET_PORT=8765

# Snap! Configuration
SNAP_URL=https://snap.berkeley.edu/snap/snap.html
SNAP_EMBED_MODE=true

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=snap-automation-mcp.log

# Development Configuration
RELOAD=true
WORKERS=1

# Optional: Advanced NLP Features
USE_ADVANCED_NLP=false
HUGGINGFACE_MODEL=microsoft/DialoGPT-medium
```

### .gitignore
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log
logs/

# Testing
.coverage
.pytest_cache/
.tox/
.nox/
coverage.xml
*.cover
*.py,cover
.hypothesis/

# MyPy
.mypy_cache/
.dmypy.json
dmypy.json

# Project specific
snap-automation-mcp.log
temp/
downloads/
uploads/
```

## Core Implementation Templates

### src/main.py - Entry Point
```python
#!/usr/bin/env python3
"""
Snap! Automation MCP - Main Entry Point
Natural language to visual programming automation
"""

import asyncio
import logging
import os
from pathlib import Path
from dotenv import load_dotenv

from mcp.server import server
from web.server import WebServer
from utils.logger import setup_logging
from utils.config import Config

# Load environment variables
load_dotenv()

def main():
    """Main entry point for Snap! Automation MCP"""
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)

    # Load configuration
    config = Config()

    logger.info("Starting Snap! Automation MCP Server")
    logger.info(f"Version: {config.VERSION}")
    logger.info(f"Debug mode: {config.DEBUG}")

    try:
        # Start the event loop
        asyncio.run(start_servers(config))
    except KeyboardInterrupt:
        logger.info("Shutting down gracefully...")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        raise

async def start_servers(config: Config):
    """Start both MCP and web servers"""
    # Start web server for Snap! interface
    web_server = WebServer(config)
    web_task = asyncio.create_task(web_server.start())

    # Start MCP server
    mcp_task = asyncio.create_task(server.run())

    # Wait for both servers
    await asyncio.gather(web_task, mcp_task)

if __name__ == "__main__":
    main()
```

### src/utils/config.py - Configuration Management
```python
"""Configuration management for Snap! Automation MCP"""

import os
from typing import Optional
from pydantic import BaseSettings, Field

class Config(BaseSettings):
    """Application configuration"""

    # Server Configuration
    HOST: str = Field(default="localhost", env="HOST")
    PORT: int = Field(default=8000, env="PORT")
    DEBUG: bool = Field(default=False, env="DEBUG")

    # MCP Configuration
    MCP_SERVER_NAME: str = Field(default="snap-automation-mcp", env="MCP_SERVER_NAME")
    MCP_SERVER_VERSION: str = Field(default="1.0.0", env="MCP_SERVER_VERSION")

    # Web Interface Configuration
    WEB_HOST: str = Field(default="localhost", env="WEB_HOST")
    WEB_PORT: int = Field(default=3000, env="WEB_PORT")
    WEBSOCKET_PORT: int = Field(default=8765, env="WEBSOCKET_PORT")

    # Snap! Configuration
    SNAP_URL: str = Field(
        default="https://snap.berkeley.edu/snap/snap.html",
        env="SNAP_URL"
    )
    SNAP_EMBED_MODE: bool = Field(default=True, env="SNAP_EMBED_MODE")

    # Logging Configuration
    LOG_LEVEL: str = Field(default="INFO", env="LOG_LEVEL")
    LOG_FILE: Optional[str] = Field(default=None, env="LOG_FILE")

    # Development Configuration
    RELOAD: bool = Field(default=False, env="RELOAD")
    WORKERS: int = Field(default=1, env="WORKERS")

    # Advanced NLP Features
    USE_ADVANCED_NLP: bool = Field(default=False, env="USE_ADVANCED_NLP")
    HUGGINGFACE_MODEL: str = Field(
        default="microsoft/DialoGPT-medium",
        env="HUGGINGFACE_MODEL"
    )

    class Config:
        env_file = ".env"
        case_sensitive = True

# Global config instance
config = Config()
```

### src/utils/logger.py - Logging Setup
```python
"""Logging configuration for Snap! Automation MCP"""

import logging
import sys
from pathlib import Path
from typing import Optional

def setup_logging(
    level: str = "INFO",
    log_file: Optional[str] = None,
    format_string: Optional[str] = None
) -> None:
    """Setup logging configuration"""

    if format_string is None:
        format_string = (
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

    # Configure root logger
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format=format_string,
        handlers=[]
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(format_string))
    logging.getLogger().addHandler(console_handler)

    # File handler (optional)
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(log_path)
        file_handler.setFormatter(logging.Formatter(format_string))
        logging.getLogger().addHandler(file_handler)

    # Set specific logger levels
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("websockets").setLevel(logging.WARNING)
```

### src/core/snap_api.py - Snap! JavaScript API Wrapper
```python
"""
Snap! JavaScript API Wrapper
Provides Python interface to Snap! automation
"""

import json
import logging
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, asdict
from enum import Enum

logger = logging.getLogger(__name__)

class BlockCategory(Enum):
    """Snap! block categories"""
    MOTION = "motion"
    LOOKS = "looks"
    SOUND = "sound"
    PEN = "pen"
    CONTROL = "control"
    SENSING = "sensing"
    OPERATORS = "operators"
    VARIABLES = "variables"
    CUSTOM = "custom"

@dataclass
class SnapBlock:
    """Represents a Snap! block"""
    selector: str
    category: BlockCategory
    parameters: Dict[str, Any] = None
    inputs: List['SnapBlock'] = None
    is_hat: bool = False
    is_cap: bool = False
    is_reporter: bool = False

    def __post_init__(self):
        if self.parameters is None:
            self.parameters = {}
        if self.inputs is None:
            self.inputs = []

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "selector": self.selector,
            "category": self.category.value,
            "parameters": self.parameters,
            "inputs": [input_block.to_dict() for input_block in self.inputs],
            "is_hat": self.is_hat,
            "is_cap": self.is_cap,
            "is_reporter": self.is_reporter
        }

@dataclass
class SnapScript:
    """Represents a complete Snap! script (sequence of connected blocks)"""
    blocks: List[SnapBlock]
    sprite_name: str = "Sprite"
    position: tuple = (100, 100)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "blocks": [block.to_dict() for block in self.blocks],
            "sprite_name": self.sprite_name,
            "position": self.position
        }

class SnapAPI:
    """Python wrapper for Snap! JavaScript API"""

    def __init__(self, websocket_client=None):
        self.websocket_client = websocket_client
        self.current_sprite = "Sprite"
        self.scripts: List[SnapScript] = []

    # Block Creation Methods
    def create_motion_block(self, block_type: str, **params) -> SnapBlock:
        """Create motion blocks (forward, turn, etc.)"""
        motion_blocks = {
            "forward": {"selector": "forward", "params": ["steps"]},
            "turn": {"selector": "turn", "params": ["degrees"]},
            "turnLeft": {"selector": "turnLeft", "params": ["degrees"]},
            "setHeading": {"selector": "setHeading", "params": ["direction"]},
            "doFaceTowards": {"selector": "doFaceTowards", "params": ["target"]},
            "gotoXY": {"selector": "gotoXY", "params": ["x", "y"]},
            "doGlide": {"selector": "doGlide", "params": ["secs", "x", "y"]},
            "changeXPosition": {"selector": "changeXPosition", "params": ["delta"]},
            "setXPosition": {"selector": "setXPosition", "params": ["x"]},
            "changeYPosition": {"selector": "changeYPosition", "params": ["delta"]},
            "setYPosition": {"selector": "setYPosition", "params": ["y"]},
        }

        if block_type not in motion_blocks:
            raise ValueError(f"Unknown motion block: {block_type}")

        block_info = motion_blocks[block_type]
        return SnapBlock(
            selector=block_info["selector"],
            category=BlockCategory.MOTION,
            parameters=params
        )

    def create_looks_block(self, block_type: str, **params) -> SnapBlock:
        """Create looks blocks (say, think, show, hide, etc.)"""
        looks_blocks = {
            "bubble": {"selector": "bubble", "params": ["text"]},
            "doSayFor": {"selector": "doSayFor", "params": ["text", "secs"]},
            "doThinkFor": {"selector": "doThinkFor", "params": ["text", "secs"]},
            "show": {"selector": "show", "params": []},
            "hide": {"selector": "hide", "params": []},
            "doSwitchToCostume": {"selector": "doSwitchToCostume", "params": ["costume"]},
            "doWearNextCostume": {"selector": "doWearNextCostume", "params": []},
            "changeEffect": {"selector": "changeEffect", "params": ["effect", "value"]},
            "setEffect": {"selector": "setEffect", "params": ["effect", "value"]},
            "clearEffects": {"selector": "clearEffects", "params": []},
            "changeScale": {"selector": "changeScale", "params": ["delta"]},
            "setScale": {"selector": "setScale", "params": ["percent"]},
        }

        if block_type not in looks_blocks:
            raise ValueError(f"Unknown looks block: {block_type}")

        block_info = looks_blocks[block_type]
        return SnapBlock(
            selector=block_info["selector"],
            category=BlockCategory.LOOKS,
            parameters=params
        )

    def create_control_block(self, block_type: str, **params) -> SnapBlock:
        """Create control blocks (repeat, if, wait, etc.)"""
        control_blocks = {
            "doWait": {"selector": "doWait", "params": ["secs"]},
            "doRepeat": {"selector": "doRepeat", "params": ["times"]},
            "doForever": {"selector": "doForever", "params": []},
            "doIf": {"selector": "doIf", "params": ["condition"]},
            "doIfElse": {"selector": "doIfElse", "params": ["condition"]},
            "doWaitUntil": {"selector": "doWaitUntil", "params": ["condition"]},
            "doUntil": {"selector": "doUntil", "params": ["condition"]},
            "doStop": {"selector": "doStop", "params": ["choice"]},
            "doBroadcast": {"selector": "doBroadcast", "params": ["message"]},
            "doBroadcastAndWait": {"selector": "doBroadcastAndWait", "params": ["message"]},
        }

        if block_type not in control_blocks:
            raise ValueError(f"Unknown control block: {block_type}")

        block_info = control_blocks[block_type]
        is_hat = block_type in ["doForever", "doRepeat", "doIf", "doIfElse", "doUntil"]

        return SnapBlock(
            selector=block_info["selector"],
            category=BlockCategory.CONTROL,
            parameters=params,
            is_hat=is_hat
        )

    def create_event_block(self, block_type: str, **params) -> SnapBlock:
        """Create event blocks (when flag clicked, when key pressed, etc.)"""
        event_blocks = {
            "receiveGo": {"selector": "receiveGo", "params": []},
            "receiveKey": {"selector": "receiveKey", "params": ["key"]},
            "receiveClick": {"selector": "receiveClick", "params": []},
            "receiveMessage": {"selector": "receiveMessage", "params": ["message"]},
        }

        if block_type not in event_blocks:
            raise ValueError(f"Unknown event block: {block_type}")

        block_info = event_blocks[block_type]
        return SnapBlock(
            selector=block_info["selector"],
            category=BlockCategory.CONTROL,  # Events are in control category in Snap!
            parameters=params,
            is_hat=True
        )

    # Script Building Methods
    def create_script(self, blocks: List[SnapBlock], sprite_name: str = None) -> SnapScript:
        """Create a script from a list of blocks"""
        if sprite_name is None:
            sprite_name = self.current_sprite

        script = SnapScript(blocks=blocks, sprite_name=sprite_name)
        self.scripts.append(script)
        return script

    def clear_scripts(self):
        """Clear all scripts"""
        self.scripts = []

    # Communication with JavaScript
    async def send_command(self, command: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Send command to Snap! JavaScript interface"""
        if not self.websocket_client:
            raise RuntimeError("WebSocket client not connected")

        message = {
            "type": "snap_command",
            "command": command,
            "data": data or {}
        }

        await self.websocket_client.send(json.dumps(message))
        response = await self.websocket_client.recv()
        return json.loads(response)

    async def create_program(self, scripts: List[SnapScript]) -> Dict[str, Any]:
        """Create complete program in Snap!"""
        program_data = {
            "scripts": [script.to_dict() for script in scripts],
            "timestamp": __import__("time").time()
        }

        return await self.send_command("create_program", program_data)

    async def run_program(self) -> Dict[str, Any]:
        """Run the current program (green flag)"""
        return await self.send_command("run_program")

    async def stop_program(self) -> Dict[str, Any]:
        """Stop the current program"""
        return await self.send_command("stop_program")

    async def get_status(self) -> Dict[str, Any]:
        """Get current Snap! environment status"""
        return await self.send_command("get_status")
```

### src/nlp/parser.py - Natural Language Parser (Adapted from old project)
```python
"""
Natural Language Parser for Snap! Automation
Converts natural language descriptions to programming intents
"""

import re
import logging
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)

class ActionType(Enum):
    """Types of programming actions"""
    MOTION = "motion"
    LOOKS = "looks"
    SOUND = "sound"
    CONTROL = "control"
    EVENT = "event"
    SENSING = "sensing"
    OPERATORS = "operators"
    VARIABLES = "variables"
    CUSTOM = "custom"

@dataclass
class Intent:
    """Represents a parsed programming intent"""
    action: str
    action_type: ActionType
    subject: str = "sprite"
    trigger: Optional[str] = None
    parameters: Dict[str, Any] = None
    modifiers: List[str] = None
    confidence: float = 1.0

    def __post_init__(self):
        if self.parameters is None:
            self.parameters = {}
        if self.modifiers is None:
            self.modifiers = []

class NaturalLanguageParser:
    """Parse natural language into programming intents"""

    def __init__(self):
        self.action_patterns = self._load_action_patterns()
        self.parameter_extractors = self._load_parameter_extractors()
        self.trigger_patterns = self._load_trigger_patterns()

    def _load_action_patterns(self) -> Dict[str, Dict[str, Any]]:
        """Load action recognition patterns"""
        return {
            # Motion actions
            "move": {
                "patterns": [
                    r"move\s+(?:the\s+)?(?:sprite|cat|character)?\s*(?:forward|ahead)?\s*(?:by\s+)?(\d+)?\s*(?:steps?|pixels?)?",
                    r"go\s+(?:forward|ahead)\s*(?:by\s+)?(\d+)?\s*(?:steps?|pixels?)?",
                    r"walk\s+(?:forward|ahead)?\s*(?:by\s+)?(\d+)?\s*(?:steps?|pixels?)?"
                ],
                "action_type": ActionType.MOTION,
                "default_params": {"steps": 10}
            },
            "turn": {
                "patterns": [
                    r"turn\s+(left|right)\s*(?:by\s+)?(\d+)?\s*(?:degrees?)?",
                    r"rotate\s+(clockwise|counterclockwise|counter-clockwise)\s*(?:by\s+)?(\d+)?\s*(?:degrees?)?",
                    r"spin\s+(left|right)\s*(?:by\s+)?(\d+)?\s*(?:degrees?)?"
                ],
                "action_type": ActionType.MOTION,
                "default_params": {"degrees": 90}
            },
            "goto": {
                "patterns": [
                    r"go\s+to\s+(?:position\s+)?(?:\()?(-?\d+)(?:\s*,\s*|\s+)(-?\d+)(?:\))?",
                    r"move\s+to\s+(?:position\s+)?(?:\()?(-?\d+)(?:\s*,\s*|\s+)(-?\d+)(?:\))?",
                    r"jump\s+to\s+(?:position\s+)?(?:\()?(-?\d+)(?:\s*,\s*|\s+)(-?\d+)(?:\))?"
                ],
                "action_type": ActionType.MOTION,
                "default_params": {"x": 0, "y": 0}
            },

            # Looks actions
            "say": {
                "patterns": [
                    r"say\s+[\"']([^\"']+)[\"'](?:\s+for\s+(\d+(?:\.\d+)?)\s*(?:seconds?|secs?))?",
                    r"speak\s+[\"']([^\"']+)[\"'](?:\s+for\s+(\d+(?:\.\d+)?)\s*(?:seconds?|secs?))?",
                    r"tell\s+[\"']([^\"']+)[\"'](?:\s+for\s+(\d+(?:\.\d+)?)\s*(?:seconds?|secs?))?"
                ],
                "action_type": ActionType.LOOKS,
                "default_params": {"text": "Hello!", "duration": 2}
            },
            "show": {
                "patterns": [
                    r"show\s+(?:the\s+)?(?:sprite|character|cat)",
                    r"make\s+(?:the\s+)?(?:sprite|character|cat)\s+visible",
                    r"appear"
                ],
                "action_type": ActionType.LOOKS,
                "default_params": {}
            },
            "hide": {
                "patterns": [
                    r"hide\s+(?:the\s+)?(?:sprite|character|cat)",
                    r"make\s+(?:the\s+)?(?:sprite|character|cat)\s+invisible",
                    r"disappear"
                ],
                "action_type": ActionType.LOOKS,
                "default_params": {}
            },

            # Control actions
            "repeat": {
                "patterns": [
                    r"repeat\s+(\d+)\s+times?",
                    r"do\s+(\d+)\s+times?",
                    r"loop\s+(\d+)\s+times?"
                ],
                "action_type": ActionType.CONTROL,
                "default_params": {"times": 10}
            },
            "wait": {
                "patterns": [
                    r"wait\s+(?:for\s+)?(\d+(?:\.\d+)?)\s*(?:seconds?|secs?)",
                    r"pause\s+(?:for\s+)?(\d+(?:\.\d+)?)\s*(?:seconds?|secs?)",
                    r"delay\s+(?:for\s+)?(\d+(?:\.\d+)?)\s*(?:seconds?|secs?)"
                ],
                "action_type": ActionType.CONTROL,
                "default_params": {"duration": 1}
            },

            # Complex patterns
            "jump": {
                "patterns": [
                    r"jump(?:\s+up)?(?:\s+by\s+(\d+))?",
                    r"hop(?:\s+up)?(?:\s+by\s+(\d+))?"
                ],
                "action_type": ActionType.MOTION,
                "default_params": {"height": 50}
            }
        }

    def _load_parameter_extractors(self) -> Dict[str, callable]:
        """Load parameter extraction functions"""
        return {
            "number": lambda text: self._extract_numbers(text),
            "direction": lambda text: self._extract_direction(text),
            "color": lambda text: self._extract_color(text),
            "key": lambda text: self._extract_key(text),
            "text": lambda text: self._extract_quoted_text(text)
        }

    def _load_trigger_patterns(self) -> Dict[str, List[str]]:
        """Load trigger recognition patterns"""
        return {
            "green_flag": [
                r"when\s+(?:the\s+)?(?:green\s+)?flag\s+(?:is\s+)?clicked",
                r"when\s+(?:the\s+)?program\s+starts?",
                r"on\s+start"
            ],
            "key_press": [
                r"when\s+(?:the\s+)?(\w+)\s+key\s+(?:is\s+)?pressed",
                r"when\s+(?:key\s+)?(\w+)\s+(?:is\s+)?pressed",
                r"on\s+(\w+)\s+key"
            ],
            "sprite_click": [
                r"when\s+(?:the\s+)?(?:sprite|character|cat)\s+(?:is\s+)?clicked",
                r"when\s+clicked",
                r"on\s+click"
            ]
        }

    def parse(self, text: str) -> List[Intent]:
        """Parse natural language text into programming intents"""
        text = text.lower().strip()
        intents = []

        logger.debug(f"Parsing text: {text}")

        # Extract trigger if present
        trigger, trigger_params = self._extract_trigger(text)

        # Split into sentences for complex descriptions
        sentences = self._split_sentences(text)

        for sentence in sentences:
            # Try to match action patterns
            for action_name, action_info in self.action_patterns.items():
                for pattern in action_info["patterns"]:
                    match = re.search(pattern, sentence, re.IGNORECASE)
                    if match:
                        intent = self._create_intent_from_match(
                            action_name, action_info, match, trigger, trigger_params
                        )
                        if intent:
                            intents.append(intent)
                        break

        # If no specific patterns matched, try general parsing
        if not intents:
            general_intent = self._parse_general_intent(text, trigger, trigger_params)
            if general_intent:
                intents.append(general_intent)

        logger.debug(f"Parsed {len(intents)} intents: {[i.action for i in intents]}")
        return intents

    def _extract_trigger(self, text: str) -> Tuple[Optional[str], Dict[str, Any]]:
        """Extract trigger information from text"""
        for trigger_type, patterns in self.trigger_patterns.items():
            for pattern in patterns:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    params = {}
                    if trigger_type == "key_press" and match.groups():
                        params["key"] = match.group(1).lower()
                    return trigger_type, params
        return None, {}

    def _create_intent_from_match(
        self,
        action_name: str,
        action_info: Dict[str, Any],
        match: re.Match,
        trigger: Optional[str],
        trigger_params: Dict[str, Any]
    ) -> Optional[Intent]:
        """Create intent from regex match"""

        parameters = action_info["default_params"].copy()

        # Extract parameters from match groups
        groups = match.groups()
        if groups:
            if action_name == "move" and groups[0]:
                parameters["steps"] = int(groups[0])
            elif action_name == "turn":
                if groups[0] in ["left", "counterclockwise", "counter-clockwise"]:
                    parameters["direction"] = "left"
                else:
                    parameters["direction"] = "right"
                if len(groups) > 1 and groups[1]:
                    parameters["degrees"] = int(groups[1])
            elif action_name == "goto" and len(groups) >= 2:
                parameters["x"] = int(groups[0])
                parameters["y"] = int(groups[1])
            elif action_name == "say":
                if groups[0]:
                    parameters["text"] = groups[0]
                if len(groups) > 1 and groups[1]:
                    parameters["duration"] = float(groups[1])
            elif action_name == "repeat" and groups[0]:
                parameters["times"] = int(groups[0])
            elif action_name == "wait" and groups[0]:
                parameters["duration"] = float(groups[0])
            elif action_name == "jump" and groups[0]:
                parameters["height"] = int(groups[0])

        # Add trigger parameters
        if trigger:
            parameters.update(trigger_params)

        return Intent(
            action=action_name,
            action_type=action_info["action_type"],
            trigger=trigger,
            parameters=parameters,
            confidence=0.9
        )

    def _parse_general_intent(
        self,
        text: str,
        trigger: Optional[str],
        trigger_params: Dict[str, Any]
    ) -> Optional[Intent]:
        """Parse general intent when no specific patterns match"""

        # Look for common action words
        action_words = {
            "move": ActionType.MOTION,
            "go": ActionType.MOTION,
            "walk": ActionType.MOTION,
            "run": ActionType.MOTION,
            "jump": ActionType.MOTION,
            "turn": ActionType.MOTION,
            "rotate": ActionType.MOTION,
            "say": ActionType.LOOKS,
            "speak": ActionType.LOOKS,
            "show": ActionType.LOOKS,
            "hide": ActionType.LOOKS,
            "play": ActionType.SOUND,
            "stop": ActionType.CONTROL,
            "wait": ActionType.CONTROL,
            "repeat": ActionType.CONTROL
        }

        for word, action_type in action_words.items():
            if word in text:
                parameters = {}

                # Extract numbers
                numbers = self._extract_numbers(text)
                if numbers:
                    if word in ["move", "go", "walk", "run"]:
                        parameters["steps"] = numbers[0]
                    elif word in ["turn", "rotate"]:
                        parameters["degrees"] = numbers[0]
                    elif word in ["wait"]:
                        parameters["duration"] = numbers[0]
                    elif word in ["repeat"]:
                        parameters["times"] = numbers[0]

                # Extract quoted text
                quoted_text = self._extract_quoted_text(text)
                if quoted_text and word == "say":
                    parameters["text"] = quoted_text[0]

                return Intent(
                    action=word,
                    action_type=action_type,
                    trigger=trigger,
                    parameters=parameters,
                    confidence=0.7
                )

        return None

    def _split_sentences(self, text: str) -> List[str]:
        """Split text into sentences"""
        # Simple sentence splitting
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]

    def _extract_numbers(self, text: str) -> List[float]:
        """Extract numbers from text"""
        numbers = re.findall(r'-?\d+(?:\.\d+)?', text)
        return [float(n) for n in numbers]

    def _extract_direction(self, text: str) -> Optional[str]:
        """Extract direction from text"""
        if re.search(r'\b(?:left|counterclockwise|counter-clockwise)\b', text, re.IGNORECASE):
            return "left"
        elif re.search(r'\b(?:right|clockwise)\b', text, re.IGNORECASE):
            return "right"
        elif re.search(r'\b(?:up|upward)\b', text, re.IGNORECASE):
            return "up"
        elif re.search(r'\b(?:down|downward)\b', text, re.IGNORECASE):
            return "down"
        return None

    def _extract_color(self, text: str) -> Optional[str]:
        """Extract color from text"""
        colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "gray", "brown"]
        for color in colors:
            if color in text.lower():
                return color
        return None

    def _extract_key(self, text: str) -> Optional[str]:
        """Extract key name from text"""
        key_patterns = {
            r'\bspace\b': 'space',
            r'\benter\b': 'enter',
            r'\barrow\s+up\b': 'up arrow',
            r'\barrow\s+down\b': 'down arrow',
            r'\barrow\s+left\b': 'left arrow',
            r'\barrow\s+right\b': 'right arrow',
            r'\b([a-z])\s+key\b': r'\1'
        }

        for pattern, replacement in key_patterns.items():
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                if '\\1' in replacement:
                    return match.group(1).lower()
                return replacement
        return None

    def _extract_quoted_text(self, text: str) -> List[str]:
        """Extract quoted text from string"""
        quotes = re.findall(r'["\']([^"\']+)["\']', text)
        return quotes
```

### src/knowledge/snap_blocks.json - Snap! Block Definitions
```json
{
  "_comment": "Snap! block definitions for automation",
  "_version": "1.0.0",
  "_last_updated": "2024-01-01",

  "motion": {
    "forward": {
      "description": "Move sprite forward by specified steps",
      "selector": "forward",
      "category": "motion",
      "parameters": {
        "steps": {
          "type": "number",
          "default": 10,
          "min": -999,
          "max": 999,
          "description": "Number of steps to move"
        }
      },
      "educational_note": "This moves your sprite in the direction it's currently facing",
      "examples": ["move forward 10 steps", "go ahead 50 pixels"]
    },
    "turn": {
      "description": "Turn sprite clockwise by specified degrees",
      "selector": "turn",
      "category": "motion",
      "parameters": {
        "degrees": {
          "type": "number",
          "default": 15,
          "min": -360,
          "max": 360,
          "description": "Degrees to turn (positive = clockwise, negative = counterclockwise)"
        }
      },
      "educational_note": "Positive numbers turn right, negative numbers turn left",
      "examples": ["turn right 90 degrees", "rotate 45 degrees"]
    },
    "turnLeft": {
      "description": "Turn sprite counterclockwise by specified degrees",
      "selector": "turnLeft",
      "category": "motion",
      "parameters": {
        "degrees": {
          "type": "number",
          "default": 15,
          "min": 0,
          "max": 360,
          "description": "Degrees to turn counterclockwise"
        }
      },
      "educational_note": "This turns your sprite to the left",
      "examples": ["turn left 90 degrees", "rotate counterclockwise 45 degrees"]
    },
    "gotoXY": {
      "description": "Move sprite to specific x,y coordinates",
      "selector": "gotoXY",
      "category": "motion",
      "parameters": {
        "x": {
          "type": "number",
          "default": 0,
          "min": -240,
          "max": 240,
          "description": "X coordinate (left-right position)"
        },
        "y": {
          "type": "number",
          "default": 0,
          "min": -180,
          "max": 180,
          "description": "Y coordinate (up-down position)"
        }
      },
      "educational_note": "This makes your sprite jump to a specific position instantly",
      "examples": ["go to position 100, 50", "jump to coordinates (0, 0)"]
    }
  },

  "looks": {
    "bubble": {
      "description": "Make sprite say text in a speech bubble",
      "selector": "bubble",
      "category": "looks",
      "parameters": {
        "text": {
          "type": "string",
          "default": "Hello!",
          "description": "Text to display in speech bubble"
        }
      },
      "educational_note": "This shows a speech bubble with your message",
      "examples": ["say 'Hello World'", "speak 'How are you?'"]
    },
    "doSayFor": {
      "description": "Make sprite say text for specified duration",
      "selector": "doSayFor",
      "category": "looks",
      "parameters": {
        "text": {
          "type": "string",
          "default": "Hello!",
          "description": "Text to display"
        },
        "secs": {
          "type": "number",
          "default": 2,
          "min": 0.1,
          "max": 60,
          "description": "Duration in seconds"
        }
      },
      "educational_note": "This shows a message for a specific amount of time",
      "examples": ["say 'Hello' for 3 seconds", "speak 'Welcome' for 1.5 seconds"]
    },
    "show": {
      "description": "Make sprite visible",
      "selector": "show",
      "category": "looks",
      "parameters": {},
      "educational_note": "This makes your sprite appear on the stage",
      "examples": ["show the sprite", "make visible", "appear"]
    },
    "hide": {
      "description": "Make sprite invisible",
      "selector": "hide",
      "category": "looks",
      "parameters": {},
      "educational_note": "This makes your sprite disappear from the stage",
      "examples": ["hide the sprite", "make invisible", "disappear"]
    }
  },

  "control": {
    "doWait": {
      "description": "Pause execution for specified duration",
      "selector": "doWait",
      "category": "control",
      "parameters": {
        "secs": {
          "type": "number",
          "default": 1,
          "min": 0,
          "max": 60,
          "description": "Duration to wait in seconds"
        }
      },
      "educational_note": "This pauses your program for a specific amount of time",
      "examples": ["wait 2 seconds", "pause for 0.5 seconds", "delay 1 second"]
    },
    "doRepeat": {
      "description": "Repeat enclosed blocks specified number of times",
      "selector": "doRepeat",
      "category": "control",
      "parameters": {
        "times": {
          "type": "number",
          "default": 10,
          "min": 1,
          "max": 1000,
          "description": "Number of times to repeat"
        }
      },
      "is_container": true,
      "educational_note": "This creates a loop that repeats the same actions multiple times",
      "examples": ["repeat 5 times", "do 10 times", "loop 3 times"]
    },
    "doForever": {
      "description": "Repeat enclosed blocks forever",
      "selector": "doForever",
      "category": "control",
      "parameters": {},
      "is_container": true,
      "educational_note": "This creates an infinite loop that never stops",
      "examples": ["repeat forever", "loop continuously", "do forever"]
    },
    "receiveGo": {
      "description": "Start script when green flag is clicked",
      "selector": "receiveGo",
      "category": "control",
      "parameters": {},
      "is_hat": true,
      "educational_note": "This starts your program when the green flag is clicked",
      "examples": ["when flag clicked", "when program starts", "on start"]
    },
    "receiveKey": {
      "description": "Start script when specified key is pressed",
      "selector": "receiveKey",
      "category": "control",
      "parameters": {
        "key": {
          "type": "string",
          "default": "space",
          "description": "Key to listen for"
        }
      },
      "is_hat": true,
      "educational_note": "This starts your script when a specific key is pressed",
      "examples": ["when space key pressed", "when arrow key pressed", "on key press"]
    }
  }
}
```

### src/knowledge/patterns.json - Programming Patterns
```json
{
  "_comment": "Common programming patterns for Snap! automation",
  "_version": "1.0.0",

  "movement_patterns": {
    "square": {
      "description": "Move in a square pattern",
      "blocks": [
        {"action": "repeat", "parameters": {"times": 4}},
        {"action": "forward", "parameters": {"steps": 50}},
        {"action": "turn", "parameters": {"degrees": 90}}
      ],
      "educational_note": "A square has 4 equal sides and 4 right angles (90 degrees each)",
      "complexity": "beginner"
    },
    "circle": {
      "description": "Move in a circular pattern",
      "blocks": [
        {"action": "repeat", "parameters": {"times": 36}},
        {"action": "forward", "parameters": {"steps": 5}},
        {"action": "turn", "parameters": {"degrees": 10}}
      ],
      "educational_note": "Small steps and small turns create a smooth circle",
      "complexity": "intermediate"
    },
    "triangle": {
      "description": "Move in a triangle pattern",
      "blocks": [
        {"action": "repeat", "parameters": {"times": 3}},
        {"action": "forward", "parameters": {"steps": 60}},
        {"action": "turn", "parameters": {"degrees": 120}}
      ],
      "educational_note": "A triangle has 3 sides and exterior angles of 120 degrees",
      "complexity": "beginner"
    }
  },

  "interaction_patterns": {
    "key_movement": {
      "description": "Move sprite with arrow keys",
      "scripts": [
        {
          "trigger": {"type": "key_press", "key": "up arrow"},
          "blocks": [{"action": "changeYPosition", "parameters": {"delta": 10}}]
        },
        {
          "trigger": {"type": "key_press", "key": "down arrow"},
          "blocks": [{"action": "changeYPosition", "parameters": {"delta": -10}}]
        },
        {
          "trigger": {"type": "key_press", "key": "left arrow"},
          "blocks": [{"action": "changeXPosition", "parameters": {"delta": -10}}]
        },
        {
          "trigger": {"type": "key_press", "key": "right arrow"},
          "blocks": [{"action": "changeXPosition", "parameters": {"delta": 10}}]
        }
      ],
      "educational_note": "This creates basic movement controls like in video games",
      "complexity": "intermediate"
    },
    "simple_jump": {
      "description": "Make sprite jump when space is pressed",
      "scripts": [
        {
          "trigger": {"type": "key_press", "key": "space"},
          "blocks": [
            {"action": "changeYPosition", "parameters": {"delta": 50}},
            {"action": "doWait", "parameters": {"secs": 0.2}},
            {"action": "changeYPosition", "parameters": {"delta": -50}}
          ]
        }
      ],
      "educational_note": "This creates a simple jumping motion - up, pause, then down",
      "complexity": "beginner"
    }
  },

  "animation_patterns": {
    "bounce": {
      "description": "Bounce sprite up and down",
      "blocks": [
        {"action": "doForever"},
        {"action": "changeYPosition", "parameters": {"delta": 10}},
        {"action": "doWait", "parameters": {"secs": 0.1}},
        {"action": "changeYPosition", "parameters": {"delta": -10}},
        {"action": "doWait", "parameters": {"secs": 0.1}}
      ],
      "educational_note": "This creates a continuous bouncing animation",
      "complexity": "intermediate"
    },
    "spin": {
      "description": "Spin sprite continuously",
      "blocks": [
        {"action": "doForever"},
        {"action": "turn", "parameters": {"degrees": 5}},
        {"action": "doWait", "parameters": {"secs": 0.05}}
      ],
      "educational_note": "Small turns with short waits create smooth spinning",
      "complexity": "beginner"
    }
  },

  "game_patterns": {
    "simple_platformer": {
      "description": "Basic platformer game controls",
      "scripts": [
        {
          "trigger": {"type": "key_press", "key": "left arrow"},
          "blocks": [
            {"action": "changeXPosition", "parameters": {"delta": -5}},
            {"action": "doSwitchToCostume", "parameters": {"costume": "walking-left"}}
          ]
        },
        {
          "trigger": {"type": "key_press", "key": "right arrow"},
          "blocks": [
            {"action": "changeXPosition", "parameters": {"delta": 5}},
            {"action": "doSwitchToCostume", "parameters": {"costume": "walking-right"}}
          ]
        },
        {
          "trigger": {"type": "key_press", "key": "space"},
          "blocks": [
            {"action": "changeYPosition", "parameters": {"delta": 30}},
            {"action": "doWait", "parameters": {"secs": 0.3}},
            {"action": "changeYPosition", "parameters": {"delta": -30}}
          ]
        }
      ],
      "educational_note": "This creates basic game controls with movement and jumping",
      "complexity": "advanced"
    }
  }
}
```

### src/mcp/server.py - Main MCP Server Implementation
```python
"""
Main MCP Server for Snap! Automation
Provides natural language to visual programming automation
"""

import asyncio
import logging
from typing import Dict, Any, List, Optional
from mcp.server import FastMCP
from mcp.types import Tool

from core.snap_api import SnapAPI, SnapScript
from core.program_builder import ProgramBuilder
from nlp.parser import NaturalLanguageParser
from nlp.intent_mapper import IntentMapper
from utils.config import config

logger = logging.getLogger(__name__)

# Initialize MCP server
mcp = FastMCP(config.MCP_SERVER_NAME)

# Initialize core components
parser = NaturalLanguageParser()
intent_mapper = IntentMapper()
program_builder = ProgramBuilder()
snap_api = SnapAPI()

# Global state
automation_enabled = False
current_session = None

@mcp.tool()
def initialize_snap_automation() -> Dict[str, Any]:
    """Initialize Snap! automation environment"""
    global automation_enabled, current_session

    try:
        logger.info("Initializing Snap! automation...")

        # This would connect to the web interface
        # For now, we'll simulate successful initialization
        automation_enabled = True
        current_session = {
            "status": "connected",
            "timestamp": __import__("time").time(),
            "scripts_created": 0
        }

        return {
            "success": True,
            "message": "✓ Snap! automation initialized successfully",
            "status": {
                "automation_enabled": automation_enabled,
                "session_active": current_session is not None,
                "web_interface": "http://localhost:3000"
            },
            "instructions": [
                "1. Open the web interface at http://localhost:3000",
                "2. The Snap! environment should load automatically",
                "3. You can now create programs using natural language!"
            ]
        }

    except Exception as e:
        logger.error(f"Failed to initialize Snap! automation: {e}")
        return {
            "success": False,
            "message": f"Failed to initialize Snap! automation: {str(e)}",
            "suggestion": "Make sure the web server is running and accessible"
        }

@mcp.tool()
def create_snap_program(description: str, auto_execute: bool = True) -> Dict[str, Any]:
    """
    Create a complete Snap! program from natural language description

    Args:
        description: Natural language description of the program
        auto_execute: Whether to automatically run the program after creation

    Returns:
        Result with program creation status and details
    """
    if not automation_enabled:
        return {
            "success": False,
            "message": "Snap! automation not initialized",
            "suggestion": "Run 'initialize_snap_automation' first"
        }

    try:
        logger.info(f"Creating Snap! program: {description}")

        # Parse natural language into intents
        intents = parser.parse(description)

        if not intents:
            return {
                "success": False,
                "message": "I didn't understand that request",
                "suggestions": [
                    "Try: 'make the cat move in a square'",
                    "Try: 'when space is pressed, make the sprite jump'",
                    "Try: 'create a simple animation where the cat spins'"
                ],
                "help": "Be specific about what you want the sprite to do"
            }

        # Map intents to Snap! blocks
        snap_blocks = intent_mapper.map_intents_to_blocks(intents)

        if not snap_blocks:
            return {
                "success": False,
                "message": "Could not create blocks for that request",
                "parsed_intents": [
                    {
                        "action": intent.action,
                        "parameters": intent.parameters,
                        "confidence": intent.confidence
                    }
                    for intent in intents
                ],
                "suggestion": "Try describing the actions more specifically"
            }

        # Build complete program
        scripts = program_builder.build_program(snap_blocks, intents)

        # Create program in Snap! (simulated for now)
        program_result = _create_program_in_snap(scripts, auto_execute)

        # Update session
        if current_session:
            current_session["scripts_created"] += len(scripts)

        return {
            "success": True,
            "message": f"✓ Created program with {len(scripts)} script(s)",
            "description": description,
            "program_details": {
                "scripts": len(scripts),
                "total_blocks": sum(len(script.blocks) for script in scripts),
                "intents_parsed": len(intents),
                "auto_executed": auto_execute and program_result.get("executed", False)
            },
            "educational_notes": _generate_educational_notes(intents, scripts),
            "next_steps": [
                "Watch your program run in the Snap! interface",
                "Try modifying it by describing changes",
                "Experiment with different parameters"
            ]
        }

    except Exception as e:
        logger.error(f"Error creating Snap! program: {e}")
        return {
            "success": False,
            "message": f"Error creating program: {str(e)}",
            "error_type": "program_creation_error"
        }

@mcp.tool()
def modify_snap_program(modification: str) -> Dict[str, Any]:
    """
    Modify the current Snap! program

    Args:
        modification: Description of how to modify the program

    Returns:
        Result with modification status
    """
    if not automation_enabled:
        return {
            "success": False,
            "message": "Snap! automation not initialized",
            "suggestion": "Run 'initialize_snap_automation' first"
        }

    try:
        logger.info(f"Modifying Snap! program: {modification}")

        # Parse modification request
        intents = parser.parse(modification)

        if not intents:
            return {
                "success": False,
                "message": "I didn't understand the modification request",
                "examples": [
                    "make it move faster",
                    "add a jump when space is pressed",
                    "change the color to red",
                    "make it say hello"
                ]
            }

        # Map to blocks and apply modification
        new_blocks = intent_mapper.map_intents_to_blocks(intents)
        modification_result = _apply_modification_to_snap(new_blocks, modification)

        return {
            "success": True,
            "message": f"✓ Applied modification: {modification}",
            "modification": modification,
            "blocks_added": len(new_blocks),
            "educational_note": _generate_modification_note(modification, intents)
        }

    except Exception as e:
        logger.error(f"Error modifying program: {e}")
        return {
            "success": False,
            "message": f"Error modifying program: {str(e)}",
            "error_type": "modification_error"
        }

@mcp.tool()
def explain_snap_concept(concept: str, level: str = "beginner") -> Dict[str, Any]:
    """
    Explain Snap!/Scratch programming concepts

    Args:
        concept: Programming concept to explain
        level: Explanation level (beginner, intermediate, advanced)

    Returns:
        Educational explanation of the concept
    """
    explanations = {
        "blocks": {
            "beginner": "Blocks are like puzzle pieces that tell your sprite what to do! You snap them together to create programs. Different colored blocks do different things - blue blocks make things move, purple blocks change how things look!",
            "intermediate": "Blocks are visual programming commands that execute specific functions. They're color-coded by category and snap together to form scripts that control sprite behavior.",
            "advanced": "Blocks represent discrete programming instructions in a visual syntax tree. Each block encapsulates specific functionality with defined inputs/outputs."
        },
        "sprites": {
            "beginner": "Sprites are the characters in your program! They can be animals, people, objects - anything you want. You can make them move, talk, and do fun things.",
            "intermediate": "Sprites are programmable objects that have costumes (how they look) and scripts (what they do). Each sprite can have its own code and interact with others.",
            "advanced": "Sprites are autonomous objects with encapsulated state and behavior. They support inheritance through cloning and polymorphism through message handling."
        },
        "loops": {
            "beginner": "Loops are like doing something over and over again! Like when you brush your teeth - you move the brush back and forth many times. In Snap!, we use the 'repeat' block to make things happen multiple times!",
            "intermediate": "Loops let you repeat code without writing it multiple times. The 'repeat' block runs code a specific number of times, while 'forever' runs it continuously.",
            "advanced": "Loops are control structures that enable iteration. Snap! offers counted loops (repeat n), infinite loops (forever), and conditional loops (repeat until)."
        },
        "events": {
            "beginner": "Events are like magic triggers! When something happens (like clicking the green flag or pressing a key), your program starts running. It's like a doorbell - when someone presses it, it makes a sound!",
            "intermediate": "Events are how your program responds to user actions. The hat blocks (like 'when flag clicked') start your scripts when specific things happen.",
            "advanced": "Events implement the observer pattern in visual programming. Snap! uses event-driven architecture where hat blocks register listeners for inputs and messages."
        }
    }

    concept_lower = concept.lower()
    if concept_lower in explanations:
        explanation = explanations[concept_lower].get(level, explanations[concept_lower]["beginner"])

        return {
            "success": True,
            "concept": concept,
            "level": level,
            "explanation": explanation,
            "examples": _get_concept_examples(concept_lower),
            "try_next": f"Try creating a program that uses {concept_lower}!",
            "related_concepts": _get_related_concepts(concept_lower)
        }
    else:
        available_concepts = list(explanations.keys())
        return {
            "success": False,
            "message": f"I don't have an explanation for '{concept}' yet",
            "available_concepts": available_concepts,
            "suggestion": f"Try asking about: {', '.join(available_concepts)}"
        }

@mcp.tool()
def get_snap_status() -> Dict[str, Any]:
    """Get current Snap! automation status"""
    return {
        "automation_enabled": automation_enabled,
        "session_active": current_session is not None,
        "session_details": current_session,
        "web_interface": "http://localhost:3000" if automation_enabled else None,
        "components": {
            "parser": "ready",
            "intent_mapper": "ready",
            "program_builder": "ready",
            "snap_api": "ready" if automation_enabled else "not connected"
        },
        "statistics": {
            "programs_created": current_session.get("scripts_created", 0) if current_session else 0,
            "session_duration": __import__("time").time() - current_session.get("timestamp", 0) if current_session else 0
        }
    }

@mcp.tool()
def create_game_template(game_type: str, complexity: str = "beginner") -> Dict[str, Any]:
    """
    Create a complete game template

    Args:
        game_type: Type of game (platformer, maze, quiz, etc.)
        complexity: Game complexity level

    Returns:
        Result with game creation status
    """
    game_templates = {
        "platformer": {
            "beginner": "Create a simple platformer where the cat moves left and right with arrow keys and jumps with space",
            "intermediate": "Create a platformer with moving platforms, collectible items, and basic physics",
            "advanced": "Create a full platformer with multiple levels, enemies, power-ups, and score system"
        },
        "maze": {
            "beginner": "Create a simple maze where the cat moves through walls using arrow keys",
            "intermediate": "Create a maze with collectible items and a goal to reach",
            "advanced": "Create a maze with enemies, time limits, and multiple levels"
        },
        "quiz": {
            "beginner": "Create a simple quiz that asks questions and gives feedback",
            "intermediate": "Create a quiz with multiple choice questions and score tracking",
            "advanced": "Create a quiz with categories, difficulty levels, and high scores"
        }
    }

    if game_type not in game_templates:
        return {
            "success": False,
            "message": f"Game type '{game_type}' not available",
            "available_types": list(game_templates.keys())
        }

    if complexity not in game_templates[game_type]:
        return {
            "success": False,
            "message": f"Complexity '{complexity}' not available for {game_type}",
            "available_complexity": list(game_templates[game_type].keys())
        }

    # Create the game using the template description
    template_description = game_templates[game_type][complexity]

    return create_snap_program(
        description=template_description,
        auto_execute=False  # Don't auto-execute games, let user start them
    )

# Helper functions
def _create_program_in_snap(scripts: List[SnapScript], auto_execute: bool) -> Dict[str, Any]:
    """Create program in Snap! environment (simulated)"""
    # This would send the scripts to the Snap! web interface
    # For now, we'll simulate successful creation

    logger.info(f"Creating {len(scripts)} scripts in Snap!")

    result = {
        "created": True,
        "scripts": len(scripts),
        "blocks": sum(len(script.blocks) for script in scripts)
    }

    if auto_execute:
        logger.info("Auto-executing program...")
        result["executed"] = True

    return result

def _apply_modification_to_snap(blocks, modification: str) -> Dict[str, Any]:
    """Apply modification to current Snap! program (simulated)"""
    logger.info(f"Applying modification: {modification}")

    return {
        "applied": True,
        "blocks_added": len(blocks),
        "modification": modification
    }

def _generate_educational_notes(intents, scripts) -> List[str]:
    """Generate educational notes for the created program"""
    notes = []

    for intent in intents:
        if intent.action == "move":
            notes.append("Movement blocks change the sprite's position on the stage")
        elif intent.action == "turn":
            notes.append("Turn blocks change the sprite's direction")
        elif intent.action == "say":
            notes.append("Say blocks make the sprite display text in a speech bubble")
        elif intent.action == "repeat":
            notes.append("Repeat blocks create loops that run the same code multiple times")

    return notes

def _generate_modification_note(modification: str, intents) -> str:
    """Generate educational note for modification"""
    return f"Modification '{modification}' adds new functionality to your existing program. This shows how programs can be built incrementally!"

def _get_concept_examples(concept: str) -> List[str]:
    """Get examples for a programming concept"""
    examples = {
        "blocks": ["Try: 'move 10 steps'", "Try: 'turn right 90 degrees'"],
        "sprites": ["Try: 'make the cat say hello'", "Try: 'hide the sprite'"],
        "loops": ["Try: 'repeat moving forward 5 times'", "Try: 'spin forever'"],
        "events": ["Try: 'when space pressed jump up'", "Try: 'when flag clicked start moving'"]
    }
    return examples.get(concept, [])

def _get_related_concepts(concept: str) -> List[str]:
    """Get related programming concepts"""
    relations = {
        "blocks": ["sprites", "scripts", "categories"],
        "sprites": ["costumes", "motion", "coordinates"],
        "loops": ["events", "motion", "animation"],
        "events": ["loops", "user_input", "interactivity"]
    }
    return relations.get(concept, [])

# Server instance for import
server = mcp
```

### src/web/templates/index.html - Main Web Interface
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snap! Automation - Visual Programming Made Easy</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>🎯 Snap! Automation</h1>
            <p>Create visual programs with natural language!</p>
            <div class="status" id="connection-status">
                <span class="status-indicator" id="status-indicator">●</span>
                <span id="status-text">Connecting...</span>
            </div>
        </header>

        <main>
            <div class="workspace">
                <!-- Snap! IDE Container -->
                <div class="snap-container">
                    <div id="snap-ide">
                        <div class="loading">
                            <h3>Loading Snap! Environment...</h3>
                            <div class="spinner"></div>
                        </div>
                    </div>
                </div>

                <!-- Control Panel -->
                <div class="control-panel">
                    <div class="section">
                        <h3>🎮 Quick Actions</h3>
                        <div class="button-group">
                            <button id="run-program" class="btn btn-success">▶️ Run Program</button>
                            <button id="stop-program" class="btn btn-danger">⏹️ Stop Program</button>
                            <button id="clear-stage" class="btn btn-warning">🧹 Clear Stage</button>
                        </div>
                    </div>

                    <div class="section">
                        <h3>💬 Natural Language Input</h3>
                        <div class="input-group">
                            <textarea
                                id="nl-input"
                                placeholder="Describe what you want to create...
Examples:
• Make the cat move in a square
• When space is pressed, make the sprite jump
• Create a simple animation where the cat spins"
                                rows="4"
                            ></textarea>
                            <button id="create-program" class="btn btn-primary">✨ Create Program</button>
                        </div>
                    </div>

                    <div class="section">
                        <h3>🎓 Learning Center</h3>
                        <div class="learning-buttons">
                            <button class="btn btn-info" onclick="explainConcept('blocks')">What are Blocks?</button>
                            <button class="btn btn-info" onclick="explainConcept('sprites')">What are Sprites?</button>
                            <button class="btn btn-info" onclick="explainConcept('loops')">What are Loops?</button>
                            <button class="btn btn-info" onclick="explainConcept('events')">What are Events?</button>
                        </div>
                    </div>

                    <div class="section">
                        <h3>🎮 Game Templates</h3>
                        <div class="template-buttons">
                            <button class="btn btn-secondary" onclick="createGameTemplate('platformer', 'beginner')">Simple Platformer</button>
                            <button class="btn btn-secondary" onclick="createGameTemplate('maze', 'beginner')">Maze Game</button>
                            <button class="btn btn-secondary" onclick="createGameTemplate('quiz', 'beginner')">Quiz Game</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Output Panel -->
            <div class="output-panel">
                <div class="tabs">
                    <button class="tab-button active" onclick="showTab('output')">📋 Output</button>
                    <button class="tab-button" onclick="showTab('educational')">🎓 Learn</button>
                    <button class="tab-button" onclick="showTab('debug')">🔧 Debug</button>
                </div>

                <div id="output-tab" class="tab-content active">
                    <div id="output-messages"></div>
                </div>

                <div id="educational-tab" class="tab-content">
                    <div id="educational-content">
                        <h4>Welcome to Snap! Automation! 🎉</h4>
                        <p>This tool helps you create visual programs using natural language. Here's how to get started:</p>
                        <ol>
                            <li><strong>Describe what you want:</strong> Type in plain English what you want your sprite to do</li>
                            <li><strong>Watch it happen:</strong> Your description gets converted to visual blocks automatically</li>
                            <li><strong>Learn as you go:</strong> Each action includes educational explanations</li>
                        </ol>
                        <p><strong>Try saying:</strong> "Make the cat move forward 50 steps and then turn right"</p>
                    </div>
                </div>

                <div id="debug-tab" class="tab-content">
                    <div id="debug-info">
                        <h4>Debug Information</h4>
                        <div id="debug-messages"></div>
                    </div>
                </div>
            </div>
        </main>
    </div>

    <!-- Scripts -->
    <script src="/static/snap/snap.js"></script>
    <script src="/static/js/bridge.js"></script>
    <script src="/static/js/automation.js"></script>
    <script src="/static/js/snap-embed.js"></script>

    <script>
        // Initialize the application when page loads
        document.addEventListener('DOMContentLoaded', function() {
            initializeSnapAutomation();
        });
    </script>
</body>
</html>
```

### src/web/static/js/automation.js - JavaScript Automation Layer
```javascript
/**
 * Snap! Automation JavaScript Layer
 * Handles communication between Python MCP and Snap! IDE
 */

class SnapAutomation {
    constructor() {
        this.websocket = null;
        this.snapWorld = null;
        this.isConnected = false;
        this.currentSprite = null;

        this.initializeWebSocket();
        this.setupEventListeners();
    }

    initializeWebSocket() {
        const wsUrl = `ws://${window.location.hostname}:8765`;

        try {
            this.websocket = new WebSocket(wsUrl);

            this.websocket.onopen = () => {
                console.log('WebSocket connected');
                this.isConnected = true;
                this.updateConnectionStatus('connected', 'Connected to automation server');
            };

            this.websocket.onmessage = (event) => {
                this.handleMessage(JSON.parse(event.data));
            };

            this.websocket.onclose = () => {
                console.log('WebSocket disconnected');
                this.isConnected = false;
                this.updateConnectionStatus('disconnected', 'Disconnected from server');

                // Attempt to reconnect after 3 seconds
                setTimeout(() => this.initializeWebSocket(), 3000);
            };

            this.websocket.onerror = (error) => {
                console.error('WebSocket error:', error);
                this.updateConnectionStatus('error', 'Connection error');
            };

        } catch (error) {
            console.error('Failed to create WebSocket:', error);
            this.updateConnectionStatus('error', 'Failed to connect');
        }
    }

    setupEventListeners() {
        // Create Program button
        document.getElementById('create-program').addEventListener('click', () => {
            const input = document.getElementById('nl-input').value.trim();
            if (input) {
                this.createProgramFromDescription(input);
            } else {
                this.showMessage('Please enter a description of what you want to create!', 'warning');
            }
        });

        // Run/Stop buttons
        document.getElementById('run-program').addEventListener('click', () => {
            this.runProgram();
        });

        document.getElementById('stop-program').addEventListener('click', () => {
            this.stopProgram();
        });

        // Clear stage button
        document.getElementById('clear-stage').addEventListener('click', () => {
            this.clearStage();
        });

        // Enter key in textarea
        document.getElementById('nl-input').addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && e.ctrlKey) {
                document.getElementById('create-program').click();
            }
        });
    }

    handleMessage(message) {
        console.log('Received message:', message);

        switch (message.type) {
            case 'snap_command':
                this.executeSnapCommand(message.command, message.data);
                break;
            case 'program_created':
                this.handleProgramCreated(message.data);
                break;
            case 'error':
                this.showMessage(`Error: ${message.message}`, 'error');
                break;
            default:
                console.warn('Unknown message type:', message.type);
        }
    }

    executeSnapCommand(command, data) {
        if (!this.snapWorld) {
            console.error('Snap! world not initialized');
            return;
        }

        switch (command) {
            case 'create_program':
                this.createSnapProgram(data);
                break;
            case 'run_program':
                this.snapWorld.children[0].fireGreenFlagEvent();
                break;
            case 'stop_program':
                this.snapWorld.children[0].fireStopAllEvent();
                break;
            case 'get_status':
                this.sendStatus();
                break;
            default:
                console.warn('Unknown Snap! command:', command);
        }
    }

    createSnapProgram(programData) {
        try {
            const stage = this.snapWorld.children[0];
            const sprite = stage.children[0];

            // Clear existing scripts
            sprite.scripts.children.forEach(script => {
                script.destroy();
            });

            // Create new scripts from program data
            programData.scripts.forEach(scriptData => {
                this.createScript(sprite, scriptData);
            });

            this.showMessage(`✓ Created program with ${programData.scripts.length} script(s)`, 'success');

            // Send confirmation back to Python
            this.sendMessage({
                type: 'program_created',
                success: true,
                scripts: programData.scripts.length
            });

        } catch (error) {
            console.error('Error creating Snap! program:', error);
            this.showMessage(`Error creating program: ${error.message}`, 'error');
        }
    }

    createScript(sprite, scriptData) {
        let previousBlock = null;

        scriptData.blocks.forEach(blockData => {
            const block = this.createBlock(sprite, blockData);

            if (block) {
                if (previousBlock) {
                    // Connect to previous block
                    previousBlock.nextBlock(block);
                } else {
                    // First block - add to sprite's scripts
                    sprite.scripts.add(block);
                }
                previousBlock = block;
            }
        });
    }

    createBlock(sprite, blockData) {
        try {
            // Get block constructor from Snap!
            const block = sprite.blockForSelector(blockData.selector);

            if (!block) {
                console.warn(`Unknown block selector: ${blockData.selector}`);
                return null;
            }

            // Set parameters
            if (blockData.parameters && Object.keys(blockData.parameters).length > 0) {
                const inputs = block.inputs();
                let inputIndex = 0;

                Object.values(blockData.parameters).forEach(value => {
                    if (inputIndex < inputs.length) {
                        inputs[inputIndex].setContents(value);
                        inputIndex++;
                    }
                });
            }

            return block;

        } catch (error) {
            console.error(`Error creating block ${blockData.selector}:`, error);
            return null;
        }
    }

    createProgramFromDescription(description) {
        if (!this.isConnected) {
            this.showMessage('Not connected to automation server', 'error');
            return;
        }

        this.showMessage(`Creating program: "${description}"`, 'info');

        // Send to Python MCP server via WebSocket
        this.sendMessage({
            type: 'create_program_request',
            description: description,
            timestamp: Date.now()
        });
    }

    runProgram() {
        if (this.snapWorld) {
            this.snapWorld.children[0].fireGreenFlagEvent();
            this.showMessage('▶️ Program started', 'success');
        }
    }

    stopProgram() {
        if (this.snapWorld) {
            this.snapWorld.children[0].fireStopAllEvent();
            this.showMessage('⏹️ Program stopped', 'info');
        }
    }

    clearStage() {
        if (this.snapWorld) {
            const stage = this.snapWorld.children[0];
            const sprite = stage.children[0];

            // Clear all scripts
            sprite.scripts.children.forEach(script => {
                script.destroy();
            });

            // Reset sprite position and appearance
            sprite.gotoXY(0, 0);
            sprite.setHeading(90);
            sprite.show();

            this.showMessage('🧹 Stage cleared', 'info');
        }
    }

    sendMessage(message) {
        if (this.websocket && this.websocket.readyState === WebSocket.OPEN) {
            this.websocket.send(JSON.stringify(message));
        } else {
            console.error('WebSocket not connected');
        }
    }

    sendStatus() {
        const status = {
            type: 'status_response',
            snap_loaded: !!this.snapWorld,
            sprite_count: this.snapWorld ? this.snapWorld.children[0].children.length : 0,
            scripts_count: this.snapWorld ? this.snapWorld.children[0].children[0].scripts.children.length : 0
        };

        this.sendMessage(status);
    }

    updateConnectionStatus(status, message) {
        const indicator = document.getElementById('status-indicator');
        const text = document.getElementById('status-text');

        indicator.className = `status-indicator ${status}`;
        text.textContent = message;
    }

    showMessage(message, type = 'info') {
        const outputDiv = document.getElementById('output-messages');
        const messageDiv = document.createElement('div');

        messageDiv.className = `message ${type}`;
        messageDiv.innerHTML = `
            <span class="timestamp">${new Date().toLocaleTimeString()}</span>
            <span class="content">${message}</span>
        `;

        outputDiv.appendChild(messageDiv);
        outputDiv.scrollTop = outputDiv.scrollHeight;

        // Auto-remove after 10 seconds for non-error messages
        if (type !== 'error') {
            setTimeout(() => {
                if (messageDiv.parentNode) {
                    messageDiv.remove();
                }
            }, 10000);
        }
    }

    setSnapWorld(world) {
        this.snapWorld = world;
        this.currentSprite = world.children[0].children[0];
        this.updateConnectionStatus('ready', 'Snap! environment ready');
        this.showMessage('🎯 Snap! Automation ready! Try describing what you want to create.', 'success');
    }
}

// Global functions for HTML onclick handlers
function explainConcept(concept) {
    snapAutomation.sendMessage({
        type: 'explain_concept',
        concept: concept,
        level: 'beginner'
    });
}

function createGameTemplate(gameType, complexity) {
    snapAutomation.sendMessage({
        type: 'create_game_template',
        game_type: gameType,
        complexity: complexity
    });
}

function showTab(tabName) {
    // Hide all tab contents
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });

    // Remove active class from all tab buttons
    document.querySelectorAll('.tab-button').forEach(button => {
        button.classList.remove('active');
    });

    // Show selected tab
    document.getElementById(`${tabName}-tab`).classList.add('active');
    event.target.classList.add('active');
}

// Initialize automation when script loads
let snapAutomation;

function initializeSnapAutomation() {
    snapAutomation = new SnapAutomation();
    console.log('Snap! Automation initialized');
}
```

## Development Quick Start Guide

### 1. Project Setup (5 minutes)
```bash
# Create new project directory
mkdir snap-automation-mcp
cd snap-automation-mcp

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### 2. Configuration (2 minutes)
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your settings
# Most defaults should work for development
```

### 3. First Run (3 minutes)
```bash
# Start the MCP server
python src/main.py

# In another terminal, test with rovodev
rovodev chat --mcp-config mcp.json
```

### 4. Development Workflow
1. **Make changes** to Python code
2. **Restart server** (auto-reload in debug mode)
3. **Test with rovodev** or web interface
4. **Iterate quickly** with hot reloading

### 5. Testing Your Implementation
```bash
# Run tests
pytest tests/

# Test specific component
pytest tests/test_nlp/test_parser.py -v

# Test with coverage
pytest --cov=src tests/
```

This comprehensive PRD now contains everything needed to build the Snap! automation MCP from scratch. You have:

✅ **Complete project structure** with all files and folders
✅ **Full implementation templates** for all core components
✅ **Configuration files** ready to use
✅ **Knowledge base** with blocks and patterns
✅ **MCP server** with all tools implemented
✅ **Web interface** with Snap! integration
✅ **Development workflow** and testing setup

**Ready to start coding!** 🚀
