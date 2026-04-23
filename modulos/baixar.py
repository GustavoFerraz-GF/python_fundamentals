import yt_dlp

url = "https://www.youtube.com/watch?v=9em32dDnTck"  # Ex: https://www.youtube.com/watch?v=abc123

opcoes = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:/Users/gferr/Downloads/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(opcoes) as ydl:
    print("Baixando...")
    ydl.download([url])
    print("Concluído!")