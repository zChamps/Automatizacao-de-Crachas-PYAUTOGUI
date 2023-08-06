def filtro_rm():

    import pyautogui
    import pyperclip 
    pyautogui.click(568,485, duration=0.8)

    with open("matriculas.txt", "r") as mt:
        for i in mt:
            pyperclip.copy(i)
            pyautogui.doubleClick(885,268, duration=0.5)
            pyautogui.hotkey("ctrl", "v")
            pyautogui.click(1019,339)


if __name__ == "__main__":
    import pyautogui
    pyautogui.click(611,879)
    pyautogui.click(772,783)
    filtro_rm()