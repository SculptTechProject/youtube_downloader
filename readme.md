# YouTube Downloader

Prosty skrypt do pobierania filmów z YouTube przy użyciu `yt-dlp`.

## 📥 Instalacja
1. Pobierz repozytorium:
   ```sh
   git clone https://github.com/SculptTechProject/youtube_downloader.git
   cd YouTube_downloader
   ```
2. Utwórz wirtualne środowisko i zainstaluj zależności:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```
3. Zainstaluj `ffmpeg`:
   - **Linux (Ubuntu/Debian)**: `sudo apt install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Windows**: Pobierz i skonfiguruj `ffmpeg` z [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)

## 🚀 Użycie
Uruchom skrypt:
```sh
python main.py
```
Podaj URL filmu z YouTube i poczekaj na pobranie pliku.

## 📌 Wymagania
- Python 3.8+
- `yt-dlp`
- `ffmpeg`

Miłego pobierania! 🎥
