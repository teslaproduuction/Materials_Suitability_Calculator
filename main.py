import math
# Функция для вычисления К1
def calculate_K1(lambda_value, sigma_B, alpha, E):
    return ((lambda_value * (sigma_B*10**6) )/ ((alpha*10**(-6)) * E*10**9))
# Функция для вычисления К2
def calculate_K2(lambda_value, delta, alpha, E):
    return (lambda_value * delta) / ((alpha*10**-6) * E*10**9)*10**-5

# Функция для вычисления К3
def calculate_K3(lambda_value, KSU, alpha, E):
    return ((lambda_value * (KSU)) /( (alpha*10**-6) * E*10**9))#*10**-4

# Функция для вычисления К4
def calculate_K4(lambda_value, c, alpha, rho):
    return (lambda_value /( (alpha*10**-6)* c * rho))

# Функция для вычисления К5
def calculate_K5(a, alpha, E):
    return (a /((alpha*10**-6) * E*10**9))*10**-13

# Функция для вычисления К6
def calculate_K6(sigma_B, mu, alpha, E):
    return ((sigma_B*10**6)* (1 - mu)) / ((alpha*10**-6) * E*10**9)

# Функция для вычисления К7
def calculate_K7(a, sigma_B, mu, alpha, E):
    return (a * (sigma_B*10**6) * (1 - mu)) /((alpha*10**-6) * E*10**9)#*10**-3

# Функция для вычисления К8
def calculate_K8(sigma_B, HRC, E):
    return (sigma_B*10**6) / (HRC * (E*10**2))#*10**-4

# Функция для вычисления К9
def calculate_K9(sigma_0_2, tau, alpha):
    return (sigma_0_2*10**6)/(tau * (alpha*10**-6))#*10**6
# Функция для вычисления К10
def calculate_K10(sigma_0_2_t_max):
    return sigma_0_2_t_max / (sigma_0_2)

# Функция для вычисления К11
def calculate_K11(delta, alpha, delta_t, mu, sigma_0_2, E):
    return (delta / (2 * ((alpha*10**-6) * delta_t / (1 - mu) - (2 * (sigma_0_2*10**2) / E*10**9))))#*10**3

# Функция для вычисления К12
def calculate_K12(KSU, sigma_0_2, alpha, t_k, E):
    return (KSU / ((sigma_0_2*10**-6) * ((alpha*10**-6) * t_k - 2 * (sigma_0_2*10**6) / E*10**9)))#*10**-6

# Функция для вычисления К13
def calculate_K13(sigma_B, psi, sigma_0_2, alpha, delta_t):
    return ((sigma_B * psi) / (sigma_0_2 * (1 - psi ** 2) * alpha * delta_t))

# Функция для вычисления К14
def calculate_K14(sigma_B, delta, psi, sigma_0_2, E, alpha, delta_t):
    return ((((sigma_B*10**6) * (1 + delta + psi) - sigma_0_2*10**6) / (E*10**9 * (alpha*10**-6 * delta_t) ** 2)))

# Функция для вычисления К15
def calculate_K15(sigma_B, alpha, delta_t, mu, sigma_0_2, E):
    numerator = sigma_B*10**6 - alpha*10**-6 * delta_t * E*10**9 / (1 - mu)
    denominator = sigma_0_2*10**6 / E*10**9 + (alpha*10**-6 * delta_t) / (1 - mu) * (alpha*10**-6 * delta_t * E*10**9) / (1 - mu)
    return ((numerator / denominator) ** 2)#*10**3

# Функция для вычисления К16
def calculate_K16(psi, alpha, delta_t, mu, sigma_0_2, E):
    numerator = math.log(100 / (100 - psi), 10)
    denominator = 2 * (alpha*10**-6 * delta_t) / (1 - mu) - 4 * (sigma_0_2*10**6 / E*10**2)
    return (numerator / denominator)

# Вычисление sigma_0_2_t_max и delta_t
def calculate_delta_t(t_k, t_f):
    return t_k - t_f
# delta_t = t_k - t_f
def calculate_sigma_0_2_t_max(alpha, E, delta_t, mu):
    return ((alpha*10**-6) * (E*10**2) * delta_t) / (1 - mu)
# sigma_0_2_t_max = ((alpha*10**-6) * (E*10**2) * delta_t) / (1 - mu)

def calculate_a(lambda_value, c, rho):
    return lambda_value / (c * rho)
#a = lambda_value / (c * rho)

c = float(565)
lambda_value = float(42)
rho = float(7676)
alpha = float(14.3)
E = float(175)
HRC = float(45)
sigma_B = float(620)
sigma_0_2 = float(500)
KSU = float(73)
delta = float(23)
psi = float(70)
mu = float(0.30)
tau = float(1)
t_k = float(150)
t_f = float(2)
delta_t = calculate_delta_t(t_k, t_f)
sigma_0_2_t_max = calculate_sigma_0_2_t_max(alpha, E, delta_t, mu)
a = calculate_a(lambda_value, c, rho)

