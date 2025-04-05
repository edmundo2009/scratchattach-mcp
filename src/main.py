from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import scratchattach as sa
from dotenv import load_dotenv
import os
import json

load_dotenv()

mcp = FastMCP("scratchattach")

try:
    session = sa.login(username=os.environ.get("SCRATCH_USERNAME"), password=os.environ.get("SCRATCH_PASSWORD"))
except sa.utils.exceptions.LoginFailure:
    print("Failed to log in. Please make sure you have the correct credentials in your .env file.")
    os._exit(1)

print(f"Logged in as {session.username}")
me = session.get_linked_user()

@mcp.tool()
def set_my_about_me(text: str) -> str:
    try:
        me.set_bio(text)
        return "Success!"
    except Exception as e:
        return f"Error: {e}"
    
@mcp.tool()
def set_my_what_im_working_on(text: str) -> str:
    try:
        me.set_wiwo(text)
        return "Success!"
    except Exception as e:
        return f"Error: {e}"
    
@mcp.tool()
def get_user_info(username: str) -> str:
    try:
        user = session.connect_user(username)
        data = {k: v for k, v in user.__dict__.items() if not k.startswith("_") and not k.startswith("update")}
        return json.dumps(data)
    except sa.utils.exceptions.UserNotFound:
        return "User not found."
    except Exception as e:
        return f"Unexpected error: {e}"
    
@mcp.tool()
def get_project_info(id: int) -> str:
    try:
        project = session.connect_project(id)
        data = {k: v for k, v in project.__dict__.items() if not k.startswith("_") and not k.startswith("update") and not k.startswith("project_token")}
        return json.dumps(data)
    except sa.utils.exceptions.ProjectNotFound:
        return "Project not found."
    except Exception as e:
        return f"Unexpected error: {e}"


if __name__ == "__main__":
    print("MCP Server started!")
    mcp.run(transport='stdio')