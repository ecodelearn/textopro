from deep_translator import GoogleTranslator

def split_text(text, max_length):
    words = text.split(' ')
    current_length = 0
    current_part = []
    parts = []

    for word in words:
        if current_length + len(word) + 1 > max_length:
            parts.append(' '.join(current_part))
            current_part = [word]
            current_length = len(word) + 1
        else:
            current_part.append(word)
            current_length += len(word) + 1

    if current_part:
        parts.append(' '.join(current_part))

    return parts

def translate_text(original_text, detected_language):
    target_language = 'pt' if detected_language.startswith('en') else 'en'
    text_parts = split_text(original_text, 4999)
    translated_text = ""

    translator = GoogleTranslator(source=detected_language, target=target_language)
    for part in text_parts:
        translated_text += translator.translate(part) + " "

    translated_text = translated_text.strip()

    return translated_text, target_language
