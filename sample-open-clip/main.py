# 필요한 라이브러리 임포트
import open_clip  # OpenCLIP 라이브러리 - CLIP 모델의 오픈소스 구현체
from PIL import Image  # 이미지 처리를 위한 Python Imaging Library
import torch  # PyTorch 딥러닝 프레임워크

# CLIP 모델과 전처리기 로드
# ViT-g-14 모델을 사용하며, laion2B-s12B-b42K 데이터셋으로 사전학습된 가중치 사용
model, preprocess = open_clip.create_model_from_pretrained('hf-hub:laion/CLIP-ViT-g-14-laion2B-s12B-b42K')
# 텍스트 토큰화를 위한 토크나이저 로드
tokenizer = open_clip.get_tokenizer('hf-hub:laion/CLIP-ViT-g-14-laion2B-s12B-b42K')

# 이미지 로드 및 전처리
image_path = './cat.jpeg'  # 분석할 이미지 경로
image = Image.open(image_path).convert('RGB')  # 이미지를 RGB 형식으로 로드()
image = preprocess(image).unsqueeze(0)  # 이미지 전처리 및 배치 차원 추가

# 분류할 텍스트 후보들 토큰화
text = tokenizer(["a dog", "a cat", "a person", "a car", "a bird"])

# 그래디언트 계산 없이 추론 수행
with torch.no_grad():
    # 이미지와 텍스트 특징 추출
    image_features = model.encode_image(image)  # 이미지 특징 벡터 추출
    text_features = model.encode_text(text)     # 텍스트 특징 벡터 추출
    
    # 특징 벡터 정규화 (L2 정규화)
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)

    # 코사인 유사도 계산 및 소프트맥스로 확률 변환
    text_probs = (100.0 * image_features @ text_features.T).softmax(dim=-1)

# 결과 출력
print("Label probs:", text_probs)

# main.py 밖에서도 사용할 수 있도록 변수들을 export
# __all__ 리스트에 추가된 변수들은 이제 from main import [변수명] 으로 사용할 수 있음
__all__ = ['model', 'preprocess', 'tokenizer', 'image_path', 'text_probs']


