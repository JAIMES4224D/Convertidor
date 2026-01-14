# 🎵 DEVPASS Converter - YouTube to MP3 High Fidelity

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blueviolet?style=for-the-badge)
![FFmpeg](https://img.shields.io/badge/Engine-FFmpeg-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)

Una herramienta de escritorio profesional diseñada para descargar y convertir contenido de YouTube a formato MP3 con la máxima calidad de audio posible (320kbps).

Desarrollado bajo la marca **DEVPASS DIGITAL SOLUTIONS** como una solución robusta frente a los convertidores web llenos de publicidad.

## 🚀 Características Principales

* **🎧 Calidad de Estudio:** Fuerza la extracción de audio usando el codec `libmp3lame` a **320kbps** (Bitrate constante).
* **🎨 Interfaz Moderna (GUI):** Construida con `CustomTkinter`, ofrece modo oscuro/claro automático y un diseño minimalista tipo Windows 11.
* **⚡ Concurrencia (Threading):** Implementación de hilos separados para la lógica de descarga y la UI, evitando que la ventana se congele ("No responde") durante procesos pesados.
* **📂 Gestión de Archivos:** Permite al usuario seleccionar rutas de destino personalizadas.
* **📦 100% Portable:** Empaquetado en un solo ejecutable (`.exe`) con FFmpeg embebido, sin necesidad de instalaciones externas.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Core:** `yt-dlp` (Gestión de descargas y evasión de throttling).
* **Motor de Conversión:** `FFmpeg` & `FFprobe`.
* **Interfaz:** `CustomTkinter` & `Tkinter`.
* **Compilación:** `PyInstaller` (OneFile mode).

## 💻 Instalación y Uso (Código Fuente)

Si deseas ejecutar el proyecto desde el código fuente:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/TuUsuario/DevPass-Converter.git](https://github.com/TuUsuario/DevPass-Converter.git)
    cd DevPass-Converter
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configurar FFmpeg:**
    Asegúrate de tener `ffmpeg.exe` y `ffprobe.exe` en la carpeta raíz del proyecto o agregados a tus variables de entorno.

4.  **Ejecutar:**
    ```bash
    python gui.py
    ```

## 📦 Descargar Ejecutable (.exe)

Puedes encontrar la última versión compilada lista para usar en la sección de **Releases**.
*(Simplemente descarga, ejecuta y disfruta. No requiere instalación).*

## ⚠️ Disclaimer Legal

Este software fue desarrollado con fines educativos y de uso personal ("Fair Use"). El usuario es responsable de respetar los derechos de autor y los Términos de Servicio de YouTube.

## 📄 Licencia y Derechos de Autor

Este proyecto está protegido bajo la licencia **CC BY-NC 4.0** (Creative Commons Non-Commercial).

❌ **Prohibido:**
* Vender este software.
* Incluir este código en paquetes de software de pago.
* Usarlo para generar ingresos directos o indirectos.

✅ **Permitido:**
* Descargarlo para uso personal.
* Modificarlo para aprender (Uso Educativo).
* Compartirlo con amigos (dando crédito a DEVPASS).

**Copyright © 2026 DEVPASS DIGITAL SOLUTIONS**
---
**Desarrollado por [Jeferson Jaimes](https://www.linkedin.com/in/jeferson-jociney-jaimes-passuni-700a58236/)**
*Systems Engineer | DEVPASS DIGITAL SOLUTIONS*
