def rg_ctps(a):

    import pyautogui

    from time import sleep
    i = 1
    while i <= a:
        if i == 1:            
            # 2 - dar um duplo clique no primeiro campo e ctrl c
            pyautogui.doubleClick(803,187,duration=0.2)
            pyautogui.hotkey('ctrl', 'c')

            # 3 - ir para a planilha
            pyautogui.click(569,878, duration=0.5)
            pyautogui.click(633,797, duration=0.3)

            # 4 - selecionar o primeiro campo
            pyautogui.click(438,295, duration=0.5)

            # 5 - ctrl v
            pyautogui.hotkey('ctrl', 'v')

            # 6 - voltar para o RM
            pyautogui.click(616,880, duration=0.3)

            # 7 - duplo clique no campo de baixo e ctrl c
            pyautogui.doubleClick(792,338, duration=0.4)
            pyautogui.hotkey('ctrl', 'c')

            #8 - selecionar o proximo colaborador
            pyautogui.click(467,108, duration=0.5)

            # 9 - ir para a planilha
            pyautogui.click(569,878, duration=0.5)
            pyautogui.click(633,797, duration=0.8)


            # 10 - selecionar o segundo campo e
            pyautogui.click(553,297) 
            # 11 - ctrl v
            pyautogui.hotkey('ctrl', 'v')
            i += 1

        else:
        #     # 12 - voltar para o RM
            pyautogui.click(616,880, duration=0.4)
        #     # 13 - dar um duplo clique no primeiro campo e ctrl c
            pyautogui.doubleClick(803,187,duration=1)
            pyautogui.hotkey('ctrl', 'c')
        #     #14 - ir para a planilha
            pyautogui.click(569,878, duration=0.5)
            pyautogui.click(633,797, duration=0.3)
        #     #15 - Apertar na seta para baixo e para a esquerda
            pyautogui.press('down')
            pyautogui.press('left')
        #     #16 - ctrl v
            pyautogui.hotkey('ctrl', 'v')
        #     #17 - voltar para o RM
            pyautogui.click(616,880, duration=1)
        #     #18 - duplo clique no campo de baixo e ctrl c
            pyautogui.doubleClick(792,338, duration=0.3)
            pyautogui.hotkey('ctrl', 'c')

            #19 - selecionar o proximo colaborador
            pyautogui.click(467,108, duration=0.5)

        #     # 21 - ir para a planilha
            pyautogui.click(569,878, duration=0.5)
            pyautogui.click(633,797, duration=0.3)
        #     #22 - apertar para a direita
            pyautogui.press('right')
        #     #23 colar
            pyautogui.hotkey('ctrl', 'v')
            i += 1
            continue