#coding: utf-8

#importowanie bibliotek 

from visual import *
from math import *

# nazwa sceny 

scene.title='Ruch czastki w jednorodnym polu magnetycznym'
scene.width = scene.height = 800
granice=box(pos=(0,0,0),axis=(100,0,0),size=(55,55,55),opacity=0)
scene.autoscale=False

# pole magnetyczne
def pole ():
<<<<<<< HEAD
    xi=-16
    while xi <= 16:
        yi=-17
        while yi <= 7:
            yi += 4
            zi=-16
            while zi <= 16:
                wektor = arrow(pos=(xi,yi,zi), axis=(0,2,0), color=color.yellow,shaftwidth=0.07)
                zi += 4
        xi += 4
    return

# punkt poza wizualizacja
def poza (x):
    if x <= -35 :
        x=-34
    elif x >= 35 :
        x= 34

    return (x)
=======
	xi=-16
	while xi <= 16:
		yi=-17
		while yi <= 7:
			yi += 4
			zi=-16
			while zi <= 16:
				wektor = arrow(pos=(xi,yi,zi), axis=(0,2,0), color=color.yellow,shaftwidth=0.07)
				zi += 4
		xi += 4
	return

# punkt poza wizualizacja
def poza (x):
	if x <= -35 :
		x=-34
	elif x >= 35 :
		x= 34
	
	return (x)
>>>>>>> 2d26567eb0231f6c459485ea93038d7bc626abc8

# korekta przejscia przez zero oraz ustawienie wartosci granicznych wektora

def korekta (gg,gd,k,x):
<<<<<<< HEAD
    if x > gg :
        x= gg
    elif x < gd:
        x= gd
    if x==0:
        return (x)
    elif x>-k and x<k :
        x=0
        return (x)
    else:
        return (x)
=======
	if x > gg :
		x= gg	
	elif x < gd:
		x= gd
	if x==0:
		return (x)
	elif x>-k and x<k :
		x=0
		return (x)	
	else:
		return (x)
>>>>>>> 2d26567eb0231f6c459485ea93038d7bc626abc8


# ustawienie delta t 

dt =0.01

## pole magentyczne 
#wizualizacja biegunów magnetycznych

siatka = []

for x in arange(-16, 16+4, 4):
<<<<<<< HEAD
    siatka.append(curve(pos=[(x,-16,-16),(x,-16,16)], color=(0,0,1)))
    siatka.append(curve(pos=[(x,16,-16),(x,16,16)], color=(1,0,0)))
for z in arange(-16, 16+4, 4):
    siatka.append(curve(pos=[(-16,-16,z),(16,-16,z)], color=(0,0,1)))
    siatka.append(curve(pos=[(-16,16,z),(16,16,z)], color=(1,0,0)))

biegunN=box(pos=(0,-16,0), axis=(32,0,0), size=(32,.5,32), color=color.blue , opacity = 0.3)
biegunNlbl=label(pos=(16,-16,16), text="N", color=color.blue, opacity=0, height=10)

=======
	siatka.append(curve(pos=[(x,-16,-16),(x,-16,16)], color=(0,0,1)))
	siatka.append(curve(pos=[(x,16,-16),(x,16,16)], color=(1,0,0)))	
for z in arange(-16, 16+4, 4):
	siatka.append(curve(pos=[(-16,-16,z),(16,-16,z)], color=(0,0,1)))
	siatka.append(curve(pos=[(-16,16,z),(16,16,z)], color=(1,0,0)))
	
biegunN=box(pos=(0,-16,0), axis=(32,0,0), size=(32,.5,32), color=color.blue , opacity = 0.3)
biegunNlbl=label(pos=(16,-16,16), text="N", color=color.blue, opacity=0, height=10)
	
>>>>>>> 2d26567eb0231f6c459485ea93038d7bc626abc8
biegunS=box(pos=(0,16,0), axis=(32,0,0), size=(32,.5,32), color=color.red  , opacity = 0.3)
biegunSlbl=label(pos=(16,16,16), text="S", color=color.red, opacity=0, height=10)

