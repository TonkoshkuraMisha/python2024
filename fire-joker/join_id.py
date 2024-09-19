import true_reels


# Функция для преобразования списка в строку
def transform_list_to_string(input_list):
    return ' '.join(map(str, input_list))


# Списки, которые нужно преобразовать
reels_to_transform = {
    "reels1": true_reels.reels1,
    "reels2": true_reels.reels2,
    "reels3": true_reels.reels3,
    "reels1_on_fire": true_reels.reels1_on_fire,
    "reels2_on_fire": true_reels.reels2_on_fire,
    "reels3_on_fire": true_reels.reels3_on_fire
}

# Открываем файл для перезаписи
with open("true_reels.py", "w") as file:
    file.write("# Переписанный файл с объединенными списками в строки\n\n")

    # Преобразуем и записываем каждый список в файл
    for reel_name, reel_data in reels_to_transform.items():
        reel_string = transform_list_to_string(reel_data)
        file.write(f"{reel_name} = '{reel_string}'\n")
