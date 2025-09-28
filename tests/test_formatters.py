#!/usr/bin/env python3
"""Tests for output formatters"""

import unittest
import json
import os
import sys
from typing import List

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from programming.formatters import TextFormatter, PictoBloxFormatter
from programming.block_generator import ScratchBlock, BlockSequence


class TestTextFormatter(unittest.TestCase):
    """Test cases for TextFormatter"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.formatter = TextFormatter()
        
        # Create sample blocks for testing
        self.sample_block = ScratchBlock(
            opcode="motion_movesteps",
            category="motion",
            inputs={"STEPS": 10},
            description="Move forward/backward by steps"
        )
        
        self.sample_sequence = BlockSequence(
            blocks=[self.sample_block],
            explanation="This makes your sprite walk!",
            difficulty="beginner"
        )
    
    def test_formatter_initialization(self):
        """Test that TextFormatter initializes correctly"""
        self.assertIsNotNone(self.formatter)
    
    def test_format_single_block(self):
        """Test formatting a single block"""
        result = self.formatter.format(self.sample_sequence)
        
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        
        # Should contain step information (numbered format)
        self.assertIn("1.", result)

        # Should contain explanation
        self.assertIn("This makes your sprite walk!", result)
    
    def test_format_multiple_blocks(self):
        """Test formatting multiple blocks"""
        blocks = [
            ScratchBlock(
                opcode="event_whenflagclicked",
                category="events",
                description="When green flag clicked"
            ),
            ScratchBlock(
                opcode="motion_movesteps",
                category="motion",
                inputs={"STEPS": 10},
                description="Move forward/backward by steps"
            )
        ]
        
        sequence = BlockSequence(
            blocks=blocks,
            explanation="Start program and move sprite",
            difficulty="beginner"
        )
        
        result = self.formatter.format(sequence)
        
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)
        
        # Should have multiple steps (numbered format)
        self.assertIn("1.", result)
        self.assertIn("2.", result)
    
    def test_format_empty_sequence(self):
        """Test formatting empty block sequence"""
        empty_sequence = BlockSequence(blocks=[], explanation="", difficulty="beginner")
        
        result = self.formatter.format(empty_sequence)
        
        self.assertIsInstance(result, str)
        # Should handle empty sequence gracefully
    
    def test_format_with_inputs(self):
        """Test formatting blocks with various inputs"""
        block_with_inputs = ScratchBlock(
            opcode="motion_changexby",
            category="motion",
            inputs={"DX": 50},
            description="Move left/right"
        )
        
        sequence = BlockSequence(
            blocks=[block_with_inputs],
            explanation="Move horizontally",
            difficulty="beginner"
        )
        
        result = self.formatter.format(sequence)
        
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)


class TestPictoBloxFormatter(unittest.TestCase):
    """Test cases for PictoBloxFormatter"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.formatter = PictoBloxFormatter()
        
        # Create sample blocks for testing
        self.sample_block = ScratchBlock(
            opcode="motion_movesteps",
            category="motion",
            inputs={"STEPS": 10},
            description="Move forward/backward by steps"
        )
        
        self.sample_sequence = BlockSequence(
            blocks=[self.sample_block],
            explanation="This makes your sprite walk!",
            difficulty="beginner"
        )
    
    def test_formatter_initialization(self):
        """Test that PictoBloxFormatter initializes correctly"""
        self.assertIsNotNone(self.formatter)
    
    def test_format_returns_json_string(self):
        """Test that format returns valid JSON string"""
        result = self.formatter.format(self.sample_sequence)
        
        self.assertIsInstance(result, str)
        
        # Should be valid JSON
        try:
            parsed = json.loads(result)
            self.assertIsInstance(parsed, dict)
        except json.JSONDecodeError:
            self.fail("Formatter should return valid JSON")
    
    def test_format_structure(self):
        """Test that formatted output has correct structure"""
        result = self.formatter.format(self.sample_sequence)
        parsed = json.loads(result)
        
        # Check required top-level keys
        self.assertIn("objName", parsed)
        self.assertIn("sounds", parsed)
        self.assertIn("costumes", parsed)
        self.assertIn("currentCostumeIndex", parsed)
        self.assertIn("scripts", parsed)
        
        # Check types
        self.assertIsInstance(parsed["objName"], str)
        self.assertIsInstance(parsed["sounds"], list)
        self.assertIsInstance(parsed["costumes"], list)
        self.assertIsInstance(parsed["currentCostumeIndex"], int)
        self.assertIsInstance(parsed["scripts"], list)
    
    def test_format_with_multiple_blocks(self):
        """Test formatting multiple blocks"""
        blocks = [
            ScratchBlock(
                opcode="event_whenflagclicked",
                category="events",
                description="When green flag clicked"
            ),
            ScratchBlock(
                opcode="motion_movesteps",
                category="motion",
                inputs={"STEPS": 10},
                description="Move forward/backward by steps"
            )
        ]
        
        sequence = BlockSequence(
            blocks=blocks,
            explanation="Start and move",
            difficulty="beginner"
        )
        
        result = self.formatter.format(sequence)
        parsed = json.loads(result)
        
        # Should have scripts
        self.assertIsInstance(parsed["scripts"], list)
        if len(parsed["scripts"]) > 0:
            script = parsed["scripts"][0]
            self.assertIsInstance(script, dict)
            # Should have blocks within the script
            self.assertIn("blocks", script)
    
    def test_format_empty_sequence(self):
        """Test formatting empty block sequence"""
        empty_sequence = BlockSequence(blocks=[], explanation="", difficulty="beginner")
        
        result = self.formatter.format(empty_sequence)
        
        # Should still return valid JSON
        try:
            parsed = json.loads(result)
            self.assertIsInstance(parsed, dict)
        except json.JSONDecodeError:
            self.fail("Should return valid JSON even for empty sequence")
    
    def test_block_conversion(self):
        """Test individual block conversion"""
        block = ScratchBlock(
            opcode="motion_changexby",
            category="motion",
            inputs={"DX": 25},
            fields={"DIRECTION": "right"},
            description="Move horizontally"
        )
        
        sequence = BlockSequence(blocks=[block], explanation="Test", difficulty="beginner")
        result = self.formatter.format(sequence)
        parsed = json.loads(result)
        
        # Should have valid structure
        self.assertIn("scripts", parsed)


