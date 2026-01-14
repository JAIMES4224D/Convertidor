# -----------------------------------------------------------------------------
# DEVPASS CONVERTER - YouTube to MP3 High Fidelity
# Copyright (c) 2026 DEVPASS DIGITAL SOLUTIONS (Jeferson Jaimes)
#
# Este software es propiedad intelectual de DEVPASS DIGITAL SOLUTIONS.
# Se distribuye bajo la licencia "Creative Commons Atribución-NoComercial 4.0".
# 
# ESTÁ TOTALMENTE PROHIBIDO SU USO COMERCIAL O LUCRO.
# Se permite el uso personal y educativo.
# -----------------------------------------------------------------------------
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
