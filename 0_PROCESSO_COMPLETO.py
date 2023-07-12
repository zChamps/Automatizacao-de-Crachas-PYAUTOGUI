from a1__abrir_chamados import chamados_externo
from b1__abrir_formularios import chamados_interno
from d__criar_filtro import filtro_rm
from e__pegar_dados_sistema import pegar_dados_rm
from f__pegar_RG_CTPS import rg_ctps
from b2__abrir_formularios_email import chamados_internos_integracao
from a2__abrir_chamados_email import chamados_email
import time
import pyautogui

chamados_integracao = None

print("Olá, seja bem vindo ao confeccionador automático de crachás!")
num_crachas = int(input("Quantos crachás deseja fazer? "))
while True:
    #Perguntar se os crachás são de segunda via ou admissionais 
    adm_svia = input("E esses crachás, são admissionais ou segunda via? ")
    #Caso f0rem admissionais
    if adm_svia.startswith("ad"):
        while True:
            #perguta se serão para a integração ou para outras sedes
            int_fora = input("Os crachás admissionais, serão para a integração ou para outras sedes? ")
            #caso seja para a integração
            if int_fora.startswith("in"):
                while True:
                    chamados_integracao = input("Você deseja abrir os chamados especificos da integração automaticamente? ")
                    if chamados_integracao == "sim":
                        chamados_email()
                        break
                    elif chamados_integracao.lower() == "nao" or chamados_integracao.lower() == "não":
                        break
                    else:
                        continue
                break
            #caso seja para outras sedes
            elif int_fora.startswith("ou"):
                break
            
            else:
                print("Digite uma opção válida! ")
                continue
        break   
    elif adm_svia.startswith("se"):
        break
    else:
        print("Digite uma opção válida!")
        continue

if not chamados_integracao == "sim":
    print("Certo! Iniciando preparativos agora e o processo em 3,2,1...")
    pyautogui.click(661,888)
    time.sleep(3)

    #Começa a abrir os chamados de crachás
    chamados_externo(num_crachas)


    pyautogui.click(737,334)
    for _ in range(3):
        pyautogui.hotkey("ctrl", "+")

    chamados_interno(num_crachas)

    pyautogui.press("s")
    pyautogui.press("enter")
    time.sleep(1.5)
    pyautogui.press("a")
    pyautogui.press("enter")

if adm_svia.startswith("ad") or chamados_integracao == "nao" or chamados_integracao == "não":
    while True:
        print("Feche as abas contendo as fotos após salvá-las.")
        tempo = input("Salve as fotos, após isso digite 'ok' para continuar o processo: ")
        if tempo == "ok":
            break
        else:
            print("Digite a opção correta!")
            continue

if chamados_integracao == "sim" or chamados_integracao == "nao" or chamados_integracao == "não":
        pyautogui.click(661,888)
        time.sleep(3.5)
        chamados_internos_integracao(num_crachas)
        pyautogui.press("s")
        pyautogui.press("enter")
        time.sleep(1.5)
        pyautogui.press("a")
        pyautogui.press("enter")

#entrar Rm
pyautogui.click(613,876)

#mudar empresa para serval limpeza
pyautogui.click(59,16, duration=1.5)
pyautogui.click(136,42, duration=1.5)
pyautogui.click(584,404, duration=1.5)
pyautogui.press("1")
pyautogui.press("tab")
pyautogui.click(905,596, duration=1.5)
pyautogui.click(906,599, duration=1.5)
pyautogui.click(951,508, duration=2.5)
time.sleep(4.5)

#abrir centro de filtros no RM
pyautogui.click(234,46, duration=2)
pyautogui.click(37,91, duration=2)
time.sleep(2.5)


#escolher se abrirá filtro de segunda via ou filtro admissional
if adm_svia.startswith("se"):
    pyautogui.click(639,424, duration=1.5)
    pyautogui.click(970,276, duration=1)
    pyautogui.click(565,489, duration=1)

elif adm_svia.startswith("ad"):
    #Caso seja admissional escolherá o filtro da integração
    if int_fora.startswith("in"):
        pyautogui.click(638,214, duration=1.5)
        pyautogui.click(970,276, duration=1)
        pyautogui.click(591,479, duration=1) 
    #ou o filtro dos crachás para unidades de fora
    elif int_fora.startswith("ou"):
        pyautogui.click(644,368, duration=1.5)
        pyautogui.click(970,276, duration=1)
        pyautogui.click(591,479, duration=1)

#Codigo que adiciona as matriculas no filtro
filtro_rm()
time.sleep(1.5)
#Salvar o filtro e executá-lo
pyautogui.click(1041,701, duration=1)
pyautogui.click(884,668, duration=1)
pyautogui.click(17,816, duration=1)
time.sleep(3)

#Codigo que copia e cola os dados do RM, na planilha. Além de simplificar os nomes e as escalas
pegar_dados_rm(num_crachas)

#entrar no RM
pyautogui.click(614,884, duration=1)


#redefinir a altura do rm
if num_crachas >= 19:
    pyautogui.moveTo(1565,317)
    pyautogui.mouseDown()
    time.sleep(2)
    pyautogui.mouseUp()
#Codigo que pega o RG e CTPS das pessoas dentro do filtro individual e cola na planilha
pyautogui.doubleClick(205,338, duration=0.6)
time.sleep(8)
pyautogui.click(415,192, duration=1)
rg_ctps(num_crachas)
