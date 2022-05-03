import numpy as np

def modified_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    mean=1
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

def round_predict(number:int=1) -> int:
    """_summary_

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
    min=1
    max=100
    count=0
    
    while True:
        count+=1
        mid=round((min+max)/2)
        
        if mid > number:
            max=mid
        
        if mid < number:
            min=mid
        
        if mid == number:
            break # выход из цикла, если угадали
        
        if min==1 and max==2:
            count+=1
            mid=1
            if mid == number:
                break
            
    return count
        

def score_game(function) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        function ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(function(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(round_predict)
