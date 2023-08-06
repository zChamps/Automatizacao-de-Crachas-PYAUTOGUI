from a_abrir_chamados import chamados_externo
from e_criar_filtro_rm import filtro_rm
from f_pegar_dados_RM import pegar_dados_rm
from g_pegar_rg_ctps import rg_ctps
from a_chamados_email_int import chamados_email
from b_abrir_arquivos_fonte import abrir_arquivos_fonte
from b_copiar_arquivos_fonte import copiar_arquivos_fonte
from d_matricula_foto import matricula_foto
import time
import pyautogui

chamados_integracao = None

print("Olá, seja bem vindo ao confeccionador automático de crachás!")
num_crachas = int(input("Quantos crachás deseja fazer? "))
while True:
    #verificação se os chamados serão admissionais ou de segunda via
    admissional_segunda_via = input("Os crachás serão admissionais ou de segunda via? ")
    if admissional_segunda_via.lower() == "segunda via":
        chamados_externo(num_crachas)
        break

    #verificação para saber se irá abrir os chamados pelas matriculas do email ou automaticamente
    elif admissional_segunda_via.lower()=="admissional" or  admissional_segunda_via.lower()=="admissionais" or admissional_segunda_via.lower()=="adm":
        integracao_ou_filial = input("E eles serão para a integração ou para as filiais? ")
        if integracao_ou_filial.lower() == "filiais":
            chamados_externo(num_crachas)
            break
        elif integracao_ou_filial.lower() == "integração":
            chamados_email()
            break
    
    else:
        print("Digite uma opção válida!")
        continue

time.sleep(2.5)
#Após ter os chamados abertos, irá abrir os arquivos fonte das paginas
abrir_arquivos_fonte(num_crachas)

#Irá passar por cada aba de arquivo código-fonte e copiar o HTML
copiar_arquivos_fonte(num_crachas)

#irá pegar todos os links, salvar as fotos de todos, transformar em matriculas e colocá-las no arquivo
matricula_foto()
if num_crachas >= 20:
    time.sleep(45)
elif num_crachas >= 10:
    time.sleep(35)
elif num_crachas < 10:
    time.sleep(25)

#entrar Rm
pyautogui.click(613,876)

#mudar empresa para serval limpeza
pyautogui.click(59,16, duration=1.5)
pyautogui.click(136,42, duration=1.5)
pyautogui.click(584,404, duration=1.5)
pyautogui.press("1")
pyautogui.press("tab")
pyautogui.click(905,596, duration=2.5)
pyautogui.click(906,599, duration=2.5)
pyautogui.click(951,508, duration=2.5)
time.sleep(4.5)

#abrir centro de filtros no RM
pyautogui.click(234,46, duration=2)
pyautogui.click(37,91, duration=2)
time.sleep(4)


#escolher se abrirá filtro de segunda via ou filtro admissional
if admissional_segunda_via.startswith("se"):
    pyautogui.click(639,424, duration=2)
    pyautogui.click(970,276, duration=1.5)
    pyautogui.click(565,489, duration=1.5)

elif admissional_segunda_via.startswith("ad"):
    #Caso seja admissional escolherá o filtro da integração
    if integracao_ou_filial.startswith("in"):
        pyautogui.click(638,214, duration=2)
        pyautogui.click(970,276, duration=1.5)
        pyautogui.click(591,479, duration=1.5) 
    #ou o filtro dos crachás para unidades de fora
    elif integracao_ou_filial.startswith("fil"):
        pyautogui.click(662,368, duration=2)
        pyautogui.click(971,275, duration=1.5)
        pyautogui.click(567,488, duration=1.5)

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
