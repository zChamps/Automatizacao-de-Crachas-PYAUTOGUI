def links(a):
    from bs4 import BeautifulSoup
    import pyperclip
    from urllib.parse import urljoin
    from time import sleep

    lista_links = []

    contador=1
        #PEGA O CODIGO FONTE DA PAGINA E ENCONTRA O LINK DO FORMULÁRIO ABREVIADO
    while a >= contador:
        print("Pegue o proximo codigo fonte!")
        sleep(3)
        link = pyperclip.paste()

        soup = BeautifulSoup(link, "html.parser")

        links = soup.find_all('a')

        link_formulario  = []

        for i in links:
            link_formulario.append(i)

        link_extraido = link_formulario[-3]





        #IRÁ TRANSFORMAR O LINK ABREVIADO NO LINK COMPLETO
        html = str(link_extraido)
        base_url = 'https://intranet.gruposerval.com.br/tela/atendimentos/registros-form.php?id='

        # Criar um objeto BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Obter o valor do atributo 'href'
        href = soup.a['href']

        # Reconstruir o link completo usando a URL base
        full_link = urljoin(base_url, href)

        # Imprimir o link completo
        lista_links.append(full_link)
        contador+=1

    with open("links.txt" , "w") as arquivo:
        for i in lista_links:
            arquivo.write(f"{i} \n")

if __name__ == "__main__":
    links(1)