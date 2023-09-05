from deep_translator import (GoogleTranslator,
                             ChatGptTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)

langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
print(langs_dict)


lang = single_detection('bonjour la vie', api_key='9b2233808370f91e5e2f4449b5cb79b4')
print('Language is:', lang)


text = 'happy coding'
translated = GoogleTranslator(source='auto', target='de').translate(text=text)
print('Translated text is:', translated)

path = "text.txt"
translatedText = MyMemoryTranslator(source='uk-UA', target='vi-VN').translate_file(path)
print(translatedText)