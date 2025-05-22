from dotenv import load_dotenv
from agents import Agent, Runner, FileSearchTool
import chainlit as cl

load_dotenv()

agent = Agent(
    model="gpt-4.1-mini",  
    name="my-agent",
    instructions="You are helpful assistant, always search in file for information",
    tools=[FileSearchTool(
        max_num_results=3,
        vector_store_ids=["vs_682f69090d588191beeb4098f199ace5"]
    )]
)

@cl.on_message
async def main(message:cl.Message):
    user_question = message.content

    res = Runner.run_sync(agent, user_question)

    await cl.Message(content = res.final_output).send()
