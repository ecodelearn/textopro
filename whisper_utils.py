import whisper
import torch

def load_model():
    models = ['tiny', 'base', 'small', 'medium', 'large']
    print("Selecione o modelo Whisper:")
    for i, model in enumerate(models):
        print(f"{i + 1}. {model}")
    choice = int(input("Digite o número correspondente ao modelo: ")) - 1
    if 0 <= choice < len(models):
        model_name = models[choice]
    else:
        print("Seleção inválida.")
        sys.exit(1)

    # Carrega o modelo Whisper com suporte a GPU
    model = whisper.load_model(model_name, device="cuda" if torch.cuda.is_available() else "cpu")
    return model

def transcribe_audio(model, segment, language="auto"):
    segment_audio = whisper.pad_or_trim(segment)
    mel = whisper.log_mel_spectrogram(segment_audio).to(model.device)

    # Print tensor shape for debugging
    print(f"Tamanho do tensor mel: {mel.shape}")

    options = whisper.DecodingOptions(language=language if language != 'auto' else None)
    try:
        result = whisper.decode(model, mel, options)
        return result.text
    except RuntimeError as e:
        print(f"Erro ao transcrever segmento: {e}")
        return ""