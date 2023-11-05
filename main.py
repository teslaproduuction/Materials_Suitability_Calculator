import math
import matplotlib.pyplot as plt
import numpy as np
import eel
import os
import sys, io
# Функция для вычисления К1
def calculate_K1(lambda_value, sigma_B, alpha, E):
    return ((lambda_value * (sigma_B * 10 ** 6)) / ((alpha * 10 ** (-6)) * E * 10 ** 9))


# Функция для вычисления К2
def calculate_K2(lambda_value, delta, alpha, E):
    return (lambda_value * delta) / ((alpha * 10 ** -6) * E * 10 ** 9) * 10 ** -5


# Функция для вычисления К3
def calculate_K3(lambda_value, KSU, alpha, E):
    return ((lambda_value * (KSU)) / ((alpha * 10 ** -6) * E * 10 ** 9))  # *10**-4


# Функция для вычисления К4
def calculate_K4(lambda_value, c, alpha, rho):
    return (lambda_value / ((alpha * 10 ** -6) * c * rho))


# Функция для вычисления К5
def calculate_K5(lambda_value, c, rho, alpha, E):
    a = calculate_a(lambda_value, c, rho)
    return (a / ((alpha * 10 ** -6) * E * 10 ** 9)) * 10 ** -13


# Функция для вычисления К6
def calculate_K6(sigma_B, mu, alpha, E):
    return ((sigma_B * 10 ** 6) * (1 - mu)) / ((alpha * 10 ** -6) * E * 10 ** 9)


# Функция для вычисления К7
def calculate_K7(lambda_value, c, rho, sigma_B, mu, alpha, E):
    a = calculate_a(lambda_value, c, rho)
    return (a * (sigma_B * 10 ** 6) * (1 - mu)) / ((alpha * 10 ** -6) * E * 10 ** 9)  # *10**-3


# Функция для вычисления К8
def calculate_K8(sigma_B, HRC, E):
    return (sigma_B * 10 ** 6) / (HRC * (E * 10 ** 2))  # *10**-4


# Функция для вычисления К9
def calculate_K9(sigma_0_2, tau, alpha):
    return (sigma_0_2 * 10 ** 6) / (tau * (alpha * 10 ** -6))  # *10**6


# Функция для вычисления К10
def calculate_K10(t_k, t_f, alpha, E, mu, sigma_0_2):
    delta_t = calculate_delta_t(t_k, t_f)
    sigma_0_2_t_max = calculate_sigma_0_2_t_max(alpha, E, delta_t, mu)
    return sigma_0_2_t_max / sigma_0_2


# Функция для вычисления К11
def calculate_K11(delta, alpha, mu, t_k, t_f, sigma_0_2, E):
    delta_t = calculate_delta_t(t_k, t_f)
    return (delta / (
                2 * ((alpha * 10 ** -6) * delta_t / (1 - mu) - (2 * (sigma_0_2 * 10 ** 2) / E * 10 ** 9))))  # *10**3


# Функция для вычисления К12
def calculate_K12(KSU, sigma_0_2, alpha, t_k, E):
    return (KSU / ((sigma_0_2 * 10 ** -6) * (
                (alpha * 10 ** -6) * t_k - 2 * (sigma_0_2 * 10 ** 6) / E * 10 ** 9)))  # *10**-6


# Функция для вычисления К13
def calculate_K13(sigma_B, psi, sigma_0_2, alpha, t_k, t_f):
    delta_t = calculate_delta_t(t_k, t_f)
    return ((sigma_B * psi) / (sigma_0_2 * (1 - psi ** 2) * alpha * delta_t))


# Функция для вычисления К14
def calculate_K14(sigma_B, delta, psi, sigma_0_2, E, alpha, t_k, t_f):
    delta_t = calculate_delta_t(t_k, t_f)
    return ((((sigma_B * 10 ** 6) * (1 + delta + psi) - sigma_0_2 * 10 ** 6) / (
                E * 10 ** 9 * (alpha * 10 ** -6 * delta_t) ** 2)))


# Функция для вычисления К15
def calculate_K15(sigma_B, alpha, t_k, t_f, mu, sigma_0_2, E):
    delta_t = calculate_delta_t(t_k, t_f)
    numerator = sigma_B * 10 ** 6 - alpha * 10 ** -6 * delta_t * E * 10 ** 9 / (1 - mu)
    denominator = sigma_0_2 * 10 ** 6 / E * 10 ** 9 + (alpha * 10 ** -6 * delta_t) / (1 - mu) * (
                alpha * 10 ** -6 * delta_t * E * 10 ** 9) / (1 - mu)
    return ((numerator / denominator) ** 2)  # *10**3


# Функция для вычисления К16
def calculate_K16(psi, alpha, t_k, t_f, mu, sigma_0_2, E):
    delta_t = calculate_delta_t(t_k, t_f)
    numerator = math.log(100 / (100 - psi), 10)
    denominator = 2 * (alpha * 10 ** -6 * delta_t) / (1 - mu) - 4 * (sigma_0_2 * 10 ** 6 / E * 10 ** 2)
    return (numerator / denominator)


# Вычисление sigma_0_2_t_max и delta_t
def calculate_delta_t(t_k, t_f):
    return t_k - t_f


