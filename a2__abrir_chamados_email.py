def chamados_email():

    import pyautogui as pa
    import time
    import pyperclip as pc
    lista_mat = []

    #######COLOCAR ZOOM NO 80%

    #SALVANDO AS MATRICULAS A SEREM ADICIONADAS NO TXT

    while True:
        matriculas = input("Digite as matriculas a seguir: ")
        if matriculas.lower() == "s":
            break
        if not matriculas == "" or matriculas == " " or matriculas == "\n":
            lista_mat.append(matriculas)

    caminho = r"CAMINHO_ARQUIVO"


    #apagar todo o conteudo do arquivo
    with open(caminho, 'w') as arquivo:
        arquivo.write('')

    #salvando os dados no arquivo
    with open(caminho, "w") as arquivo:
        for i in lista_mat:
            arquivo.write(str(i) + "\n")

    #######################################################################################

    #ABRIR CHAMADOS COM AS MATRICULAS SALVAS

    #abrir o Google
    pa.click(266,880, duration=0.8)
    pa.click(371,790, duration=0.8)

    #entrar no protocolo com o tela previamente aberto e logado
    pa.click(52,372, duration=0.8)
    pa.click(74,416, duration=0.8)
    time.sleep(4)

    #abrir os chamados
    with open(caminho, "r") as arquivo:
        for i in arquivo:
            pc.copy(i)
            pa.doubleClick(1434,482, duration=0.5)
            pa.hotkey("ctrl", "v")
            pa.keyDown("ctrl")
            pa.click(260,565, duration=0.5)
            pa.keyUp("ctrl")