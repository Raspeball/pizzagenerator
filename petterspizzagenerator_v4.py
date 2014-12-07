### --- Pizzagenerator for Petter's Pizza --- ###
## Sist oppdatert: desember 2014 ##
## ----- ----- ##
#
#
import random
import easygui as egui
# --- --- #
#
egui.msgbox("Velkommen til denne Pizzavelgeren for Petter's Pizza!")
antall = int(egui.enterbox('Hvor mange personer skal ete pizza?:'))
#
pizzaetere = ["Navn"]*antall # for å få antall linjer å skrive inn navn i
velgringer = egui.multenterbox("Skriv inn navn til de som skal ete pizza:", "Pizzan00bs",pizzaetere) #tar inn navn for å velge en ringer senere
#
pizzanavn = ['"La Rosa"','"Petters Spesial"','"Turbo Spesial"','"Toni Spesial"','"Capricho"','"Olivera"','"Campera"','"Taco Pizza"','"La Napolitana"','"El Toro"','"La Pepperoni"','"Martita"','"Vegetar"','"Nivelv Spesial"','"Kebab Pizza"']
pizzalist = range(len(pizzanavn))
pizzadic = {}
#
for i in range(len(pizzalist)):
	pizzadic[pizzalist[i]] = pizzanavn[i]
#
def ChoosePizza(pers): # Velger hvilke pizza man skal bestille der input er antall personer
	temppizzalist = list(pizzadic.keys())
	npizza = 0
	if pers%2 == 1:
		npizza = (pers/2) + 1
	else: 
		npizza = pers/2
	
	cpizza = [None]*npizza
	for i in range(npizza):
		cpizza[i] = random.choice(temppizzalist)
		temppizzalist.remove(cpizza[i])
		
	return cpizza
#
orderpizza = ChoosePizza(antall)
ringer = random.choice(velgringer)
ringemsg = ringer + " ringer etter pizza!"
egui.msgbox(ringemsg, ok_button = "RING TLF: 73 93 72 74")
#
msgpizza = 'Vi bestiller følgende pizza: '
#
p = len(orderpizza)
if p > 1: # 1>1 returns False, so this line ensures the case of 2 or more pizzas to be ordered 
	while p > 1:
		msgpizza = msgpizza + ', ' + str(pizzadic[orderpizza[(p-1)]])
		p = p-1
	#
	msgpizza = msgpizza + ' og ' + str(pizzadic[orderpizza[0]])
else:
	msgpizza = msgpizza + ' ' + str(pizzadic[orderpizza[(p-1)]])
#
#
egui.msgbox(msgpizza, ok_button = "Vel bekomme.")
#
#		
