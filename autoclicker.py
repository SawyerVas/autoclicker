import pyautogui
import time
import threading
from pynput import keyboard

# Флаги для управления автокликером
clicking = False
exit_flag = False

# Функция для автоматического клика
def auto_click():
    global clicking
    while not exit_flag:
        if clicking:
            pyautogui.click()
        time.sleep(0.01)  # Интервал между кликами

# Обработчики нажатия клавиш
def on_press(key):
    global clicking, exit_flag
    try:
        if key.char == 's':
            clicking = not clicking
            state = "включен" if clicking else "выключен"
            color = "\033[92m" if clicking else "\033[91m"  # Зеленый для включен, красный для выключен
            print(f"{color}Автокликер {state}.\033[0m")  # \033[0m для сброса цвета
        elif key.char == 'e':
            exit_flag = True
            print("Выход из программы.")
    except AttributeError:
        pass

# Основной поток для автокликера
click_thread = threading.Thread(target=auto_click)
click_thread.start()

# Слушатель клавиатуры
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# Дождемся завершения потока
click_thread.join()
