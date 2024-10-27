# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkFont

# Функция для подсчета слов, символов и предложений
def count_text():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Предупреждение", "Введите текст для анализа.")
        return

    words = len(text.split())
    characters = len(text.replace(" ", ""))
    sentences = text.count('.') + text.count('!') + text.count('?')

    # Обновление результатов
    word_count_label.config(text=f"Количество слов: {words}")
    char_count_label.config(text=f"Количество символов (без пробелов): {characters}")
    sentence_count_label.config(text=f"Количество предложений: {sentences}")

# Создание окна
root = tk.Tk()
root.title("Счетчик слов")
root.geometry("400x350")
root.resizable(False, False)

# Настройка стиля
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 10))

# Заголовок
ttk.Label(root, text="Счетчик слов в тексте", font=("Arial", 16, "bold")).pack(pady=10)

# Поле ввода текста
text_input = tk.Text(root, wrap="word", width=40, height=8, font=("Arial", 11))
text_input.pack(pady=5)

# Кнопка для подсчета
count_button = ttk.Button(root, text="Подсчитать", command=count_text)
count_button.pack(pady=10)

# Метки для отображения результатов
word_count_label = ttk.Label(root, text="Количество слов: 0")
word_count_label.pack()

char_count_label = ttk.Label(root, text="Количество символов (без пробелов): 0")
char_count_label.pack()

sentence_count_label = ttk.Label(root, text="Количество предложений: 0")
sentence_count_label.pack()

# Запуск основного цикла приложения
root.mainloop()