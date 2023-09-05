import os
from google.cloud import translate_v2 as translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"google-key.json"

def TransLate(lang: str, strr: str) -> dict:
    translate_client = translate.Client()

    if isinstance(strr, bytes):
        text = strr.decode("utf-8")

    result = translate_client.translate(strr, target_language=lang)
    return result

def LangDetect(txt: str) -> dict:
    translate_client = translate.Client()
    result = translate_client.detect_language(txt)
    return result

def CodeLang(lang: str) -> dict:
    translate_client = translate.Client()
    results = translate_client.get_languages(target_language=lang)
    return results

def LanguageList(text: str, input_lang: str):
    from tabulate import tabulate

    table = [["N", "Language", "ISO-639 code", "Text"]]

    target_langs = CodeLang(input_lang)

    for i, lang_info in enumerate(target_langs):
        lang_code = lang_info['language']
        lang_name = lang_info['name']
        result = TransLate(lang_code, text)
        translated_text = result["translatedText"]
        table.append([i + 1, lang_name, lang_code, translated_text])

    print(tabulate(table, headers="firstrow", tablefmt="grid"))


# def TransLate(lang: str, strr: str) -> dict:
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     if isinstance(strr, bytes):
#         text = strr.decode("utf-8")

#     result = translate_client.translate(strr, target_language=lang)

#     print("Text: {}".format(result["input"]))
#     print("Translation: {}".format(result["translatedText"]))
#     print("Detected source language: {}".format(result["detectedSourceLanguage"]))

#     return result

# def LangDetect(txt: str) -> dict:
#     """Detects the text's language."""
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     result = translate_client.detect_language(txt)

#     print("Confidence: {}".format(result["confidence"]))
#     print("Language: {}".format(result["language"]))

#     return result

# def CodeLang(lang: str) -> dict:

#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     results = translate_client.get_languages(target_language=lang)

#     for language in results:
#         print("{name} ({language})".format(**language))

#     return results

# def LanguageList(text: str, input_lang: str):
#     from tabulate import tabulate

#     # Створити таблицю для відображення результатів
#     table = [["N", "Language", "ISO-639 code", "Text"]]

#     # Отримати список мов для вказаної мови введеного тексту
#     target_langs = CodeLang(input_lang)

#     # Переклад введеного тексту для кожної мови та додавання результатів у таблицю
#     for i, lang_info in enumerate(target_langs):
#         lang_code = lang_info['language']
#         lang_name = lang_info['name']
#         result = TransLate(lang_code, text)
#         translated_text = result["translatedText"]
#         table.append([i+1, lang_name, lang_code, translated_text])
#     # Вивести таблицю
#     print(tabulate(table, headers="firstrow", tablefmt="grid"))
#     print('Ok')



# def TransLate(lang: str, strr: str) -> dict:
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     if isinstance(strr, bytes):
#         text = strr.decode("utf-8")

#     result = translate_client.translate(strr, target_language=lang)

#     print("Text: {}".format(result["input"]))
#     print("Translation: {}".format(result["translatedText"]))
#     print("Detected source language: {}".format(result["detectedSourceLanguage"]))

#     return result
#     pass

# def LangDetect(txt: str) -> dict:
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     result = translate_client.detect_language(txt)

#     print("Confidence: {}".format(result["confidence"]))
#     print("Language: {}".format(result["language"]))

#     return result
#     pass

# def CodeLang(lang: str) -> dict:
#     from google.cloud import translate_v2 as translate

#     translate_client = translate.Client()

#     results = translate_client.get_languages(target_language=lang)

#     for language in results:
#         print("{name} ({language})".format(**language))

#     return results
#     pass

# def LanguageList(text: str, input_lang: str):
#     from tabulate import tabulate

#     # Створити таблицю для відображення результатів
#     table = [["N", "Language", "ISO-639 code", "Text"]]

#     # Отримати список мов для вказаної мови введеного тексту
#     target_langs = CodeLang(input_lang)

#     # Переклад введеного тексту для кожної мови та додавання результатів у таблицю
#     for i, lang_info in enumerate(target_langs):
#         lang_code = lang_info['language']
#         lang_name = lang_info['name']
#         result = TransLate(lang_code, text)
#         translated_text = result["translatedText"]
#         table.append([i+1, lang_name, lang_code, translated_text])
#     # Вивести таблицю
#     print(tabulate(table, headers="firstrow", tablefmt="grid"))
#     print('Ok')
#     pass

# while True:
#     print("Оберіть функцію:")
#     print("1. Переклад")
#     print("2. Детект мови")
#     print("3. Список мов")
#     print("4. Переклад на всі мови")
#     print("5. Вихід")

#     choice = input("Введіть номер функції або '5' для виходу: ")

#     if choice == '1':
#         lang = input("Введіть цільову мову для перекладу: ")
#         text = input("Введіть текст для перекладу: ")
#         TransLate(lang, text)
#     elif choice == '2':
#         text = input("Введіть текст для визначення мови: ")
#         LangDetect(text)
#     elif choice == '3':
#         lang = input("Введіть цільову мову для отримання списку мов: ")
#         CodeLang(lang)
#     elif choice == '4':
#         text = input("Введіть текст для перекладу: ")
#         input_lang = input("Введіть мову: ")
#         LanguageList(text, input_lang)
#     elif choice == '5':
#         break
#     else:
#         print("Неправильний вибір. Спробуйте ще раз.")

