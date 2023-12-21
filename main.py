import json
import math
import sqlite3

import eel
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, ttest_ind

globals()['flag'] = False


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
    except:
        get_result(flag=True)


@eel.expose
def dropdown_select(selected_alloy):
    try:
        conn = sqlite3.connect('BAZA.sl3')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT c, lambda, rho, alpha, E, HRC, sigma_B, sigma_0_2, KSU, delta, psi, mu, tau, t_k, t_f FROM Сплавы WHERE name=?",
            (selected_alloy,))
        result = cursor.fetchone()
        conn.close()
        return result
    except:
        get_result(flag=True)

# Функция для вычисления К1
def calculate_K1(lambda_value, sigma_B, alpha, E):
    try:
        result = ((lambda_value * (sigma_B * 10 ** 6)) / ((alpha * 10 ** (-6)) * E * 10 ** 9))
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К2
def calculate_K2(lambda_value, delta, alpha, E):
    try:
        result = (lambda_value * delta) / ((alpha * 10 ** -6) * E * 10 ** 9) * 10 ** -5
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К3
def calculate_K3(lambda_value, KSU, alpha, E):
    try:
        result = ((lambda_value * (KSU)) / ((alpha * 10 ** -6) * E * 10 ** 9))
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К4
def calculate_K4(lambda_value, c, alpha, rho):
    try:
        result = (lambda_value / ((alpha * 10 ** -6) * c * rho)) * 10 ** -2
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К5
def calculate_K5(lambda_value, c, rho, alpha, E):
    try:
        a = calculate_a(lambda_value, c, rho)
        result = (a / ((alpha * 10 ** -6) * E * 10 ** 9)) * 10 ** -13
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К6
def calculate_K6(sigma_B, mu, alpha, E):
    try:
        result = ((sigma_B * 10 ** 6) * (1 - mu)) / ((alpha * 10 ** -6) * E * 10 ** 9)
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К7
def calculate_K7(lambda_value, c, rho, sigma_B, mu, alpha, E):
    try:
        a = calculate_a(lambda_value, c, rho)
        result = (a * (sigma_B * 10 ** 6) * (1 - mu)) / ((alpha * 10 ** -6) * E * 10 ** 9)
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К8
def calculate_K8(sigma_B, HRC, E):
    try:
        result = (sigma_B * 10 ** 6) / (HRC * (E * 10 ** 9))
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К9
def calculate_K9(sigma_0_2, tau, alpha):
    try:
        result = (sigma_0_2 * 10 ** 6) / (tau * (alpha * 10 ** -6))
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)


# Функция для вычисления К10
def calculate_K10(t_k, t_f, alpha, E, mu, sigma_0_2):
    try:
        delta_t = calculate_delta_t(t_k, t_f)
        sigma_0_2_t_max = calculate_sigma_0_2_t_max(alpha, E, delta_t, mu)
        result = sigma_0_2_t_max / sigma_0_2
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)


# Функция для вычисления К11
def calculate_K11(delta, alpha, mu, t_k, t_f, sigma_0_2, E):
    try:
        delta_t = calculate_delta_t(t_k, t_f)
        result = (delta / (2 * (
                ((alpha * 10 ** -6 * delta_t) / (1 - mu)) - ((2 * (sigma_0_2 * 10 ** 6)) / (E * 10 ** 9)))))
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К12
def calculate_K12(KSU, sigma_0_2, alpha, t_k, E):
    try:
        result = (KSU / (sigma_0_2 * 10 ** -6 * (
                ((alpha * 10 ** -6) * t_k) - (2 * (sigma_0_2 * 10 ** 6)) / (E * 10 ** 9))))
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К13
def calculate_K13(sigma_B, psi, sigma_0_2, alpha, t_k, t_f):
    try:
        delta_t = calculate_delta_t(t_k, t_f)
        result = (((sigma_B * 10 ** 6) * psi) / (sigma_0_2 * (1 - (psi ** 2)) * alpha * delta_t))
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К14
def calculate_K14(sigma_B, delta, psi, sigma_0_2, E, alpha, t_k, t_f):
    try:
        delta_t = calculate_delta_t(t_k, t_f)
        result = ((((sigma_B * 10 ** 6) * (1 + delta + psi) - sigma_0_2 * 10 ** 6) / (
                E * 10 ** 9 * (alpha * 10 ** -6 * delta_t) ** 2)))
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К15
def calculate_K15(sigma_B, alpha, t_k, t_f, mu, sigma_0_2, E):
    try:
        delta_t = calculate_delta_t(t_k, t_f)
        numerator = (sigma_B * 10 ** 6 - alpha * 10 ** -6 * delta_t * E * 10 ** 9 / (1 - mu))
        denominator = (((sigma_0_2 * 10 ** 6) / (E * 10 ** 9)) + ((alpha * 10 ** -6 * delta_t) / (1 - mu)) * (
                (alpha * 10 ** -6 * delta_t * E * 10 ** 9) / (1 - mu)))
        result = ((numerator / denominator) ** 2)  # *10**3
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

