from deep_translator import GoogleTranslator

of_language = input()
to_language = input()

to_translate = input()

translated = GoogleTranslator(source=of_language, target=to_language).translate(to_translate)

print(translated)