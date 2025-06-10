from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# LangChain의 프롬프트 템플릿을 정의합니다.
# ChatPromptTemplate은 대화형 프롬프트를 만들기 위한 템플릿입니다.
prompt = ChatPromptTemplate.from_messages([
    # 시스템 메시지: 에이전트의 역할과 행동을 정의합니다
    ("system", "너는 주어진 도구를 사용해서 사용자의 요청을 해결하는 AI Agent야."),
    
    # 사용자 메시지: 사용자의 입력을 받습니다
    ("user", "{input}"),
    
    # MessagesPlaceholder: 에이전트의 중간 작업 기록을 저장하는 공간입니다
    # agent_scratchpad는 에이전트가 도구를 사용할 때마다 그 기록을 저장합니다
    MessagesPlaceholder(variable_name="agent_scratchpad")
])
