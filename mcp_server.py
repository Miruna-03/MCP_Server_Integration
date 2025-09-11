from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent
import asyncio

server = Server("local-code-processor")

@server.list_tools()
async def list_tools():
    return [{
        "name": "process_code",
        "description": "Process code with a given prompt",
        "inputSchema": {
            "type": "object",
            "properties": {
                "prompt": {"type": "string"},
                "code": {"type": "string"}
            },
            "required": ["prompt", "code"]
        }
    }]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "process_code":
        prompt = arguments.get("prompt", "")
        code = arguments.get("code", "")
        result = f"Processed with prompt: {prompt}\nCode length: {len(code)} characters"
        return [TextContent(type="text", text=result)]
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())