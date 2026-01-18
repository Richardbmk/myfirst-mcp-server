# MyFirst MCP Server

## Overview

This project is a basic Model Context Protocol (MCP) server implemented in Python. It serves as a starting point for building MCP-compliant services, providing a simple structure to extend and customize for your own use cases.

## Features

- Minimal Python server setup
- Ready to extend for custom MCP endpoints
- Easy to run and configure

## Getting Started

### Prerequisites

- Python 3.8 or higher

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Richardbmk/myfirst-mcp-server.git
   cd myfirst-mcp-server
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
   _If `requirements.txt` is not present, install dependencies as specified in `pyproject.toml`._

### Running the Server

To start the server, run:

```sh
python main.py
```

## Project Structure

- `main.py` — Entry point for the MCP server.
- `pyproject.toml` — Project metadata and dependencies.
- `README.md` — Project overview and instructions.
- `__pycache__/` — Python bytecode cache (auto-generated).

## Customization

- Extend `main.py` to add new endpoints or logic.
- Update `pyproject.toml` to manage dependencies.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
