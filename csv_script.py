import pandas as pd

try:
    # Завантажуємо дані з файлу
    df = pd.read_csv("data.csv")
    print("✅ Дані завантажено успішно!")

    # Виводимо заголовки, щоб переконатися, що вони правильні
    print("📌 Заголовки у файлі:", df.columns.tolist())

    # Перетворюємо стовпець Date у формат дати
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values(by="Date")
    else:
        print("❌ Стовпець 'Date' не знайдено!")

    # Обчислюємо середнє значення у стовпці Amount
    if "Amount" in df.columns:
        average_amount = df["Amount"].mean()
        print(f"📊 Середнє значення Amount: {average_amount:.2f}")
    else:
        print("❌ Стовпець 'Amount' не знайдено!")

    # Зберігаємо оброблені дані у новий файл
    df.to_csv("processed_data.csv", index=False)
    print("✅ Дані збережено у processed_data.csv")

except Exception as e:
    print("🚨 Помилка:", e)