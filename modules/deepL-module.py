from deep_translator import (GoogleTranslator,MyMemoryTranslator,single_detection,)


def LanguageList():
    langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
    print(langs_dict)


def LangDetect():
    textLangDetect = input('Введіть текст для детекту мови: ')
    lang = single_detection(textLangDetect, api_key='9b2233808370f91e5e2f4449b5cb79b4')
    print('Language is:', lang)

def TransLate():
    text = input('Введіть текст для перекладу: ')
    targetLanguage = input('Введіть мову стандартом: ')
    translated = GoogleTranslator(source='auto', target=targetLanguage).translate(text=text)
    print('Translated text is:', translated)

def TranslateFromFile():
    filePath = input('Enter file name: ')
    path = filePath
    translatedText = MyMemoryTranslator(source='uk-UA', target='vi-VN').translate_file(path)
    print(translatedText)

LangDetect()