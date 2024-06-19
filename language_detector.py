import whisper
from langdetect import detect, LangDetectException

def detect_language(model, audio, max_duration=300):
    start_duration = 60
    while start_duration <= max_duration:
        print(f"Tentando detectar idioma com {start_duration} segundos de áudio...")
        segment = whisper.pad_or_trim(audio[:start_duration * whisper.audio.SAMPLE_RATE])
        mel = whisper.log_mel_spectrogram(segment).to(model.device)
        options = whisper.DecodingOptions(without_timestamps=True)
        result = whisper.decode(model, mel, options)
        text = result.text.strip()
        if text:
            try:
                detected_language = detect(text)
                print(f"Idioma detectado: {detected_language}")
                return detected_language
            except LangDetectException:
                pass
        start_duration += 30
    print("Não foi possível detectar o idioma. Definindo como inglês.")
    return 'en'
