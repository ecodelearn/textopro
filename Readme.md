# Escolha o Idioma | Choose the Language

- [Português](#textopro)
- [English](#textopro---audio-and-video-transcriber-and-translator)

---

# TextoPro

## Transcritor e Tradutor de Áudio e Vídeo

Este projeto é um transcritor e tradutor de áudio automatizado usando Whisper da OpenAI. O script pode baixar vídeos do YouTube, extrair o áudio, transcrever e traduzir o texto, salvando em arquivos de texto separados.

## Créditos

Daniel Dias  
Site: [https://inarte.com.br](https://inarte.com.br)  
Administrador da Comunidade Sandeco e apoiador do canal [YouTube Sandeco](https://youtube.com/@sandeco)

Matheus Bach  
LeGen: [matheusbach/legen](https://github.com/matheusbach/legen)

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

```plaintext
texto-pro/
├── __init__.py
├── downloader.py
├── file_manager.py
├── main.py
├── transcriber.py
├── translator.py
├── utils.py
├── whisper_utils.py
├── venv/
│   └── ... (arquivos da virtual environment)
└── requirements.txt
```

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
  ```

  Em seguida, recarregue o `~/.bashrc`:
  ```bash
  source ~/.bashrc
  ```

- **No Windows**:
  Adicione `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.4\bin` ao PATH nas variáveis de ambiente do sistema.

#### 5. Instale o cuDNN

- **Baixe o cuDNN**: Acesse o site de download do cuDNN e baixe a versão que corresponde à sua versão do CUDA.

- **Instale o cuDNN**:

  - **No Linux**:

    Extraia os arquivos do cuDNN e copie-os para os diretórios do CUDA:
    ```bash
    tar -xzvf cudnn-<version>-linux-x64-v<version>.tgz
    sudo cp cuda/include/cudnn*.h /usr/local/cuda/include
    sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64
    sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
    ```

  - **No Windows**:

    Extraia os arquivos do cuDNN e copie-os para os diretórios do CUDA. Normalmente, você colocará os arquivos no diretório `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.4`.

#### 6. Verifique a Instalação

Para verificar se o CUDA e o cuDNN estão instalados corretamente, execute os seguintes comandos:
```bash
nvcc --version
```
Você deve ver a versão do CUDA Toolkit instalada.

#### 7. Instale o PyTorch com Suporte a CUDA

Finalmente, instale o PyTorch com suporte a CUDA:
```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu11x
```

#### 8. Verifique se o PyTorch Detecta a GPU

Para garantir que o PyTorch está configurado corretamente para usar a GPU, execute o seguinte código no Python:
```python
import torch
print(torch.cuda.is_available())
```
Se a instalação estiver correta, isso deve retornar `True`.

## Instalação do Projeto

Clone o repositório:

```bash
git clone https://github.com/ecodelearn/textopro.git
cd textopro
```

Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Instale o `ffmpeg` e `yt-dlp`, se ainda não estiverem instalados:

```bash
sudo apt-get install ffmpeg
pip install yt-dlp
```

## Uso

Execute o script principal:

```bash
python main.py
```

Siga as instruções na tela:

1. Escolha fornecer um caminho para um arquivo `.mp4` ou baixar do YouTube.
2. Se optar por baixar do YouTube, forneça o link do vídeo.
3. Selecione o idioma de entrada.
4. Selecione o modelo Whisper a ser usado.
5. A transcrição e tradução serão salvas no diretório `textos_transcritos`.

---

# TextoPro - Audio and Video Transcriber and Translator

This project is an automated audio transcriber and translator using OpenAI's Whisper. The script can download YouTube videos, extract the audio, transcribe, and translate the text, saving them into separate text files.

## Credits

Daniel Dias  
Website: [https://inarte.com.br](https://inarte.com.br)  
Administrator of Sandeco Community and supporter of [YouTube Sandeco](https://youtube.com/@sandeco)

Matheus Bach  
LeGen: [matheusbach/legen](https://github.com/matheusbach/legen)

## Menu Functions

### Main Menu

When running the main script `main.py`, you'll see the main menu with options to provide a path to an `.mp4` file or download a YouTube video. Choose one of the options:

1. Provide a path to an `.mp4` file
2. Download from YouTube

### Input Language Selection

After choosing the video source, the script will ask you to select the input language. You will see a list of supported languages. Type the number corresponding to the desired language.

### Whisper Model Selection

The script will ask you to select the Whisper model to be used. Choose one of the available models by typing the corresponding number.

### Processing and Saving

The script will process the audio, generate the transcription and translation, and save the results in separate text files in the `textos_transcritos` directory.

## Technical Information and Installation

### Project Structure

```plaintext
texto-pro/
├── __init__.py
├── downloader.py
├── file_manager.py
├── main.py
├── transcriber.py
├── translator.py
├── utils.py
├── whisper_utils.py
├── venv/
│   └── ... (virtual environment files)
└── requirements.txt
```

### Files and Functions

- **`downloader.py`**: Contains the function `download_video(url)` that downloads a YouTube video using `yt_dlp` and saves it in the `temp` directory.
- **`file_manager.py`**: 
  - `save_transcription(base_filename, original_text, translated_text, target_language)`: Saves the transcription and translation into separate files.
  - `handle_downloaded_video(mp4_file_path, keep_video, new_output_filename)`: Moves or removes the downloaded video based on the user's choice.
- **`main.py`**: Main script managing the program flow.
- **`transcriber.py`**: Contains the function `process_audio_file(mp3_file_path, model, input_language, output_filename)` that processes the audio and generates the transcription.
- **`translator.py`**: Contains the function `translate_text(original_text, detected_language)` that translates the transcription text to the desired language.
- **`utils.py`**: 
  - `clear_screen()`: Clears the screen.
  - `select_language()`: Allows the selection of the input language.
- **`whisper_utils.py`**: Contains the function `load_model()` that loads the appropriate Whisper model.

### Prerequisites

- Python 3.7 or higher
- ffmpeg
- yt-dlp
- CUDA and cuDNN (for GPU acceleration)
- Install dependencies listed in `requirements.txt`

### CUDA and cuDNN Installation

#### 1. Check GPU Compatibility

Ensure your GPU is CUDA-compatible on [NVIDIA's website](https://developer.nvidia.com/cuda-gpus).

#### 2. Download and Install NVIDIA Drivers

1. **Download the appropriate driver for your GPU**: Go to the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx) and download the correct driver for your GPU.
2. **Install the driver**: Follow NVIDIA's installation instructions.

#### 3. Install CUDA Toolkit

1. **Download CUDA Toolkit**: Visit the [CUDA Toolkit download page](https://developer.nvidia.com/cuda-downloads) and download the correct version for your operating system.
2. **Install CUDA Toolkit**:
   - On Linux, follow the instructions to install the CUDA Toolkit. Typically, you will run commands like:

     ```bash
     sudo dpkg -i cuda-repo-<distro>_<version>_amd64.deb
     sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/<distro>/x86_64/7fa2af80.pub
     sudo apt-get update
     sudo apt-get install cuda
     ```

   - On Windows, run the installer and follow the on-screen instructions.

#### 4. Add CUDA to PATH

After installation, add CUDA to your PATH:

- **On Linux**:
  Add the following lines to your `~/.bashrc`:

  ```bash
  export PATH=/usr/local/cuda/bin:$PATH
  export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
  ```

  Then reload the `~/.bashrc`:
  ```bash
  source ~/.bashrc
  ```

- **On Windows**:
  Add `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.4\bin` to the system environment variables PATH.

#### 5. Install cuDNN

- **Download cuDNN**: Visit the cuDNN download page and download the version that matches your CUDA version.

- **Install cuDNN**:

  - **On Linux**:

    Extract the cuDNN files and copy them to the CUDA directories:
    ```bash
    tar -xzvf cudnn-<version>-linux-x64-v<version>.tgz
    sudo cp cuda/include/cudnn*.h /usr/local/cuda/include
    sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda/lib64
    sudo chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda/lib64/libcudnn*
    ```

  - **On Windows**:

    Extract the cuDNN files and copy them to the CUDA directories. Typically, you will place the files in `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.4`.

#### 6. Verify Installation

To verify that CUDA and cuDNN are correctly installed, run the following commands:
```bash
nvcc --version
```
You should see the installed version of the CUDA Toolkit.

#### 7. Install PyTorch with CUDA Support

Finally, install PyTorch with CUDA support:
```bash
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu11x
```

#### 8. Check if PyTorch Detects the GPU

To ensure PyTorch is properly set up to use the GPU, run the following code in Python:
```python
import torch
print(torch.cuda.is_available())
```
If the installation is correct, this should return `True`.

## Project Installation

Clone the repository:

```bash
git clone https://github.com/ecodelearn/textopro.git
cd textopro
```

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Install `ffmpeg` and `yt-dlp` if not already installed:

```bash
sudo apt-get install ffmpeg
pip install yt-dlp
```

## Usage

Run the main script:

```bash
python main.py
```

Follow the on-screen instructions:

1. Choose to provide a path to an `.mp4` file or download from YouTube.
2. If downloading from YouTube, provide the video link.
3. Select the input language.
4. Select the Whisper model to be used.
5. The transcription and translation will be saved in the `textos_transcritos` directory.

This project is licensed under the terms of the [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/).
