import os
import subprocess
import sys
import torch
from downloader import download_video
from transcriber import process_audio_file
from translator import translate_text
from file_manager import save_transcription, handle_downloaded_video
from utils import clear_screen, select_language, split_text
from whisper_utils import load_model

def main():
    clear_screen()

    if not os.path.exists("temp"):
        os.makedirs("temp")

    source_choice = input("Você quer fornecer um caminho para um arquivo .mp4 (1) ou baixar do YouTube (2)? ")

    if source_choice == "1":
        mp4_file_path = input("Digite o caminho completo para o arquivo .mp4 e tecle ENTER: ")
        if not os.path.isfile(mp4_file_path):
            print("Arquivo não encontrado.")
            return
        new_output_filename = os.path.basename(mp4_file_path)
    elif source_choice == "2":
        video_url = input("Cole o link do vídeo: ")
        new_output_filename = download_video(video_url)
        mp4_file_path = f"temp/{new_output_filename}"
    else:
        print("Escolha inválida.")
        return

    input_language = select_language()

    os.makedirs("textos_transcritos", exist_ok=True)
    
    # Carregar o modelo Whisper
    print("Baixando e carregando o modelo Whisper...")
    model = load_model()

    # Extrair áudio do arquivo MP4 usando ffmpeg, se o arquivo de áudio ainda não existir
    wav_file_path = mp4_file_path.replace('.mp4', '.wav')
    if not os.path.isfile(wav_file_path):
        command = ['ffmpeg', '-i', mp4_file_path, '-q:a', '0', '-map', 'a', wav_file_path]
        with open(os.devnull, 'w') as devnull:
            subprocess.run(command, check=True, stdout=devnull, stderr=devnull)

    original_text, detected_language = process_audio_file(wav_file_path, model, input_language, new_output_filename)

    translated_text, target_language = translate_text(original_text, detected_language)

    # Salvar transcrição e tradução em arquivos separados
    save_transcription(new_output_filename, original_text, translated_text, target_language)

    if source_choice == "2":
        keep_video = input("Você quer manter o vídeo baixado (sim/não)? ").strip().lower() == "sim"
        handle_downloaded_video(mp4_file_path, keep_video, new_output_filename)

    del model
    torch.cuda.empty_cache()
    print("Processo concluído.")

if __name__ == "__main__":
    main()
