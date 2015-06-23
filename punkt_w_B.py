
from visual import *
from math import *

# nazwa sceny


scene.title='Ruch czastki w jednorodnym polu magnetycznym'
scene.width = scene.height = 800
granice=box(pos=(0,0,0),axis=(100,0,0),size=(55,55,55),opacity=0)
scene.autoscale=Falsep

# pole magnetyczne
def pole ():
    xi=-24 #-16
    while xi <= 24: #16
        yi=-17 #-17 !!!!!25
        while yi <= 9: #7
            yi += 4
            zi=-24 #-16
            while zi <= 24: #16
                wektor = arrow(pos=(xi,yi,zi), axis=(0,2,0), color=color.yellow,shaftwidth=0.07)
                zi += 4
        xi += 4
    return

# punkt poza wizualizacja
def poza (x):
    if x <= -55 : #-35
        x=-54 # -34
    elif x >= 55 : #35
        x= 54 #34

    return x

# korekta przejscia przez zero oraz ustawienie wartosci granicznych wektora

def korekta (gg,gd,k,x):
    if x > gg :
        x= gg
    elif x < gd:
        x= gd
    if x==0:
        return x
    elif x>-k and x<k :
        x=0
        return x
    else:
        return x


# ustawienie delta t

dt =0.1

## pole magentyczne
#wizualizacja biegunow magnetycznych

siatka = []

for x in arange(-24, 24+4, 4):
    siatka.append(curve(pos=[(x,-16,-24),(x,-16,24)], color=(0,0,1)))
    siatka.append(curve(pos=[(x,16,-24),(x,16,24)], color=(1,0,0)))
for z in arange(-24, 24+4, 4):
    siatka.append(curve(pos=[(-24,-16,z),(24,-16,z)], color=(0,0,1)))
    siatka.append(curve(pos=[(-24,16,z),(24,16,z)], color=(1,0,0)))


biegunN=box(pos=(0,-16,0), axis=(48,0,0), size=(48,.5,48), color=color.blue , opacity = 0.3)
biegunNlbl=label(pos=(24,-16,24), text="N", color=color.blue, opacity=0, height=10)

biegunS=box(pos=(0,16,0), axis=(48,0,0), size=(48,.5,48), color=color.red  , opacity = 0.3)
biegunSlbl=label(pos=(24,16,24), text="S", color=color.red, opacity=0, height=10)

# ustawienie wektora pola
tekst='   '
y=0
warunek=True
while warunek:
    wektor = arrow(pos=(24,-16,24), axis=(0,y,0), color=(1,0.7, 0.7),shaftwidth=0.2) #15 na 23 i analogicznie
    wektorlbl=label(pos=(-5,-20,15), text="Ustawienie wektora B", color=(1,0.7, 0.7), opacity=0, height=10)
    scenalbl1=label(pos=(-10,-27,15), text='UP - gora   DOWN - dol      BACKSPACE - O.K. ', color=(1,0.7, 0.7), opacity=0, height=10)
    klawisz = scene.kb.getkey()
    wektor.visible = False
    wektorlbl.visible = False
    scenalbl1.visible = False
    if klawisz=='up':
        y +=0.1
        y=korekta (7,0,0.1,y)
    elif klawisz=='down':
        y += -0.1
        y=korekta (7,0,0.1,y)
    elif klawisz=='backspace':
        BP=(0,y*0.01,0)              #y=0.1; y*e-5  ==/== 0.1e-5 !!!
        pole ()
        warunek=False

B=BP
#print ('Pole magnetyczne - ',BP)


# punkt powrotu petli
scena=True
#while scena:
scenalbl1=label(pos=(-10,-27,15), text='UP - gora   DOWN - dol      BACKSPACE - O.K. ', color=(1,0.7, 0.7), opacity=0, height=10)
scenalbl2=label(pos=(-10,-29,15), text='LEFT - lewo  RIGHT - prawo     p - przod  t - tyl', color=(1,0.7, 0.7), opacity=0, height=10)


# ustawianie punktu

punktlbl=label(pos=(-5,-20,15), text="Wybierz typ czastki e-elektron, p-proton", color=(1,0.7, 0.7), opacity=0, height=10)

xi=yi=zi=0
warunek=True
while warunek :
    klawisz = scene.kb.getkey()
    if klawisz=='e':
        #przyjeto elektron
        punkt = sphere(pos = (xi, yi, zi), radius = .5, color = color.green, trail = curve(color=color.green))
        punkt.ladunek=-1.6e-19
        punkt.masa=9.1e-31
        punkt.a=vector()
        punkt.v=vector()
        punkt.trajectory=curve(color=color.green,radius=.1)
        punktlbl.visible = False
        warunek=False
    elif klawisz=='p':
        #przyjeto proton
        punkt = sphere(pos = (xi, yi, zi), radius = .8, color = color.red, trail = curve(color=color.red))
        punkt.ladunek=1.6e-19
        punkt.masa=1.7e-27
        punkt.a=vector()
        punkt.v=vector()
        punkt.trajectory=curve(color=color.red,radius=.1)
        punktlbl.visible = False
        warunek=False
    elif klawisz != 'e' and klawisz != 'p':
        continue
    #       print ('Niewlasciwy wybor ')
    elif klawisz=='backspace':
        punktlbl.visible = False
        warunek=False

