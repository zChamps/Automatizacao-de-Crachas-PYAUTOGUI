def matricula_foto():

    import requests
    import re
    from bs4 import BeautifulSoup
    import shutil
    import os
    from urllib.parse import urljoin
    from PIL import Image
    matriculas1 = []
        
    with open("links.txt", "r") as arquivo:
        for i in arquivo:

    # Faz a requisição para obter o conteúdo HTML da página
            requisitar = requests.get(i)
            html = requisitar.text

            soup = BeautifulSoup(html, 'html.parser')

            # Encontra todos os textos na página
            textos = soup.get_text()

            # Define o padrão usando uma expressão regular
            padrao = r"\w+ \((\d+)\)"

            matriculas = re.findall(padrao, textos)
            

            if matriculas:
                for matricula in matriculas:
                    
                    if len (matricula) > 5:
                        matriculas1.append(matricula)
                        matriculas_foto = matricula

        ##############################################################################################################



            # Faz o download do conteúdo HTML da página
            response = requests.get(i)
            html_content = response.text
            html_content = response.text

            soup = BeautifulSoup(html_content, 'html.parser')

            # Encontra todas as tags de imagem na página
            image_tags = soup.find_all('img')

            # Diretório de destino para salvar as imagens
            diretorio_de_destino = r'Diretório'

            # Verifica se o diretório de destino existe, se não, cria-o
            if not os.path.exists(diretorio_de_destino):
                os.makedirs(diretorio_de_destino)

            # Loop pelas tags de imagem encontradas
            for img in image_tags:
                # Obtém o URL da imagem
                image_url = img['src']
                
                # Verifica se o nome da imagem não é 'formulario_cracha.png' e 'serval_50.png'
                if image_url.split('/')[-1] != 'formulario_cracha.png' and image_url.split('/')[-1] != 'serval_50.png':
                    # Converte URL relativa em URL absoluta
                    absolute_url = urljoin(i, image_url)
                    
                    # Faz o download da imagem
                    response = requests.get(absolute_url, stream=True)
                    
                    # Verifica se o download foi bem-sucedido
                    if response.status_code == 200:
                        # Cria o caminho completo do arquivo de destino
                        foto_final = matriculas_foto[2:]
                        filename = foto_final + ".jpg"
                        destination_path = os.path.join(diretorio_de_destino, filename)
                        
                        # Salva a imagem no diretório de destino
                        with open(destination_path, 'wb') as out_file:
                            response.raw.decode_content = True
                            shutil.copyfileobj(response.raw, out_file)
                        
                        imagem_original =  Image.open(destination_path)
                        imagem = imagem_original.convert("RGB")
                        largura_cm = 29   
                        altura_cm = 42

                        # Converte as dimensões em centímetros para pixels
                        PPI = imagem.info.get('dpi', (72, 72))[0]  # Obtém a resolução da imagem em pixels por polegada (horizontal)
                        largura_px = int(largura_cm * PPI / 2.54)
                        altura_px = int(altura_cm * PPI / 2.54)

                        # Redimensiona a imagem
                        imagem_redimensionada = imagem.resize((largura_px, altura_px), resample=Image.LANCZOS)
                        # imagem_redimensionada = imagem.resize((largura_px, altura_px))
                        caminho_salvar = f"caminho onde a imagem será salva"
                        # Salva a imagem redimensionada
                        imagem_redimensionada.save(caminho_salvar)
                        
                    else:
                        print('Falha ao fazer o download da imagem:', image_url)


    with open("matriculas.txt", "w") as arquivo:
        for i in matriculas1:
            arquivo.write(i + "\n")






if __name__ == "__main__":
    matricula_foto()