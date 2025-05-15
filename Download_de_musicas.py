#PRA RODAR, INSTALE O PIP DO PYTHON - APOS 
#python get-pip.py

# Caso apresente alguma coisa
# python -m pip install yt-dlp


import os
import tkinter as tk
from tkinter import messagebox

# Caminho fixo de destino
destino = r"D:\Users\Public\Area de Trabalho\Musicas\%(title)s.%(ext)s"

def baixar():
    url = entrada.get().strip()
    if not url:
        messagebox.showwarning("Aviso", "Por favor, cole o link da música ou playlist.")
        return
    comando = f'yt-dlp -x --audio-format mp3 -o "{destino}" "{url}"'
    print("Executando:", comando)
    os.system(comando)
    messagebox.showinfo("Concluído", "Download finalizado!")

# Criando a janela
janela = tk.Tk()
janela.title("YouTube Downloader")
janela.geometry("500x150")

# Texto explicativo
label = tk.Label(janela, text="Cole o link do vídeo ou playlist do YouTube:")
label.pack(pady=10)

# Campo de entrada
entrada = tk.Entry(janela, width=60)
entrada.pack()

# Botão de download
botao = tk.Button(janela, text="Baixar MP3", command=baixar)
botao.pack(pady=10)

# Executar a interface
janela.mainloop()
