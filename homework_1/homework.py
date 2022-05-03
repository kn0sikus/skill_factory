"""Игра угадай число
Компьютер сам загадывает и сам угадывает число (3 различных метода)
"""

import numpy as np

def modified_predict(number:int=1) -> int: # 1ый метод
    """Угадываем число случайным образом с модификацией

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    min=1
    max=101
    
    while True:
        count += 1
        predict_number = np.random.randint(min, max)
        
        if predict_number > number:
            max=predict_number
        
        if predict_number < number:
            min=predict_number+1
        
        if predict_number == number:
            break # выход из цикла, если угадали
        
    return(count)

def mean_predict(number:int=1) -> int: # 2ой метод
    """Угадываем число методом среднее арифметическое

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: Число попыток
    """
    min=1
    max=100
    count=0
    
    while True:
        count+=1
        mean=round((min+max)/2)
        
        if mean > number:
            max=mean
        
        if mean < number:
            min=mean
        
        if mean == number:
            break # выход из цикла, если угадали
        
        if min==1 and max==2:
            count+=1
            mean=1
            if mean == number:
                break
            
    return count

def random_predict(number:int=1) -> int: # 3ий метод
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)
        

def score_game(function) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        function ([type]): метод угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(function(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    return(score)

print(f"Алгоритм modified_predict угадывает число в среднем за {score_game(modified_predict)} попыток")
print(f"Алгоритм mean_predict угадывает число в среднем за {score_game(mean_predict)} попыток")
print(f"Алгоритм random_predict угадывает число в среднем за {score_game(random_predict)} попыток")