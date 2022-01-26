import pyautogui as pag
row = 1
col = 1
col_max = [10, 9, 7]
while True:
    if col > col_max[row - 1]:
        row += 1
        col = 1
    if row > 3:
        break
    if col == 10:
        pag.typewrite("110")
    else:
        pag.typewrite(str(row * 10 + col))
    col += 1
    pag.press('enter')
