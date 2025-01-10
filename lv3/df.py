import numpy as np
import matplotlib.pyplot as plt

R_L = [0, 104.9, 205.0, 303.0, 405.0, 507, 606, 706, 804, 903, 1002, 1101, 1200, 1300, 1404, 1502, 2002, 3002, 3998, 4990]
V_L = [0, 0.543, 0.991, 1.371, 1.698, 1.980, 2.229, 2.448, 2.644, 2.819, 2.984, 3.126, 3.255, 3.374, 3.485, 3.582, 3.98, 4.48, 4.78, 4.98]
P_L = []
d
for V, R in zip(V_L, R_L):
    if R != 0:
        power = (V ** 2) / R
        power_mW = power * 1000
    else:
        power_mW = 0
    P_L.append(power_mW)

# 결과 반환
for i in range(len(P_L)):
    print(P_L[i])

# 그래프 출력
plt.figure(figsize=(8, 6))
plt.plot(np.array(R_L) / 1000, P_L, marker='o', linestyle='-', color='black')  # Converting R_L to kΩ for plotting
plt.xlabel(r'$R_L$ (k$\Omega$)')
plt.ylabel('$P_L$ (mW)')
plt.grid(True)
plt.axvline(x=1, linestyle='--', color='gray')  # Example of a reference line at R_L = 1 kΩ
plt.show()
