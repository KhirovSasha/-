#Використовуємо базовий образ з Python
FROM python:3

#Копіємо код додатку в контейнер
COPY app.py /

#Встановлюємо залежності
RUN pip install flask

#Запускаємо додатку за замовчуванням
CMD ["python", "./app.py"]