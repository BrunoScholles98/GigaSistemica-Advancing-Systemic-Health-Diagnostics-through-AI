import os
import gdown

def download_file_from_google_drive(file_id):
    # Nome do arquivo para salvar localmente
    output = "dataset.zip"
    
    # URL para download via gdown
    url = f"https://drive.google.com/uc?id={file_id}"
    
    # Baixa o arquivo
    print(f"Baixando o dataset para {output}...")
    gdown.download(url, output, quiet=False)

    # Descompacta o arquivo, se necessário
    if output.endswith(".zip"):
        print("Descompactando o arquivo...")
        os.system(f"unzip {output} -d ./dataset")
        print("Dataset descompactado na pasta './dataset'.")

if __name__ == "__main__":
    # ID do arquivo no Google Drive (extraído do link)
    file_id = "1wtF7tJy0Rn1SWawRLstssg6a2hOzhTxM"
    download_file_from_google_drive(file_id)
