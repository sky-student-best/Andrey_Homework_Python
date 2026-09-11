def month_to_season(month: int) -> str:

    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        raise ValueError("Номер месяца должен быть от 1 до 12.")


month_num = 11
season = month_to_season(month_num)
print(f"Месяц {month_num}: {season}")
