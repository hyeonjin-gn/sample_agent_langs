import sys
import os
from dotenv import load_dotenv

from agent_builder import build_agent_executor

def main():
    print("곱셈 에이전트가 준비되었습니다. (종료하려면 'quit' 또는 'exit'를 입력하세요)")
    print("예시: '3과 4를 곱해줘'")
    
    while True:
        user_input = input("\n질문을 입력하세요: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("프로그램을 종료합니다.")
            break
            
        try:
            # 사용자 입력을 기반으로 에이전트 실행기 생성
            agent_executor = build_agent_executor(user_input)
            response = agent_executor.invoke({"input": user_input})
            print(f"\n답변: {response['output']}")
        except Exception as e:
            print(f"\n오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()



