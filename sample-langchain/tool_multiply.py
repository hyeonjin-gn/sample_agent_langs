from langchain_core.tools import tool

@tool
def multiply(x: int, y: int) -> int:
    """
    두 정수를 곱하는 LangChain 도구입니다.
    
    @tool 데코레이터는 이 함수를 LangChain 에이전트가 사용할 수 있는 도구로 변환합니다.
    에이전트는 이 도구의 설명을 읽고, 언제 이 도구를 사용해야 할지 결정합니다.
    
    Args:
        x (int): 첫 번째 정수
        y (int): 두 번째 정수

    Returns:
        int: x와 y를 곱한 값을 반환합니다.
    """
    # 문자열이 들어온 경우 정수로 변환
    # LangChain 에이전트는 때로 문자열로 값을 전달할 수 있습니다
    if isinstance(x, str):
        x = int(x)
    if isinstance(y, str):
        y = int(y)
    return x * y