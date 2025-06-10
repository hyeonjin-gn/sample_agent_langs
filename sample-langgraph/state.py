
from typing import TypedDict, Annotated
# add_messages는 두개의 메시지 인자를 받아 하나의 메시지 리스트로 변환해주는 리듀스 함수입니다.
from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    # 대화 상태는 add_messages 함수를 이용해 하나의 메시지 리스트로 관리됩니다.
    messages: Annotated[list, add_messages]

    



