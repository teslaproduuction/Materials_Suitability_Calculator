import math
import eel


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
    return (sigma_B * 10 ** 6) / (HRC * (E * 10 ** 9))


# Функция для вычисления К9
def calculate_K9(sigma_0_2, tau, alpha):
    # print("sigma_0_2 = ", sigma_0_2, "tau = ", tau, "alpha = ", alpha)
    return (sigma_0_2 * 10 ** 6) / (tau * (alpha * 10 ** -6)) * 10 ** 15


# Функция для вычисления К10
def calculate_K10(t_k, t_f, alpha, E, mu, sigma_0_2):
    delta_t = calculate_delta_t(t_k, t_f)
    sigma_0_2_t_max = calculate_sigma_0_2_t_max(alpha, E, delta_t, mu)
    return sigma_0_2_t_max / sigma_0_2


# Функция для вычисления К11
def calculate_K11(delta, alpha, mu, t_k, t_f, sigma_0_2, E):
    delta_t = calculate_delta_t(t_k, t_f)
    print("к11", "delta = ", delta, "alpha = ", alpha, "mu = ", mu, "t_k = ", t_k, "t_f = ", t_f, "sigma_0_2 = ",
          sigma_0_2, "E = ", E, "delta_t = ", delta_t)
    return (delta / (2 * (
                ((alpha * 10 ** -6 * delta_t) / (1 - mu)) - ((2 * (sigma_0_2 * 10 ** 6)) / (E * 10 ** 9)))))  # *10**3
    # (delta / (2 * (((alpha * 10 ** -6 * delta_t)/(1 - mu)) - ((2 * (sigma_0_2 * 10 ** 6) )/ (E * 10 ** 9)) )))


# Функция для вычисления К12
def calculate_K12(KSU, sigma_0_2, alpha, t_k, E):
    return (KSU / (sigma_0_2 * 10 ** -6 * (
                ((alpha * 10 ** -6) * t_k) - (2 * (sigma_0_2 * 10 ** 6)) / (E * 10 ** 9)))) * 10 ** -5
    # (KSU / (sigma_0_2 * 10 ** -6 * (((alpha * 10 ** -6) * t_k) - (2 * (sigma_0_2 * 10 ** 6)) / (E * 10 ** 9))))


# Функция для вычисления К13
def calculate_K13(sigma_B, psi, sigma_0_2, alpha, t_k, t_f):
    delta_t = calculate_delta_t(t_k, t_f)
    return (((sigma_B * 10 ** 6) * psi) / (sigma_0_2 * (1 - (psi ** 2)) * alpha * delta_t))


# Функция для вычисления К14
def calculate_K14(sigma_B, delta, psi, sigma_0_2, E, alpha, t_k, t_f):
    delta_t = calculate_delta_t(t_k, t_f)
    return ((((sigma_B * 10 ** 6) * (1 + delta + psi) - sigma_0_2 * 10 ** 6) / (
            E * 10 ** 9 * (alpha * 10 ** -6 * delta_t) ** 2)))


# Функция для вычисления К15
def calculate_K15(sigma_B, alpha, t_k, t_f, mu, sigma_0_2, E):
    delta_t = calculate_delta_t(t_k, t_f)
    numerator = (sigma_B * 10 ** 6 - alpha * 10 ** -6 * delta_t * E * 10 ** 9 / (1 - mu))
    denominator = (((sigma_0_2 * 10 ** 6) / (E * 10 ** 9)) + ((alpha * 10 ** -6 * delta_t) / (1 - mu)) * (
                (alpha * 10 ** -6 * delta_t * E * 10 ** 9) / (1 - mu)))
    # print("numerator = ", numerator, "denominator = ", denominator)
    return ((numerator / denominator) ** 2)  # *10**3


# Функция для вычисления К16
def calculate_K16(psi, alpha, t_k, t_f, mu, sigma_0_2, E):
    delta_t = calculate_delta_t(t_k, t_f)
    numerator = math.log(1 / (1 - psi))
    denominator = ((2 * (((alpha * 10 ** -6) * delta_t) / (1 - mu))) - (4 * ((sigma_0_2 * 10 ** 6) / (E * 10 ** 9))))
    # print("numerator = ", numerator, "denominator = ", denominator)
    return (numerator / denominator)


# Вычисление sigma_0_2_t_max и delta_t
def calculate_delta_t(t_k, t_f):
    return t_k - t_f


# delta_t = t_k - t_f
def calculate_sigma_0_2_t_max(alpha, E, delta_t, mu):
    return ((alpha * 10 ** -6) * (E * 10 ** 9) * delta_t) / (1 - mu)


