scratchattach-mcp-educational/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup.py                    # For easy installation
│
├── src/
│   ├── main.py                 # Enhanced MCP server
│   │
│   ├── programming/
│   │   ├── __init__.py
│   │   ├── block_generator.py  # Data-driven block generation
│   │   ├── parsers.py          # Natural language parsers
│   │   └── formatters.py       # Output formatters
│   │
│   ├── knowledge/
│   │   ├── __init__.py
│   │   ├── scratch_blocks.json # Comprehensive block definitions
│   │   ├── patterns.json       # Programming patterns
│   │   └── tutorials.json      # Pre-built tutorial templates
│   │
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py          # Utility functions
│       └── validators.py       # Input validation
│
├── tests/
│   ├── __init__.py
│   ├── test_block_generation.py
│   ├── test_parsers.py
│   ├── test_formatters.py
│   ├── test_mcp_integration.py
│   └── fixtures/
│       ├── sample_inputs.json
│       └── expected_outputs.json
│
├── examples/
│   ├── sample_queries.md
│   ├── generated_projects/
│   │   ├── simple_jump.pbl
│   │   ├── keyboard_control.sb3
│   │   └── bouncing_ball.txt
│   └── mcp_client_examples.py
│
└── docs/
    ├── user_guide.md
    ├── api_reference.md
    ├── educational_philosophy.md
    └── troubleshooting.md