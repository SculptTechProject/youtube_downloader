import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': '%(title)s.mp4',
        'merge_output_format': 'mp4'
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Pobieranie zakończone!")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    url = input("Podaj URL filmu z YouTube: ")
    download_video(url)