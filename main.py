import math
import sqlite3
import eel
import numpy as np
import re
from scipy.stats import spearmanr, ttest_rel, ttest_ind


@eel.expose
def dropdown():
    try:
        conn = sqlite3.connect('BAZA.sl3')
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT name FROM Сплавы ORDER BY name")
        result = cursor.fetchall()
        alloys = [row[0] for row in result]
        conn.close()
        return alloys
    except Exception as e:
        return str(e)


@eel.expose
def dropdown_select(selected_alloy):
    conn = sqlite3.connect('baza.sl3')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT c, lambda, rho, alpha, E, HRC, sigma_B, sigma_0_2, KSU, delta, psi, mu, tau, t_k, t_f FROM Сплавы WHERE name=?",
        (selected_alloy,))
    result = cursor.fetchone()
    print(result)
    conn.close()
    return result


# Функция для вычисления К1
def calculate_K1(lambda_value, sigma_B, alpha, E):
    result = ((lambda_value * (sigma_B * 10 ** 6)) / ((alpha * 10 ** (-6)) * E * 10 ** 9))
    return scientific_notation(result)


# Функция для вычисления К2
def calculate_K2(lambda_value, delta, alpha, E):
    result = (lambda_value * delta) / ((alpha * 10 ** -6) * E * 10 ** 9) * 10 ** -5
    return scientific_notation(result)


# Функция для вычисления К3
def calculate_K3(lambda_value, KSU, alpha, E):
    result = ((lambda_value * (KSU)) / ((alpha * 10 ** -6) * E * 10 ** 9))
    return scientific_notation(result)


# Функция для вычисления К4
def calculate_K4(lambda_value, c, alpha, rho):
    result = (lambda_value / ((alpha * 10 ** -6) * c * rho)) * 10 ** -2
    return scientific_notation(result)


# Функция для вычисления К5
def calculate_K5(lambda_value, c, rho, alpha, E):
    a = calculate_a(lambda_value, c, rho)
    result = (a / ((alpha * 10 ** -6) * E * 10 ** 9)) * 10 ** -13
    return scientific_notation(result)


# Функция для вычисления К6
def calculate_K6(sigma_B, mu, alpha, E):
    result = ((sigma_B * 10 ** 6) * (1 - mu)) / ((alpha * 10 ** -6) * E * 10 ** 9)
    return scientific_notation(result)


# Функция для вычисления К7
def calculate_K7(lambda_value, c, rho, sigma_B, mu, alpha, E):
    a = calculate_a(lambda_value, c, rho)
    result = (a * (sigma_B * 10 ** 6) * (1 - mu)) / ((alpha * 10 ** -6) * E * 10 ** 9)
    return scientific_notation(result)


# Функция для вычисления К8
def calculate_K8(sigma_B, HRC, E):
    result = (sigma_B * 10 ** 6) / (HRC * (E * 10 ** 9))
    return scientific_notation(result)


# Функция для вычисления К9
def calculate_K9(sigma_0_2, tau, alpha):
    result = (sigma_0_2 * 10 ** 6) / (tau * (alpha * 10 ** -6))
    return scientific_notation(result)


# Функция для вычисления К10
def calculate_K10(t_k, t_f, alpha, E, mu, sigma_0_2):
    delta_t = calculate_delta_t(t_k, t_f)
    sigma_0_2_t_max = calculate_sigma_0_2_t_max(alpha, E, delta_t, mu)
    result = sigma_0_2_t_max / sigma_0_2
    return scientific_notation(result)


# Функция для вычисления К11
def calculate_K11(delta, alpha, mu, t_k, t_f, sigma_0_2, E):
    delta_t = calculate_delta_t(t_k, t_f)
    result = (delta / (2 * (
            ((alpha * 10 ** -6 * delta_t) / (1 - mu)) - ((2 * (sigma_0_2 * 10 ** 6)) / (E * 10 ** 9)))))
    return scientific_notation(result)


# Функция для вычисления К12
def calculate_K12(KSU, sigma_0_2, alpha, t_k, E):
    result = (KSU / (sigma_0_2 * 10 ** -6 * (
            ((alpha * 10 ** -6) * t_k) - (2 * (sigma_0_2 * 10 ** 6)) / (E * 10 ** 9))))
    return scientific_notation(result)


# Функция для вычисления К13
def calculate_K13(sigma_B, psi, sigma_0_2, alpha, t_k, t_f):
    delta_t = calculate_delta_t(t_k, t_f)
    result = (((sigma_B * 10 ** 6) * psi) / (sigma_0_2 * (1 - (psi ** 2)) * alpha * delta_t))
    return scientific_notation(result)


