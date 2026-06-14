from typing import Any
import httpx
from fastmcp import FastMCP

WORD_OF_DAY = "Thermal"
QUOTE_INFO = [
    "When it is not necessary to make a decision, it is necessary not to make a decision.",
    "Lord Falkland",
    1620
]

mcp = FastMCP("Wordplay")

@mcp.tool()
async def get_word_of_day() -> str:
    """Get the word of the day"""
    return WORD_OF_DAY

@mcp.tool()
async def get_quote_of_day():
    """Get the quote of the day
    
    Returns as a python table:
    ["Quote","Quote_Author",Quote_Date]
    """
    return QUOTE_INFO   

app = mcp.streamable_http_app()

@app.get("/")
async def root():
    return {
        "status": "healthy",
        "message": "Wordplay MCP Server is live!",
        "mcp_endpoint": "/mcp"
    }