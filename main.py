import pandas as pd

# Завантажуємо CSV-файл
def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Дані завантажено успішно.")
        return data
    except FileNotFoundError:
        print("Файл не знайдено!")
        return None

# Сортуємо дані за певним стовпцем
def sort_data(data, column_name):
    try:
        sorted_data = data.sort_values(by=column_name)
        print(f"Дані відсортовано по стовпцю {column_name}.")
        return sorted_data
    except KeyError:
        print(f"Стовпець {column_name} не знайдено!")
        return data

# Обчислюємо середнє значення для стовпця
def calculate_average(data, column_name):
    try:
        average = data[column_name].mean()
        print(f"Середнє значення для {column_name}: {average}")
        return average
    except KeyError:
        print(f"Стовпець {column_name} не знайдено!")
        return None

# Тестуємо функції
if __name__ == "__main__":
    file_path = 'data.csv'  # Заміни на свій шлях до CSV файлу
    data = load_csv(file_path)

    if data is not None:
        sorted_data = sort_data(data, 'Date')  # Замінити на реальний стовпець
        calculate_average(sorted_data, 'Amount')  # Замінити на реальний стовпець
