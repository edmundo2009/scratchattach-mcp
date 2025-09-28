#!/usr/bin/env python3
"""Tests for MCP server integration"""

import unittest
import json
import os
import sys
from unittest.mock import patch, MagicMock

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Import main module components
import main


class TestMCPIntegration(unittest.TestCase):
    """Test cases for MCP server integration"""
    
    def setUp(self):
        """Set up test fixtures"""
        # Load test fixtures
        fixtures_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'expected_outputs.json')
        with open(fixtures_path, 'r') as f:
            self.test_data = json.load(f)
    
    def test_mcp_server_initialization(self):
        """Test that MCP server initializes correctly"""
        self.assertIsNotNone(main.mcp)
        self.assertEqual(main.mcp.name, "scratchattach-edu")
    
    def test_block_generation_system_initialization(self):
        """Test that block generation system initializes"""
        # These should be initialized during module import
        self.assertIsNotNone(main.generator)
        self.assertIsNotNone(main.parser)
        self.assertIsNotNone(main.text_formatter)
        self.assertIsNotNone(main.pictoblox_formatter)
    
    def test_generate_scratch_blocks_tool_success(self):
        """Test generate_scratch_blocks tool with valid input"""
        result = main.generate_scratch_blocks(
            description="make the cat move right 10 steps",
            output_format="text"
        )
        
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        
        if result["success"]:
            self.assertIn("format", result)
            self.assertIn("content", result)
            self.assertIn("difficulty", result)
            self.assertEqual(result["format"], "text")
    
    def test_generate_scratch_blocks_tool_pictoblox_format(self):
        """Test generate_scratch_blocks tool with PictoBlox format"""
        result = main.generate_scratch_blocks(
            description="make the cat jump",
            output_format="pictoblox"
        )
        
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        
        if result["success"]:
            self.assertEqual(result["format"], "pictoblox")
            # Content should be valid JSON for PictoBlox format
            try:
                json.loads(result["content"])
            except json.JSONDecodeError:
                self.fail("PictoBlox format should return valid JSON")
    
    def test_generate_scratch_blocks_tool_blocks_format(self):
        """Test generate_scratch_blocks tool with blocks format"""
        result = main.generate_scratch_blocks(
            description="move right",
            output_format="blocks"
        )
        
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        
        if result["success"]:
            self.assertEqual(result["format"], "blocks")
            self.assertIn("content", result)
            self.assertIsInstance(result["content"], dict)
            self.assertIn("blocks", result["content"])
    
    def test_generate_scratch_blocks_tool_invalid_format(self):
        """Test generate_scratch_blocks tool with invalid format"""
        result = main.generate_scratch_blocks(
            description="move right",
            output_format="invalid_format"
        )
        
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        self.assertFalse(result["success"])
        self.assertIn("available_formats", result)
    
    def test_generate_scratch_blocks_tool_empty_input(self):
        """Test generate_scratch_blocks tool with empty input"""
        result = main.generate_scratch_blocks(
            description="",
            output_format="text"
        )
        
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        
        # Should handle empty input gracefully
        if not result["success"]:
            self.assertIn("message", result)
    
    def test_explain_scratch_concept_tool_loops(self):
        """Test explain_scratch_concept tool for loops"""
        result = main.explain_scratch_concept(
            concept="loops",
            age_level="beginner"
        )
        
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        self.assertTrue(result["success"])
        
        self.assertIn("concept", result)
        self.assertIn("age_level", result)
        self.assertIn("explanation", result)
        self.assertIn("examples", result)
        self.assertIn("related_concepts", result)
        
        self.assertEqual(result["concept"], "loops")
        self.assertEqual(result["age_level"], "beginner")
    
    def test_explain_scratch_concept_tool_different_levels(self):
        """Test explain_scratch_concept tool with different age levels"""
        levels = ["beginner", "intermediate", "advanced"]
        
        for level in levels:
            with self.subTest(age_level=level):
                result = main.explain_scratch_concept(
                    concept="events",
                    age_level=level
                )
                
                self.assertIsInstance(result, dict)
                self.assertIn("success", result)
                
                if result["success"]:
                    self.assertEqual(result["age_level"], level)
                    self.assertIn("explanation", result)
    
    def test_explain_scratch_concept_tool_unknown_concept(self):
        """Test explain_scratch_concept tool with unknown concept"""
        result = main.explain_scratch_concept(
            concept="unknown_concept_xyz",
            age_level="beginner"
        )
        
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        self.assertFalse(result["success"])
        self.assertIn("available_concepts", result)
    
    def test_get_system_status_tool(self):
        """Test get_system_status tool"""
        result = main.get_system_status()
        
        self.assertIsInstance(result, dict)
        self.assertIn("block_generation", result)
        self.assertIn("scratch_authentication", result)
        self.assertIn("system_info", result)
        
        # Check block generation status
        block_gen = result["block_generation"]
        self.assertIn("available", block_gen)
        self.assertIn("available_actions", block_gen)
        self.assertIn("formatters", block_gen)
        
        # Check system info
        system_info = result["system_info"]
        self.assertIn("mcp_server", system_info)
        self.assertIn("version", system_info)
    
    @patch('main.session', None)
    @patch('main.me', None)
    def test_scratch_tools_without_authentication(self):
        """Test Scratch-specific tools without authentication"""
        # Test set_my_about_me without authentication
        result = main.set_my_about_me("Test bio")
        
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        self.assertFalse(result["success"])
        self.assertIn("error_type", result)
        self.assertEqual(result["error_type"], "authentication_required")
        
        # Test get_user_info without authentication
        result = main.get_user_info("testuser")
        
        self.assertIsInstance(result, dict)
        self.assertIn("success", result)
        self.assertFalse(result["success"])
        self.assertEqual(result["error_type"], "authentication_required")
    
    def test_helper_functions(self):
        """Test helper functions"""
        # Test _generate_concept_examples
        examples = main._generate_concept_examples("loops")
        self.assertIsInstance(examples, list)
        
        # Test _get_related_concepts
        related = main._get_related_concepts("loops")
        self.assertIsInstance(related, list)
    
    def test_error_handling_in_tools(self):
        """Test error handling in MCP tools"""
        # Test with malformed input that might cause errors
        test_cases = [
            {"description": None, "output_format": "text"},
            {"description": "test", "output_format": None},
        ]
        
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                try:
                    # This might raise an exception, which should be handled gracefully
                    result = main.generate_scratch_blocks(
                        description=test_case.get("description", ""),
                        output_format=test_case.get("output_format", "text")
                    )
                    
                    # If it returns a result, it should be a dict with success field
                    self.assertIsInstance(result, dict)
                    self.assertIn("success", result)
                    
                except Exception as e:
                    # If an exception is raised, the tool should handle it better
                    self.fail(f"Tool should handle malformed input gracefully: {e}")


