# OOP Chat Agent

This project is a chat agent specialized in Object-Oriented Programming (OOP) using the OpenAI API.

## Setup

1. **Install Dependencies**: Ensure you have `uv` installed. If not, you can install it using:

   ```bash
   pip install uv
   ```

2. **Sync Dependencies**: Run the following command to sync the project dependencies:

   ```bash
   uv sync
   ```

3. **Environment Variables**: Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Running the Project

To run the project, use the following command:

```bash
uv run chainlit run .\src\oop_chatagent\main.py -w
```

## Functionality

- The chat agent will respond to queries related to Object-Oriented Programming.
- If a query is not related to OOP, the agent will prompt the user to ask an OOP-related question.

## Author

- Muhammad Raffey (muhammadraffey26@gmail.com)
