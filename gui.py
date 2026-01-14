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
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import yt_dlp
import threading
import os

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue") 

class DevPassConverter(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("DEVPASS DIGITAL SOLUTIONS - MP3 Converter")
        self.geometry("700x450")
        self.resizable(False, False)
        try:
            self.iconbitmap("icon.ico")
        except Exception as e:
            print(f"Advertencia: No se pudo cargar el icono. {e}")

    
        self.download_folder = os.getcwd() 

    
        self.lbl_title = ctk.CTkLabel(self, text="DEVPASS CONVERTER", font=("Roboto Medium", 24))
        self.lbl_title.pack(pady=(30, 10))

        self.lbl_subtitle = ctk.CTkLabel(self, text="Descarga audio en Alta Calidad (320kbps)", font=("Roboto", 14), text_color="gray")
        self.lbl_subtitle.pack(pady=(0, 30))

        
        self.input_frame = ctk.CTkFrame(self)
        self.input_frame.pack(pady=10, padx=40, fill="x")

        self.entry_url = ctk.CTkEntry(self.input_frame, placeholder_text="Pega el enlace de YouTube aquí...", height=40)
        self.entry_url.pack(side="left", fill="x", expand=True, padx=(10, 10), pady=10)

        
        self.btn_folder = ctk.CTkButton(self, text="📂 Seleccionar Carpeta", command=self.select_folder, fg_color="#2B2B2B", hover_color="#3A3A3A")
        self.btn_folder.pack(pady=10)
        
        self.lbl_path = ctk.CTkLabel(self, text=f"Guardar en: {self.download_folder}", font=("Arial", 10), text_color="gray")
        self.lbl_path.pack(pady=(0, 20))

    
        self.btn_download = ctk.CTkButton(self, text="DESCARGAR MP3", command=self.start_download_thread, height=50, font=("Roboto Medium", 16))
        self.btn_download.pack(pady=10, padx=40, fill="x")

        
        self.lbl_status = ctk.CTkLabel(self, text="Listo para trabajar", font=("Roboto", 12))
        self.lbl_status.pack(pady=(20, 5))

        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=5)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.download_folder = folder
            self.lbl_path.configure(text=f"Guardar en: {self.download_folder}")

    def start_download_thread(self):
        
        url = self.entry_url.get()
        if not url:
            messagebox.showwarning("Alerta", "Por favor ingresa una URL válida.")
            return
        
        self.btn_download.configure(state="disabled", text="Procesando...")
        self.progress_bar.set(0)
        
        
        thread = threading.Thread(target=self.download_logic, args=(url,))
        thread.start()

    def download_logic(self, url):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f'{self.download_folder}/%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }],
                'progress_hooks': [self.my_hook], 
                'quiet': True,
                'no_warnings': True,
            }

            self.update_status("Conectando con YouTube...", "orange")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            self.update_status("¡Conversión completada con éxito!", "green")
            messagebox.showinfo("Éxito", "El audio se ha descargado correctamente.")
            self.entry_url.delete(0, 'end') 

        except Exception as e:
            self.update_status(f"Error: {str(e)}", "red")
            messagebox.showerror("Error Crítico", f"Ocurrió un error:\n{e}")
        
        finally:
            
            self.after(0, lambda: self.btn_download.configure(state="normal", text="DESCARGAR MP3"))

    def my_hook(self, d):
        if d['status'] == 'downloading':
            try:
                
                total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
                downloaded = d.get('downloaded_bytes')
                if total_bytes:
                    percentage = downloaded / total_bytes
                
                    self.after(0, lambda: self.progress_bar.set(percentage))
                    
                
                    percent_str = str(int(percentage * 100))
                    self.update_status(f"Descargando: {percent_str}%", "text_color")
            except:
                pass
        
        elif d['status'] == 'finished':
            self.update_status("Convirtiendo a MP3 (Usando FFmpeg)...", "blue")
            self.after(0, lambda: self.progress_bar.set(1)) 

    def update_status(self, text, color_code):
        color = "white"
        if color_code == "green": color = "#2CC985"
        elif color_code == "red": color = "#FF5555"
        elif color_code == "orange": color = "#F1C40F"
        elif color_code == "blue": color = "#3B8ED0"
        
            
        self.after(0, lambda: self.lbl_status.configure(text=text, text_color=color))

if __name__ == "__main__":
    app = DevPassConverter()

    app.mainloop()
