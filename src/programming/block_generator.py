# programming/block_generator.py - Revised Data-Driven Implementation

import json
import os
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass

@dataclass
class Intent:
  """Represents parsed user intent"""
  action: str
  subject: str = "sprite"
  trigger: Optional[str] = None
  parameters: Dict[str, Any] = None
  modifiers: List[str] = None
  
  def __post_init__(self):
    if self.parameters is None:
      self.parameters = {}
    if self.modifiers is None:
      self.modifiers = []

@dataclass 
class ScratchBlock:
  """Represents a single Scratch block"""
  opcode: str
  category: str
  inputs: Dict[str, Any] = None
  fields: Dict[str, Any] = None
  description: str = ""
  
  def __post_init__(self):
    if self.inputs is None:
      self.inputs = {}
    if self.fields is None:
      self.fields = {}

@dataclass
class BlockSequence:
  """Represents a sequence of connected blocks"""
  blocks: List[ScratchBlock]
  explanation: str = ""
  difficulty: str = "beginner"

class BlockGenerator:
  """Converts intents to Scratch block sequences - Data-driven approach"""
  
  def __init__(self, knowledge_path: str = None, patterns_path: str = None):
    """
    Initialize BlockGenerator with configurable knowledge sources
    
    Args:
      knowledge_path: Path to scratch_blocks.json
      patterns_path: Path to patterns.json or patterns.py
    """
    # Set default paths if not provided
    if knowledge_path is None:
      knowledge_path = self._get_default_path("knowledge/scratch_blocks.json")
    if patterns_path is None:
      patterns_path = self._get_default_path("knowledge/patterns.json")
      
    # Load knowledge base
    self.knowledge_base = self._load_knowledge_base(knowledge_path)
    self.block_templates = self.knowledge_base.get("blocks", {})
    self.categories = self.knowledge_base.get("categories", {})
    
    # Load patterns
    self.pattern_library = self._load_patterns(patterns_path)
    
    # Create action-to-block mapping from knowledge base
    self.action_mapping = self._build_action_mapping()
    
    print(f"BlockGenerator initialized:")
    print(f"  - {len(self.block_templates)} block categories loaded")
    print(f"  - {len(self.pattern_library)} patterns loaded")
  
  def _get_default_path(self, relative_path: str) -> str:
    """Get default path relative to this file"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(os.path.dirname(current_dir), relative_path)
  
  def _load_knowledge_base(self, path: str) -> Dict[str, Any]:
    """Load Scratch block definitions from JSON knowledge base"""
    try:
      with open(path, 'r', encoding='utf-8') as f:
        knowledge = json.load(f)
        print(f"Successfully loaded knowledge base from {path}")
        return knowledge
    except FileNotFoundError:
      print(f"Warning: Knowledge base not found at {path}. Using minimal defaults.")
      return self._get_minimal_knowledge_base()
    except json.JSONDecodeError as e:
      print(f"Error: Could not parse knowledge base at {path}: {e}")
      return self._get_minimal_knowledge_base()
    except Exception as e:
      print(f"Unexpected error loading knowledge base: {e}")
      return self._get_minimal_knowledge_base()
  
  def _load_patterns(self, path: str) -> Dict[str, Any]:
    """Load programming patterns from JSON file"""
    try:
      with open(path, 'r', encoding='utf-8') as f:
        patterns = json.load(f)
        print(f"Successfully loaded patterns from {path}")
        return patterns
    except FileNotFoundError:
      print(f"Warning: Patterns file not found at {path}. Using built-in patterns.")
      return self._get_default_patterns()
    except json.JSONDecodeError as e:
      print(f"Error: Could not parse patterns file at {path}: {e}")
      return self._get_default_patterns()
    except Exception as e:
      print(f"Unexpected error loading patterns: {e}")
      return self._get_default_patterns()
  
  def _get_minimal_knowledge_base(self) -> Dict[str, Any]:
    """Fallback minimal knowledge base if file loading fails"""
    return {
      "blocks": {
        "motion": {
          "motion_movesteps": {
            "description": "Move forward/backward",
            "kid_explanation": "Makes your sprite walk!",
            "inputs": ["STEPS"],
            "default_values": {"STEPS": 10}
          },
          "motion_changexby": {
            "description": "Move left/right",
            "kid_explanation": "Makes your sprite move sideways!",
            "inputs": ["DX"],
            "default_values": {"DX": 10}
          }
        },
        "events": {
          "event_whenflagclicked": {
            "description": "When green flag clicked",
            "kid_explanation": "Starts your program!",
            "inputs": [],
            "is_hat_block": True
          }
        }
      },
      "categories": {
        "motion": {"color": "#4C97FF"},
        "events": {"color": "#FFBF00"}
      }
    }
  
  def _get_default_patterns(self) -> Dict[str, Any]:
    """Fallback patterns if file loading fails"""
    return {
      "jump": {
        "description": "Make sprite jump",
        "blocks": ["motion_changeyby"],
        "parameters": {"DY": 50},
        "explanation": "This makes your sprite jump up!"
      }
    }
  
  def _build_action_mapping(self) -> Dict[str, Dict[str, Any]]:
    """Build action-to-block mapping from knowledge base"""
    mapping = {}

    # Extract action mappings from block descriptions and metadata
    for category, blocks in self.block_templates.items():
      for block_id, block_info in blocks.items():
        # Map common actions to blocks based on block purpose
        if category == "motion":
          if "move" in block_info.get("description", "").lower():
            if "steps" in block_info.get("description", "").lower():
              mapping["move"] = {
                "block_id": block_id,
                "category": category,
                "info": block_info
              }
              # Also map horizontal movement to the same block for left/right
              mapping["move_horizontal"] = {
                "block_id": block_id,
                "category": category,
                "info": block_info
              }
          elif "gotoxy" in block_id.lower():
            mapping["move_vertical"] = {
              "block_id": block_id,
              "category": category,
              "info": block_info
            }
          elif "turn" in block_info.get("description", "").lower():
            if "right" in block_id.lower() or "clockwise" in block_info.get("description", "").lower():
              mapping["turn_right"] = {
                "block_id": block_id,
                "category": category,
                "info": block_info
              }
            elif "left" in block_id.lower() or "counter-clockwise" in block_info.get("description", "").lower():
              mapping["turn_left"] = {
                "block_id": block_id,
                "category": category,
                "info": block_info
              }

        elif category == "events":
          if "flag" in block_info.get("description", "").lower():
            mapping["start"] = {
              "block_id": block_id,
              "category": category,
              "info": block_info
            }
          elif "key" in block_info.get("description", "").lower():
            mapping["key_press"] = {
              "block_id": block_id,
              "category": category,
              "info": block_info
            }

        elif category == "looks":
          if "say" in block_info.get("description", "").lower():
            mapping["say"] = {
              "block_id": block_id,
              "category": category,
              "info": block_info
            }

        elif category == "sound":
          if "play" in block_info.get("description", "").lower():
            mapping["play_sound"] = {
              "block_id": block_id,
              "category": category,
              "info": block_info
            }

    return mapping
  
  def generate_blocks(self, intents: List[Intent]) -> BlockSequence:
    """Generate block sequence from intents using knowledge base"""
    all_blocks = []
    explanations = []
    
    for intent in intents:
      blocks, explanation = self._generate_for_intent(intent)
      all_blocks.extend(blocks)
      explanations.append(explanation)
    
    return BlockSequence(
      blocks=all_blocks,
      explanation=" ".join(explanations),
      difficulty=self._calculate_difficulty(intents)
    )
  
  def _generate_for_intent(self, intent: Intent) -> Tuple[List[ScratchBlock], str]:
    """Generate blocks for a single intent using knowledge base"""
    blocks = []
    
    # Check for complex patterns first
    if intent.action in self.pattern_library:
      return self._generate_from_pattern(intent)
    
    # Add trigger block if present
    if intent.trigger:
      trigger_block = self._create_trigger_block(intent)
      if trigger_block:
        blocks.append(trigger_block)
    
    # Add action block using knowledge base
    action_block = self._create_action_block(intent)
    if action_block:
      blocks.append(action_block)
      
    explanation = self._generate_explanation(intent, blocks)
    return blocks, explanation
  
  def _create_trigger_block(self, intent: Intent) -> Optional[ScratchBlock]:
    """Create trigger block using knowledge base"""
    trigger_mapping = {
      "key_press": "key_press",
      "flag_click": "start",
      "sprite_click": "click"
    }
    
    mapped_trigger = trigger_mapping.get(intent.trigger)
    if mapped_trigger and mapped_trigger in self.action_mapping:
      block_info = self.action_mapping[mapped_trigger]
      
      # Create block from knowledge base
      block = ScratchBlock(
        opcode=block_info["block_id"],
        category=block_info["category"],
        description=block_info["info"].get("description", ""),
      )
      
      # Add fields if needed (like key specification)
      if intent.trigger == "key_press" and "key" in intent.parameters:
        block.fields = {"KEY_OPTION": intent.parameters["key"]}
      
      return block
    
    return None
  
  def _create_action_block(self, intent: Intent) -> Optional[ScratchBlock]:
    """Create action block using knowledge base"""
    action_key = intent.action

    # Handle directional movement
    if intent.action == "move" and "direction" in intent.parameters:
      direction = intent.parameters["direction"]
      if direction in ["left", "right"]:
        action_key = "move_horizontal"
      elif direction in ["up", "down"]:
        action_key = "move_vertical"

    if action_key in self.action_mapping:
      block_info = self.action_mapping[action_key]
      block_data = block_info["info"]

      # Create block from knowledge base
      block = ScratchBlock(
        opcode=block_info["block_id"],
        category=block_info["category"],
        description=block_data.get("description", ""),
      )

      # Add inputs based on knowledge base defaults and intent parameters
      if "inputs" in block_data and block_data["inputs"]:
        block.inputs = {}
        for input_name in block_data["inputs"]:
          # Use intent parameters or knowledge base defaults
          default_values = block_data.get("default_values", {})

          if input_name == "STEPS":
            steps = intent.parameters.get("steps", default_values.get(input_name, 10))
            # Handle left movement with negative steps
            if intent.parameters.get("direction") == "left":
              steps = -abs(steps)
            block.inputs[input_name] = steps
          elif input_name in ["DX", "DY", "X", "Y"]:
            value = intent.parameters.get("steps", default_values.get(input_name, 10))
            
            # Apply direction for horizontal/vertical movement
            if input_name == "DX" and "direction" in intent.parameters:
              if intent.parameters["direction"] == "left":
                value = -abs(value)
              else:
                value = abs(value)
            elif input_name == "DY" and "direction" in intent.parameters:
              if intent.parameters["direction"] == "down":
                value = -abs(value)
              else:
                value = abs(value)
            
            block.inputs[input_name] = value
          else:
            # Use default value from knowledge base
            block.inputs[input_name] = default_values.get(input_name, "")
      
      return block
    
    return None
  
  def _generate_from_pattern(self, intent: Intent) -> Tuple[List[ScratchBlock], str]:
    """Generate blocks from predefined pattern"""
    pattern = self.pattern_library[intent.action]
    blocks = []
    
    for block_id in pattern.get("blocks", []):
      # Find block in knowledge base
      block_found = False
      for category, category_blocks in self.block_templates.items():
        if block_id in category_blocks:
          block_info = category_blocks[block_id]
          block = ScratchBlock(
            opcode=block_id,
            category=category,
            description=block_info.get("description", ""),
          )
          
          # Apply pattern parameters
          pattern_params = pattern.get("parameters", {})
          if "inputs" in block_info:
            for input_name in block_info["inputs"]:
              if input_name in pattern_params:
                block.inputs[input_name] = pattern_params[input_name]
          
          blocks.append(block)
          block_found = True
          break
      
      if not block_found:
        print(f"Warning: Block {block_id} not found in knowledge base")
    
    explanation = pattern.get("explanation", f"This creates a {intent.action} effect!")
    return blocks, explanation
  
  def _generate_explanation(self, intent: Intent, blocks: List[ScratchBlock]) -> str:
    """Generate kid-friendly explanation using knowledge base"""
    if not blocks:
      return "I couldn't create blocks for that request."
    
    # Get kid-friendly explanations from knowledge base
    explanations = []
    for block in blocks:
      # Find block in knowledge base to get kid explanation
      for category, category_blocks in self.block_templates.items():
        if block.opcode in category_blocks:
          kid_explanation = category_blocks[block.opcode].get("kid_explanation", block.description)
          explanations.append(kid_explanation)
          break
    
    if explanations:
      return " ".join(explanations)
    else:
      return f"This creates a cool {intent.action} effect!"
  
  def _calculate_difficulty(self, intents: List[Intent]) -> str:
    """Calculate difficulty based on intent complexity"""
    if len(intents) == 1 and not intents[0].trigger:
      return "beginner"
    elif len(intents) <= 2:
      return "intermediate" 
    else:
      return "advanced"
  
  def get_available_actions(self) -> List[str]:
    """Get list of available actions from knowledge base"""
    actions = list(self.action_mapping.keys())
    actions.extend(list(self.pattern_library.keys()))
    return sorted(actions)
  
  def get_block_info(self, block_id: str) -> Optional[Dict[str, Any]]:
    """Get detailed information about a specific block"""
    for category, blocks in self.block_templates.items():
      if block_id in blocks:
        info = blocks[block_id].copy()
        info["category"] = category
        return info
    return None