# Функция для вычисления К14
def calculate_K14(sigma_B, delta, psi, sigma_0_2, E, alpha, t_k, t_f):
    delta_t = calculate_delta_t(t_k, t_f)
    result = ((((sigma_B * 10 ** 6) * (1 + delta + psi) - sigma_0_2 * 10 ** 6) / (
            E * 10 ** 9 * (alpha * 10 ** -6 * delta_t) ** 2)))
    return scientific_notation(result)


# Функция для вычисления К15
def calculate_K15(sigma_B, alpha, t_k, t_f, mu, sigma_0_2, E):
    delta_t = calculate_delta_t(t_k, t_f)
    numerator = (sigma_B * 10 ** 6 - alpha * 10 ** -6 * delta_t * E * 10 ** 9 / (1 - mu))
    denominator = (((sigma_0_2 * 10 ** 6) / (E * 10 ** 9)) + ((alpha * 10 ** -6 * delta_t) / (1 - mu)) * (
            (alpha * 10 ** -6 * delta_t * E * 10 ** 9) / (1 - mu)))
    result = ((numerator / denominator) ** 2)  # *10**3
    return scientific_notation(result)


# Функция для вычисления К16
def calculate_K16(psi, alpha, t_k, t_f, mu, sigma_0_2, E):
    delta_t = calculate_delta_t(t_k, t_f)
    numerator = math.log(1 / (1 - psi))
    denominator = ((2 * (((alpha * 10 ** -6) * delta_t) / (1 - mu))) - (4 * ((sigma_0_2 * 10 ** 6) / (E * 10 ** 9))))
    result = (numerator / denominator)
    return scientific_notation(result)


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
K_values2 = {f"K{i + 1}": [] for i in range(16)}


def scientific_notation(number):
    # Проверка на ноль, чтобы избежать ошибки в логарифме
    if number == 0:
        return "0"

    # Определение порядка числа
    order = int(math.floor(math.log10(abs(number))))

    # Мантисса
    mantissa = number / (10 ** order)

    # Вывод в формате научной нотации с надстрочной степенью
    return f"{mantissa:.5f} × 10<sup>{order}</sup>"


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
        K_values2["K1"].append(K1)
        K2 = calculate_K2(
            values_dict["lambda"][-1], values_dict["delta"][-1], values_dict["alpha"][-1], values_dict["E"][-1]
        )
        K_values["K2"].append(K2)
        K_values2["K2"].append(K2)
        K3 = calculate_K3(values_dict["lambda"][-1], values_dict["KSU"][-1], values_dict["alpha"][-1],
                          values_dict["E"][-1])
        K_values["K3"].append(K3)
        K_values2["K3"].append(K3)
        K4 = calculate_K4(values_dict["lambda"][-1], values_dict["c"][-1], values_dict["alpha"][-1],
                          values_dict["rho"][-1])
        K_values["K4"].append(K4)
        K_values2["K4"].append(K4)
        K5 = calculate_K5(values_dict["lambda"][-1], values_dict["c"][-1], values_dict["rho"][-1],
                          values_dict["alpha"][-1], values_dict["E"][-1])
        K_values["K5"].append(K5)
        K_values2["K5"].append(K5)
        K6 = calculate_K6(values_dict["sigma_B"][-1], values_dict["mu"][-1], values_dict["alpha"][-1],
                          values_dict["E"][-1])
        K_values["K6"].append(K6)
        K_values2["K6"].append(K6)
        K7 = calculate_K7(values_dict["lambda"][-1], values_dict["c"][-1], values_dict["rho"][-1],
                          values_dict["sigma_B"][-1], values_dict["mu"][-1], values_dict["alpha"][-1],
                          values_dict["E"][-1])
        K_values["K7"].append(K7)
        K_values2["K7"].append(K7)
        K8 = calculate_K8(values_dict["sigma_B"][-1], values_dict["HRC"][-1], values_dict["E"][-1])
        K_values["K8"].append(K8)
        K_values2["K8"].append(K8)
        K9 = calculate_K9(values_dict["sigma_0_2"][-1], values_dict["tau"][-1], values_dict["alpha"][-1])
        K_values["K9"].append(K9)
        K_values2["K9"].append(K9)
        K10 = calculate_K10(values_dict["t_k"][-1], values_dict["t_f"][-1], values_dict["alpha"][-1],
                            values_dict["E"][-1], values_dict["mu"][-1], values_dict["sigma_0_2"][-1])
        K_values["K10"].append(K10)
        K_values2["K10"].append(K10)
        K11 = calculate_K11(values_dict["delta"][-1], values_dict["alpha"][-1], values_dict["mu"][-1],
                            values_dict["t_k"][-1], values_dict["t_f"][-1], values_dict["sigma_0_2"][-1],
                            values_dict["E"][-1])
        K_values["K11"].append(K11)
        K_values2["K11"].append(K11)
        K12 = calculate_K12(values_dict["KSU"][-1], values_dict["sigma_0_2"][-1], values_dict["alpha"][-1],
                            values_dict["t_k"][-1], values_dict["E"][-1])
        K_values["K12"].append(K12)
        K_values2["K12"].append(K12)
        K13 = calculate_K13(values_dict["sigma_B"][-1], values_dict["psi"][-1], values_dict["sigma_0_2"][-1],
                            values_dict["alpha"][-1], values_dict["t_k"][-1], values_dict["t_f"][-1])
        K_values["K13"].append(K13)
        K_values2["K13"].append(K13)
        K14 = calculate_K14(values_dict["sigma_B"][-1], values_dict["delta"][-1], values_dict["psi"][-1],
                            values_dict["sigma_0_2"][-1], values_dict["E"][-1], values_dict["alpha"][-1],
                            values_dict["t_k"][-1], values_dict["t_f"][-1])
        K_values["K14"].append(K14)
        K_values2["K14"].append(K14)
        K15 = calculate_K15(values_dict["sigma_B"][-1], values_dict["alpha"][-1], values_dict["t_k"][-1],
                            values_dict["t_f"][-1], values_dict["mu"][-1], values_dict["sigma_0_2"][-1],
                            values_dict["E"][-1])
        K_values["K15"].append(K15)
        K_values2["K15"].append(K15)
        K16 = calculate_K16(values_dict["psi"][-1], values_dict["alpha"][-1], values_dict["t_k"][-1],
                            values_dict["t_f"][-1], values_dict["mu"][-1], values_dict["sigma_0_2"][-1],
                            values_dict["E"][-1])
        K_values["K16"].append(K16)
        K_values2["K16"].append(K16)


