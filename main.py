from pytube import YouTube

def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        print(f"Pobieranie: {yt.title}...")
        stream.download()
        print("Pobieranie zakończone!")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    url = input("Podaj URL filmu z YouTube: ")
    download_video(url)
