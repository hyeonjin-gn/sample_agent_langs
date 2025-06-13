import sys
import os
from dotenv import load_dotenv
from state import ChatState
from langgraph.graph import StateGraph, START, END
from promptTemplate import character_name, style
from node import chat_node
from langchain_core.messages import HumanMessage, AIMessage
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate
from langfuse.langchain import CallbackHandler
from langfuse import Langfuse

load_dotenv()

def main():
    # langfuse 핸들러 초기화
    langfuse_handler = CallbackHandler()
    langfuse = Langfuse()

    # langfuse 클라우드에서 production 라벨의 최신 프롬프트 가져오기
    langfuse_prompt = langfuse.get_prompt("jokerPrompt", label="production")
    langfuse_prompt_template = langfuse_prompt.get_langchain_prompt()

    print(f"주입받은 lanfuse 프롬프트: {langfuse_prompt_template}")


    # 가져온 프롬프트를 langchain 프롬프트로 변경
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(langfuse_prompt_template),
    ]
    )

    builder = StateGraph(ChatState)
    builder.add_node("chat", chat_node)
    builder.add_edge(START, "chat")
    builder.add_edge("chat", END)
    
    graph = builder.compile()

    # 채팅 노드 실행
    print("채팅을 시작합니다.")
    while True:
        user_input = input("질문을 입력하세요: ")
        if user_input.lower() in ["quit", "exit"]:
            print("채팅을 종료합니다.")
            break
            
        # 시스템 프롬프트와 사용자 입력을 메시지 형식으로 변환
        system_message = prompt.format_prompt(character_name=character_name, style=style).to_messages()[0]
        human_message = HumanMessage(content=user_input)
        
        state = {"messages": [system_message, human_message]}
        # 랭퓨즈 사용시 invoke에 콜백으로 랭퓨즈 핸들러 전달
        out = graph.invoke(state, config={"callbacks": [langfuse_handler]})
        print(out["messages"][-1].content)

if __name__ == "__main__":
    main()