# Функция для вычисления К16
def calculate_K16(psi, alpha, t_k, t_f, mu, sigma_0_2, E):
    try:
        delta_t = calculate_delta_t(t_k, t_f)
        numerator = math.log(1 / (1 - psi))
        denominator = ((2 * (((alpha * 10 ** -6) * delta_t) / (1 - mu))) - (4 * ((sigma_0_2 * 10 ** 6) / (E * 10 ** 9))))
        result = (numerator / denominator)
        result = abs(result)
        scientific, mantissa = scientific_notation(result)
        return scientific, result, mantissa
    except:
        get_result(flag=True)

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
K_values3 = {f"K{i + 1}": [] for i in range(16)}


def scientific_notation(number):
    # Проверка на ноль, чтобы избежать ошибки в логарифме
    if number == 0:
        return "0"

    # Определение порядка числа
    order = int(math.floor(math.log10(abs(number))))

    # Мантисса
    mantissa = number / (10 ** order)

    # Вывод в формате научной нотации с надстрочной степенью
    return f"{mantissa:.5f} × 10<sup>{order}</sup>", mantissa


@eel.expose
def add_to_array(*args):
    try:
        values = [float(arg) for arg in args]

        num_values_per_set = 15
        sets_of_values = [values[i:i + num_values_per_set] for i in range(0, len(values), num_values_per_set)]

        for set_values in sets_of_values:
            keys = list(values_dict.keys())
            for i, key in enumerate(keys):
                values_dict[key].append(set_values[i])

            K1, K1E, K1M = calculate_K1(values_dict["lambda"][-1], values_dict["sigma_B"][-1], values_dict["alpha"][-1],
                                        values_dict["E"][-1])
            K_values["K1"].append(K1)
            K_values2["K1"].append(K1E)
            K_values3["K1"].append(K1M)
            K2, K2E, K2M = calculate_K2(values_dict["lambda"][-1], values_dict["delta"][-1], values_dict["alpha"][-1],
                                        values_dict["E"][-1]
                                        )
            K_values["K2"].append(K2)
            K_values2["K2"].append(K2E)
            K_values3["K2"].append(K2M)
            K3, K3E, K3M = calculate_K3(values_dict["lambda"][-1], values_dict["KSU"][-1], values_dict["alpha"][-1],
                                        values_dict["E"][-1])
            K_values["K3"].append(K3)
            K_values2["K3"].append(K3E)
            K_values3["K3"].append(K3M)
            K4, K4E, K4M = calculate_K4(values_dict["lambda"][-1], values_dict["c"][-1], values_dict["alpha"][-1],
                                        values_dict["rho"][-1])
            K_values["K4"].append(K4)
            K_values2["K4"].append(K4E)
            K_values3["K4"].append(K4M)
            K5, K5E, K5M = calculate_K5(values_dict["lambda"][-1], values_dict["c"][-1], values_dict["rho"][-1],
                                        values_dict["alpha"][-1], values_dict["E"][-1])
            K_values["K5"].append(K5)
            K_values2["K5"].append(K5E)
            K_values3["K5"].append(K5M)
            K6, K6E, K6M = calculate_K6(values_dict["sigma_B"][-1], values_dict["mu"][-1], values_dict["alpha"][-1],
                                        values_dict["E"][-1])
            K_values["K6"].append(K6)
            K_values2["K6"].append(K6E)
            K_values3["K6"].append(K6M)
            K7, K7E, K7M = calculate_K7(values_dict["lambda"][-1], values_dict["c"][-1], values_dict["rho"][-1],
                                        values_dict["sigma_B"][-1], values_dict["mu"][-1], values_dict["alpha"][-1],
                                        values_dict["E"][-1])
            K_values["K7"].append(K7)
            K_values2["K7"].append(K7E)
            K_values3["K7"].append(K7M)
            K8, K8E, K8M = calculate_K8(values_dict["sigma_B"][-1], values_dict["HRC"][-1], values_dict["E"][-1])
            K_values["K8"].append(K8)
            K_values2["K8"].append(K8E)
            K_values3["K8"].append(K8M)
            K9, K9E, K9M = calculate_K9(values_dict["sigma_0_2"][-1], values_dict["tau"][-1], values_dict["alpha"][-1])
            K_values["K9"].append(K9)
            K_values2["K9"].append(K9E)
            K_values3["K9"].append(K9M)
            K10, K10E, K10M = calculate_K10(values_dict["t_k"][-1], values_dict["t_f"][-1], values_dict["alpha"][-1],
                                            values_dict["E"][-1], values_dict["mu"][-1], values_dict["sigma_0_2"][-1])
            K_values["K10"].append(K10)
            K_values2["K10"].append(K10E)
            K_values3["K10"].append(K10M)
            K11, K11E, K11M = calculate_K11(values_dict["delta"][-1], values_dict["alpha"][-1], values_dict["mu"][-1],
                                            values_dict["t_k"][-1], values_dict["t_f"][-1],
                                            values_dict["sigma_0_2"][-1],
                                            values_dict["E"][-1])
            K_values["K11"].append(K11)
            K_values2["K11"].append(K11E)
            K_values3["K11"].append(K11M)
            K12, K12E, K12M = calculate_K12(values_dict["KSU"][-1], values_dict["sigma_0_2"][-1],
                                            values_dict["alpha"][-1],
                                            values_dict["t_k"][-1], values_dict["E"][-1])
            K_values["K12"].append(K12)
            K_values2["K12"].append(K12E)
            K_values3["K12"].append(K12M)
            K13, K13E, K13M = calculate_K13(values_dict["sigma_B"][-1], values_dict["psi"][-1],
                                            values_dict["sigma_0_2"][-1],
                                            values_dict["alpha"][-1], values_dict["t_k"][-1], values_dict["t_f"][-1])
            K_values["K13"].append(K13)
            K_values2["K13"].append(K13E)
            K_values3["K13"].append(K13M)
            K14, K14E, K14M = calculate_K14(values_dict["sigma_B"][-1], values_dict["delta"][-1],
                                            values_dict["psi"][-1],
                                            values_dict["sigma_0_2"][-1], values_dict["E"][-1],
                                            values_dict["alpha"][-1],
                                            values_dict["t_k"][-1], values_dict["t_f"][-1])
            K_values["K14"].append(K14)
            K_values2["K14"].append(K14E)
            K_values3["K14"].append(K14M)
            K15, K15E, K15M = calculate_K15(values_dict["sigma_B"][-1], values_dict["alpha"][-1],
                                            values_dict["t_k"][-1],
                                            values_dict["t_f"][-1], values_dict["mu"][-1], values_dict["sigma_0_2"][-1],
                                            values_dict["E"][-1])
            K_values["K15"].append(K15)
            K_values2["K15"].append(K15E)
            K_values3["K15"].append(K15M)
            K16, K16E, K16M = calculate_K16(values_dict["psi"][-1], values_dict["alpha"][-1], values_dict["t_k"][-1],
                                            values_dict["t_f"][-1], values_dict["mu"][-1], values_dict["sigma_0_2"][-1],
                                            values_dict["E"][-1])
            K_values["K16"].append(K16)
            K_values2["K16"].append(K16E)
            K_values3["K16"].append(K16M)
    except:
        get_result(flag=True)


