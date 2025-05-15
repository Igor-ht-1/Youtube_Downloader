# Youtube_Downloader
Pra baixar musicas do br pros br


# YouTube Playlist Downloader - MP3

Este é um aplicativo simples em Python com interface gráfica para baixar músicas (MP3) de vídeos ou playlists do YouTube usando o [yt-dlp](https://github.com/yt-dlp/yt-dlp).

---

## Funcionalidades

* Baixa áudio em formato MP3 de vídeos ou playlists do YouTube.
* Interface gráfica simples e fácil de usar (Tkinter).
* Salva os arquivos na pasta definida no código (pode ser alterada).

---

## Pré-requisitos

* Python 3 instalado no sistema ([baixar aqui](https://www.python.org/downloads/))
* Biblioteca `yt-dlp` instalada
* Sistema Windows (testado)

---

## Como instalar

1. Clone este repositório ou faça download do código:

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
```

2. Instale o `yt-dlp` usando o pip:

```bash
pip install yt-dlp
```

3. (Opcional) Se não tiver o `pip` instalado, faça o download do script `get-pip.py` e instale-o:

```bash
python get-pip.py
```

---

## Como usar

1. Abra o terminal ou prompt de comando.
2. Navegue até a pasta do projeto:

```bash
cd caminho/para/a/pasta
```

3. Execute o programa:

```bash
python youtube_app.py
```

4. Cole o link do vídeo ou playlist do YouTube na janela que abrir.
5. Clique em "Baixar MP3" e aguarde o download ser concluído.

---

## Personalização

Você pode alterar o caminho onde os arquivos serão salvos modificando a variável `destino` no arquivo `youtube_app.py`:

```python
destino = r"D:\Users\Public\Area de Trabalho\Musicas\%(title)s.%(ext)s"
```

---

## Gerar Executável (.exe)

Para criar um executável Windows que roda sem precisar do Python instalado:

1. Instale o PyInstaller:

```bash
pip install pyinstaller
```

2. Gere o executável:

```bash
pyinstaller --noconsole --onefile youtube_app.py
```

3. O executável estará na pasta `dist`.

---

## Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usar e modificar.

---

## Contato

Para dúvidas ou sugestões, abra uma issue ou envie mensagem.

---

**Divirta-se baixando suas músicas favoritas! 🎵**

---

