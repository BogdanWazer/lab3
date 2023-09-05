from modules.googleTranslateModule import TransLate, LangDetect, CodeLang, LanguageList

while True:
    print("Оберіть функцію:")
    print("1. TransLate")
    print("2. LangDetect")
    print("3. CodeLang")
    print("4. LanguageList")
    print("5. Вихід")

    choice = input("Введіть номер функції або '5' для виходу: ")

    if choice == '1':
        lang = input("Введіть цільову мову для перекладу: ")
        text = input("Введіть текст для перекладу: ")
        result = TransLate(lang, text)
        print("Text: {}".format(result["input"]))
        print("Translation: {}".format(result["translatedText"]))
        print("Detected source language: {}".format(result["detectedSourceLanguage"]))
    elif choice == '2':
        text = input("Введіть текст для визначення мови: ")
        result = LangDetect(text)
        print("Confidence: {}".format(result["confidence"]))
        print("Language: {}".format(result["language"]))
    elif choice == '3':
        lang = input("Введіть цільову мову для отримання списку мов: ")
        results = CodeLang(lang)
        for language in results:
            print("{name} ({language})".format(**language))
    elif choice == '4':
        text = input("Введіть текст для відображення таблиці: ")
        input_lang = input("Введіть мову для списку мов: ")
        LanguageList(text, input_lang)
    elif choice == '5':
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
