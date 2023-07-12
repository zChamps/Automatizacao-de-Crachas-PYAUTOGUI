def pegar_dados_rm(numero_crachas):
    import pyautogui
    import time

    #ajustar a largura e altura da pagina para zero
    pyautogui.moveTo(22,826)
    pyautogui.mouseDown()
    time.sleep(2)
    pyautogui.mouseUp()
    if numero_crachas >= 19:
        pyautogui.moveTo(1565,317)
        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.mouseUp()

    #caso tenha alguma linha selecionada, tirar a seleção
    pyautogui.click(545,361, duration=0.5)

    #selecionar os dados de todos os colaboradores
    pyautogui.moveTo(100,340)
    pyautogui.mouseDown()
    pyautogui.moveTo(1553,340)
    pyautogui.moveTo(1550,774)
    time.sleep(3)
    pyautogui.mouseUp()
    pyautogui.hotkey("ctrl", "c")

    #ir para o excel
    pyautogui.click(569,878, duration=0.5)
    pyautogui.click(633,797, duration=0.3)

    #Clicar na primeira celula e colar
    pyautogui.click(73,295, duration=0.5)
    pyautogui.hotkey("ctrl", "v")

    #entrar no RM
    pyautogui.click(616,880, duration=0.4)

    #redefinir a altura do rm
    if numero_crachas >= 19:
        pyautogui.moveTo(1565,317)
        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.mouseUp()

    #copiar todos os nomes
    pyautogui.click(270,312)
    pyautogui.moveTo(240,338)
    pyautogui.mouseDown()
    pyautogui.moveTo(198,793, duration=1)
    time.sleep(2)
    pyautogui.mouseUp()
    pyautogui.hotkey("ctrl", "c")

    #####################################################################################################
    # Realizar a simplificação dos nomes
    import os
    import pyperclip
    lista = []
    nomes_final = []
    conteudo_copia = pyperclip.paste().replace("\r", "")
    linhas = conteudo_copia.split("\n")
    for i in linhas:
        lista.append(i.split(" "))

    print(lista)
    while True:
            os.system("cls")
            
            i = 0

    #verificar quantos nomes a pessoa tem e realizar a exclusão dos nomes do meio de acordo
            while i < len(lista):
                #ignorar caso o nome comece por um desses abaixo
                verificacao = lista[i][0] == "FRANCISCO" or lista[i][0] == "MARIA" or lista[i][0] == "JOSE" or lista[i][0] == "JOAO"
                if len(lista[i]) > 2 and len(lista[i]) < 4:
                    if verificacao:
                        i += 1
                        continue
                    lista[i].pop(1)
                elif len(lista[i]) > 3 and len(lista[i]) < 5:
                    if verificacao:
                        i += 1
                        continue        
                    lista[i].pop(1)
                    lista[i].pop(1)
                elif len(lista[i]) > 4 and len(lista[i]) < 6:
                    if verificacao:
                        i += 1
                        continue
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                elif len(lista[i]) > 5 and len(lista[i]) < 7:
                    if verificacao:
                        i += 1
                        continue            
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                elif len(lista[i]) > 6 and len(lista[i]) < 8:
                    if verificacao:
                        i += 1
                        continue            
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                elif len(lista[i]) > 7 and len(lista[i]) < 9:
                    if verificacao:
                        i += 1
                        continue            
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                    lista[i].pop(1)
                i += 1
            os.system("cls")
            for a in lista:
                nomes_final.append(" ".join(a))
            
            nomes_final.pop()
            lista_string = '\n'.join(nomes_final)

    #copiar os dados para a area de transferencia
            pyperclip.copy(lista_string)
            break


    ######################################################################################################

    #voltar para o excel e colar os novos nomes
    pyautogui.click(569,878, duration=0.5)
    pyautogui.click(633,797, duration=0.3)
    pyautogui.click(242,299, duration=0.3)
    pyautogui.hotkey("ctrl", "v")


    #Voltar para o RM
    pyautogui.click(616,880, duration=0.4)

    #redefinir a altura do rm
    if numero_crachas >= 19:
        pyautogui.moveTo(1565,317)
        pyautogui.mouseDown()
        time.sleep(2)
        pyautogui.mouseUp()

    #copiar todos as escalas
    pyautogui.click(270,312)    
    pyautogui.moveTo(892,336)  
    pyautogui.mouseDown()
    pyautogui.moveTo(861,804, duration=1)
    time.sleep(2)
    pyautogui.mouseUp()
    pyautogui.hotkey("ctrl", "c")

    ######################################################################################################
    #realizar a simplificação das escalas
    import pyperclip

    final_padrao = []
    lista_escalas = []
    linhas = pyperclip.paste().replace("\r", "")
    escala = linhas.split("\n")

    lista_escalas.append(escala)

    for escalas in lista_escalas:
        #verificar qual o tipo de escala
        for i2 in escalas:
            lista2 = []
            lista3 = []
            lista_padrao = []
            lista_teste_dia = []

            lista2.clear()
            lista3.clear()
            lista_padrao.clear()
            lista_teste_dia.clear()

            # escalas mais curtas
            if len(i2) > 27 and len(i2) < 34:
                for a in i2:
                    lista2.append(a)
                valor_novo = "{}{}".format(lista2[:5], lista2[17:])
                lista_padrao.append(valor_novo)

                for i in lista_padrao:
                    teste = "".join(i)
                    teste1 = teste.replace("(", "").replace(")", "").replace("'", "").replace("\"", "").replace("[", "").replace("]", "").replace(",", "")
                    if len(teste1) == 32:
                        string1 = teste1[:20].replace(" ", "")
                        string2 = teste1[-6:].replace(" ", "")
                    elif len(teste1) == 36:
                        string1 = teste1[:20].replace(" ", "")
                        string2 = teste1[-9:].replace(" ", "")
                    final = f"{string1} | {string2}"
                    final_padrao.append(final)

            # escala intermitente
            if len(i2) > 49 and len(i2) < 53:
                for i in i2:
                    lista2.append(i)
                lista_padrao.append(lista2[16:28])    

                for i in lista_padrao:
                        teste = "".join(i)
                        teste1 = teste.replace("(", "").replace(")", "").replace("'", "").replace("\"", "").replace("[", "").replace("]", "").replace(",", "")
                final_padrao.append("".join(teste1))


            # escalas 6x1 ou 5x2 maiores
            elif len(i2) > 58 and len(i2) < 63:
                lista2.append(i2[:23])    #08:00-12:00-13:00-18:00     | 07:30-12:30-13:30-16:00
                lista_teste_dia.append(i2[58:])  #SEX    |  SAB
                for i in lista2:
                    for a in i:
                        lista3.append(a)
                if "SAB" in lista_teste_dia:
                    valor_novo = "{}{} | 6x1".format(lista3[:6], lista3[18:])
                    lista_padrao.append(valor_novo)
                    
                else:
                    valor_novo = "{}{} | 5x2".format(lista3[:6], lista3[18:])
                    lista_padrao.append(valor_novo)

                for a in lista_padrao:
                    teste = "".join(a)
                    teste1 = teste.replace("(", "").replace(")", "").replace("'", "").replace("\"", "").replace("[", "").replace("]", "").replace(",", "")
                    teste2 = teste1[:19].replace(" ", "") + teste1[19:]
                    final_padrao.append(teste2)

            # escala 6x1 menor
            elif len(i2) > 47 and len(i2) < 53:
                for i in i2:
                    lista2.append(i)
                valor_novo = "{}{}{}".format(lista2[:6], lista2[18:23], "   6x1")
                
                lista_padrao.append(valor_novo)
                for i in lista_padrao:
                    teste = "".join(i)
                    teste1 = teste.replace("(", "").replace(")", "").replace("'", "").replace("\"", "").replace("[", "").replace("]", "").replace(",", "")
                string1 = teste1[:20].replace(" ", "")
                string2 = teste1[-6:].replace(" ", "")
                final = (f"{string1} | {string2}")
                final_padrao.append(final)

    lista_string = '\n'.join(final_padrao)
    #copiar os dados para a area de transferencia
    pyperclip.copy(lista_string)


    ##########################################################################################################################################

    #voltar para o excel e colar as novas escalas
    pyautogui.click(569,878, duration=0.5)
    pyautogui.click(633,797, duration=0.3)
    pyautogui.click(870,298, duration=0.3) 
    pyautogui.hotkey("ctrl", "v")