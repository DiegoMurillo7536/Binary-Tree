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

    # Revisar aquellos nodos que tengan al menos un hijo
    arbol.recorrer_nodos_almenos_con_un_hijo_par()

    # Suma de cada nodo
    arbol.visualizar_suma_hijos()
    
    # Recorrer camino para buscar un número
    valor_a_encontrar = insert_number_by_user_to_search()
    arbol.encontrar_camino(valor_a_encontrar)


main()

"""Output:
Ingresa un número que desees buscar:7
El valor 10 fue encontrado y este fue el camino antes de encontrar el valor buscado [8, 6, 7]
"""
