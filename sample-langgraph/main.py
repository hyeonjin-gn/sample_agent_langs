import sys
import os
from dotenv import load_dotenv
from state import ChatState
from langgraph.graph import StateGraph, START, END
from promptTemplate import prompt, character_name, style
from node import chat_node
from langchain_core.messages import HumanMessage, AIMessage

def main():
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
        out = graph.invoke(state)
        print(out["messages"][-1].content)

if __name__ == "__main__":
    main()
