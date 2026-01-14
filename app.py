import yt_dlp
import os

def descargar_audio(url_youtube):
    print(f"Iniciando descarga de: {url_youtube}")
    
    
    opciones = {
        'format': 'bestaudio/best', 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320', 
        }],
        'outtmpl': '%(title)s.%(ext)s', 
        'quiet': False,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(opciones) as ydl:
            
            info = ydl.extract_info(url_youtube, download=False)
            print(f"Título detectado: {info['title']}")
            print("Descargando y convirtiendo... esto puede tomar unos segundos.")
            
            # Descargar
            ydl.download([url_youtube])
            
            print(f"\n¡Éxito! Archivo guardado como: {info['title']}.mp3")
            
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    print("--- DEVPASS CONVERTER (Python + yt-dlp) ---")
    url = input("Ingresa el enlace de YouTube: ")
    if url:
        descargar_audio(url)