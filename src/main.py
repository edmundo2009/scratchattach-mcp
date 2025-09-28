# src/main.py - Revised with Decoupled Initialization

import os
import sys
import json
from typing import List, Dict, Any, Optional

# Import existing scratchattach functionality
import scratchattach as sa
from mcp import FastMCP

# Import our new block generation system
from programming.block_generator import (
    NaturalLanguageParser,
    BlockGenerator,
    Intent,
    ScratchBlock,
    BlockSequence
)
from programming.formatters import TextFormatter, PictoBloxFormatter, ScratchOnlineFormatter

# --- REVISED INITIALIZATION SECTION ---

# Initialize MCP server
mcp = FastMCP("scratchattach-edu")

# Initialize the block generation system FIRST (stateless, no Scratch session required)
try:
    print("Initializing block generation system...")

    # These components don't need Scratch authentication
    parser = NaturalLanguageParser()
    generator = BlockGenerator()  # Now loads from knowledge base
    text_formatter = TextFormatter()
    pictoblox_formatter = PictoBloxFormatter()
    scratch_formatter = ScratchOnlineFormatter()

    print("✓ Block generation system initialized successfully")
    print(
        f"✓ Available actions: {', '.join(generator.get_available_actions()[:10])}...")

except Exception as e:
    print(f"✗ Failed to initialize block generation system: {e}")
    print("This is critical - block generation features will not work")
    # We can still continue for original Scratch profile features
    generator = None
    parser = None

# Global variables for Scratch session management (separate concern)
session = None
me = None


def initialize_scratch_session():
    """Initialize Scratch session - focused only on authentication"""
    global session, me

    username = os.environ.get("SCRATCH_USERNAME")
    password = os.environ.get("SCRATCH_PASSWORD")

    if not username or not password:
        print("Warning: SCRATCH_USERNAME and SCRATCH_PASSWORD not set")
        print("Profile management features will be disabled")
        return False

    try:
        print("Authenticating with Scratch...")
        session = sa.login(username, password)
        me = session.get_linked_user()
        print(f"✓ Successfully authenticated as {me.username}")
        return True

    except Exception as e:
        print(f"✗ Scratch authentication failed: {e}")
        print("Profile management features will be disabled")
        return False

# --- MCP TOOLS SECTION ---

# Educational tools (work without Scratch authentication)


@mcp.tool()
def generate_scratch_blocks(description: str, output_format: str = "text"):
    """
    Convert natural language description to Scratch programming blocks.
    Works without Scratch login - purely educational.

    Args:
        description: Natural language description (e.g., "make the cat jump when space is pressed")
        output_format: "text", "pictoblox", "scratch", or "blocks"

    Returns:
        Generated Scratch program in requested format
    """
    if not generator or not parser:
        return {
            "success": False,
            "message": "Block generation system not available. Check initialization logs.",
            "error_type": "system_unavailable"
        }

    try:
        # Parse the natural language input
        intents = parser.parse(description)

        if not intents:
            return {
                "success": False,
                "message": "I didn't understand that request.",
                "suggestions": [
                    "make the cat move right 10 steps",
                    "when space key pressed jump up",
                    "play sound when sprite clicked",
                    "make the sprite say hello"
                ],
                "available_actions": generator.get_available_actions()
            }

        # Generate block sequence
        block_sequence = generator.generate_blocks(intents)

        # Format output based on request
        formatters = {
            "text": text_formatter,
            "pictoblox": pictoblox_formatter,
            "scratch": scratch_formatter
        }

        if output_format in formatters:
            formatted_output = formatters[output_format].format(block_sequence)
            return {
                "success": True,
                "format": output_format,
                "content": formatted_output,
                "difficulty": block_sequence.difficulty,
                "explanation": block_sequence.explanation,
                "block_count": len(block_sequence.blocks),
                "filename": f"generated_project.{'pbl' if output_format == 'pictoblox' else 'sb3' if output_format == 'scratch' else 'txt'}"
            }

        elif output_format == "blocks":
            # Return raw block data for debugging/advanced use
            from dataclasses import asdict
            blocks_data = [asdict(block) for block in block_sequence.blocks]
            return {
                "success": True,
                "format": "blocks",
                "content": {
                    "blocks": blocks_data,
                    "explanation": block_sequence.explanation,
                    "difficulty": block_sequence.difficulty,
                    "intents_parsed": [asdict(intent) for intent in intents]
                }
            }

        else:
            return {
                "success": False,
                "message": f"Unknown output format: {output_format}",
                "available_formats": ["text", "pictoblox", "scratch", "blocks"]
            }

    except Exception as e:
        return {
            "success": False,
            "message": f"Error generating blocks: {str(e)}",
            "error_type": "generation_error",
            "debug_info": {
                "input": description,
                "format": output_format,
                "generator_available": generator is not None
            }
        }