class TestFormatterIntegration(unittest.TestCase):
    """Integration tests for formatters"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.text_formatter = TextFormatter()
        self.pictoblox_formatter = PictoBloxFormatter()
        
        # Create a complex sequence for testing
        self.complex_sequence = BlockSequence(
            blocks=[
                ScratchBlock(
                    opcode="event_whenflagclicked",
                    category="events",
                    description="When green flag clicked"
                ),
                ScratchBlock(
                    opcode="motion_movesteps",
                    category="motion",
                    inputs={"STEPS": 10},
                    description="Move forward/backward by steps"
                ),
                ScratchBlock(
                    opcode="looks_say",
                    category="looks",
                    inputs={"MESSAGE": "Hello!"},
                    description="Say something"
                )
            ],
            explanation="Start program, move, and say hello",
            difficulty="intermediate"
        )
    
    def test_both_formatters_handle_same_sequence(self):
        """Test that both formatters can handle the same sequence"""
        text_result = self.text_formatter.format(self.complex_sequence)
        pictoblox_result = self.pictoblox_formatter.format(self.complex_sequence)
        
        # Both should return strings
        self.assertIsInstance(text_result, str)
        self.assertIsInstance(pictoblox_result, str)
        
        # Both should have content
        self.assertGreater(len(text_result), 0)
        self.assertGreater(len(pictoblox_result), 0)
        
        # PictoBlox result should be valid JSON
        try:
            json.loads(pictoblox_result)
        except json.JSONDecodeError:
            self.fail("PictoBlox formatter should return valid JSON")
    
    def test_formatters_with_different_difficulties(self):
        """Test formatters with different difficulty levels"""
        difficulties = ["beginner", "intermediate", "advanced"]
        
        for difficulty in difficulties:
            sequence = BlockSequence(
                blocks=[self.complex_sequence.blocks[0]],  # Single block
                explanation=f"Test {difficulty} level",
                difficulty=difficulty
            )
            
            text_result = self.text_formatter.format(sequence)
            pictoblox_result = self.pictoblox_formatter.format(sequence)
            
            # Both should work regardless of difficulty
            self.assertIsInstance(text_result, str)
            self.assertIsInstance(pictoblox_result, str)


if __name__ == '__main__':
    unittest.main()
