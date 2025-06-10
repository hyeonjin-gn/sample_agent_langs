import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.tools.render import format_tool_to_openai_function
from tool_multiply import multiply
from prompt import prompt
from dotenv import load_dotenv

# 환경 변수 로드 (.env 파일에서 OPENAI_API_KEY를 읽어옵니다)
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def build_agent():
    """
    LLM(Large Language Model)을 초기화하는 함수입니다.
    ChatOpenAI는 OpenAI의 GPT 모델을 사용하기 위한 LangChain의 래퍼입니다.
    """
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",  # 사용할 GPT 모델
        temperature=0,          # 0으로 설정하여 일관된 결과를 얻습니다
        openai_api_key=openai_api_key
    )
    return llm


def build_agent_executor(user_input: str):
    """
    에이전트 실행기를 생성하는 함수입니다.
    에이전트는 LLM이 도구를 사용할 수 있게 해주는 중간 계층입니다.
    
    Args:
        user_input (str): 사용자의 입력 메시지
    """
    # 1. LLM 초기화
    llm = build_agent()
    
    # 2. 사용할 도구 목록 정의
    tools = [multiply]
    
    # 3. 도구를 OpenAI 함수 형식으로 변환
    # 이는 LLM이 도구를 이해하고 호출할 수 있게 해줍니다
    llm_with_tools = llm.bind(
        functions=[format_tool_to_openai_function(t) for t in tools]
    )
    
    # 4. 에이전트 생성
    # - llm_with_tools: 도구를 사용할 수 있는 LLM
    # - tools: 사용 가능한 도구 목록
    # - prompt: 에이전트의 행동을 정의하는 프롬프트
    agent = create_tool_calling_agent(llm_with_tools, tools, prompt)
    
    # 5. 에이전트 실행기 생성 및 반환
    # AgentExecutor는 에이전트의 실행을 관리하고 도구 호출을 처리합니다
    return AgentExecutor.from_agent_and_tools(agent, tools)