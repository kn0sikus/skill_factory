""""  Игра: угадай число """

import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count+=1
    number_attempt = int(input("Ввведите число:"))
    
    if number_attempt > number:
        print("Загаданное число меньше!")
    
    elif number_attempt < number:
        print("Загаданное число больше!")
    
    else:
        print(f"Вы угадали число {number} за {count} попыток")
        break