import random
def barajar(baraja):
    random.shuffle(baraja)
    return baraja
def contar(jugador, cuenta):
    if(jugador == []):
        return cuenta
    if(jugador[0] == "J" or jugador[0] == "Q" or jugador[0] == "K"):
        return contar(jugador[1:], 10+cuenta)
    if(jugador[0] == "A" and cuenta+contar(jugador[1:],cuenta) > 10):
        return contar(jugador[1:], cuenta+1)
    if(jugador[0] == "A" and cuenta+contar(jugador[1:],cuenta) <10):
        return contar(jugador[1:], cuenta +11)
    return contar(jugador[1:], cuenta+jugador[0])
def jugar(baraja,jugador, cpu):
    if(len(jugador) < 2 and len(cpu) < 2):
        return jugar(baraja[2:], repartirCarta(baraja,jugador),repartirCarta(baraja[1:],cpu))
    print (jugador)
    print (cpu)
    print (contar(jugador,0))
    if(contar(jugador,0) < 21):
        if(input("Pedir carta s/n: ") == "s"):
            return jugar(baraja[1:], repartirCarta(baraja[1:],jugador), cpu)
        else:
            print ("Te has plantado en "+str(contar(jugador,0)))
            return jugarCpu(baraja[1:],cpu,contar(jugador,0))
    elif(contar(jugador,0) > 21):
        print ("Has perdido")
        exit()
    elif (contar(jugador,0)==21):
        print ("Has ganado")
        exit()
    return 0

def jugarCpu(baraja, cpu, numJugador):
    if(contar(cpu,0) > 21):
        print ("Has ganado")
        print ("Casa: "+str(contar(cpu,0)))
        print ("Tu puntaje: "+str(numJugador))
        print (cpu)
        exit()
    if(contar(cpu,0) >= numJugador and contar(cpu,0) <= 21):
        print ("La casa ha ganado")
        print ("Casa: " + str(contar(cpu, 0)))
        print ("Tu puntaje: " + str(numJugador))
        exit()
    if(contar(cpu,0) < numJugador):
        print (cpu)
        return jugarCpu(baraja[1:],repartirCarta(baraja, cpu),numJugador)

def repartirCarta(baraja, jugador):
    return jugador+[baraja[0]]

jugar(barajar([(x)for x in [2,3,4,5,6,7,8,9,"A","J","Q","K"]*4]),[],[])
