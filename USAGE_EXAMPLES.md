# How to Use scratchattach-mcp with Scratch Editor

This document shows exactly how the scratchattach-mcp works with your Scratch editor.

## Important: Manual Implementation Required

The MCP server provides **instructions and guidance** - you must manually add the blocks to your Scratch project.

## Example Workflow

### Step 1: Ask rovodev for help
In rovodev CLI, ask:
```
"Generate Scratch blocks to make the cat move left 10 steps"
```

### Step 2: Get the instructions
The MCP server responds with something like:
```
To make the cat move left 10 steps:

1. Use the "move 10 steps" block from the Motion category
2. Set the steps value to -10 (negative for left movement)
3. This will make your sprite move 10 steps to the left

Block details:
- Block: motion_movesteps
- Category: Motion (blue blocks)
- Input: STEPS = -10
```

### Step 3: Implement in Scratch manually
Now in your Scratch editor (https://scratch.mit.edu/projects/editor/):

1. **Find the Motion category** (blue blocks on the left)
2. **Drag the "move 10 steps" block** to your scripts area
3. **Change the number from 10 to -10** by clicking on it
4. **Connect it to an event block** like "when green flag clicked"

## More Complex Example

### Ask rovodev:
```
"Create a program where the cat jumps when space is pressed"
```

### MCP Response:
```
To make the cat jump when space is pressed:

1. Event block: "when [space] key pressed"
   - From Events category (yellow blocks)
   - Select "space" from the dropdown

2. Motion blocks for jumping:
   - "change y by 50" (move up)
   - "wait 0.2 seconds" (pause at top)
   - "change y by -50" (move down)

Stack these blocks together in this order.
```

### Manual Implementation:
1. Go to **Events** (yellow) → drag "when key pressed" block
2. Click dropdown, select "space"
3. Go to **Motion** (blue) → drag "change y by 10" block
4. Change "10" to "50", connect under the event block
5. Go to **Control** (orange) → drag "wait 1 seconds" block
6. Change "1" to "0.2", connect under the motion block
7. Add another "change y by 10" block, change to "-50"

## What Each Output Format Provides

### Text Format (Default)
- Human-readable instructions
- Step-by-step guidance
- Educational explanations

### PictoBlox Format
- More technical block specifications
- Useful for advanced users
- Shows exact block opcodes

### Blocks Format
- Raw data structure
- For debugging or advanced analysis
- Shows parsed intents and parameters

## Tips for Using with Scratch Editor

1. **Keep both windows open**: rovodev CLI and Scratch editor
2. **Ask specific questions**: "How do I make the sprite turn right 90 degrees?"
3. **Request explanations**: "Explain how loops work in Scratch"
4. **Use different formats**: Try "output_format": "pictoblox" for more technical details
5. **Build incrementally**: Start with simple movements, add complexity

## Common Questions

**Q: Why doesn't it automatically add blocks to my Scratch project?**
A: Browser security prevents external programs from controlling web pages. You must manually implement the suggestions.

**Q: Can it see my current Scratch project?**
A: No, it works independently. It provides general guidance based on your requests.

**Q: What if the instructions don't work exactly?**
A: Scratch versions may vary slightly. Use the instructions as guidance and adapt as needed.

**Q: Can it help with specific Scratch projects?**
A: Yes! Describe what you want to create, and it will provide step-by-step block instructions.

## Example Requests That Work Well

- "Make the cat walk back and forth"
- "Create a simple jumping game"
- "How do I make a sprite follow the mouse?"
- "Explain how to use if-then blocks"
- "Make the sprite change color when clicked"
- "Create a simple animation loop"

Remember: The MCP is your **Scratch programming tutor** - it teaches you what to do, but you implement it manually in the Scratch editor!