# ustawienie wektora pola
tekst='   '
y=0
warunek=True
while warunek:
<<<<<<< HEAD
    wektor = arrow(pos=(15,-14,15), axis=(0,y,0), color=(1,0.7, 0.7),shaftwidth=0.2)
    wektorlbl=label(pos=(-5,-20,15), text="Ustawienie wektora B", color=(1,0.7, 0.7), opacity=0, height=10)
    scenalbl1=label(pos=(-10,-27,15), text='UP - gora   DOWN - dol      BACKSPACE - O.K. ', color=(1,0.7, 0.7), opacity=0, height=10)
    klawisz = scene.kb.getkey()
    wektor.visible = False
    wektorlbl.visible = False
    scenalbl1.visible = False
    if klawisz=='up':
        y +=0.1
        y=korekta (10,0,0.1,y)
    elif klawisz=='down':
        y += -0.1
        y=korekta (10,0,0.1,y)
    elif klawisz=='backspace':
        BP=(0,y*e-5,0)
        pole ()
        warunek=False

=======
	wektor = arrow(pos=(15,-14,15), axis=(0,y,0), color=(1,0.7, 0.7),shaftwidth=0.2)
	wektorlbl=label(pos=(-5,-20,15), text="Ustawienie wektora B", color=(1,0.7, 0.7), opacity=0, height=10)
	scenalbl1=label(pos=(-10,-27,15), text='UP - gora   DOWN - dol      BACKSPACE - O.K. ', color=(1,0.7, 0.7), opacity=0, height=10)
	klawisz = scene.kb.getkey()
	wektor.visible = False
	wektorlbl.visible = False
	scenalbl1.visible = False
	if klawisz=='up':
		y +=0.1
		y=korekta (10,0,0.1,y)
	elif klawisz=='down':
		y += -0.1
		y=korekta (10,0,0.1,y)
	elif klawisz=='backspace':
		BP=(0,y*e-5,0)
		pole ()
		warunek=False
		
>>>>>>> 2d26567eb0231f6c459485ea93038d7bc626abc8
B=BP
#print ('Pole magnetyczne - ',BP)


