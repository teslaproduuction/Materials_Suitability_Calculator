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


values_dict = {
    "c": [],
    "lambda": [],
    "rho": [],
    "alpha": [],
    "E": [],
    "HRC": [],
    "sigma_B": [],
    "sigma_0_2": [],
    "KSU": [],
    "delta": [],
    "psi": [],
    "mu": [],
    "tau": [],
    "t_k": [],
    "t_f": []
}

# Создание словаря для результатов K_values
K_values = {f"K{i + 1}": [] for i in range(16)}


@eel.expose
def add_to_array(*args):
    values = [float(arg) for arg in args]

    num_values_per_set = 15
    sets_of_values = [values[i:i + num_values_per_set] for i in range(0, len(values), num_values_per_set)]

    for set_values in sets_of_values:
        keys = list(values_dict.keys())
        for i, key in enumerate(keys):
            values_dict[key].append(set_values[i])

        K1 = calculate_K1(values_dict["lambda"][-1], values_dict["sigma_B"][-1], values_dict["alpha"][-1],
                          values_dict["E"][-1])
        K_values["K1"].append(K1)
        K2 = calculate_K2(
            values_dict["lambda"][-1], values_dict["delta"][-1], values_dict["alpha"][-1], values_dict["E"][-1]
        )
        K_values["K2"].append(K2)
        K3 = calculate_K3(values_dict["lambda"][-1], values_dict["KSU"][-1], values_dict["alpha"][-1],
                          values_dict["E"][-1])
        K_values["K3"].append(K3)
        K4 = calculate_K4(values_dict["lambda"][-1], values_dict["c"][-1], values_dict["alpha"][-1],
                          values_dict["rho"][-1])
        K_values["K4"].append(K4)
        K5 = calculate_K5(values_dict["lambda"][-1], values_dict["c"][-1], values_dict["rho"][-1],
                          values_dict["alpha"][-1], values_dict["E"][-1])
        K_values["K5"].append(K5)
        K6 = calculate_K6(values_dict["sigma_B"][-1], values_dict["mu"][-1], values_dict["alpha"][-1],
                          values_dict["E"][-1])
        K_values["K6"].append(K6)
        K7 = calculate_K7(values_dict["lambda"][-1], values_dict["c"][-1], values_dict["rho"][-1],
                          values_dict["sigma_B"][-1], values_dict["mu"][-1], values_dict["alpha"][-1],
                          values_dict["E"][-1])
        K_values["K7"].append(K7)
        K8 = calculate_K8(values_dict["sigma_B"][-1], values_dict["HRC"][-1], values_dict["E"][-1])
        K_values["K8"].append(K8)
        K9 = calculate_K9(values_dict["sigma_0_2"][-1], values_dict["tau"][-1], values_dict["alpha"][-1])
        K_values["K9"].append(K9)
        K10 = calculate_K10(values_dict["t_k"][-1], values_dict["t_f"][-1], values_dict["alpha"][-1],
                            values_dict["E"][-1], values_dict["mu"][-1], values_dict["sigma_0_2"][-1])
        K_values["K10"].append(K10)
        K11 = calculate_K11(values_dict["delta"][-1], values_dict["alpha"][-1], values_dict["mu"][-1],
                            values_dict["t_k"][-1], values_dict["t_f"][-1], values_dict["sigma_0_2"][-1],
                            values_dict["E"][-1])
        K_values["K11"].append(K11)
        K12 = calculate_K12(values_dict["KSU"][-1], values_dict["sigma_0_2"][-1], values_dict["alpha"][-1],
                            values_dict["t_k"][-1], values_dict["E"][-1])
        K_values["K12"].append(K12)
        K13 = calculate_K13(values_dict["sigma_B"][-1], values_dict["psi"][-1], values_dict["sigma_0_2"][-1],
                            values_dict["alpha"][-1], values_dict["t_k"][-1], values_dict["t_f"][-1])
        K_values["K13"].append(K13)
        K14 = calculate_K14(values_dict["sigma_B"][-1], values_dict["delta"][-1], values_dict["psi"][-1],
                            values_dict["sigma_0_2"][-1], values_dict["E"][-1], values_dict["alpha"][-1],
                            values_dict["t_k"][-1], values_dict["t_f"][-1])
        K_values["K14"].append(K14)
        K15 = calculate_K15(values_dict["sigma_B"][-1], values_dict["alpha"][-1], values_dict["t_k"][-1],
                            values_dict["t_f"][-1], values_dict["mu"][-1], values_dict["sigma_0_2"][-1],
                            values_dict["E"][-1])
        K_values["K15"].append(K15)
        K16 = calculate_K16(values_dict["psi"][-1], values_dict["alpha"][-1], values_dict["t_k"][-1],
                            values_dict["t_f"][-1], values_dict["mu"][-1], values_dict["sigma_0_2"][-1],
                            values_dict["E"][-1])
        K_values["K16"].append(K16)



@eel.expose
def get_result():
    for value in values_dict.values():
        value.clear()
    return tuple([K_values[key][:] for key in K_values])


if __name__ == "__main__":
    eel.init('web')
    eel.start('index.html', mode='Arc', size=(760, 760))
