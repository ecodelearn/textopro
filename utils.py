import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def select_language():
    languages = [
        ('en', 'English'), 
        ('zh', 'Chinese'), 
        ('de', 'German'), 
        ('es', 'Spanish'), 
        ('ru', 'Russian'), 
        ('fr', 'French'), 
        ('ja', 'Japanese'), 
        ('pt', 'Portuguese'), 
        ('hi', 'Hindi'), 
        ('ko', 'Korean'),
        ('auto', 'Detectar automaticamente')
    ]
    print("Selecione o idioma de entrada:")
    for i, (code, language) in enumerate(languages):
        print(f"{i + 1}. {language}")
    choice = int(input("Digite o número correspondente ao idioma: ")) - 1
    if 0 <= choice < len(languages):
        return languages[choice][0]
    else:
        print("Seleção inválida.")
        sys.exit(1)

def select_model():
    models = ['tiny', 'base', 'small', 'medium', 'large']
    print("Selecione o modelo Whisper:")
    for i, model in enumerate(models):
        print(f"{i + 1}. {model}")
    choice = int(input("Digite o número correspondente ao modelo: ")) - 1
    if 0 <= choice < len(models):
        return models[choice]
    else:
        print("Seleção inválida.")
        sys.exit(1)

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
