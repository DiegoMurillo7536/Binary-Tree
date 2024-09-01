from tree import ArbolBinario
from utils import insert_numbers_in_list,insert_number_by_user_to_search

def main():
    arbol = ArbolBinario()
    # Crear N cantidad de nodos e insertarlos en el árbol
    values = insert_numbers_in_list()
    print(f"Valores que se van a usar en el arbol binario {values}")
    for value in values:
        arbol.insertar(value)
    arbol.recorrer_inorden()

    # Revisar aquellos nodos que al menos tengan dos hijos
    arbol.recorrer_nodos_con_dos_hijos()

    #Revisar aquellos nodos que tengan al menos un hijo
    arbol.recorrer_nodos_almenos_con_un_hijo()
    
    #Recorrer camino para buscar un número
    valor_a_encontrar = insert_number_by_user_to_search()
    
    arbol.encontrar_camino(valor_a_encontrar)
main()

"""
Ingresa la cantidad de datos aleatorios a ingresar dentro de la lista:10
Valores que se van a usar en el arbol binario [8, 6, 10, 6, 1, 7, 8, 5, 5, 7
El valor 6 ya está en el árbol.
El valor 8 ya está en el árbol.
El valor 5 ya está en el árbol.
El valor 7 ya está en el árbol.
 Árbol sin números repetidos [1, 5, 6, 7, 8, 10]
Nodos con dos hijos: [8, 6]
Nodos con al menos un hijo par: [8]

"""