# ustawianie pozycji punktu
punktlbl=label(pos=(-5,-20,15), text="Ustaw pozycje czastki", color=(1,0.7, 0.7), opacity=0, height=10)

warunek=True
while warunek:
    punkt.pos = (xi, yi, zi)
    klawisz = scene.kb.getkey()
    punktlbl.visible = False
    if klawisz=='up':
        yi += 1
        yi = poza (yi)
    elif klawisz=='down':
        yi += -1
        yi = poza (yi)
    elif klawisz=='right':
        xi += 1
        xi = poza (xi)
    elif klawisz=='left':
        xi += -1
        xi = poza (xi)
    elif klawisz=='p':
        zi += 1
        zi = poza (zi)
    elif klawisz=='t':
        zi += -1
        zi = poza (zi)
    elif klawisz=='backspace':
        punkt.pos = (xi, yi, zi)
        punktlbl.visible = False
        warunek=False

# czy maja byc widoczne wektory ruchu

punktlbl=label(pos=(-5,-20,15), text='widoczne wektory ruchu   t - tak  n - nie', color=(1,0.7, 0.7), opacity=0, height=10)


FalseTrue=False
klawisz = scene.kb.getkey()
if klawisz=='t':
    FalseTrue=True
elif klawisz=='n':
    FalseTrue=False

wektor=arrow(pos=(xi,yi,zi),color=(1, 0.7, 0.7),shaftwidth=0.1)
wektor_x=arrow(pos=(xi,yi,zi),color=color.yellow,shaftwidth=0.1)
wektor_y=arrow(pos=(xi,yi,zi),color=color.orange,shaftwidth=0.1)
wektor_z=arrow(pos=(xi,yi,zi),color=color.red,shaftwidth=0.1)

wektor_x.visible=FalseTrue
wektor_y.visible=FalseTrue
wektor_z.visible=FalseTrue

# ustawianie wektora ruchu

a=b=c=0
warunek=True
while warunek:
    punktlbl.visible=False
    wektor = arrow(pos=(xi,yi,zi), axis=(a,b,c), color=(1, 0.7, 0.7),shaftwidth=0.2)
    klawisz = scene.kb.getkey()
#	print (a,b,c)
    wektor.visible=False
    if klawisz=='up':
        b+=0.01 #0.1
        b=korekta (2,-2,0.1,b) #(2,-2,0.1,b)
    elif klawisz=='down':
        b+=-0.01 #0.1
        b=korekta (2,-2,0.1,b) #(2,-2,0.1,b)
    elif klawisz=='right':
        a+=10 #100
        a=korekta (10000,-10000,0.1,a) #(1000,-1000,0.1,a)
    elif klawisz=='left':
        a+=-10 #100
        a=korekta (10000,-10000,0.1,a) #(1000,-1000,0.1,a)
    elif klawisz=='p':
        c+=10 #100
        c=korekta (10000,-10000,0.1,c) #(1000,-1000,0.1,c)
    elif klawisz=='t':
        c+=-10 #100
        c=korekta (10000,-10000,0.1,c) #(1000,-1000,0.1,c)
    elif klawisz=='backspace':
        punkt.v=vector(10*a,10*b,10*c)
        warunek=False



print ('pp',punkt.pos,'pv',punkt.v,'dt',dt)

#ruch czastki


scenalbl1.visible=False
scenalbl2.visible=False

Fl=punkt.ladunek*cross(punkt.v,B)
punkt.a = Fl / punkt.masa


warunek=koniec=True
while koniec:

    rate(5) ###


    wektor.pos = punkt.pos
    wektor_z.pos=punkt.pos
    wektor_z.axis=(0,0,10*punkt.v.z)
    wektor_y.pos=punkt.pos
    wektor_y.axis=(0,10*punkt.v.y,0)
    wektor_x.pos=punkt.pos
    wektor_x.axis=(10*punkt.v.x,0,0)


    if -24 < punkt.pos.x < 24 and -24 < punkt.pos.y < 24 and -24 < punkt.pos.z < 24: #16
        B=BP
    #    print ('BP= ',B)
    else:
        B=(0,0,0)
    #    print ('B0= ',B)
    #print ('B= ',B)
    punkt.v=punkt.a *dt+vector(0,b,0)
    Fl = punkt.ladunek * cross(punkt.v , B )
    punkt.a = punkt.a+ Fl/punkt.masa
    punkt.pos = punkt.pos + (punkt.a) *dt*dt
    punkt.pos=punkt.pos+punkt.v*dt
    punkt.trajectory.append(pos=punkt.pos)


    if punkt.pos.x <=-45 or punkt.pos.x >= 45 or punkt.pos.y <=-45 or punkt.pos.y >= 45 or punkt.pos.z <=-45 or punkt.pos.z >= 45 : #35
        scenalbl1=label(pos=(-10,-27,15), text=' Punkt poza punktami granicznymi wizualizacji  ', color=(1,0.7, 0.7), opacity=0, height=10)

#THE BOX HAS BEEN RESIZED
#ITERATION IS UNNECESSARY DUE TO THE CHARACTER OF THIS PARTICULAR PROJECT