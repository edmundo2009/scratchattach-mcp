# Setting up scratchattach-mcp with rovodev CLI

This tutorial will guide you through setting up the scratchattach-mcp server to work with the rovodev CLI (identical to Claude Code CLI), similar to how blender-mcp is configured.

## Overview

The scratchattach-mcp is an educational MCP server that provides:
- **Natural language to Scratch block generation** (as text/instructions, not directly in browser)
- **Scratch programming concept explanations** for learning
- **Scratch profile management** (with authentication)
- **Educational tools** for learning visual programming

## Important: What This Tool Does vs. What It Cannot Do

### ✅ What scratchattach-mcp CAN do:
- Generate Scratch block instructions from natural language
- Tell you exactly which blocks to use and how to configure them
- Explain Scratch programming concepts
- Provide step-by-step instructions for creating programs
- Help you learn Scratch programming

### ❌ What scratchattach-mcp CANNOT do:
- Control your web browser
- Automatically add blocks to your Scratch project at scratch.mit.edu
- Directly interact with the Scratch website
- Move or manipulate sprites in your browser

**You will need to manually add the suggested blocks to your Scratch project based on the instructions provided.**

## Prerequisites

1. **Python 3.7+** installed on your system
2. **rovodev CLI** installed and configured
3. **uvx** (recommended) or **pip** for package management

## Step 1: Install scratchattach-mcp

### Option A: Development Installation (Recommended for local setup)
```bash
# Navigate to the scratchattach-mcp directory
cd C:\Users\Administrator\CODE\scratchattach-mcp

# Install in development mode with pip
pip install -e .
```

### Option B: Using pip (if published to PyPI)
```bash
# Install the package globally
pip install scratchattach-mcp
```

### Option C: Using uvx (if published to PyPI)
```bash
# Install the package globally using uvx
uvx install scratchattach-mcp
```

**Note:** Since this is a local development project, Option A is recommended.

### Quick Setup for Your Environment
```bash
# Navigate to your project directory
cd C:\Users\Administrator\CODE\scratchattach-mcp

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .

# Test the installation
python test_installation.py
```

## Step 2: Configure rovodev CLI

### 2.1 Update config.yml

Edit your rovodev configuration file at `C:\Users\Administrator\.rovodev\config.yml`:

```yaml
# List of allowed MCP server names
allowedMcpServers:
  - github
  - blender
  - scratchattach  # Add this line
  # - npx -y @modelcontextprotocol/server-github
  # - uvx blender-mcp
  # - uvx scratchattach-mcp  # Add this line if using uvx
```

### 2.2 Update mcp.json

Edit your MCP configuration file at `C:\Users\Administrator\.rovodev\mcp.json`:

```json
{
  "github": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-github"
    ]
  },
  "blender": {
    "command": "uvx",
    "args": [
      "blender-mcp"
    ]
  },
  "scratchattach": {
    "command": "python",
    "args": [
      "C:\\Users\\Administrator\\CODE\\scratchattach-mcp\\src\\main.py"
    ]
  }
}
```

**Alternative configurations:**

If you successfully installed with `pip install -e .`:
```json
{
  "scratchattach": {
    "command": "scratchattach-mcp"
  }
}
```

Using the batch file:
```json
{
  "scratchattach": {
    "command": "C:\\Users\\Administrator\\CODE\\scratchattach-mcp\\run_mcp.bat"
  }
}
```

### 2.3 Create a Batch File (Alternative Method)

You can also create a batch file for easier execution:

Create `C:\Users\Administrator\CODE\scratchattach-mcp\run_mcp.bat`:
```batch
@echo off
cd /d "C:\Users\Administrator\CODE\scratchattach-mcp"
call venv\Scripts\activate.bat
python src/main.py
```

**Important:** This batch file activates your virtual environment before running the server, ensuring all dependencies are available.

Then use this configuration in mcp.json:
```json
{
  "scratchattach": {
    "command": "C:\\Users\\Administrator\\CODE\\scratchattach-mcp\\run_mcp.bat"
  }
}
```

## Step 3: Set Up Environment Variables (Optional)

For Scratch profile management features, create a `.env` file or set environment variables:

```bash
# Windows Command Prompt
set SCRATCH_USERNAME=your_scratch_username
set SCRATCH_PASSWORD=your_scratch_password

# Windows PowerShell
$env:SCRATCH_USERNAME="your_scratch_username"
$env:SCRATCH_PASSWORD="your_scratch_password"

# Or create a .env file in your project directory
SCRATCH_USERNAME=your_scratch_username
SCRATCH_PASSWORD=your_scratch_password
```

**Note:** The educational features (block generation, concept explanations) work without Scratch authentication.

## Step 4: Test the Installation

### 4.1 Run Installation Test
```bash
# Run the comprehensive test script
cd C:\Users\Administrator\CODE\scratchattach-mcp
python test_installation.py
```

This will verify that all components are working correctly.

### 4.2 Test MCP Server Directly
```bash
# If installed via development mode
scratchattach-mcp

# Or run directly from source
cd C:\Users\Administrator\CODE\scratchattach-mcp
python src/main.py

# Or use the batch file
run_mcp.bat

# Or if using uvx with development installation
uvx scratchattach-mcp
```

