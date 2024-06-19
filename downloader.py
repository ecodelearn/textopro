import subprocess
import yt_dlp
import os

def download_video(video_url):
    def get_video_info(url):
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'force_generic_extractor': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'unknown_title')
            channel = info.get('uploader', 'unknown_channel')
            video_id = info.get('id', 'unknown_id')
            return title, channel, video_id

    video_title, channel_name, video_id = get_video_info(video_url)
    print(f'Título do vídeo: {video_title}')
    print(f'Nome do canal: {channel_name}')

    output_template = f"temp/{video_id}.%(ext)s"
    command = ['yt-dlp', '-f', 'bestvideo+bestaudio', '--merge-output-format', 'mp4', '-o', output_template, video_url]

    subprocess.run(command, check=True)

    safe_video_title = "".join([c if c.isalnum() else "_" for c in video_title])
    safe_channel_name = "".join([c if c.isalnum() else "_" for c in channel_name])
    new_output_filename = f"{safe_channel_name}_{safe_video_title}.mp4"
    os.rename(f"temp/{video_id}.mp4", f"temp/{new_output_filename}")

    return new_output_filename
