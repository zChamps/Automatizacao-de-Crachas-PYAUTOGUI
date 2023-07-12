import requests
import re
from bs4 import BeautifulSoup
import shutil
import os
from urllib.parse import urljoin
from PIL import Image
matriculas1 = []
i = 0
while True:
    digite_url = input("Digite a URL a ser extraida a matricula: ")

    
    if digite_url.lower() == "s":
        break
    # Faz a requisição para obter o conteúdo HTML da página
    requisitar = requests.get(f'{digite_url}')
    html = requisitar.text

    # Cria um objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(html, 'html.parser')


    # Encontra todos os textos na página
    textos = soup.get_text()

    # Define o padrão usando uma expressão regular
    padrao = r"\w+ \((\d+)\)"

    # Procura o padrão na página
    matriculas = re.findall(padrao, textos)
    

    # Verifica se o padrão foi encontrado
    if matriculas:
        for matricula in matriculas:
            # Copia cada matrícula para a área de transferência
            if len (matricula) > 5:
                matriculas1.append(matricula)
                matriculas_foto = matricula

##############################################################################################################


    # URL da página da web que você deseja analisar
    url = digite_url

    # Faz o download do conteúdo HTML da página
    response = requests.get(url)
    html_content = response.text
    html_content = response.text

    # Cria um objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontra todas as tags de imagem (tags <img>) na página
    image_tags = soup.find_all('img')

    # Diretório de destino para salvar as imagens
    destination_directory = r'CAMINHO DO ARQUIVO'

    # Verifica se o diretório de destino existe, caso contrário, cria-o
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Loop pelas tags de imagem encontradas
    for img in image_tags:
        # Obtém o URL da imagem
        image_url = img['src']
        
        # Verifica se o nome da imagem não é 'formulario_cracha.png' e 'serval_50.png'
        if image_url.split('/')[-1] != 'formulario_cracha.png' and image_url.split('/')[-1] != 'serval_50.png':
            # Converte URL relativa em URL absoluta
            absolute_url = urljoin(url, image_url)
            
            # Faz o download da imagem
            response = requests.get(absolute_url, stream=True)
            
            # Verifica se o download foi bem-sucedido
            if response.status_code == 200:
                # Cria o caminho completo do arquivo de destino
                foto_final = matriculas_foto[2:]
                filename = foto_final + ".jpg"
                destination_path = os.path.join(destination_directory, filename)
                
                # Salva a imagem no diretório de destino
                with open(destination_path, 'wb') as out_file:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, out_file)
                
                imagem =  Image.open(destination_path)
                largura_cm = 29   
                altura_cm = 42

                # Converte as dimensões em centímetros para pixels
                PPI = imagem.info.get('dpi', (72, 72))[0]  # Obtém a resolução da imagem em pixels por polegada (horizontal)
                largura_px = int(largura_cm * PPI / 2.54)
                altura_px = int(altura_cm * PPI / 2.54)

                # Redimensiona a imagem
                imagem_redimensionada = imagem.resize((largura_px, altura_px), resample=Image.LANCZOS)
                # imagem_redimensionada = imagem.resize((largura_px, altura_px))
                caminho_salvar = f"CAMINHO ARQUIVO"
                # Salva a imagem redimensionada
                imagem_redimensionada.save(caminho_salvar)
            else:
                print('Falha ao fazer o download da imagem:', image_url)


with open("matriculas.txt", "w") as arquivo:
    for i in matriculas1:
        arquivo.write(i + "\n")







input("pressione qualquer botao ")