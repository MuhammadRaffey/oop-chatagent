import os
from dotenv import load_dotenv
from typing import cast
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is present; if not, raise an error
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=openai_api_key,
    base_url="https://api.openai.com/v1",
)

@cl.on_chat_start
async def start():
    model = OpenAIChatCompletionsModel(
        model="gpt-4o-mini",
        openai_client=external_client
    )

    config = RunConfig(
        model=model,
        model_provider=external_client,
    )
    """Set up the chat session when a user connects."""

    cl.user_session.set("chat_history", [])

    cl.user_session.set("config", config)
    agent: Agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant specialized in Python and Object-Oriented Programming. Only respond to queries related to OOP. If a query is not related to OOP, indicate that it is irrelevant.",
        model=model
    )
    cl.user_session.set("agent", agent)

    await cl.Message(content="Welcome to the Python OOP Assistant! How can I help you today?").send()

@cl.on_message
async def main(message: cl.Message):
    """Process incoming messages and generate responses."""
    msg = cl.Message(content="Thinking...")
    await msg.send()

    agent: Agent = cast(Agent, cl.user_session.get("agent"))
    config: RunConfig = cast(RunConfig, cl.user_session.get("config"))

    history = cl.user_session.get("chat_history") or []
    
    try:
        result = Runner.run_sync(agent, history, run_config=config)
        
        response_content = result.final_output
        msg.content = response_content
        await msg.update()
        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("chat_history", history)
        
    except Exception as e:
        msg.content = f"Error: {str(e)}"
        await msg.update()
        print(f"Error: {str(e)}")


