import requests
import os

# URL da API pública
API_URL = "https://api.thecatapi.com/v1/images/search"

# Diretório onde as imagens serão salvas
IMAGE_DIR = "images"

# Criando a pasta caso não exista
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def baixar_imagem_de_gato():
    try:
        # Fazendo a requisição GET para a API
        response = requests.get(API_URL)
        response.raise_for_status()  # Lança erro se houver problema na resposta

        # Extraindo a URL da imagem
        data = response.json()
        image_url = data[0]['url']

        # Baixando a imagem
        img_response = requests.get(image_url)
        img_response.raise_for_status()

        # Nomeando a imagem
        img_name = os.path.join(IMAGE_DIR, f"gato_{data[0]['id']}.jpg")

        # Salvando a imagem no diretório
        with open(img_name, "wb") as img_file:
            img_file.write(img_response.content)

        print(f"✅ Imagem salva com sucesso: {img_name}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao buscar imagem: {e}")

if __name__ == "__main__":
    baixar_imagem_de_gato()
