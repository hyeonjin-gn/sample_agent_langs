import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools.render import format_tool_to_openai_function
from tool_multiply import multiply
from prompt import prompt
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def build_agent():
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0,
        openai_api_key=openai_api_key
    )
    return llm


def build_agent_executor(user_input: str):
    llm = build_agent()
    tools = [multiply]
    
    # 도구를 OpenAI 함수 형식으로 변환
    llm_with_tools = llm.bind(
        functions=[format_tool_to_openai_function(t) for t in tools]
    )
    
    # 에이전트 생성
    agent = create_tool_calling_agent(llm_with_tools, tools, prompt)
    return AgentExecutor.from_agent_and_tools(agent, tools)