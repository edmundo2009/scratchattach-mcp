@echo off
chcp 65001 >nul
cd /d "C:\Users\Administrator\CODE\scratchattach-mcp"
call venv\Scripts\activate.bat
set PYTHONIOENCODING=utf-8
python src/main.py