# delta_t = t_k - t_f
def calculate_sigma_0_2_t_max(alpha, E, delta_t, mu):
    return ((alpha * 10 ** -6) * (E * 10 ** 2) * delta_t) / (1 - mu)


# sigma_0_2_t_max = ((alpha*10**-6) * (E*10**2) * delta_t) / (1 - mu)

def calculate_a(lambda_value, c, rho):
    return lambda_value / (c * rho)


# a = lambda_value / (c * rho)
# Ваши константы в виде массивов
c_values = [565, 565]
lambda_values = [42, 55]
rho_values = [7676, 7676]
alpha_values = [14.3, 18]
E_values = [175, 60]
HRC_values = [45, 30]
sigma_B_values = [620, 450]
sigma_0_2_values = [500, 100]
KSU_values = [73, 73]
delta_values = [23, 29]
psi_values = [70, 90]
mu_values = [0.30, 0.30]
tau_values = [1, 0.42]
t_k_values = [150, 150]
t_f_values = [2, 2]

# Создание массивов для результатов
K1_values = []
K2_values = []
K3_values = []
K4_values = []
K5_values = []
K6_values = []
K7_values = []
K8_values = []
K9_values = []
K10_values = []
K11_values = []
K12_values = []
K13_values = []
K14_values = []
K15_values = []
K16_values = []

# Вычисление и сохранение результатов в массивы
for i in range(len(c_values)):
    K1 = calculate_K1(lambda_values[i], sigma_B_values[i], alpha_values[i], E_values[i])
    K2 = calculate_K2(lambda_values[i], delta_values[i], alpha_values[i], E_values[i])
    K3 = calculate_K3(lambda_values[i], KSU_values[i], alpha_values[i], E_values[i])
    K4 = calculate_K4(lambda_values[i], c_values[i], alpha_values[i], rho_values[i])
    K5 = calculate_K5(lambda_values[i], c_values[i], rho_values[i], alpha_values[i], E_values[i])
    K6 = calculate_K6(sigma_B_values[i], mu_values[i], alpha_values[i], E_values[i])
    K7 = calculate_K7(lambda_values[i], c_values[i], rho_values[i], sigma_B_values[i], mu_values[i], alpha_values[i], E_values[i])
    K8 = calculate_K8(sigma_B_values[i], HRC_values[i], E_values[i])
    K9 = calculate_K9(sigma_0_2_values[i], tau_values[i], alpha_values[i])
    K10 = calculate_K10(t_k_values[i], t_f_values[i], alpha_values[i], E_values[i], mu_values[i], sigma_0_2_values[i])
    K11 = calculate_K11(delta_values[i], alpha_values[i], mu_values[i], t_k_values[i], t_f_values[i], sigma_0_2_values[i], E_values[i])
    K12 = calculate_K12(KSU_values[i], sigma_0_2_values[i], alpha_values[i], t_k_values[i], E_values[i])
    K13 = calculate_K13(sigma_B_values[i], psi_values[i], sigma_0_2_values[i], alpha_values[i], t_k_values[i], t_f_values[i])
    K14 = calculate_K14(sigma_B_values[i], delta_values[i], psi_values[i], sigma_0_2_values[i], E_values[i], alpha_values[i], t_k_values[i], t_f_values[i])
    K15 = calculate_K15(sigma_B_values[i], alpha_values[i], t_k_values[i], t_f_values[i], mu_values[i], sigma_0_2_values[i], E_values[i])
    K16 = calculate_K16(psi_values[i], alpha_values[i], t_k_values[i], t_f_values[i], mu_values[i], sigma_0_2_values[i], E_values[i])

    # Сохранение результатов
    K1_values.append(K1)
    K2_values.append(K2)
    K3_values.append(K3)
    K4_values.append(K4)
    K5_values.append(K5)
    K6_values.append(K6)
    K7_values.append(K7)
    K8_values.append(K8)
    K9_values.append(K9)
    K10_values.append(K10)
    K11_values.append(K11)
    K12_values.append(K12)
    K13_values.append(K13)
    K14_values.append(K14)
    K15_values.append(K15)
    K16_values.append(K16)

# Вывод результатов

if __name__ == "__main__":

    print("Результаты:")
    for i in range(len(c_values)):
        print(f"Для набора данных {i + 1}:")
        print(f"К1 = {K1_values[i]}")
        print(f"К2 = {K2_values[i]}")
        print(f"К3 = {K3_values[i]}")
        print(f"К4 = {K4_values[i]}")
        print(f"К5 = {K5_values[i]}")
        print(f"К6 = {K6_values[i]}")
        print(f"К7 = {K7_values[i]}")
        print(f"К8 = {K8_values[i]}")
        print(f"К9 = {K9_values[i]}")
        print(f"К10 = {K10_values[i]}")
        print(f"К11 = {K11_values[i]}")
        print(f"К12 = {K12_values[i]}")
        print(f"К13 = {K13_values[i]}")
        print(f"К14 = {K14_values[i]}")
        print(f"К15 = {K15_values[i]}")
        print(f"К16 = {K16_values[i]}")
        print()
        eel.init('web')
        eel.start('index.html', size=(760, 760))