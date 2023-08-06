
def chamados_externo(a):

    import pyautogui

    i = 1
    while True:
        # 1 - abrir o google

            pyautogui.click(268,876, duration=0.5)
            pyautogui.click(368,793, duration=0.5)


        # 2 - abrir o formulário em outra aba
            if a == 25:
                lista25 = [(163,134),(164,163),(164,194),(164,222),(165,249),(166,278),(167,307),(166,332),(165,366),(163,392),(165,419),(165,448),(165,479),(167,506),(162,538),(165,564),(164,592),(165,622),(165,652),(166,678),(165,707),(165,737),(164,763),(162,791),(164,822),]

                pyautogui.keyDown('ctrl')
                for i in lista25:
                    pyautogui.click(i, duration=0.05)
                pyautogui.keyUp("ctrl")
                break
            elif a == 20:
                pyautogui.keyDown('ctrl')
                pyautogui.click(164,305, duration=0.1)
                pyautogui.click(164,332, duration=0.1)
                pyautogui.click(164,362, duration=0.1)
                pyautogui.click(163,389, duration=0.1)
                pyautogui.click(166,417, duration=0.1)
                pyautogui.click(164,445, duration=0.1)
                pyautogui.click(164,472, duration=0.1)
                pyautogui.click(165,500, duration=0.1)
                pyautogui.click(163,528, duration=0.1)
                pyautogui.click(164,556, duration=0.1)
                pyautogui.click(165,584, duration=0.1)
                pyautogui.click(166,611, duration=0.1)
                pyautogui.click(166,637, duration=0.1)
                pyautogui.click(164,666, duration=0.1)
                pyautogui.click(163,695, duration=0.1)
                pyautogui.click(165,722, duration=0.1)
                pyautogui.click(165,750, duration=0.1)
                pyautogui.click(166,778, duration=0.1)
                pyautogui.click(166,804, duration=0.1)
                pyautogui.click(165,833, duration=0.1)
                pyautogui.keyUp("ctrl")
                break

            elif a == 15:
                pyautogui.keyDown('ctrl')
                pyautogui.click(167,332, duration=0.05)
                pyautogui.click(166,362, duration=0.05)
                pyautogui.click(161,389, duration=0.05)
                pyautogui.click(165,417, duration=0.05)
                pyautogui.click(161,448, duration=0.05)
                pyautogui.click(165,475, duration=0.05)
                pyautogui.click(167,503, duration=0.05)
                pyautogui.click(165,531, duration=0.05)
                pyautogui.click(165,561, duration=0.05)
                pyautogui.click(165,589, duration=0.05)
                pyautogui.click(167,621, duration=0.05)
                pyautogui.click(165,647, duration=0.05)
                pyautogui.click(165,676, duration=0.05)
                pyautogui.click(167,703, duration=0.05)
                pyautogui.click(167,733, duration=0.05)
                pyautogui.keyUp("ctrl")
                break
            elif a == 10:
                pyautogui.keyDown('ctrl')
                #zoom 50%
                pyautogui.click(166,390, duration=0.05)
                pyautogui.click(167,418, duration=0.05)
                pyautogui.click(163,448, duration=0.05)
                pyautogui.click(163,475, duration=0.05)
                pyautogui.click(163,503, duration=0.05)
                pyautogui.click(167,529, duration=0.05)
                pyautogui.click(167,562, duration=0.05)
                pyautogui.click(164,592, duration=0.05)
                pyautogui.click(164,620, duration=0.05)
                pyautogui.click(163,649, duration=0.05)
                pyautogui.keyUp("ctrl")
                break
            elif a == 5:
                pyautogui.keyDown('ctrl')
                pyautogui.click(164,388, duration=0.05)
                pyautogui.click(162,417, duration=0.05)
                pyautogui.click(168,446, duration=0.05)
                pyautogui.click(167,475, duration=0.05)
                pyautogui.click(165,504, duration=0.05)
                pyautogui.keyUp("ctrl")
                break
            elif a == 9:
                pyautogui.keyDown('ctrl')
                pyautogui.click(162,390, duration=0.05)
                pyautogui.click(164,419, duration=0.05)
                pyautogui.click(165,446, duration=0.05)
                pyautogui.click(164,472, duration=0.05)
                pyautogui.click(165,499, duration=0.05)
                pyautogui.click(164,529, duration=0.05)
                pyautogui.click(167,557, duration=0.05)
                pyautogui.click(164,585, duration=0.05)
                pyautogui.click(164,611, duration=0.05)
                pyautogui.keyUp("ctrl")
                break
            elif a == 8:
                pyautogui.keyDown('ctrl')
                pyautogui.click(165,388, duration=0.05)
                pyautogui.click(167,419, duration=0.05)
                pyautogui.click(165,447, duration=0.05)
                pyautogui.click(164,477, duration=0.05)
                pyautogui.click(166,506, duration=0.05)
                pyautogui.click(165,531, duration=0.05)
                pyautogui.click(166,560, duration=0.05)
                pyautogui.click(167,590, duration=0.05)
                pyautogui.keyUp("ctrl")
                break
            elif a == 6:
                pyautogui.keyDown('ctrl')
                pyautogui.click(163,390, duration=0.05)
                pyautogui.click(165,416, duration=0.05)
                pyautogui.click(163,446, duration=0.05)
                pyautogui.click(166,472, duration=0.05)
                pyautogui.click(165,499, duration=0.05)
                pyautogui.click(166,528, duration=0.05)
                pyautogui.keyUp("ctrl")
                break
            elif a == 7:
                pyautogui.keyDown('ctrl')
                pyautogui.click(164,389, duration=0.05)
                pyautogui.click(165,419, duration=0.05)
                pyautogui.click(166,447, duration=0.05)
                pyautogui.click(163,476, duration=0.05)
                pyautogui.click(167,504, duration=0.05)
                pyautogui.click(164,533, duration=0.05)
                pyautogui.click(164,564, duration=0.05)
                pyautogui.keyUp("ctrl")
                break

            elif a == 22:
                #ALINHAR COM A PARTE AZUL
                lista22 = [(166,135), (163,163), (166,193), (164,220), (165,248), (165,278), (165,309), (165,337), (165,364), (166,393), (164,421), (165,452), (164,480), (165,507), (163,536), (164,562), (164,593), (163,622), (164,648), (164,679), (164,705), (164,736), ]
                pyautogui.keyDown('ctrl')
                
                for i in lista22:
                    pyautogui.click(i, duration=0.1)
                pyautogui.keyUp("ctrl")
                break

            elif a == 19:
                #colocar no 50% e rolar o scroll para cima 1 vez
                lista19 = [(167,318),(166,346),(164,376),(165,401),(164,432),(163,459),(165,490),(165,519),(166,546), (165,576), (165,602), (165,637), (164,660), (164,692),(162,719), (164,745),(164,778), (163,804), (164,832)]
                pyautogui.keyDown('ctrl')
                
                for i in lista19:
                    pyautogui.click(i, duration=0.1)
                pyautogui.keyUp("ctrl")
                break

            elif a == 16:
                #colocar no 50% e rolar o scroll para cima 1 vez
                lista16 = [(165,353), (165,383), (165,411), (165,438), (163,469), (164,495), (163,526), (163,554), (163,582), (165,612), (164,641), (164,667), (163,696), (164,724), (165,755), (165,782), ]
                pyautogui.keyDown('ctrl')
                
                for i in lista16:
                    pyautogui.click(i, duration=0.1)
                pyautogui.keyUp("ctrl")
                break

            elif a == 13:
                
                lista13 = [(166,354), (164,380), (165,411), (166,439), (166,468), (163,496), (164,523), (165,553), (163,584), (164,612), (164,641), (165,668), (166,696), ]
                pyautogui.keyDown('ctrl')
                
                for i in lista13:
                    pyautogui.click(i, duration=0.1)
                pyautogui.keyUp("ctrl")
                break
            elif a == 11:
                
                lista13 = [(164,359), (166,389), (166,419), (165,444), (166,477), (165,504), (166,531), (166,563), (165,587), (165,615), (160,647), ]
                pyautogui.keyDown('ctrl')
                
                for i in lista13:
                    pyautogui.click(i, duration=0.1)
                pyautogui.keyUp("ctrl")
                break

if __name__ == "__main__":
    import pyautogui
    pyautogui.click(265,883)
    pyautogui.click(370,795)
    pyautogui.click(359,6)
    # chamados_externo(11)