You should see output like:
```
Initializing block generation system...
✓ Block generation system initialized successfully
✓ Available actions: move, turn, say, play_sound, wait, repeat...
Starting scratchattach-edu MCP server...
Educational features available without Scratch login
```

### 4.3 Test with rovodev CLI
```bash
# Start rovodev CLI
rovodev

# In the CLI, test if scratchattach is available
# The server should be automatically loaded if configured correctly
```

## Step 5: Available Tools

Once configured, you'll have access to these tools through rovodev:

### Educational Tools (No Authentication Required)
- **generate_scratch_blocks**: Convert natural language to Scratch blocks
- **explain_scratch_concept**: Get kid-friendly explanations of programming concepts
- **get_system_status**: Check system component status

### Profile Management Tools (Requires Scratch Authentication)
- **set_my_about_me**: Update your Scratch profile's "About me" section
- **set_my_what_im_working_on**: Update "What I'm working on" section
- **get_user_info**: Get information about any Scratch user
- **get_project_info**: Get information about Scratch projects

## Step 6: Usage Examples

### Example 1: Generate Scratch Block Instructions
```
User: "Generate Scratch blocks to make the cat jump when space is pressed"
Response: The MCP will provide step-by-step instructions like:
1. Add "when [space] key pressed" event block
2. Add "change y by 50" motion block
3. Add "wait 0.1 seconds" control block
4. Add "change y by -50" motion block
```

### Example 2: Get Movement Instructions
```
User: "How do I make the cat move left 10 steps?"
Response: The MCP will tell you:
1. Use the "move 10 steps" block
2. Set the steps to -10 (negative for left movement)
3. Or use "change x by -10" for precise horizontal movement
```

### Example 3: Explain Programming Concepts
```
User: "Explain loops in Scratch for beginners"
Response: Educational explanation about what loops are and how to use them
```

### Example 4: Profile Management (with authentication)
```
User: "Set my Scratch profile to say I'm working on a platformer game"
Response: Updates your actual Scratch profile (requires login credentials)
```

## How to Use the Generated Instructions

1. **Ask rovodev for Scratch help**: "Generate blocks to make the cat move left"
2. **Get the instructions**: The MCP provides detailed block instructions
3. **Manually implement in Scratch**:
   - Open your Scratch project at https://scratch.mit.edu/projects/editor/
   - Follow the provided instructions to add the suggested blocks
   - Drag and connect the blocks as described

## Troubleshooting

### Common Issues

1. **"Module not found" error**
   - Ensure scratchattach-mcp is properly installed
   - Check if uvx or pip installation completed successfully

2. **"Block generation system not available"**
   - Check if all dependencies are installed: `pip install -r requirements.txt`
   - Verify Python version is 3.7+

3. **Scratch authentication fails**
   - Verify SCRATCH_USERNAME and SCRATCH_PASSWORD are set correctly
   - Note: Educational features work without authentication

4. **rovodev doesn't recognize the server**
   - Double-check config.yml and mcp.json syntax
   - Ensure "scratchattach" is in allowedMcpServers list
   - Restart rovodev CLI after configuration changes

### Verification Commands

```bash
# Check if uvx can find the package
uvx --help scratchattach-mcp

# Check Python module installation
python -c "import scratchattach; print('scratchattach installed')"
python -c "from mcp.server import FastMCP; print('MCP installed')"

# Test direct execution
python -c "from src.main import mcp; print('scratchattach-mcp ready')"
```

## Configuration Files Summary

**config.yml location:** `C:\Users\Administrator\.rovodev\config.yml`
```yaml
allowedMcpServers:
  - scratchattach
```

**mcp.json location:** `C:\Users\Administrator\.rovodev\mcp.json`
```json
{
  "scratchattach": {
    "command": "uvx",
    "args": ["scratchattach-mcp"]
  }
}
```

## Next Steps

1. Test the basic functionality with simple block generation
2. Explore educational features for learning Scratch programming
3. Set up Scratch authentication for profile management features
4. Integrate with your educational workflow or projects

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Verify all configuration files are correctly formatted
3. Test the MCP server independently before using with rovodev
4. Ensure all dependencies are properly installed

The scratchattach-mcp server is now ready to use with rovodev CLI for educational Scratch programming assistance!

## Quick Reference

### Essential Commands
```bash
# Install in development mode
cd C:\Users\Administrator\CODE\scratchattach-mcp
pip install -e .

# Test installation
python test_installation.py

# Run MCP server
scratchattach-mcp
# or
python src/main.py
# or
run_mcp.bat
```

### Key Configuration Files
- **rovodev config**: `C:\Users\Administrator\.rovodev\config.yml`
- **MCP config**: `C:\Users\Administrator\.rovodev\mcp.json`
- **Environment variables**: Set `SCRATCH_USERNAME` and `SCRATCH_PASSWORD` for profile features

### Minimal Working Configuration

**config.yml:**
```yaml
allowedMcpServers:
  - scratchattach
```

**mcp.json:**
```json
{
  "scratchattach": {
    "command": "python",
    "args": [
      "C:\\Users\\Administrator\\CODE\\scratchattach-mcp\\src\\main.py"
    ]
  }
}
```

This setup provides a complete educational Scratch programming assistant through the rovodev CLI!
