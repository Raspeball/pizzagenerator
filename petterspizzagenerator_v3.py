### --- Pizzagenerator for Petter's Pizza --- ###
# This Python file uses the following encoding: utf-8
## Sist oppdatert: november 2014 ##
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

msgpizza = 'Vi bestiller følgende pizza: '
for p in range(len(orderpizza)):
	if p == 0:
		msgpizza = msgpizza + ' ' + str(pizzadic[orderpizza[p]])
	elif len(orderpizza) > 2:
		if p == 1:
			msgpizza = msgpizza + ', ' + str(pizzadic[orderpizza[p]])
		else:
			msgpizza = msgpizza + ' og ' + str(pizzadic[orderpizza[p]])
	else:
		msgpizza = msgpizza + ' og ' + str(pizzadic[orderpizza[p]])

egui.msgbox(msgpizza, ok_button = "Vel bekomme.")

		
