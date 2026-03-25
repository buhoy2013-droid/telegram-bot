import os
import yt_dlp

def download_tiktok_stable():
    url = input("Игорь, вставь ссылку на профиль: ").strip()
    username = url.split('@')[-1].split('/')[0].split('?')[0]
    folder = f"tiktok_{username}"
    
    if not os.path.exists(folder):
        os.makedirs(folder)

    ydl_opts = {
        # Буква 'b' означает "best single file". 
        # Скрипт скачает только тот файл, где видео и звук УЖЕ слеплены вместе.
        'format': 'b[ext=mp4]/b', 
        
        # Жестко запрещаем качать картинки, обложки и прочий мусор
        'writethumbnail': False,
        'write_all_thumbnails': False,
        
        # Скачиваем от старых к новым
        'playlistreverse': True,
        'ignoreerrors': True,
        
        # Формируем простое имя файла
        'outtmpl': f'{folder}/%(upload_date)s_%(id)s_%(playlist_index)s.%(ext)s',
        
        # Маскируемся под обычный браузер
        'add_header': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        },
    }

    print(f"\n[СТАРТ] Запускаю стабильную загрузку для @{username}...")
    print("[ИНФО] Скачиваются только готовые видео. Мусор отключен.")
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"Ошибка при загрузке: {e}")

    print(f"\n[ГОТОВО] Зайди в папку {folder}. Там должны быть только видео.")

if __name__ == "__main__":
    download_tiktok_stable()