# punkt powrotu petli
scena=True
while scena:
<<<<<<< HEAD
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
            punkt.ladunek=-1.6*e-19
            punkt.masa=9.1*e-31
            punkt.a=vector()
            punkt.v=vector()
            punkt.trajectory=curve(color=color.green,radius=.2)
            punktlbl.visible = False
            warunek=False
        elif klawisz=='p':
            #przyjeto proton
            punkt = sphere(pos = (xi, yi, zi), radius = .8, color = color.red, trail = curve(color=color.red))
            punkt.ladunek=1.6*e-19
            punkt.masa=1.7*e-27
            punkt.a=vector()
            punkt.v=vector()
            punkt.trajectory=curve(color=color.red,radius=.2)
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
        wektor = arrow(pos=(xi,yi,zi), axis=(a,b,c), color=(1, 0.7, 0.7),shaftwidth=0.1)
        klawisz = scene.kb.getkey()
    #	print (a,b,c)
        wektor.visible=False
        if klawisz=='up':
            b+=0.1
            b=korekta (20,-20,0.1,b)
        elif klawisz=='down':
            b+=-0.1
            b=korekta (20,-20,0.1,b)
        elif klawisz=='right':
            a+=0.1
            a=korekta (20,-20,0.1,a)
        elif klawisz=='left':
            a+=-0.1
            a=korekta (20,-20,0.1,a)
        elif klawisz=='p':
            c+=0.1
            c=korekta (20,-20,0.1,c)
        elif klawisz=='t':
            c+=-0.1
            c=korekta (20,-20,0.1,c)
        elif klawisz=='backspace':
            punkt.v=vector(a,b,c)
            warunek=False



    #print ('pp',punkt.pos,'pv',punkt.v,'dt',dt)

    # petla ruchu czastki


    scenalbl1.visible=False
    scenalbl2.visible=False

    Fl=punkt.ladunek*cross(punkt.v,B)
    punkt.a = Fl / punkt.masa
    #print (Fl)

    warunek=koniec=True
    while koniec:

        rate(100)
        punkt.pos=punkt.pos+punkt.v*dt
        punkt.trajectory.append(pos=punkt.pos)

        wektor.pos = punkt.pos
        wektor_z.pos=punkt.pos
        wektor_z.axis=(0,0,punkt.v.z)
        wektor_y.pos=punkt.pos
        wektor_y.axis=(0,punkt.v.y,0)
        wektor_x.pos=punkt.pos
        wektor_x.axis=(punkt.v.x,0,0)


        if -16 < punkt.pos.x < 16 and -16 < punkt.pos.y < 16 and -16 < punkt.pos.z < 16:
            B=BP
            print ('BP= ',B)
        else:
            B=(0,0,0)
            print ('B0= ',B)
        print ('B= ',B)
        punkt.v=punkt.a *dt
        Fl = punkt.ladunek * cross(punkt.v , B )
        punkt.a = punkt.a+ Fl/punkt.masa
        punkt.pos = punkt.pos + (punkt.a) *dt*dt

        #print(punkt.v)
        #print(Fl)
        #print(punkt.a)



        #print ('pp',punkt.pos)

        if punkt.pos.x <=-35 or punkt.pos.x >= 35 or punkt.pos.y <=-35 or punkt.pos.y >= 35 or punkt.pos.z <=-35 or punkt.pos.z >= 35 :
            scenalbl1=label(pos=(-10,-27,15), text=' Punkt poza punktami granicznymi wizualizacji  ', color=(1,0.7, 0.7), opacity=0, height=10)
            break
    scenalbl2=label(pos=(-10,-29,15), text=' Wizualizacja nastepnej czastki ?   t - tak   n -  nie', color=(1,0.7, 0.7), opacity=0, height=10)

    klawisz = scene.kb.getkey()
    if klawisz=='n':
        scena=False
    elif klawisz=='t':
        scena=True
        scenalbl1.visible=False
        scenalbl2.visible=False

exit


        #	punkt.a.x=Fl.x/punkt.masa
        #	punkt.a.y=Fl.y/punkt.masa
        #	punkt.a.z=Fl.z/punkt.masa
        #
        #	wektor.axis=vector(punkt.v.x,punkt.v.y,punkt.v.x)
        #	Fl=punkt.ladunek*cross(punkt.v,B)
        #
        #	wektor_x.axis.x = punkt.v.x
    #	#	wektor_y.axis.y = punkt.v.y
        #	wektor_z.axis.z = punkt.v.z

        #	punkt.v.z=punkt.v.z + punkt.a.z*dt
        #	punkt.v.y=punkt.v.y - punkt.a.y*dt
        #	punkt.v.x=punkt.v.x + punkt.a.x*dt

