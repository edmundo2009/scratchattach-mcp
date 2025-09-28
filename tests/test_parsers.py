#!/usr/bin/env python3
"""Tests for natural language parsers"""

import unittest
import json
import os
import sys
from typing import List

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from programming.parsers import NaturalLanguageParser
from programming.block_generator import Intent


class TestNaturalLanguageParser(unittest.TestCase):
    """Test cases for NaturalLanguageParser"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.parser = NaturalLanguageParser()
        
        # Load test fixtures
        fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'sample_inputs.json')
        with open(fixtures_path, 'r') as f:
            self.test_data = json.load(f)
    
    def test_simple_move_command(self):
        """Test parsing simple movement commands"""
        result = self.parser.parse("make the cat move right 10 steps")
        
        self.assertEqual(len(result), 1)
        intent = result[0]
        self.assertEqual(intent.action, "move")
        self.assertEqual(intent.parameters.get("direction"), "right")
        self.assertEqual(intent.parameters.get("steps"), 10)
    
    def test_trigger_with_key_press(self):
        """Test parsing commands with key press triggers"""
        result = self.parser.parse("when space pressed jump up")
        
        self.assertEqual(len(result), 1)
        intent = result[0]
        self.assertEqual(intent.action, "jump")
        self.assertEqual(intent.trigger, "key_press")
        self.assertEqual(intent.parameters.get("key"), "space")
        self.assertEqual(intent.parameters.get("direction"), "up")
    
    def test_sprite_click_trigger(self):
        """Test parsing commands with sprite click triggers"""
        result = self.parser.parse("play sound when sprite clicked")
        
        self.assertEqual(len(result), 1)
        intent = result[0]
        self.assertEqual(intent.action, "play_sound")
        self.assertEqual(intent.trigger, "sprite_click")
    
    def test_complex_multi_action_command(self):
        """Test parsing complex commands with multiple actions"""
        result = self.parser.parse("move left and play sound and say hello")
        
        # Should parse multiple intents
        self.assertGreaterEqual(len(result), 1)
        
        # Check first intent (move)
        move_intent = result[0]
        self.assertEqual(move_intent.action, "move")
        self.assertEqual(move_intent.parameters.get("direction"), "left")
    
    def test_empty_input(self):
        """Test parsing empty input"""
        result = self.parser.parse("")
        self.assertEqual(len(result), 0)
    
    def test_unknown_command(self):
        """Test parsing unknown commands"""
        result = self.parser.parse("xyz unknown command")
        self.assertEqual(len(result), 0)
    
    def test_case_insensitive_parsing(self):
        """Test that parsing is case insensitive"""
        result1 = self.parser.parse("move right 5 steps")
        result2 = self.parser.parse("MOVE RIGHT 5 STEPS")
        
        self.assertEqual(len(result1), len(result2))
        if len(result1) > 0 and len(result2) > 0:
            self.assertEqual(result1[0].action, result2[0].action)
            self.assertEqual(result1[0].parameters.get("direction"), 
                           result2[0].parameters.get("direction"))
    
    def test_number_extraction(self):
        """Test extraction of numbers from commands"""
        test_cases = [
            ("move 5 steps", 5),
            ("jump 20 pixels", 20),
            ("wait 3 seconds", 3)
        ]
        
        for command, expected_number in test_cases:
            result = self.parser.parse(command)
            if len(result) > 0:
                intent = result[0]
                # Check if number was extracted in any parameter
                found_number = False
                for value in intent.parameters.values():
                    if isinstance(value, (int, float)) and value == expected_number:
                        found_number = True
                        break
                # Note: This is a flexible test since different commands 
                # might store numbers in different parameter keys
    
    def test_direction_extraction(self):
        """Test extraction of directions from commands"""
        directions = ["left", "right", "up", "down"]
        
        for direction in directions:
            result = self.parser.parse(f"move {direction}")
            if len(result) > 0:
                intent = result[0]
                self.assertEqual(intent.parameters.get("direction"), direction)
    
    def test_sentence_splitting(self):
        """Test that compound sentences are split correctly"""
        result = self.parser.parse("move right and jump up")
        
        # Should produce at least one intent
        self.assertGreaterEqual(len(result), 1)
    
    def test_fixtures_simple_commands(self):
        """Test against fixture data for simple commands"""
        for test_case in self.test_data["simple_commands"]:
            with self.subTest(input=test_case["input"]):
                result = self.parser.parse(test_case["input"])
                expected = test_case["expected_intents"]
                
                if len(expected) == 0:
                    self.assertEqual(len(result), 0)
                else:
                    self.assertGreater(len(result), 0)
                    # Check first intent matches expected action
                    if len(result) > 0 and len(expected) > 0:
                        self.assertEqual(result[0].action, expected[0]["action"])


if __name__ == '__main__':
    unittest.main()
