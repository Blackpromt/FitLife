# Константы для расчёта нормы воды.
WATER_PER_KG = 30
ML_PER_LITER = 1000

# Приветствие и сбор данных пользователя.
print(
    'Добро пожаловать в FitLife! Я помогу рассчитать '
    'индекс массы тела и дневную норму воды'
)

user_name = input('Как вас зовут? ')
user_age = int(input('Сколько вам лет? '))
user_weight = float(input('Введите ваш вес в кг: '))
user_height = float(input('Введите рост в метрах (формат: 1.75, не 175): '))


# Расчёт индекса массы тела.
def calculate_bmi(weight, height):
    bmi = round(weight / (height ** 2), 1)
    return bmi


# Расчёт суточной нормы воды в литрах.
def calculate_water(weight):
    water_ml = weight * WATER_PER_KG
    water_l = water_ml / ML_PER_LITER
    return water_l


# Получение результатов расчётов.
rezult_bmi = calculate_bmi(user_weight, user_height)
rezult_water = calculate_water(user_weight)

# Вывод результатов пользователю.
print(f"{user_name}, ваши результаты готовы!")
print(f"Ваш возраст: {user_age} лет")
print(f"Индекс массы тела (ИМТ): {rezult_bmi:.1f}")
print(f"Рекомендуемая суточная норма воды: {rezult_water:.1f} л. в день")
print("Расчет окончен. Будьте здоровы!")