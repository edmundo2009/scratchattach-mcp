#!/usr/bin/env python3
"""
Test script to verify scratchattach-mcp installation and functionality
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import scratchattach as sa
        print("✓ scratchattach imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import scratchattach: {e}")
        return False
    
    try:
        from mcp.server import FastMCP
        print("✓ MCP server imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import MCP server: {e}")
        return False
    
    try:
        from programming.block_generator import BlockGenerator
        from programming.parsers import NaturalLanguageParser
        from programming.formatters import TextFormatter, PictoBloxFormatter
        print("✓ Block generation system imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import block generation system: {e}")
        return False
    
    return True

def test_block_generation():
    """Test basic block generation functionality"""
    print("\nTesting block generation...")
    
    try:
        from programming.block_generator import BlockGenerator
        from programming.parsers import NaturalLanguageParser
        from programming.formatters import TextFormatter
        
        parser = NaturalLanguageParser()
        generator = BlockGenerator()
        formatter = TextFormatter()
        
        # Test simple generation
        intents = parser.parse("make the cat say hello")
        if intents:
            blocks = generator.generate_blocks(intents)
            output = formatter.format(blocks)
            print("✓ Block generation test passed")
            print(f"  Sample output: {output[:100]}...")
            return True
        else:
            print("✗ Parser returned no intents")
            return False
            
    except Exception as e:
        print(f"✗ Block generation test failed: {e}")
        return False

def test_mcp_server():
    """Test MCP server initialization"""
    print("\nTesting MCP server...")
    
    try:
        from mcp.server import FastMCP
        mcp = FastMCP("test-server")
        print("✓ MCP server initialization test passed")
        return True
    except Exception as e:
        print(f"✗ MCP server test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=== scratchattach-mcp Installation Test ===\n")
    
    # Add src directory to path for imports
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    if os.path.exists(src_path):
        sys.path.insert(0, src_path)
        print(f"Added {src_path} to Python path")
    
    tests = [
        test_imports,
        test_block_generation,
        test_mcp_server
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=== Test Results ===")
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed! scratchattach-mcp is ready to use.")
        return 0
    else:
        print("✗ Some tests failed. Check the output above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