@eel.expose
def get_result(flag=None):
    if flag == True:
        clear()
        return None, None, None, flag
        print("Ошибка")
    else:
        try:
            print("Исходные данные:", K_values3)
            K_results = tuple([K_values[key][:] for key in K_values])
            rangs = spearman_correlation(K_values2)

            # Заменяем NaN значения на None
            K_values3_no_nan = {key: [value if not math.isnan(value) else None for value in values] for key, values in
                                K_values3.items()}
            print("Данные после обработки:", K_values3_no_nan)

            # Преобразуем данные в JSON
            data_json = json.dumps(K_values3_no_nan)
            return K_results, rangs, data_json, flag
        except:
            clear()
            flag = True
            return None, None, None, flag


@eel.expose
def clear():
    for value in values_dict.values():
        value.clear()
    for value in K_values.values():
        value.clear()
    for value in K_values2.values():
        value.clear()
    for value in K_values3.values():
        value.clear()


# спеарман
def spearman_correlation(data):
    results_array = []  # массив для результатов

    for key, values in data.items():
        values_float = [float(value) for value in values]

        half_length = len(values_float) // 2
        even_elements = values_float[:half_length]
        odd_elements = values_float[half_length:]

        # print("even", even_elements)
        # print("odd", odd_elements)
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