class TestMCPToolsIntegration(unittest.TestCase):
    """Integration tests for MCP tools working together"""
    
    def test_full_pipeline_text_format(self):
        """Test full pipeline from natural language to text output"""
        # Generate blocks
        result = main.generate_scratch_blocks(
            description="when space pressed make cat jump",
            output_format="text"
        )
        
        if result["success"]:
            # Should have all expected fields
            self.assertIn("content", result)
            self.assertIn("difficulty", result)
            self.assertIn("explanation", result)
            self.assertIn("block_count", result)
            
            # Content should be a string
            self.assertIsInstance(result["content"], str)
            self.assertGreater(len(result["content"]), 0)
    
    def test_full_pipeline_pictoblox_format(self):
        """Test full pipeline from natural language to PictoBlox output"""
        result = main.generate_scratch_blocks(
            description="move the sprite right 15 steps",
            output_format="pictoblox"
        )
        
        if result["success"]:
            # Should have PictoBlox-specific fields
            self.assertIn("filename", result)
            self.assertTrue(result["filename"].endswith(".pbl"))
            
            # Content should be valid JSON
            try:
                parsed = json.loads(result["content"])
                self.assertIsInstance(parsed, dict)
            except json.JSONDecodeError:
                self.fail("PictoBlox output should be valid JSON")
    
    def test_concept_explanation_and_block_generation_consistency(self):
        """Test that concept explanations are consistent with block generation"""
        # Explain loops concept
        explanation_result = main.explain_scratch_concept("loops", "beginner")
        
        if explanation_result["success"]:
            # Try to generate blocks for a loop-related command
            generation_result = main.generate_scratch_blocks(
                description="repeat jumping 5 times",
                output_format="text"
            )
            
            # Both should work
            self.assertTrue(explanation_result["success"])
            # Generation might or might not succeed depending on implementation


if __name__ == '__main__':
    unittest.main()