=======
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
			punkt.ladunek=-1.6*e-19
			punkt.masa=9.1*e-31
			punkt.a=vector()
			punkt.v=vector()
			punkt.trajectory=curve(color=color.green,radius=.2)
			punktlbl.visible = False
			warunek=False
		elif klawisz=='p':
			#przyjeto proton
			punkt = sphere(pos = (xi, yi, zi), radius = .8, color = color.red, trail = curve(color=color.red))		
			punkt.ladunek=1.6*e-19
			punkt.masa=1.7*e-27
			punkt.a=vector()
			punkt.v=vector()
			punkt.trajectory=curve(color=color.red,radius=.2)
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
		wektor = arrow(pos=(xi,yi,zi), axis=(a,b,c), color=(1, 0.7, 0.7),shaftwidth=0.1)	
		klawisz = scene.kb.getkey()
	#	print (a,b,c)
		wektor.visible=False	
		if klawisz=='up':
			b+=0.1
			b=korekta (20,-20,0.1,b)
		elif klawisz=='down':
			b+=-0.1
			b=korekta (20,-20,0.1,b)
		elif klawisz=='right':
			a+=0.1
			a=korekta (20,-20,0.1,a)		
		elif klawisz=='left':
			a+=-0.1
			a=korekta (20,-20,0.1,a)
		elif klawisz=='p':
			c+=0.1
			c=korekta (20,-20,0.1,c)
		elif klawisz=='t':
			c+=-0.1
			c=korekta (20,-20,0.1,c)
		elif klawisz=='backspace':
			punkt.v=vector(a,b,c)
			warunek=False
		
			

	#print ('pp',punkt.pos,'pv',punkt.v,'dt',dt)
	       
	# petla ruchu czastki
	
	
	scenalbl1.visible=False
	scenalbl2.visible=False
		
	Fl=punkt.ladunek*cross(punkt.v,B)

	warunek=koniec=True		                        
	while koniec:
		
		rate(100)
		punkt.pos=punkt.pos+punkt.v*dt
		punkt.trajectory.append(pos=punkt.pos)
		
		wektor.pos = punkt.pos
		wektor_z.pos=punkt.pos
		wektor_z.axis=(0,0,punkt.v.z)
		wektor_y.pos=punkt.pos
		wektor_y.axis=(0,punkt.v.y,0)
		wektor_x.pos=punkt.pos
		wektor_x.axis=(punkt.v.x,0,0)	
		
		while warunek:			
			if -16 < punkt.pos.x < 16 and -16 < punkt.pos.y < 16 and -16 < punkt.pos.z < 16:
				B=BP
				#print ('BP= ',B)
			else:
				B=(0,0,0)
				#print ('B0= ',B)
			#print ('B= ',B)
			punkt.v=punkt.a / punkt.masa
			Fl = punkt.ladunek * cross( v , B )
			punkt.a = punkt.a+ Fl*dt
			punkt.pos = punkt.pos + (punkt.a / punkt.masa) *dt
			break
	
		#print ('pp',punkt.pos)
	
		if punkt.pos.x <=-35 or punkt.pos.x >= 35 or punkt.pos.y <=-35 or punkt.pos.y >= 35 or punkt.pos.z <=-35 or punkt.pos.z >= 35 :
			scenalbl1=label(pos=(-10,-27,15), text=' Punkt poza punktami granicznymi wizualizacji  ', color=(1,0.7, 0.7), opacity=0, height=10)
			break
	scenalbl2=label(pos=(-10,-29,15), text=' Wizualizacja nastepnej czastki ?   t - tak   n -  nie', color=(1,0.7, 0.7), opacity=0, height=10)
				
	klawisz = scene.kb.getkey()
	if klawisz=='n':
		scena=False
	elif klawisz=='t':
		scena=True
		scenalbl1.visible=False
		scenalbl2.visible=False
		
exit


		#	punkt.a.x=Fl.x/punkt.masa
		#	punkt.a.y=Fl.y/punkt.masa
		#	punkt.a.z=Fl.z/punkt.masa
		#	
		#	wektor.axis=vector(punkt.v.x,punkt.v.y,punkt.v.x)
		#	Fl=punkt.ladunek*cross(punkt.v,B)
		#	
		#	wektor_x.axis.x = punkt.v.x
	#	#	wektor_y.axis.y = punkt.v.y
		#	wektor_z.axis.z = punkt.v.z 
			
		#	punkt.v.z=punkt.v.z + punkt.a.z*dt
		#	punkt.v.y=punkt.v.y - punkt.a.y*dt
		#	punkt.v.x=punkt.v.x + punkt.a.x*dt
			
>>>>>>> 2d26567eb0231f6c459485ea93038d7bc626abc8
