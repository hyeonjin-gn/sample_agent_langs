from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

system_message = "너는 주어진 도구를 사용해서 사용자의 요청을 해결하는 AI Agent야."
prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])
