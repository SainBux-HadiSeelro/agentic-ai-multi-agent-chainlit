from agent import myagent, manager
import chainlit as cl
import asyncio


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("history", [])
    cl.user_session.set("current_agent", manager)
    await cl.Message(
        content="Welcome to the Hadi's multi-agent system! How can I assist you today?"
    ).send()


@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    history = cl.user_session.get("history")
    current_agent = cl.user_session.get("current_agent")
    
    response = await myagent(user_input, history=history, current_agent=current_agent)
    
    # Update history and current agent
    cl.user_session.set("history", response.to_input_list())
    cl.user_session.set("current_agent", response.last_agent)
    
    await cl.Message(
        content=f"{response.final_output}"
    ).send()
 