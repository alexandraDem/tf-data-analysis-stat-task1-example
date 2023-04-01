import pandas as pd
import numpy as np


chat_id = 433719125 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    log_x = np.log(x)
    a = log_x.mean()
    return a
