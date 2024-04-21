from collections import defaultdict


def solicitar_gramatica():
    gramaticas = []
    num_gramaticas = int(input())

    for _ in range(num_gramaticas):
        gramatica = defaultdict(list)
        num_no_terminales, num_cadenas = map(int, input().split())

        for _ in range(num_no_terminales):
            no_terminal, *producciones = input().split()
            gramatica[no_terminal] = producciones

        cadenas = [input().strip() for _ in range(num_cadenas)]

        gramaticas.append((gramatica, cadenas))

    return gramaticas


def cyk(subcadena, gramatica):
    tabla = defaultdict(set)
    n = len(subcadena)
    for i in range(1, n + 1):
        for j in range(n - i + 1):
            if i == 1:
                for llave in gramatica:
                    if subcadena[j:j + i] in gramatica[llave]:
                        tabla[(j, j + i)].add(llave)
            else:
                for k in range(1, i):
                    for A in tabla[(j, j + k)]:
                        for B in tabla[(j + k, j + i)]:
                            for var in [x + y for x in A for y in B]:
                                for llave in gramatica:
                                    if var in gramatica[llave]:
                                        tabla[(j, j + i)].add(llave)
    return tabla


def main():
    print("ingresar la entrada de la manera indicada en el documento de la entrega:")
    gramaticas = solicitar_gramatica()
    print("\n" + "output" + "\n")
    for gramatica, cadenas in gramaticas:

        for cadena in cadenas:

            tabla = cyk(cadena, gramatica)

            if 'S' in tabla[(0, len(cadena))]:
                print("yes")
            else:
                print("no")
        print()


if __name__ == "__main__":
    main()