@mcp.tool()
def explain_scratch_concept(concept: str, age_level: str = "beginner"):
    """
    Explain Scratch programming concepts in kid-friendly language.
    Works without Scratch login - purely educational.

    Args:
        concept: Programming concept to explain (e.g., "loops", "events", "sprites")
        age_level: "beginner", "intermediate", "advanced"
    """
    try:
        explanations = {
            "loops": {
                "beginner": "Loops are like doing something over and over again! Like when you brush your teeth - you move the brush back and forth many times. In Scratch, we use the 'forever' block to make things repeat!",
                "intermediate": "Loops let you repeat code without writing it multiple times. The 'forever' block runs code continuously, while 'repeat 10' runs it exactly 10 times. This makes animations and games possible!",
                "advanced": "Loops are control structures that enable iteration. Scratch offers forever loops (infinite), counted loops (repeat n), and conditional loops (repeat until). They're essential for efficient code and complex behaviors."
            },
            "events": {
                "beginner": "Events are like magic triggers! When something happens (like clicking the green flag or pressing a key), your program starts running. It's like a doorbell - when someone presses it, it makes a sound!",
                "intermediate": "Events are how your program responds to user actions or conditions. The green hat blocks (like 'when flag clicked') start your scripts when specific things happen. This makes your programs interactive!",
                "advanced": "Events implement the observer pattern in visual programming. Scratch uses event-driven architecture where hat blocks register listeners for user inputs, broadcast messages, and sensor changes."
            },
            "sprites": {
                "beginner": "Sprites are the characters in your Scratch program! They can be animals, people, objects - anything you want. You can make them move, talk, and do fun things. It's like having toy characters that come to life!",
                "intermediate": "Sprites are programmable objects that have costumes (how they look) and scripts (what they do). Each sprite can have its own code, and they can interact with each other through messages and collision detection.",
                "advanced": "Sprites are autonomous objects with encapsulated state (position, costumes, variables) and behavior (scripts). They support inheritance through cloning and polymorphism through broadcast message handling."
            },
            "blocks": {
                "beginner": "Blocks are like puzzle pieces that tell your sprite what to do! You snap them together to create programs. Different colored blocks do different things - blue blocks make things move, purple blocks change how things look!",
                "intermediate": "Blocks are visual programming commands that execute specific functions. They're color-coded by category (motion, looks, sound, etc.) and snap together to form scripts that control sprite behavior.",
                "advanced": "Blocks represent discrete programming instructions in a visual syntax tree. Each block encapsulates specific functionality with defined inputs/outputs, enabling drag-and-drop programming while maintaining computational completeness."
            }
        }

        concept_lower = concept.lower()
        if concept_lower in explanations:
            explanation = explanations[concept_lower].get(
                age_level, explanations[concept_lower]["beginner"])

            # Add relevant examples based on concept
            examples = _generate_concept_examples(concept_lower)
            related = _get_related_concepts(concept_lower)

            return {
                "success": True,
                "concept": concept,
                "age_level": age_level,
                "explanation": explanation,
                "examples": examples,
                "related_concepts": related,
                "try_next": f"Ask me to explain: {', '.join(related[:3])}"
            }

        else:
            available_concepts = list(explanations.keys())
            return {
                "success": False,
                "message": f"I don't have an explanation for '{concept}' yet.",
                "available_concepts": available_concepts,
                "suggestion": f"Try asking about: {', '.join(available_concepts)}"
            }

    except Exception as e:
        return {
            "success": False,
            "message": f"Error explaining concept: {str(e)}",
            "error_type": "explanation_error"
        }

