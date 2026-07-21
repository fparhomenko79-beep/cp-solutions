import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import tensorflow as tf
import os

# Функция для обучения (та же самая, на случай если модели еще нет)
def train_and_save_model(model_name='mnist_model.keras'):
    print("Загрузка датасета MNIST и обучение...")
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=5)
    model.save(model_name)
    return model

# Класс графического интерфейса
class DigitRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Распознавание рукописных цифр")
        
        # Информационное табло
        self.result_label = tk.Label(root, text="Загрузка модели...", font=("Arial", 14))
        self.result_label.pack(pady=10)
        
        # Холст для рисования (280x280 пикселей)
        self.canvas = tk.Canvas(root, width=280, height=280, bg='white', cursor="cross")
        self.canvas.pack(pady=10)
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        
        # Создаем скрытое изображение PIL для сохранения рисунка
        self.image = Image.new("RGB", (280, 280), "white")
        self.draw = ImageDraw.Draw(self.image)
        
        # Кнопки
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Распознать", command=self.recognize, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Очистить", command=self.clear_canvas, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
        
        # Загрузка нейросети
        self.model_name = 'mnist_model.keras'
        # Используем метод after, чтобы окно появилось до начала загрузки
        self.root.after(100, self.load_model)

    def load_model(self):
        if os.path.exists(self.model_name):
            self.model = tf.keras.models.load_model(self.model_name)
            self.result_label.config(text="Модель готова! Нарисуйте цифру.")
        else:
            self.result_label.config(text="Обучаю модель (задайте окно в фон)...")
            self.root.update()
            self.model = train_and_save_model(self.model_name)
            self.result_label.config(text="Модель обучена! Нарисуйте цифру.")

    def draw_lines(self, event):
        # Рисуем толстой кистью (радиус 10)
        r = 10
        x, y = event.x, event.y
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="black", outline="black")
        self.draw.ellipse([x-r, y-r, x+r, y+r], fill="black")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (280, 280), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.result_label.config(text="Холст очищен. Рисуйте.")

    def recognize(self):
        # 1. Подготовка изображения (как в предыдущем скрипте)
        img = self.image.convert('L') # В оттенки серого
        img = ImageOps.invert(img)    # Инверсия (белая цифра на черном фоне)
        img = img.resize((28, 28))    # Сжатие до формата MNIST
        img_array = np.array(img) / 255.0 # Нормализация от 0 до 1
        img_array = np.expand_dims(img_array, axis=0) # Добавление размерности
        
        # 2. Предсказание
        prediction = self.model.predict(img_array)
        predicted_digit = np.argmax(prediction)
        confidence = np.max(prediction) * 100
        
        # 3. Вывод результата
        self.result_label.config(text=f"Это цифра: {predicted_digit} (Уверенность: {confidence:.2f}%)")

# Запуск программы
if __name__ == "__main__":
    root = tk.Tk()
    app = DigitRecognizerApp(root)
    root.mainloop()