import random

def generar_situacion():
    """
    Elije una de la situaciones declaradas de manera aleatoria, 
    esta contiene los datos que se necesiten para procesar el karma

    returns:
        tuple: Contiene tres elementos
            - str: Situacion a presentar.
            - list: Lista de las decisiones a tomar y el valor de karma que representan.
            - int: Cantidad de elementos que tiene la lista.
    """
    nsituacion= random.randint(1,1)
    
    if nsituacion== 1:
        situacion="La reina te pide que acabes con los rebeldes que protestan por la libertad de sus familiares"
        decision= ["Acabar con los rebeldes",-15, "Oponerse a la reina",15, "Retirarse de la situacion",-5] # 1, 3, 5, 7, 9
        ndecision=6
    return situacion, decision, ndecision
    
def evaluar_decision(decision, karmaTotal):
    """
    Captura la decision del jugador y encuentra el valor del karma de su decisión para asi 
    alterar el karma total del jugador

    args:
        decision (list): Lista con las posibles decisiones y su valor
        karmaTotal (int): El karma con el que cuenta actualmente el jugador antes de su alteración

    returns:
        int: El karma que tiene el jugador despues de su alteración
    """
    decisionTomada= int(input(""))
    karmaRecibido=  decision[decisionTomada + decisionTomada - 1]
    karmaTotal+= karmaRecibido

    return karmaTotal
    
def mostrar_karma(karmaTotal):
    """ 
    Muestra el karma que tiene el jugador junto con un mensaje segun su cantidad de karma

    Args:
        karmaTotal (int): El karma actual que tiene el jugador con el cual se decide el mensaje a mostrar

    returns: 
        None 
    """
    if karmaTotal > 100:
        print("Tu karma es de",karmaTotal,"tus bondadosas acciones llenan tu alma de luz" )
    elif karmaTotal>5:
        print("Tu karma es de",karmaTotal,"vas por el camino del bien, y la luz empieza a guiar tu camino")
    elif karmaTotal <-100:
        print("Tu karma es de",karmaTotal,"te has vuelto uno con la oscuridad y siembras su caos o donde vayas")
    elif karmaTotal <-5:
        print("Tu karma es de",karmaTotal,"tu corazon empieza a aceptar la oscuridad que se esconde en el mundo")
    else:
        print("Tu karma es de",karmaTotal,"tu corazon no sabe que destino seguir, la luz te pide que ayudes a quien lo necesita, " \
        "que la oscuridad esta impaciente por que empieces a sembrar el caos")

def simulacion(karmaTotal):
    """
    Aqui se ejecutan todas las funciones para desarrollar la simulacion
    Se utilizan las funciones para obtener los valores y luego mostrarlos aqui, utilizando la logica necesaria

    args:
        karmaTotal (int): Es el karma actual del jugador el cual se utiliza para mandarselo a las otras funciones

    returns:
        -int: Se manda el karmaTotal final con el que se quedo el jugador para actualizar el karma global del jugador
    """
    situacion, decision, ndecision= generar_situacion()
    print (situacion)
    i2=1
    for i in range(0,ndecision, 2 ):
        print(i2,decision[i])
        i2+=1
       
    karmaTotal= evaluar_decision(decision=decision, karmaTotal=karmaTotal)
    
    mostrar_karma(karmaTotal=karmaTotal)
    
    return karmaTotal