c2 = float(565)
lambda_value2 = float(55)
rho2 = float(7676)
alpha2 = float(18)
E2 = float(60)
HRC2 = float(30)
sigma_B2 = float(450)
sigma_0_22 = float(100)
KSU2 = float(73)
delta2 = float(29)
psi2 = float(90)
mu2 = float(0.30)
tau2 = float(0.42)
t_k2 = float(150)
t_f2 = float(2)
delta_t2 = calculate_delta_t(t_k2, t_f2)
sigma_0_2_t_max2 = calculate_sigma_0_2_t_max(alpha2, E2, delta_t2, mu2)
a2 = calculate_a(lambda_value2, c2, rho2)

# Запрос ввода данных от пользователя
# c = float(input("Введите значение удельной теплоемкости материала (c): "))
# lambda_value = float(input("Введите значение теплопроводности материала (λ): "))
# rho = float(input("Введите значение плотности материала (ρ): "))
# a = float(input("Введите значение коэффициента температуропроводности материала (a): "))
# E = float(input("Введите значение модуля упругости материала (E): "))
# HRC = float(input("Введите значение твердости материала по Роквеллу (HRC): "))
# sigma_B = float(input("Введите значение предела прочности материала (σ_B): "))
# sigma_0_2 = float(input("Введите значение предела текучести материала (σ_0.2): "))
# KSU = float(input("Введите значение ударной вязкости материала (КСU): "))
# delta = float(input("Введите значение относительного удлинения материала (δ): "))
# psi = float(input("Введите значение относительное сужение материала (ψ): "))
# mu = float(input("Введите значение коэффициента Пуассона (μ): "))
# alpha = float(input("Введите значение коэффициента линейного расширения материала (α): "))
# tau = float(input("Введите время нагрева за цикл (τ): "))
# t_k = float(input("Введите значение температуры контакта штампа с заготовкой (t_к): "))
# t_f = float(input("Введите значение температуры подогрева штампа перед началом работы (t_ф): "))



# Вычисление и вывод значений критериев К1-K16
print("Результаты вычислений:")
print(f"К1 = {calculate_K1(lambda_value, sigma_B, alpha, E)}")
print(f"К2 = {calculate_K2(lambda_value, delta, alpha, E)}")
print(f"К3 = {calculate_K3(lambda_value, KSU, alpha, E)}")
print(f"К4 = {calculate_K4(lambda_value, c, alpha, rho)}")
print(f"К5 = {calculate_K5(a, alpha, E)}")
print(f"К6 = {calculate_K6(sigma_B, mu, alpha, E)}")
print(f"К7 = {calculate_K7(a, sigma_B, mu, alpha, E)}")
print(f"К8 = {calculate_K8(sigma_B, HRC, E)}")
print(f"К9 = {calculate_K9(sigma_0_2, tau, alpha)}")
print(f"К10 = {calculate_K10(sigma_0_2_t_max)}")
print(f"К11 = {calculate_K11(delta, alpha, delta_t, mu, sigma_0_2, E)}")
print(f"К12 = {calculate_K12(KSU, sigma_0_2, alpha, t_k, E)}")
print(f"К13 = {calculate_K13(sigma_B, psi, sigma_0_2, alpha, delta_t)}")
print(f"К14 = {calculate_K14(sigma_B, delta, psi, sigma_0_2, E, alpha, delta_t)}")
print(f"К15 = {calculate_K15(sigma_B, alpha, delta_t, mu, sigma_0_2, E)}")
print(f"К16 = {calculate_K16(psi, alpha, delta_t, mu, sigma_0_2, E)}")

print("Результаты вычислений:")
print(f"К1 = {calculate_K1(lambda_value2, sigma_B2, alpha2, E2)}")
print(f"К2 = {calculate_K2(lambda_value2, delta2, alpha2, E2)}")
print(f"К3 = {calculate_K3(lambda_value2, KSU2, alpha2, E2)}")
print(f"К4 = {calculate_K4(lambda_value2, c2, alpha2, rho2)}")
print(f"К5 = {calculate_K5(a2, alpha2, E2)}")
print(f"К6 = {calculate_K6(sigma_B2, mu2, alpha2, E2)}")
print(f"К7 = {calculate_K7(a2, sigma_B2, mu2, alpha2, E2)}")
print(f"К8 = {calculate_K8(sigma_B2, HRC2, E2)}")
print(f"К9 = {calculate_K9(sigma_0_22, tau2, alpha2)}")
print(f"К10 = {calculate_K10(sigma_0_2_t_max2)}")
print(f"К11 = {calculate_K11(delta2, alpha2, delta_t2, mu2, sigma_0_22, E2)}")
print(f"К12 = {calculate_K12(KSU2, sigma_0_22, alpha2, t_k2, E2)}")
print(f"К13 = {calculate_K13(sigma_B2, psi2, sigma_0_22, alpha2, delta_t2)}")
print(f"К14 = {calculate_K14(sigma_B2, delta2, psi2, sigma_0_22, E2, alpha2, delta_t2)}")
print(f"К15 = {calculate_K15(sigma_B2, alpha2, delta_t2, mu2, sigma_0_22, E2)}")
print(f"К16 = {calculate_K16(psi2, alpha2, delta_t2, mu2, sigma_0_22, E2)}")