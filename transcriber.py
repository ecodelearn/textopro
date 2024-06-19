import whisper
import numpy as np
from tqdm import tqdm

def process_audio_file(mp3_file_path, model, input_language, output_filename):
    # Carrega o áudio
    audio = whisper.load_audio(mp3_file_path)
    sample_rate = whisper.audio.SAMPLE_RATE
    duration = len(audio) / sample_rate

    # Transcreve o arquivo de áudio em segmentos
    segments = np.array_split(audio, int(duration // 30) + 1)
    all_text = ""

    print(f"Transcrevendo áudio de {mp3_file_path}...")
    for segment in tqdm(segments, desc="Transcrição", unit="segmento"):
        segment_audio = whisper.pad_or_trim(segment)
        mel = whisper.log_mel_spectrogram(segment_audio).to(model.device)
        options = whisper.DecodingOptions(language=input_language if input_language != 'auto' else None)
        result = whisper.decode(model, mel, options)
        all_text += result.text + " "

    original_text = all_text.strip()
    print("Transcrição original salva.")
    
    return original_text, input_language