# Scratch profile management tools (require authentication)


@mcp.tool()
def set_my_about_me(text: str):
    """Set the 'About me' section of the authenticated user's profile"""
    if not session or not me:
        return {
            "success": False,
            "message": "Scratch authentication required. Set SCRATCH_USERNAME and SCRATCH_PASSWORD environment variables.",
            "error_type": "authentication_required"
        }

    try:
        me.set_bio(text)
        return {"success": True, "message": "Profile updated successfully!"}
    except Exception as e:
        return {"success": False, "message": str(e), "error_type": "scratch_api_error"}


@mcp.tool()
def set_my_what_im_working_on(text: str):
    """Set the 'What I'm working on' section of the authenticated user's profile"""
    if not session or not me:
        return {
            "success": False,
            "message": "Scratch authentication required. Set SCRATCH_USERNAME and SCRATCH_PASSWORD environment variables.",
            "error_type": "authentication_required"
        }

    try:
        me.set_wiwo(text)
        return {"success": True, "message": "Profile updated successfully!"}
    except Exception as e:
        return {"success": False, "message": str(e), "error_type": "scratch_api_error"}


@mcp.tool()
def get_user_info(username: str):
    """Get information about a Scratch user"""
    if not session:
        return {
            "success": False,
            "message": "Scratch authentication required for user lookup.",
            "error_type": "authentication_required"
        }

    try:
        user = session.connect_user(username)
        data = {k: v for k, v in user.__dict__.items()
                if not k.startswith("_") and not k.startswith("update")}
        return {"success": True, "data": data}
    except sa.exceptions.UserNotFound:
        return {"success": False, "message": "User not found", "error_type": "user_not_found"}
    except Exception as e:
        return {"success": False, "message": str(e), "error_type": "scratch_api_error"}


@mcp.tool()
def get_project_info(id: int):
    """Get information about a Scratch project"""
    if not session:
        return {
            "success": False,
            "message": "Scratch authentication required for project lookup.",
            "error_type": "authentication_required"
        }

    try:
        project = session.connect_project(id)
        data = {k: v for k, v in project.__dict__.items()
                if not k.startswith("_") and not k.startswith("update")}
        return {"success": True, "data": data}
    except sa.exceptions.ProjectNotFound:
        return {"success": False, "message": "Project not found", "error_type": "project_not_found"}
    except Exception as e:
        return {"success": False, "message": str(e), "error_type": "scratch_api_error"}

# Helper functions


def _generate_concept_examples(concept: str) -> List[str]:
    """Generate relevant examples for a concept"""
    examples_map = {
        "loops": [
            "Try: 'make the cat move right forever'",
            "Try: 'repeat jumping 5 times'"
        ],
        "events": [
            "Try: 'when space pressed make cat jump'",
            "Try: 'when flag clicked start music'"
        ],
        "sprites": [
            "Try: 'make the cat say hello'",
            "Try: 'when cat clicked change color'"
        ],
        "blocks": [
            "Try: 'move 10 steps' (motion block)",
            "Try: 'play sound meow' (sound block)"
        ]
    }
    return examples_map.get(concept, [])


def _get_related_concepts(concept: str) -> List[str]:
    """Get related concepts for learning progression"""
    relations = {
        "loops": ["events", "motion", "animation"],
        "events": ["loops", "user_input", "interactivity"],
        "sprites": ["costumes", "motion", "coordinates"],
        "blocks": ["scripts", "categories", "inputs"]
    }
    return relations.get(concept, [])

# System status tool


@mcp.tool()
def get_system_status():
    """Get status of all system components"""
    return {
        "block_generation": {
            "available": generator is not None and parser is not None,
            "available_actions": generator.get_available_actions() if generator else [],
            "formatters": ["text", "pictoblox", "scratch", "blocks"]
        },
