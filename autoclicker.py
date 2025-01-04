import pyautogui
import time
import threading

# Флаги для управления автокликером
clicking = False
exit_flag = False

# Функция для автоматического клика
def auto_click():
    global clicking
    while not exit_flag:
        if clicking:
            pyautogui.click()
        time.sleep(0.05)  # Интервал между кликами

# Основной поток для автокликера
click_thread = threading.Thread(target=auto_click)
click_thread.start()

print("Нажмите 's', чтобы начать или остановить кликер.")
print("Нажмите 'e', чтобы выйти.")

try:
    while not exit_flag:
        user_input = input("Введите команду: ").lower()
        if user_input == 's':
            clicking = not clicking
            state = "включен" if clicking else "выключен"
            print(f"Автокликер {state}.")
        elif user_input == 'e':
            exit_flag = True
            print("Выход из программы.")
except KeyboardInterrupt:
    print("Программа остановлена пользователем.")

# Дождемся завершения потока
click_thread.join()
