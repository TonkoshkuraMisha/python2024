import true_reels

# Задаем словарь замен
replacements = {
    80: 9,
    25: 8,
    20: 7,
    15: 6,
    7: 5,
    6: 4,
    5: 3,
    4: 2,
    2: 1
}


def replace_numbers_in_list(lst, replacements):
    """Заменяет числа в списке на значения из словаря замен."""
    return [replacements.get(num, num) for num in lst]


# Списки рилов, которые нужно обновить
reels_to_update = ['reels1', 'reels2', 'reels3', 'reels1_on_fire', 'reels2_on_fire', 'reels3_on_fire']

# Обновляем списки рилов
updated_reels = {reel_name: replace_numbers_in_list(getattr(true_reels, reel_name), replacements)
                 for reel_name in reels_to_update}

# Переписываем файл true_reels.py
with open('true_reels.py', 'w') as f:
    for reel_name, updated_reel in updated_reels.items():
        f.write(f'{reel_name} = {updated_reel}\n')

print("Списки рилов успешно обновлены и сохранены в true_reels.py.")
