#coding: utf-8
from visual import *
from math import *

# nazwa sceny


# DZIAŁA: PROTON, X=100 (MOŻE BYĆ TROCHĘ WIĘKSZE), Y=0.6 (POWINNO BYĆ MNIEJSZE), B=0.4, dt=0.01,
# ELEKTRON, X=100 (MOŻE BYĆ WIĘKSZE), Y=0.6 (DOBRE), B=0.4, dt=0.01
# CIĘŻKO BĘDZIE DOBRAĆ PARAMETRY POD ELEKTRON I PROTON, OGROMNA RÓŻNICA W PROMIENIU, MOŻE POTRZEBNE 2 PRZYPADKI (???)
# PROMIEŃ ROŚNIE Z CZASEM (I MA ODCHYŁY W OBIE STRONY), PRAWDOPODOBNIE ZA DUŻY SKOK (NIE MOŻNA ZMIEJSZYĆ BO WOLNO)


scene.title='Ruch czastki w jednorodnym polu magnetycznym'
scene.width = scene.height = 800
granice=box(pos=(0,0,0),axis=(100,0,0),size=(55,55,55),opacity=0) #granice=box(pos=(0,0,0),axis=(100,0,0),size=(55,55,55),opacity=0)
scene.autoscale=False

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

dt =0.01

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
biegunNlbl=label(pos=(24,-17,24), text="N", color=color.blue, opacity=0, height=15)

biegunS=box(pos=(0,16,0), axis=(48,0,0), size=(48,.5,48), color=color.red  , opacity = 0.3)
biegunSlbl=label(pos=(24,17,24), text="S", color=color.red, opacity=0, height=15)

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
        BP=(0,y*0.001,0)              #y=0.1; y*e-5  ==/== 0.1e-5 !!!
        pole ()
        warunek=False
BB=y*0.001
B=BP
#print ('Pole magnetyczne - ',BP)
print BB

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
        punkt.masa=9.1e-25  # jednostka: mg
        punkt.a=vector()
        punkt.v=vector()
        punkt.trajectory=curve(color=color.green,radius=.1)
        punktlbl.visible = False
        warunek=False
    elif klawisz=='p':
        #przyjeto proton
        punkt = sphere(pos = (xi, yi, zi), radius = .8, color = color.red, trail = curve(color=color.red))
        punkt.ladunek=1.6e-19
        punkt.masa=1.7e-24  # jednostka: g
        punkt.a=vector()
        punkt.v=vector()
        punkt.trajectory=curve(color=color.red,radius=.15)
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
        punkt.temppos = vector(xi, yi, zi)
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
        b+=0.5 #0.1
        b=korekta (5,-5,0.1,b) #(2,-2,0.1,b)
    elif klawisz=='down':
        b+=-0.5 #0.1
        b=korekta (5,-5,0.1,b) #(2,-2,0.1,b)
    elif klawisz=='right':
        a+=0.5 #100
        a=korekta (10,-10,0.1,a) #(1000,-1000,0.1,a)
    elif klawisz=='left':
        a+=-0.5 #100
        a=korekta (10,-10,0.1,a) #(1000,-1000,0.1,a)
    elif klawisz=='p':
        c+=0.5 #100
        c=korekta (10,-10,0.1,c) #(1000,-1000,0.1,c)
    elif klawisz=='t':
        c+=-0.5 #100
        c=korekta (10,-10,0.1,c) #(1000,-1000,0.1,c)
    elif klawisz=='backspace':
        punkt.v=vector(a,b,c)
        warunek=False



print ('pp',punkt.pos,'pv',punkt.v,'dt',dt)

#ruch czastki


scenalbl1.visible=False
scenalbl2.visible=False

Fl=punkt.ladunek*cross(punkt.v,B)
punkt.a = Fl / punkt.masa

v=math.sqrt(a**2+c**2)
warunek=koniec=True
print (punkt.masa,v,punkt.ladunek,BB)
radius=100*(punkt.masa*v)/(punkt.ladunek*BB)
r=math.fabs(radius)
t=0
omega=v/radius
print ('radius',radius,'r',r)
print ('omega',omega)

while koniec:

    rate(50) ###
    t=t+dt
    cosValue=math.cos(omega*t)
    sinValue=math.sin(omega*t)
    punkt.pos.x=r*cosValue
    punkt.pos.z=r*sinValue
    punkt.pos.y=b*t

    print ('t',t,punkt.pos.x,punkt.pos.y,punkt.pos.z)

    wektor.pos = punkt.temppos+punkt.pos
    wektor_z.pos=punkt.temppos+punkt.pos
    wektor_z.axis=(0,0,punkt.v.z)
    wektor_y.pos=punkt.temppos+punkt.pos
    wektor_y.axis=(0,punkt.v.y,0)
    wektor_x.pos=punkt.temppos+punkt.pos
    wektor_x.axis=(punkt.v.x,0,0)


    if -24 < punkt.pos.x < 24 and -24 < punkt.pos.y < 24 and -24 < punkt.pos.z < 24: #16
        B=BP
    #    print ('BP= ',B)
    else:
        B=(0,0,0)
    #    print ('B0= ',B)
    #print ('B= ',B)

   # Fl = punkt.ladunek * cross(punkt.v , B )
   # punkt.a =punkt.a + Fl/punkt.masa
   # punkt.pos = punkt.pos + (punkt.a)*dt*dt
   # punkt.v=punkt.a *dt+vector(0,b,0) #!!!!!!!!!!!!!!!!
    punkt.pos=punkt.temppos+vector(punkt.pos.x,punkt.pos.y,punkt.pos.z)
    punkt.trajectory.append(pos=punkt.pos)
    print ('pos',punkt.pos)

    if punkt.pos.x <=-45 or punkt.pos.x >= 45 or punkt.pos.y <=-45 or punkt.pos.y >= 45 or punkt.pos.z <=-45 or punkt.pos.z >= 45 : #35
        scenalbl1=label(pos=(-10,-27,15), text=' Czastka poza granicami wizualizacji ', color=(1,0.7, 0.7), opacity=0, height=10)

#THE BOX HAS BEEN RESIZED
#ITERATION IS UNNECESSARY DUE TO THE CHARACTER OF THIS PARTICULAR PROJECT