import numpy as np
import pandas as pd

# 상수 정의
mu_0 = 4 * np.pi * 1e-7  # 진공의 투자율 (T·m/A)
n = 7310  # turns/m
i = 0.426  # 전류 (A)
L = 0.134  # 솔레노이드 길이 (m)
R = 0.01575  # 솔레노이드 반지름 (m)

# z 값 (cm -> m로 변환)
z_values = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]) * 0.01

# 이론값 계산 함수
def calculate_theoretical_B(z):
    term1 = (L / 2 + z) / np.sqrt((L / 2 + z) ** 2 + R ** 2)
    term2 = (L / 2 - z) / np.sqrt((L / 2 - z) ** 2 + R ** 2)
    B = (mu_0 * n * i / 2) * (term1 + term2)
    return B * 1e3  # mT 단위로 변환

# 이론값 계산
theoretical_B_values = [calculate_theoretical_B(z) for z in z_values]

# 실험 결과 입력
experimental_B_values = np.array([
    [-19.3, -19.3, -19.3],
    [-19.2, -19.2, -19.2],
    [-18.8, -18.8, -18.8],
    [-18.4, -18.3, -18.4],
    [-16.2, -16.2, -16.3],
    [-12.8, -12.7, -12.8],
    [-7.6, -7.7, -7.7],
    [-4.1, -4.0, -4.2],
    [-2.1, -2.0, -2.1]
])
mean_experimental_B_values = experimental_B_values.mean(axis=1)

# 오차 계산
errors = np.abs(mean_experimental_B_values - theoretical_B_values)

# 결과 출력
df = pd.DataFrame({
    'z (cm)': z_values * 100,  # cm로 출력
    'B (mT) (실험 평균값)': mean_experimental_B_values,
    'B (mT) (이론값)': theoretical_B_values,
    '오차 (mT)': errors
})

import ace_tools as tools; tools.display_dataframe_to_user(name="실험 결과와 오차 비교", dataframe=df)
