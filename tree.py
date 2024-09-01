from node import Node


class ArbolBinario:
    def __init__(self):
        self.root = None

    def insertar(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insertar_recursivo(value, self.root)

    def _insertar_recursivo(self, value, actual_node):
        if value < actual_node.value:
            if actual_node.left is None:
                actual_node.left = Node(value)
            else:
                self._insertar_recursivo(value, actual_node.left)
        elif value > actual_node.value:
            if actual_node.right is None:
                actual_node.right = Node(value)
            else:
                self._insertar_recursivo(value, actual_node.right)
        elif value == actual_node.value:
            print(f"El valor {value} ya está en el árbol.")

    def buscar(self, value):
        return self._buscar_recursivo(value, self.root)

    def _buscar_recursivo(self, value, actual_node):
        if actual_node is None:
            return False
        elif value == actual_node.value:
            return True
        elif value < actual_node.value:
            return self._buscar_recursivo(value, actual_node.left)
        else:
            return self._buscar_recursivo(value, actual_node.right)

    def recorrer_inorden(self):
        elementos = []
        self._recorrer_inorden_recursivo(self.root, elementos)
        print(f"Árbol sin números repetidos {elementos}")

        return elementos

    def _recorrer_inorden_recursivo(self, actual_node, elementos):
        if actual_node:
            self._recorrer_inorden_recursivo(actual_node.left, elementos)
            elementos.append(actual_node.value)
            self._recorrer_inorden_recursivo(actual_node.right, elementos)

    def recorrer_preorden(self):
        elementos = []
        self._recorrer_preorden_recursivo(self.root, elementos)
        return elementos

    def _recorrer_preorden_recursivo(self, actual_node, elementos):
        if actual_node:
            elementos.append(actual_node.value)
            self._recorrer_preorden_recursivo(actual_node.left, elementos)
            self._recorrer_preorden_recursivo(actual_node.right, elementos)

    def recorrer_postorden(self):
        elementos = []
        self._recorrer_postorden_recursivo(self.root, elementos)
        return elementos

    def _recorrer_postorden_recursivo(self, actual_node, elementos):
        if actual_node:
            self._recorrer_postorden_recursivo(actual_node.left, elementos)
            self._recorrer_postorden_recursivo(actual_node.right, elementos)
            elementos.append(actual_node.value)

    def recorrer_nodos_con_dos_hijos(self):
        elementos = []
        self._recorrer_preorden_recursivo_dos_hijos(self.root, elementos)
        print(f"Nodos con dos hijos: {elementos}")
        return elementos

    def _recorrer_preorden_recursivo_dos_hijos(self, actual_node, elementos):
        if actual_node:
            # Aquí chequeamos si el nodo actual tiene dos hijos
            if actual_node.left and actual_node.right:
                elementos.append(actual_node.value)

                # Llamamos recursivamente para recorrer el subárbol izquierdo
                self._recorrer_preorden_recursivo_dos_hijos(actual_node.left, elementos)

                # Llamamos recursivamente para recorrer el subárbol derecho
                self._recorrer_preorden_recursivo_dos_hijos(
                    actual_node.right, elementos
                )

    def recorrer_nodos_almenos_con_un_hijo_par(self):
        elementos = []
        self._recorrer_preorden_recursivo_con_almenos_un_hijo_par(self.root, elementos)
        print(f"Nodos con al menos un hijo par: {elementos}")
        return elementos        

    def _recorrer_preorden_recursivo_con_almenos_un_hijo_par(self, actual_node, elementos):
        if actual_node:
            # Aquí chequeamos si el nodo actual tiene dos hijos
            if actual_node.left:
                if actual_node.left.value % 2 == 0:
                    elementos.append(actual_node.value)
                # Llamamos recursivamente para recorrer el subárbol izquierdo
                self._recorrer_preorden_recursivo_con_almenos_un_hijo_par(
                    actual_node.left, elementos
                )
            if actual_node.right:
                if actual_node.right.value % 2 == 0:
                    elementos.append(actual_node.value)
                # Llamamos recursivamente para recorrer el subárbol derecho
                self._recorrer_preorden_recursivo_con_almenos_un_hijo_par(
                    actual_node.right, elementos
                )

    def visualizar_suma_hijos(self):
        # Método público que llama al método recursivo
        self._visualizar_suma_hijos_recursivo(self.root)

    def _visualizar_suma_hijos_recursivo(self, actual_node):
        # Método recursivo para visualizar la suma de los hijos en preorden
        if actual_node is None:
            return 0

        # Calculamos la suma de los hijos
        suma_hijos = 0
        if actual_node.left:
            suma_hijos += actual_node.left.value
        if actual_node.right:
            suma_hijos += actual_node.right.value

        # Visualizamos la suma de los hijos para el nodo actual
        print(f"Nodo {actual_node.value} tiene suma de hijos: {suma_hijos}")

        # Llamamos recursivamente para el hijo izquierdo y derecho
        self._visualizar_suma_hijos_recursivo(actual_node.left)
        self._visualizar_suma_hijos_recursivo(actual_node.right)

    def encontrar_camino(self, valor_buscado):
        camino = []
        if self._encontrar_camino_recursivo(self.root, valor_buscado, camino):
            return camino
        else:
            return "El nodo no existe"

    def _encontrar_camino_recursivo(self, actual_node, valor_buscado, camino):
        if actual_node is None:
            return False
        camino.append(actual_node.value)
        if actual_node.value == valor_buscado:
            print(
                f"El valor {valor_buscado} fue encontrado y este fue el camino antes de encontrar el valor buscado {camino}"
            )
            return True
        if self._encontrar_camino_recursivo(
            actual_node.left, valor_buscado, camino
        ) or self._encontrar_camino_recursivo(actual_node.right, valor_buscado, camino):
            return True
        camino.pop()
        return False
