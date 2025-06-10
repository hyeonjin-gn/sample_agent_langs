# 조커와의 대화 (Joker Chat)

LangChain과 LangGraph를 활용한 조커 캐릭터와의 대화형 챗봇 프로젝트입니다.

## 프로젝트 개요

이 프로젝트는 영화 '다크 나이트'의 조커 캐릭터를 모방한 대화형 AI 챗봇입니다. LangChain의 LLM 기능과 LangGraph의 상태 관리 기능을 활용하여 조커의 특유한 성격과 대화 스타일을 구현했습니다.

## 주요 기능

- 조커 캐릭터의 특성을 반영한 대화 시스템
- LangGraph를 활용한 상태 관리
- OpenAI GPT-3.5 Turbo 모델 기반 응답 생성
- 대화 기록 유지 및 컨텍스트 관리

## 설치 방법

1. Python 3.8 이상이 필요합니다.

2. uv를 사용한 의존성 설치:
```bash
# 가상환경 생성
uv venv

# 가상환경 활성화
source .venv/bin/activate  # Unix/macOS
# 또는
.venv\Scripts\activate     # Windows

# pyproject.toml의 의존성 설치
uv pip install -e .
```

3. 환경 변수 설정:
`.env` 파일을 생성하고 다음 내용을 추가하세요:
```
OPENAI_API_KEY=your_api_key_here
```

## 실행 방법

```bash
python main.py
```

## 프로젝트 구조

- `main.py`: 메인 실행 파일
- `Node.py`: LangGraph 노드 구현
- `state.py`: 상태 관리 클래스
- `promptTemplate.py`: 조커 캐릭터 프롬프트 템플릿

## 사용된 기술

- LangChain
- LangGraph
- OpenAI GPT-3.5 Turbo
- Python 3.x

## 주의사항

- OpenAI API 키가 필요합니다.
- 인터넷 연결이 필요합니다.
- GPT-3.5 Turbo 모델 사용으로 인한 API 비용이 발생할 수 있습니다.

## 라이선스

MIT License
