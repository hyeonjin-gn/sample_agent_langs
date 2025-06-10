from langchain_core.tools import tool

@tool
def multiply(x: int, y: int) -> int:
    """두 정수를 곱하는 함수입니다.

    Args:
        x (int): 첫 번째 정수
        y (int): 두 번째 정수

    Returns:
        int: x와 y를 곱한 값을 반환합니다.
    """
    # 문자열이 들어온 경우 정수로 변환
    if isinstance(x, str):
        x = int(x)
    if isinstance(y, str):
        y = int(y)
    return x * y