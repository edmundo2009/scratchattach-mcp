#!/usr/bin/env python3
"""
Quick test for block generation
"""

import sys
import os

# Add src directory to path
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)

try:
    from programming.block_generator import BlockGenerator
    from programming.parsers import NaturalLanguageParser
    from programming.formatters import TextFormatter
    
    print("Testing block generation...")
    
    parser = NaturalLanguageParser()
    generator = BlockGenerator()
    formatter = TextFormatter()
    
    # Test simple movement
    test_phrases = [
        "move the cat left 10 steps",
        "make the sprite move right",
        "move left by 5 steps"
    ]
    
    for phrase in test_phrases:
        print(f"\nTesting: '{phrase}'")
        intents = parser.parse(phrase)
        print(f"Parsed intents: {len(intents)}")
        
        if intents:
            for intent in intents:
                print(f"  Intent: action={intent.action}, parameters={intent.parameters}")
            
            blocks = generator.generate_blocks(intents)
            print(f"Generated blocks: {len(blocks.blocks)}")
            
            if blocks.blocks:
                for block in blocks.blocks:
                    print(f"  Block: {block.opcode} - {block.description}")
                    if hasattr(block, 'inputs') and block.inputs:
                        print(f"    Inputs: {block.inputs}")
            else:
                print("  No blocks generated")
                
            output = formatter.format(blocks)
            print(f"Formatted output: {output[:100]}...")
        else:
            print("  No intents parsed")
    
    print("\nTest completed!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
