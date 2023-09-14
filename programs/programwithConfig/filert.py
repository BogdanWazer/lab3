import json
import os
from deep_translator import GoogleTranslator
from deep_translator.exceptions import NotValidPayload

# Зчитування конфігураційного файлу JSON
try:
    with open('config.json', 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    print("Помилка: Конфігураційний файл не знайдено.")
    exit()

# Перевірка наявності вказаного файлу
file_name = config["filename"]
if not os.path.isfile(file_name):
    print(f"Помилка: Файл '{file_name}' не знайдено.")
    exit()

# Зчитування вмісту файлу для перекладу, декодування, перевірка на помилки
try:
    with open(file_name, 'r', encoding='utf-8') as input_file:
        text_to_translate = input_file.read()
except FileNotFoundError:
    print("Помилка: Вхідний файл не знайдено.")
    exit()

# Функціонал перекладання тексту
try:
    translator = GoogleTranslator(source='auto', target=config["language"])
    translated_text = translator.translate(text=text_to_translate)

    # Виведення інформації про файл та перекладений текст
    file_size = os.path.getsize(file_name)
    num_characters = len(text_to_translate)
    num_words = len(text_to_translate.split())
    num_sentences = text_to_translate.count('.') + text_to_translate.count('!') + text_to_translate.count('?')

    file_info = f"Назва файлу: {file_name}\n" \
                f"Розмір файлу: {file_size} байт\n" \
                f"Кількість символів: {num_characters}\n" \
                f"Кількість слів: {num_words}\n" \
                f"Кількість речень: {num_sentences}\n"

    print(file_info)
    print("Результат перекладу:")
    print(translated_text)

    # Збереження інформації та результату у файл "translatedText.txt"
    with open('translatedText.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(file_info)
        output_file.write("\nРезультат перекладу:\n")
        output_file.write(translated_text)

    print("Інформацію та результат перекладу збережено у файлі 'translatedText.txt'")
except NotValidPayload:
    print("Помилка: Помилка перекладу. Перевірте конфігурацію мови в конфігураційному файлі.")
except Exception as e:
    print(f"Помилка: {e}")



# import json
# from deep_translator import (GoogleTranslator)


# # Зчитування конфігураційного файлу JSON
# try:
#     with open('config.json', 'r', encoding='utf-8') as config_file:
#         config = json.load(config_file)
# except FileNotFoundError:
#     print("Помилка: Конфігураційний файл не знайдено.")
#     exit()

# fileName = config["filename"]
# language = config["language"]
# output = config["output"]

# # Зчитування вмісту вхідного файлу
# try:
#     with open(fileName, 'r', encoding='utf-8') as input_file:
#         textToTranslate = input_file.read()
# except FileNotFoundError:
#     print("Помилка: Вхідний файл не знайдено.")
#     exit()

# # Переклад тексту



# translatedText = GoogleTranslator(source='auto', target=language).translate(text=textToTranslate)

# with open('translatedText.txt', 'w', encoding='utf-8') as output_file:
#     output_file.write(translatedText)


# # Перевірка обмежень
# if len(translated.text) <= config['symbols']:
#     if config['output'] == "файл":
#         output_file_name = f"{config['filename'].split('.')[0]}_{config['language']}.txt"
#         try:
#             with open(output_file_name, 'w', encoding='utf-8') as output_file:
#                 output_file.write(translated.text)
#             print("Ok")
#         except Exception as e:
#             print(f"Помилка: {e}")
#     elif config['output'] == "екран":
#         print("Назва мови:", config['language'])
#         print("Перекладений текст:")
#         print(translated.text)
# else:
#     print("Помилка: Обмеження кількості символів перевищено.")