# sigma_0_2_t_max = ((alpha*10**-6) * (E*10**2) * delta_t) / (1 - mu)

def calculate_a(lambda_value, c, rho):
    return lambda_value / (c * rho)


# a = lambda_value / (c * rho)
# Ваши константы в виде массивов
# c_values = [565, 565]
# lambda_values = [42, 55]
# rho_values = [7676, 7676]
# alpha_values = [14.3, 18]
# E_values = [175, 60]
# HRC_values = [45, 30]
# sigma_B_values = [620, 450]
# sigma_0_2_values = [500, 100]
# KSU_values = [73, 73]
# delta_values = [23, 29]
# psi_values = [70, 90]
# mu_values = [0.30, 0.30]
# tau_values = [1, 0.42]
# t_k_values = [150, 150]
# t_f_values = [2, 2]

c_values = []
lambda_values = []
rho_values = []
alpha_values = []
E_values = []
HRC_values = []
sigma_B_values = []
sigma_0_2_values = []
KSU_values = []
delta_values = []
psi_values = []
mu_values = []
tau_values = []
t_k_values = []
t_f_values = []

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


def print_K():
    print(K1_values)
    print(K2_values)
    print(K3_values)
    print(K4_values)
    print(K5_values)
    print(K6_values)
    print(K7_values)
    print(K8_values)
    print(K9_values)
    print(K10_values)
    print(K11_values)
    print(K12_values)
    print(K13_values)
    print(K14_values)
    print(K15_values)
    print(K16_values)


@eel.expose
def add_to_array(*args):
    values = [float(arg) for arg in args]

    num_values_per_set = 15
    sets_of_values = [values[i:i + num_values_per_set] for i in range(0, len(values), num_values_per_set)]

    for set_values in sets_of_values:
        c_value, lambda_value, rho_value, alpha_value, E_value, HRC_value, sigma_B_value, sigma_0_2_value, \
        KSU_value, delta_value, psi_value, mu_value, tau_value, t_k_value, t_f_value = set_values

        K1 = calculate_K1(lambda_value, sigma_B_value, alpha_value, E_value)
        K2 = calculate_K2(lambda_value, delta_value, alpha_value, E_value)
        K3 = calculate_K3(lambda_value, KSU_value, alpha_value, E_value)
        K4 = calculate_K4(lambda_value, c_value, alpha_value, rho_value)
        K5 = calculate_K5(lambda_value, c_value, rho_value, alpha_value, E_value)
        K6 = calculate_K6(sigma_B_value, mu_value, alpha_value, E_value)
        K7 = calculate_K7(lambda_value, c_value, rho_value, sigma_B_value, mu_value, alpha_value, E_value)
        K8 = calculate_K8(sigma_B_value, HRC_value, E_value)
        K9 = calculate_K9(sigma_0_2_value, tau_value, alpha_value)
        K10 = calculate_K10(t_k_value, t_f_value, alpha_value, E_value, mu_value, sigma_0_2_value)
        K11 = calculate_K11(delta_value, alpha_value, mu_value, t_k_value, t_f_value, sigma_0_2_value, E_value)
        K12 = calculate_K12(KSU_value, sigma_0_2_value, alpha_value, t_k_value, E_value)
        K13 = calculate_K13(sigma_B_value, psi_value, sigma_0_2_value, alpha_value, t_k_value, t_f_value)
        K14 = calculate_K14(sigma_B_value, delta_value, psi_value, sigma_0_2_value, E_value, alpha_value, t_k_value,
                            t_f_value)
        K15 = calculate_K15(sigma_B_value, alpha_value, t_k_value, t_f_value, mu_value, sigma_0_2_value, E_value)
        K16 = calculate_K16(psi_value, alpha_value, t_k_value, t_f_value, mu_value, sigma_0_2_value, E_value)

        K_values = [K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12, K13, K14, K15, K16]

        for i, K_value in enumerate(K_values):
            globals()[f"K{i + 1}_values"].append(K_value)


@eel.expose
def get_result():
    dump_values = []
    values = [
        K1_values, K2_values, K3_values, K4_values, K5_values, K6_values, K7_values, K8_values,
        K9_values, K10_values, K11_values, K12_values, K13_values, K14_values, K15_values, K16_values
    ]
    for value in values:
        dump_values.append(value.copy())
        value.clear()
    return tuple(dump_values)


if __name__ == "__main__":
    eel.init('web')
    eel.start('index.html', mode='Arc', size=(760, 760))
