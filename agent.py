from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled
import os


load_dotenv()
set_tracing_disabled(True)

provider = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash-lite",
    openai_client=provider,
)

##web developer Agent
web_dev = Agent(
    name="Web developer",
    instructions="Build responsive and performant website using modern frameworks. If the user asks about app development or marketing, hand off to the appropriate agent or manager.",
    model=model,
    handoff_description="hand off to web developer if the task is related to web development."
)

##app developer Agent
app_dev = Agent(
    name="App developer",
    instructions="Build responsive and performant App using modern frameworks. If the user asks about web development or marketing, hand off to the appropriate agent or manager.",
    model=model,
    handoff_description="hand off to app developer if the task is related to app development."
)

##marketing agent
marketing = Agent(
    name="Marketing expert Agent",
    instructions="create and execute marketing strategies for product launches. If the user asks about web or app development, hand off to the appropriate agent or manager.",
    model=model,
    handoff_description="hand off to marketing agent if the task is related to marketing."
)

##manager agent
manager = Agent(
    name="manager",
    instructions="you will chat with the user and delegate tasks to specialized agents based on their requests.",
    model=model,
    handoffs=[web_dev, app_dev, marketing]
)

web_dev.handoffs = [manager, app_dev, marketing]
app_dev.handoffs = [manager, web_dev, marketing]
marketing.handoffs = [manager, web_dev, app_dev]

async def myagent(user_input, history=None, current_agent=None):
    agent_to_run = current_agent or manager

    if history:
        input_data = history + [{"role": "user", "content": user_input}]
    else:
        input_data = user_input

    response = await Runner.run(
        agent_to_run,
        input=input_data
    )

    return response

