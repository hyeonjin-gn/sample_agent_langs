# 필요한 라이브러리 임포트
import streamlit as st  # 웹 인터페이스 구현을 위한 Streamlit
import plotly.express as px  # 인터랙티브 시각화를 위한 Plotly
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
    # Plotly를 사용한 인터랙티브 막대 그래프
    fig = px.bar(
        x=labels,
        y=probs,
        title="이미지 분류 확률",
        labels={"x": "분류", "y": "확률 (%)"},
        text=[f"{p:.2f}%" for p in probs]  # 막대 위에 확률값 표시
    )
    
    # 그래프 스타일 설정
    fig.update_traces(
        textposition='outside',
        marker_color='rgb(55, 83, 109)'
    )
    
    # 레이아웃 설정
    fig.update_layout(
        yaxis_range=[0, 100],
        showlegend=False,
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

# 두 번째 탭: 상세 결과
with tab2:
    # 도넛 차트로 상세 결과 표시
    fig = px.pie(
        values=probs,
        names=labels,
        title="분류 확률 분포",
        hole=0.4  # 도넛 차트로 만들기 위한 중앙 구멍
    )
    
    # 차트 스타일 설정
    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        marker=dict(
            colors=px.colors.sequential.Plasma_r
        )
    )
    
    # 레이아웃 설정
    fig.update_layout(
        height=500,
        showlegend=False,
        annotations=[dict(text='확률<br>분포', x=0.5, y=0.5, font_size=20, showarrow=False)]
    )
    
    # 두 컬럼으로 나누어 표시
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # 상세 확률값을 테이블로 표시
        st.subheader("상세 확률값")
        data = {
            "분류": labels,
            "확률 (%)": [f"{p:.2f}%" for p in probs]
        }
        st.table(data)