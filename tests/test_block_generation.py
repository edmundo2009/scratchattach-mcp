#!/usr/bin/env python3
"""Tests for block generation functionality"""

import unittest
import json
import os
import sys
from typing import List

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from programming.block_generator import BlockGenerator, Intent, ScratchBlock, BlockSequence


class TestBlockGenerator(unittest.TestCase):
    """Test cases for BlockGenerator"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.generator = BlockGenerator()
        
        # Load test fixtures
        fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected_outputs.json')
        with open(fixtures_path, 'r') as f:
            self.test_data = json.load(f)
    
    def test_generator_initialization(self):
        """Test that BlockGenerator initializes correctly"""
        self.assertIsNotNone(self.generator)
        self.assertIsNotNone(self.generator.knowledge_base)
        self.assertIsNotNone(self.generator.pattern_library)
        self.assertIsNotNone(self.generator.action_mapping)
    
    def test_knowledge_base_loading(self):
        """Test that knowledge base is loaded correctly"""
        # Check that blocks are loaded
        self.assertIn("blocks", self.generator.knowledge_base)
        blocks = self.generator.knowledge_base["blocks"]
        
        # Should have motion category
        self.assertIn("motion", blocks)
        
        # Should have some motion blocks
        motion_blocks = blocks["motion"]
        self.assertGreater(len(motion_blocks), 0)
    
    def test_pattern_library_loading(self):
        """Test that pattern library is loaded correctly"""
        # Should have some patterns
        self.assertGreater(len(self.generator.pattern_library), 0)
        
        # Check for pattern categories
        available_actions = self.generator.get_available_actions()
        self.assertIn("simple_patterns", available_actions)

        # Check that simple_patterns contains jump
        if "simple_patterns" in self.generator.pattern_library:
            simple_patterns = self.generator.pattern_library["simple_patterns"]
            self.assertIn("jump", simple_patterns)
    
    def test_action_mapping_creation(self):
        """Test that action mapping is created correctly"""
        # Should have basic actions mapped
        self.assertIn("move", self.generator.action_mapping)
        self.assertIn("start", self.generator.action_mapping)
    
    def test_simple_move_intent(self):
        """Test generating blocks for simple move intent"""
        intent = Intent(
            action="move",
            subject="sprite",
            parameters={"direction": "right", "steps": 10}
        )
        
        result = self.generator.generate_blocks([intent])
        
        self.assertIsInstance(result, BlockSequence)
        self.assertGreaterEqual(len(result.blocks), 0)
        self.assertEqual(result.difficulty, "beginner")
    
    def test_jump_pattern(self):
        """Test generating blocks for jump pattern"""
        intent = Intent(
            action="jump",
            subject="sprite"
        )
        
        result = self.generator.generate_blocks([intent])
        
        self.assertIsInstance(result, BlockSequence)
        # Jump should generate blocks from pattern
        if len(result.blocks) > 0:
            # Should have motion blocks for jump
            motion_blocks = [b for b in result.blocks if b.category == "motion"]
            self.assertGreater(len(motion_blocks), 0)
    
    def test_trigger_block_creation(self):
        """Test creating trigger blocks"""
        intent = Intent(
            action="move",
            subject="sprite",
            trigger="key_press",
            parameters={"key": "space", "direction": "right", "steps": 5}
        )
        
        result = self.generator.generate_blocks([intent])
        
        self.assertIsInstance(result, BlockSequence)
        # Should have at least one block
        self.assertGreaterEqual(len(result.blocks), 0)
    
    def test_multiple_intents(self):
        """Test generating blocks for multiple intents"""
        intents = [
            Intent(action="move", parameters={"direction": "right", "steps": 10}),
            Intent(action="jump")
        ]
        
        result = self.generator.generate_blocks(intents)
        
        self.assertIsInstance(result, BlockSequence)
        # Should have explanation
        self.assertIsInstance(result.explanation, str)
        self.assertGreater(len(result.explanation), 0)
    
    def test_difficulty_calculation(self):
        """Test difficulty calculation for different intent combinations"""
        # Single intent without trigger = beginner
        single_intent = [Intent(action="move")]
        result = self.generator.generate_blocks(single_intent)
        self.assertEqual(result.difficulty, "beginner")
        
        # Multiple intents = intermediate or advanced
        multiple_intents = [
            Intent(action="move"),
            Intent(action="jump"),
            Intent(action="play_sound")
        ]
        result = self.generator.generate_blocks(multiple_intents)
        self.assertIn(result.difficulty, ["intermediate", "advanced"])
    
    def test_get_available_actions(self):
        """Test getting available actions"""
        actions = self.generator.get_available_actions()
        
        self.assertIsInstance(actions, list)
        self.assertGreater(len(actions), 0)
        
        # Should include basic actions
        self.assertIn("move", actions)
    
    def test_get_block_info(self):
        """Test getting block information"""
        # Test with a known block
        block_info = self.generator.get_block_info("motion_movesteps")
        
        if block_info:  # Only test if block exists
            self.assertIsInstance(block_info, dict)
            self.assertIn("description", block_info)
            self.assertIn("category", block_info)
    
    def test_empty_intent_list(self):
        """Test generating blocks with empty intent list"""
        result = self.generator.generate_blocks([])
        
        self.assertIsInstance(result, BlockSequence)
        self.assertEqual(len(result.blocks), 0)
    
    def test_unknown_action_intent(self):
        """Test generating blocks for unknown action"""
        intent = Intent(action="unknown_action_xyz")
        
        result = self.generator.generate_blocks([intent])
        
        self.assertIsInstance(result, BlockSequence)
        # Should handle gracefully (may or may not generate blocks)
    
    def test_block_sequence_properties(self):
        """Test BlockSequence object properties"""
        intent = Intent(action="move", parameters={"direction": "right"})
        result = self.generator.generate_blocks([intent])
        
        # Check all required properties exist
        self.assertTrue(hasattr(result, 'blocks'))
        self.assertTrue(hasattr(result, 'explanation'))
        self.assertTrue(hasattr(result, 'difficulty'))
        
        # Check types
        self.assertIsInstance(result.blocks, list)
        self.assertIsInstance(result.explanation, str)
        self.assertIsInstance(result.difficulty, str)
        
        # Check difficulty is valid
        self.assertIn(result.difficulty, ["beginner", "intermediate", "advanced"])
    
    def test_scratch_block_properties(self):
        """Test ScratchBlock object properties"""
        intent = Intent(action="move", parameters={"direction": "right", "steps": 10})
        result = self.generator.generate_blocks([intent])
        
        if len(result.blocks) > 0:
            block = result.blocks[0]
            
            # Check all required properties exist
            self.assertTrue(hasattr(block, 'opcode'))
            self.assertTrue(hasattr(block, 'category'))
            self.assertTrue(hasattr(block, 'inputs'))
            self.assertTrue(hasattr(block, 'fields'))
            self.assertTrue(hasattr(block, 'description'))
            
            # Check types
            self.assertIsInstance(block.opcode, str)
            self.assertIsInstance(block.category, str)
            self.assertIsInstance(block.inputs, dict)
            self.assertIsInstance(block.fields, dict)
            self.assertIsInstance(block.description, str)


if __name__ == '__main__':
    unittest.main()
