from modules.deepLModule import LanguageList, LangDetect, TransLate, TranslateFromFile

while True:
    print("Оберіть функцію:")
    print("1. Список підтримуваних мов")
    print("2. Визначення мови тексту")
    print("3. Переклад тексту")
    print("4. Переклад тексту з файлу")
    print("5. Вихід")

    choice = input("Введіть номер функції або '5' для виходу: ")

    if choice == '1':
        LanguageList()
    elif choice == '2':
        LangDetect()
    elif choice == '3':
        TransLate()
    elif choice == '4':
        TranslateFromFile()
    elif choice == '5':
        break
    else:
        print("Неправильний вибір. Спробуйте ще раз.")
