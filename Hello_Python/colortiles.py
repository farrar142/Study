#△ ☆ □ ◇ 〓 │ ─ ∩  (16x23) width x height  blank = 368 - 152 (문양당 8x14x2개씩 셋트)

import tkinter
import random

window=tkinter.Tk()

window.title("Color Tiles Game")
window.geometry("713x416+100+100")
window.resizable(True,True)


grid_range = []
grid_row = []
width = 16
height = 23
shape_list = []
randrange = random.randrange
counter = 0

for i in range(0,28):
    shape_list.append("△")
    shape_list.append("☆")
    shape_list.append("□")
    shape_list.append("◇")
    shape_list.append("〓")
    shape_list.append("│")
    shape_list.append("─")
    shape_list.append("∩")


for i in range(0,width):
    grid_row = []
    for j in range(0,height):
        k = " "
        grid_row.append(k)
    grid_range.append(grid_row)

while shape_list:
    random.shuffle(shape_list)
    i1 = randrange(0,width)
    j1 = randrange(0,height)
    if grid_range[i1][j1] == " ":
        grid_range[i1][j1] = shape_list[0]
        shape_list.pop(0)
        counter += 1
print(counter)

for i in range(0,len(grid_range)):
    for j in range(0,len(grid_range[0])):
        grid_range[i][j] = tkinter.Button(window, text=grid_range[i][j],width = 3,height = 1)
        grid_range[i][j].grid(row=i,column=j)













window.mainloop()