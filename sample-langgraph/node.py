from state import ChatState
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage

# LLM 객체를 전역 변수로 한 번만 생성
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# 채팅 노드는 상태를 입력받아 다음 노드에게 상태를 이어 반환합니다. 
# 노드는 메서드입니다...
def chat_node(state: ChatState) -> ChatState:
    messages = state["messages"]
    response = llm.invoke(messages)
    # 응답을 AIMessage로 변환하여 추가
    return {"messages": messages + [AIMessage(content=response.content)]}




