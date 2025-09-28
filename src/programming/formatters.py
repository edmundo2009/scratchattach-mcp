from typing import Dict, Any
import json


class PictoBloxFormatter:
  """
  Format blocks for PictoBlox/SB3 export.
  NOTE: The generated structure is a simplified representation. A full implementation
  requires a precise mapping to the complex Scratch project JSON specification,
  including handling of IDs, parent-child relationships, and specific input/field structures.
  """

  def format(self, block_sequence: BlockSequence) -> str:
    """Convert block sequence to PictoBlox project format"""
    project = {
      "objName": "Stage",
      "sounds": [],
      "costumes": [],
      "currentCostumeIndex": 0,
      "scripts": [self._blocks_to_script(block_sequence.blocks)],
      "variables": {},
      "lists": {}
    }
    return json.dumps(project, indent=2)

  def _blocks_to_script(self, blocks: List[ScratchBlock]) -> Dict[str, Any]:
    """Convert blocks to PictoBlox script format"""
    script_blocks = []

    for block in blocks:
      pb_block = self._convert_block(block)
      if pb_block:
        script_blocks.append(pb_block)

    return {
      "x": 48,
      "y": 48,
      "blocks": script_blocks
    }

  def _convert_block(self, block: ScratchBlock) -> Dict[str, Any]:
    """Convert ScratchBlock to PictoBlox format"""
    # Map Scratch opcodes to PictoBlox format
    opcode_mapping = {
      "event_whenflagclicked": "event_whenflagclicked",
      "event_whenkeypressed": "event_whenkeypressed",
      "motion_changexby": "motion_changexby",
      "motion_changeyby": "motion_changeyby",
      "sound_play": "sound_play"
    }

    pb_opcode = opcode_mapping.get(block.opcode, block.opcode)

    pb_block = {
      "opcode": pb_opcode,
      "next": None,
      "parent": None,
      "inputs": self._convert_inputs(block.inputs),
      "fields": self._convert_fields(block.fields),
      "shadow": False,
      "topLevel": False
    }

    return pb_block

  def _convert_inputs(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Convert inputs to PictoBlox format"""
    converted = {}
    for key, value in inputs.items():
      if isinstance(value, (int, float)):
        converted[key] = [1, [4, str(value)]]
      else:
        converted[key] = [1, [10, str(value)]]
    return converted

  def _convert_fields(self, fields: Dict[str, Any]) -> Dict[str, Any]:
    """Convert fields to PictoBlox format"""
    return {key: [str(value), None] for key, value in fields.items()}


class TextFormatter:
  """Format blocks as human-readable text"""

  def format(self, block_sequence: BlockSequence) -> str:
    """Convert to step-by-step instructions"""
    output = []
    output.append(
      f"# Your Scratch Program ({block_sequence.difficulty} level)")
    output.append("")
    output.append("## What it does:")
    output.append(block_sequence.explanation)
    output.append("")
    output.append("## Programming steps:")

    for i, block in enumerate(block_sequence.blocks, 1):
      output.append(f"{i}. {block.description}")

      # Add technical details for intermediate/advanced
      if block_sequence.difficulty != "beginner":
        output.append(f"   - Block type: {block.category}")
        if block.inputs:
          output.append(f"   - Settings: {block.inputs}")

    output.append("")
    output.append("## Try this next:")
    output.append(self._suggest_next_steps(block_sequence))

    return "\n".join(output)

  def _suggest_next_steps(self, block_sequence: BlockSequence) -> str:
    """Suggest what to try next"""
    suggestions = {
      "beginner": "Try adding a sound effect or making your sprite change color!",
      "intermediate": "Can you make it repeat forever? Or add more keys to control?",
      "advanced": "Try creating a complete game with scoring and multiple sprites!"
    }
    return suggestions.get(block_sequence.difficulty, "Keep experimenting!")

# Integration example


def generate_scratch_program(user_input: str, output_format: str = "text") -> str:
  """Complete pipeline from natural language to Scratch program"""

  # Parse input
  parser = NaturalLanguageParser()
  intents = parser.parse(user_input)

  if not intents:
    return "I didn't understand that. Try something like 'make the cat move right' or 'when space pressed jump'."

  # Generate blocks
  generator = BlockGenerator()
  block_sequence = generator.generate_blocks(intents)

  # Format output
  if output_format == "pictoblox":
    formatter = PictoBloxFormatter()
  else:
    formatter = TextFormatter()

  return formatter.format(block_sequence)


# Test examples
test_cases = [
  "make the cat move right 10 steps",
  "when space pressed jump up",
  "play sound when sprite clicked",
  "move left and play sound and say hello"
]

print("=== Block Generation System Demo ===\n")

for test_input in test_cases:
  print(f"Input: '{test_input}'")
  print("Output:")
  result = generate_scratch_program(test_input)
  print(result)
  print("\n" + "="*50 + "\n")