@eel.expose
def get_result():
    # print(K_values2)
    K_results = tuple([K_values[key][:] for key in K_values])
    rangs = spearman_correlation(K_values2)
    return K_results, rangs


@eel.expose
def get_resultR():
    R_results = spearman_correlation(K_values2)
    # for result in R_results:
        # print(result)
    return R_results


@eel.expose
def clear():
    for value in values_dict.values():
        value.clear()
    for value in K_values.values():
        value.clear()
    for value in K_values2.values():
        value.clear()


def convert_to_float(value):
    # Remove HTML markup
    value = re.sub(r'<sup>([+-]?\d+)</sup>', r'^\1', value)

    # Replace '×' with 'x'
    value = value.replace('×', 'x')

    # Extract the coefficient and exponent from the string representation
    match = re.match(r'([-+]?\d*\.\d+|\d+) x 10\^([-+]?\d+)', value)
    if match:
        coefficient, exponent = map(float, match.groups())
        return coefficient * 10 ** exponent
    else:
        return np.float64(value)


# спеарман
def spearman_correlation(data):
    results_array = []  # массив для результатов

    for key, values in data.items():
        values_float = [convert_to_float(value) for value in values]

        even_indices = [i for i in range(0, len(values_float), 2)]
        odd_indices = [i for i in range(1, len(values_float), 2)]

        even_elements = [values_float[i] for i in even_indices]
        odd_elements = [values_float[i] for i in odd_indices]

        # Спирмен
        correlation_coefficient, p_value_spearman = spearmanr(even_elements, odd_elements)
        correlation_coefficient = round(correlation_coefficient, 1)
        if math.isnan(correlation_coefficient):
            correlation_coefficient = 'недостаточно данных'
        # Стьюдент
        t_statistic, p_value_ttest = ttest_ind(even_elements, odd_elements)
        p_value_ttest = round(p_value_ttest, 3)

        # результирующий массив
        results_array.append((key, correlation_coefficient, p_value_ttest))

    return results_array


if __name__ == "__main__":
    eel.init('web')
    try:
        eel.start('index.html', mode='Arc', size=(800, 900))
    except OSError as e:
        if "Can't find Google Chrome/Chromium installation" in str(e):
            eel.start('index.html', mode="browser")
        else:
            print(f"Error: {e}")
