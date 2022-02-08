from PIL import Image
import math
MAX_ITERATIONS = 160
HEIGHT = 720
WIDTH = 1080
SCALE_X = (5*16/8)/2
SCALE_Y = (5*9/8)/2

def f(c):
    z = c
    dz = complex(1,0)
    n = 0
    while abs(z) <= 1.5 and n < MAX_ITERATIONS:
        z = z*z + 0.8*math.e ** complex(-0.5,0.7)
        dz = 2*z*dz
        n += 1
    return abs(z)*math.log(abs(z),10)/abs(dz)

img = Image.new("L",(WIDTH,HEIGHT))
pix = img.load()


for x in range(img.size[0]):
    for y in range(img.size[1]):
        c = complex(SCALE_X*(x-WIDTH/2)/WIDTH,SCALE_Y*(y-HEIGHT/2)/HEIGHT)
        result = f(c)
        if(result < 0.000015):
            pix[(x,y)] = 0
        else:
            pix[(x,y)] = 255

img.save("julia.png","PNG")