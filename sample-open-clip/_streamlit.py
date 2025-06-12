# 필요한 라이브러리 임포트
import streamlit as st  # 웹 인터페이스 구현을 위한 Streamlit
import matplotlib.pyplot as plt  # 데이터 시각화를 위한 Matplotlib
from main import model, preprocess, tokenizer, image_path, text_probs  # main.py에서 필요한 변수들 임포트

# Streamlit 페이지 설정
st.set_page_config(page_title="CLIP 이미지 분류 결과", layout="wide")  # 페이지 제목과 레이아웃 설정
st.title("CLIP 이미지 분류 결과")  # 페이지 메인 제목

# 사이드바에 이미지 표시
with st.sidebar:
    st.header("입력 이미지")
    st.image(image_path, caption="분석된 이미지", width=300)  # use_column_width 대신 width 사용

# 메인 컨텐츠 영역
# 탭으로 결과 표시
tab1, tab2 = st.tabs(["확률 분포", "상세 결과"])

# 결과 시각화를 위한 데이터 준비
labels = ["a dog", "a cat", "a person", "a car", "a bird"]  # 분류 레이블
probs = text_probs[0].numpy() * 100  # 확률값을 백분율로 변환

# 첫 번째 탭: 확률 분포 그래프
with tab1:
    fig, ax = plt.subplots(figsize=(10, 6))  # 그래프 크기 설정
    bars = ax.bar(labels, probs)  # 막대 그래프 생성
    ax.set_title('이미지 분류 확률')  # 그래프 제목
    ax.set_ylabel('확률 (%)')  # y축 레이블
    ax.set_ylim(0, 100)  # y축 범위 설정 (0-100%)
    
    # 각 막대 위에 확률값 표시
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f}%',  # 소수점 둘째 자리까지 표시
                ha='center', va='bottom')  # 텍스트 정렬 설정
    
    st.pyplot(fig)  # Streamlit에 그래프 표시

# 두 번째 탭: 상세 결과
with tab2:
    # 결과를 카드 형태로 표시
    for label, prob in zip(labels, probs):
        with st.container():
            st.metric(label=label, value=f"{prob:.2f}%") 