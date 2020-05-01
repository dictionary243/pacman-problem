from PIL import Image,ImageDraw
import time


def color_chooser(ch):
    if ch=="#":
        color='grey'
    elif ch=='p':
        color='red'
    elif ch=='-':
        color='white'
    else:
        color='blue'
    return color
def pacman_viewer(data,path):
    img=Image.new('RGB',(400,400),color='white')
    d=ImageDraw.Draw(img)
    for i in range(8):
        for j in range(8):
            color=color_chooser(data[i][j])
            d.rectangle([(50*j,50*i),(50*(j+1),((i+1)*50))],fill=color,outline='black')
    img.show()
    time.sleep(5)

    for [i,j] in path:
        d.rectangle([(50*j,50*i),(50*(j+1),((i+1)*50))],fill='yellow',outline='black')
        img.show()
        time.sleep(3)
