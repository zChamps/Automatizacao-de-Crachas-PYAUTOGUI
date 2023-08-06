def copiar_arquivos_fonte(a):

    import pyautogui
    import threading
    from z_arquivo_de_apoio import links
    from time import sleep



    linkst = threading.Thread(target=links, args=(a,))
    # processot = threading.Thread(target=processo)
    if a == 25:
        coordenadas = [(72,16), (125,16), (178,15), (228,15), (282,14), (333,15), (385,16), (438,14), (491,14), (540,16), (594,15), (646,16), (696,14), (750,17), (804,15), (855,15), (905,15), (958,15), (1008,15), (1060,15), (1111,15), (1162,14), (1210,16), (1261,16), (1315,15) ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)

    if a == 22:
        coordenadas = [(84,11), (142,14), (204,15), (264,12), (321,13), (381,14), (442,16), (500,14), (557,10), (616,15), (678,16), (732,16), (791,16), (848,17), (907,15), (966,13), (1023,16), (1081,16), (1138,17), (1201,19), (1253,16), (1313,17), ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)


    elif a == 20:
        coordenadas = [(90,18) (156,17), (222,14), (287,12), (355,16), (417,16), (482,16), (547,15), (607,17), (675,17), (739,14), (802,19), (866,16), (931,14), (994,18), (1059,18), (1121,15), (1185,17), (1252,15), (1312,13)  ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)

    elif a == 19:
        coordenadas = [(92,15), (161,17), (231,17), (296,14), (361,15), (430,16), (499,18), (569,17), (634,17), (703,17), (771,17), (838,12), (908,17), (976,17), (1043,18), (1111,16), (1179,17), (1245,13), (1314,20), ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)
            
    elif a == 17:
        coordenadas = [(102,16), (179,17), (257,17), (330,14), (408,13), (480,14), (558,14), (632,16), (714,21), (783,17), (860,16), (938,16), (1009,14), (1095,14), (1162,15), (1237,16), (1306,16), ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)

    elif a == 16:
        coordenadas = [(109,17), (190,15), (268,14), (347,14), (429,14), (508,15), (589,19), (670,15), (750,18), (825,14), (910,19), (985,22), (1071,14), (1150,18), (1225,16), (1308,15), ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)

    elif a == 15:
        coordenadas = [(111,18), (199,13), (285,10), (369,16), (455,18), (540,16), (629,13), (716,17), (801,14), (885,14), (974,16), (1053,16), (1140,14), (1226,17), (1310,15), ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)

    elif a == 13:
        coordenadas = [(130,16), (228,19), (324,18), (423,15), (523,15), (624,15), (721,14), (816,15), (915,12), (1014,12), (1116,18), (1209,17), (1308,12), ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)

    elif a == 11:
        coordenadas = [(156,19), (268,17), (383,20), (504,16), (617,16), (739,15), (854,20), (962,14), (1079,18), (1186,14), (1309,18), ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)

    elif a == 10:
        coordenadas = [(171,15), (293,17), (420,15), (545,14), (672,15), (800,16), (928,15), (1051,12), (1169,15), (1294,19), ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)

    elif a == 7:
        coordenadas = [(228,13), (403,14), (579,15), (757,13), (929,21), (1109,13), (1289,14), ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)
    elif a == 5:
        coordenadas = [(305,11), (554,18), (793,16), (1031,18), (1271,14), ]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)

    elif a == 2:
        coordenadas = [(593,15), (1046,14)]
        linkst.start()
        for i in coordenadas:
            pyautogui.click(i, duration=0.4)
            pyautogui.hotkey("ctrl", "a")
            sleep(0.5)
            pyautogui.hotkey("ctrl", "c")
            sleep(2)

    linkst.join()     
if __name__ == "__main__":
    copiar_arquivos_fonte(25)