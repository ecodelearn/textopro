# Transcritor e Tradutor de Áudio e Vídeo

Este projeto é um transcritor e tradutor de áudio automatizado usando Whisper da OpenAI. O script pode baixar vídeos do YouTube, extrair o áudio, transcrever e traduzir o texto, salvando em arquivos de texto separados.

## Créditos

Daniel Dias  
Site: [https://inarte.com.br](https://inarte.com.br)  
Administrador da Comunidade Sandeco e apoiador do canal [YouTube Sandeco](https://youtube.com/@sandeco)

## Funcionamento dos Menus de Seleção

### Menu Principal

Ao executar o script principal `main.py`, você verá o menu principal com a opção de fornecer um caminho para um arquivo `.mp4` ou baixar um vídeo do YouTube. Escolha uma das opções:

1. Fornecer um caminho para um arquivo `.mp4`
2. Baixar do YouTube

### Seleção de Idioma de Entrada

Após escolher a fonte do vídeo, o script solicitará que você selecione o idioma de entrada. Você verá uma lista de idiomas suportados. Digite o número correspondente ao idioma desejado.

### Seleção do Modelo Whisper

O script solicitará que você selecione o modelo Whisper a ser usado. Escolha um dos modelos disponíveis digitando o número correspondente.

### Processamento e Salvamento

O script processará o áudio, gerará a transcrição e a tradução, e salvará os resultados em arquivos de texto separados no diretório `textos_transcritos`.

## Informações Técnicas e de Instalação

### Estrutura do Projeto

transcritor/
│
├── novo/
│ ├── init.py
│ ├── downloader.py
│ ├── file_manager.py
│ ├── main.py
│ ├── transcriber.py
│ ├── translator.py
│ ├── utils.py
│ └── whisper_utils.py
│
├── venv/
│ └── ... (arquivos da virtual environment)
│
└── requirements.txt


### Arquivos e Funções

- **`downloader.py`**: Contém a função `download_video(url)` que baixa um vídeo do YouTube usando `yt_dlp` e salva no diretório `temp`.
- **`file_manager.py`**: 
  - `save_transcription(base_filename, original_text, translated_text, target_language)`: Salva a transcrição e tradução em arquivos separados.
  - `handle_downloaded_video(mp4_file_path, keep_video, new_output_filename)`: Move ou remove o vídeo baixado com base na escolha do usuário.
- **`main.py`**: Script principal que gerencia o fluxo do programa.
- **`transcriber.py`**: Contém a função `process_audio_file(mp3_file_path, model, input_language, output_filename)` que processa o áudio e gera a transcrição.
- **`translator.py`**: Contém a função `translate_text(original_text, detected_language)` que traduz o texto da transcrição para o idioma desejado.
- **`utils.py`**: 
  - `clear_screen()`: Limpa a tela.
  - `select_language()`: Permite a seleção do idioma de entrada.
- **`whisper_utils.py`**: Contém a função `load_model()` que carrega o modelo Whisper apropriado.

### Pré-requisitos

- Python 3.7 ou superior
- ffmpeg
- yt-dlp
- CUDA e cuDNN (para aceleração com GPU)
- Instalar dependências listadas no `requirements.txt`

### Instalação do CUDA e cuDNN

#### 1. Verifique a Compatibilidade da GPU

Verifique se sua GPU é compatível com CUDA no [site da NVIDIA](https://developer.nvidia.com/cuda-gpus).

#### 2. Baixe e Instale os Drivers NVIDIA

1. **Baixe o driver apropriado para sua GPU**: Vá para o [site de download de drivers da NVIDIA](https://www.nvidia.com/Download/index.aspx) e baixe o driver adequado para sua placa gráfica.
2. **Instale o driver**: Siga as instruções de instalação fornecidas pela NVIDIA.

#### 3. Instale o CUDA Toolkit

1. **Baixe o CUDA Toolkit**: Acesse o [site de download do CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) e baixe a versão apropriada para seu sistema operacional.
2. **Instale o CUDA Toolkit**:
   - No Linux, siga as instruções para instalar o CUDA Toolkit. Normalmente, você executará comandos como:

     ```bash
     sudo dpkg -i cuda-repo-<distro>_<version>_amd64.deb
     sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/<distro>/x86_64/7fa2af80.pub
     sudo apt-get update
     sudo apt-get install cuda
     ```

   - No Windows, execute o instalador e siga as instruções na tela.

#### 4. Adicione o CUDA ao PATH

Após a instalação, adicione o CUDA ao seu PATH:

- **No Linux**:
  Adicione as seguintes linhas ao seu `~/.bashrc`:

  ```bash
  export PATH=/usr/local/cuda/bin:$PATH
  export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
Em seguida, recarregue o ~/.bashrc:


source ~/.bashrc
No Windows:
Adicione C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.4\bin ao PATH nas variáveis de ambiente do sistema.
5. Instale o cuDNN
Baixe o cuDNN: Acesse o site de download do cuDNN e baixe a versão que corresponde à sua versão do CUDA.
Instale o cuDNN:
No Linux:

Extraia os arquivos do cuDNN e copie-os para os diretórios do CUDA:


tar -xzvf cudnn-<version>-linux-x64-v<version>.tgz
sudo cp cuda/include/cudnn*.h /usr/local/cuda/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
No Windows:

Extraia os arquivos do cuDNN e copie-os para os diretórios do CUDA. Normalmente, você colocará os arquivos no diretório C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.4.
6. Verifique a Instalação
Para verificar se o CUDA e o cuDNN estão instalados corretamente, execute os seguintes comandos:


nvcc --version
Você deve ver a versão do CUDA Toolkit instalada.

7. Instale o PyTorch com Suporte a CUDA
Finalmente, instale o PyTorch com suporte a CUDA:


pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu11x
8. Verifique se o PyTorch Detecta a GPU
Para garantir que o PyTorch está configurado corretamente para usar a GPU, execute o seguinte código no Python:


import torch
print(torch.cuda.is_available())
Se a instalação estiver correta, isso deve retornar True.

Instalação do Projeto
Clone o repositório:

git clone https://github.com/seu-usuario/transcritor.git
cd transcritor/novo
Crie um ambiente virtual:


python -m venv venv
source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
Instale as dependências:


pip install -r requirements.txt
Instale o ffmpeg e yt-dlp, se ainda não estiverem instalados:


sudo apt-get install ffmpeg
pip install yt-dlp
Uso
Execute o script principal:


python main.py
Siga as instruções na tela:

Escolha fornecer um caminho para um arquivo .mp4 ou baixar do YouTube.
Se optar por baixar do YouTube, forneça o link do vídeo.
Selecione o idioma de entrada.
Selecione o modelo Whisper a ser usado.
A transcrição e tradução serão salvas no diretório textos_transcritos.


MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
