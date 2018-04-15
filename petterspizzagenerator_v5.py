### --- Pizzagenerator for Petter's Pizza --- ###
# This Python file uses the following encoding: utf-8
## Sist oppdatert: april 2018 ##
## ----- ----- ##
#
## Import ##
import random
import easygui as egui
# --- --- #
#
#
def Pizzagenerator():
    # Intro #
    egui.msgbox("Velkommen til denne Pizzavelgeren for Petter's Pizza!")
    #
    # Navn og antall #
    antall = int(egui.enterbox('Hvor mange personer skal ete pizza?:'))
    antall_navn = ["Navn"]*antall # for å få antall linjer å skrive inn navn i
    pizzaetere = egui.multenterbox("Skriv inn navn til de som skal ete pizza:", "Pizzan00bs",antall_navn) #tar inn navn for å velge en ringer senere
    #
    # Meny #
    meny = ['"La Rosa"','"Petters Spesial"','"Turbo Spesial"','"Toni Spesial"','"Capricho"','"Olivera"','"Campera"','"Taco Pizza"','"La Napolitana"','"El Toro"','"La Pepperoni"','"Martita"','"Vegetar"','"Nidelv Spesial"','"Kebab Pizza"'] #liste med pizzaer som står på menyen
    #
    # Lage meny som kan velges fra
    #pizzalist = range(len(meny)) #unødvendig liste?
    meny_dic = {}
    for i in range(len(meny)): # lager en dic med navn på pizza og nr (ikke samvar med nr på menyen - det er ingen nr. på pizzaene på menyen)
    	meny_dic[i] = meny[i]
        #
    #
    #
    # Funksjon for å velge pizza #
    def ChoosePizza(pers,mulige_pizza):
        # Velger hvilke pizza man skal bestille der input er antall personer og en liste over mulige pizza
    	temppizzalist = mulige_pizza # Pizzavelgeren velger ikke to av samme pizza, så må ha muligheten til å forkaste en valgt pizza for så å velge tilfeldig blant de resterende
    	npizza = 0
    	if pers%2 == 1: #pizzavelgeren beregner 0.5 pizza/pers
    		npizza = int(pers/2) + 1 #int må brukes fordi python3
    	else:
    		npizza = pers/2
            #
        #
    	choice_pizza = []
    	for i in range(npizza): #plukker ut npizza tilfeldig valgte pizza fra mulige_pizza
            pc = random.choice(temppizzalist)
            choice_pizza.append(pc)
            temppizzalist.remove(pc)
            #
        #
    	return choice_pizza
        #
    #
    # Funksjon for å klargjøre bestillingen #
    def OrderPizza():
        order = ChoosePizza(antall,list(meny_dic.keys()))
        # Ringe inn bestilling #
        ringer = random.choice(pizzaetere) #alle elementer i pizzaetere er str
        ringe_msg = ringemsg = ringer + " ringer etter pizza!"
        egui.msgbox(ringemsg, ok_button = "RING TLF: 73 93 72 74")
        #
        # Vise på skjerm pizza som skal bestilles #
        order_pizza_msg = 'Vi bestiller følgende pizza: '
        p = len(order)
        if p > 1: #sjekke hvor mange pizza som skal bestilles; 1>1 returnerere False, så denne linjen sikrer oss 2 eller flere pizza (len(order) = 0 er det samme som ikke å bestille pizza))
            while p > 1: # for å kunne avrunde bestillings-teksten med en "og" før siste pizza
                order_pizza_msg += meny_dic[order[p-1]] + ','
                p = p-1
                #
            order_pizza_msg += ' og ' + meny_dic[order[0]]
            #
        else: #dersom det bare er en pizza som skal bestilles
            order_pizza_msg += ' ' + meny_dic[order[p-1]]
            #
        #
        # Oppsummering #
        egui.msgbox(order_pizza_msg, ok_button = "Vel bekomme.")
        #
    #
    # Kalle funksjonene for å kjøre programmet #
    OrderPizza()
    #
#
# Kjøre programmet #
Pizzagenerator()
#
#
#
