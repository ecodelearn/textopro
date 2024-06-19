import os
import shutil

def save_transcription(base_filename, original_text, translated_text, target_language):
    output_dir = "textos_transcritos"
    os.makedirs(output_dir, exist_ok=True)
    
    original_filename = os.path.join(output_dir, f"{base_filename}_original.txt")
    translated_filename = os.path.join(output_dir, f"{base_filename}_{target_language}.txt")
    
    with open(original_filename, 'w', encoding='utf-8') as f:
        f.write(original_text)
    
    with open(translated_filename, 'w', encoding='utf-8') as f:
        f.write(translated_text)

    print(f"Transcrições salvas em:\n - {original_filename}\n - {translated_filename}")

def handle_downloaded_video(mp4_file_path, keep_video, new_output_filename):
    if keep_video:
        videos_dir = "videos_youtube"
        os.makedirs(videos_dir, exist_ok=True)
        new_path = os.path.join(videos_dir, new_output_filename)
        shutil.move(mp4_file_path, new_path)
        print(f"Vídeo movido para {new_path}")
    else:
        os.remove(mp4_file_path)
        print(f"Vídeo {mp4_file_path} removido")
