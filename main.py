from tree import ArbolBinario
from utils import insert_numbers_in_list

def main():
    arbol = ArbolBinario()
    
    values = insert_numbers_in_list()
    print(f"Valores que se van a usar en el arbol binario {values}")
    for value in values:
        arbol.insertar(value)
    arbol.recorrer_inorden()
    arbol.recorrer_nodos_con_dos_hijos()
    arbol.recorrer_nodos_almenos_con_un_hijo()

main()
