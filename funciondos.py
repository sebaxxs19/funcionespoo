import random

def probabilidad(num_lanzalmientos,num_caras):

    resultados=[random.choice([0,1])] for _ in range (num_lanzaminetos)
    
    prob=resultados.count(1)/num_lanzalmientos
    return prob

    num_lanzalmientos=10
    num_caras=6
    
    prob=probabilidad(num_lanzalmientos,num_caras)
    print(f"la probabilidad de obtener {num_caras} en {num_lanzalmientos} es{prob:.4f}")