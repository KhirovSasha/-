import os
import time

while True:
    # Перелічуємо файли в каталозі "time"
    files = os.listdir("time")

    # Якщо в каталозі є файли, то виводимо їх назви та вміст
    if len(files) > 0:
        for file in files:
            with open(os.path.join("time", file), "r") as f:
                content = f.read()
            print(f"Назва файлу: {file}\nResult: {content}\n")

    # Затримка на 5 секунд перед наступною перевіркою
    time.sleep(5)