# GCC218 - Algoritmos em Grafos - 2021/2
# Alunos: Antônio Mauricio Lanza de Sá e Melo Marques - Matrícula: 202020088
#         Victor Gonçalves Lima - Matrícula: 202020775
# Turma: 10A
# Data: 17/04/2022
# Atividade Avaliativa 6 - Exercício de Implementação



class Grafo:

    lista_adjacencia = {}

    def __init__(self, n: int) -> None:
        for i in range(1, n + 1):
            self.lista_adjacencia[str(i)] = {}
            self.lista_adjacencia[str(i)][str(i)] = 0

    def inserirAresta(self, u: str, v: str, p: int) -> None:
        self.lista_adjacencia[u][v] = p

    def removerAresta(self, u: str, v: str) -> None:
        self.lista_adjacencia[u].pop(v)


def calcularCusto(pessoas: int, vagas: int, g: Grafo, inicio: str, fim: str) -> str:

    custo = 0

    while(pessoas > 0):
        if(pessoas < vagas):
            viajantes = pessoas
        else:
            viajantes = vagas
        caminho = caminhoMaisBarato(g, inicio, fim)
        n = len(caminho)
        if(n == 1):
            return "impossivel"
        for i in range(n - 1, -1, -1):
            if(i > 0):
                u, v = caminho[i], caminho[i - 1]
                custo += viajantes * g.lista_adjacencia[u][v]
                g.removerAresta(u, v)
                #g.removerAresta(v, u)
        pessoas -= viajantes

    return str(custo)



def caminhoMaisBarato(g: Grafo, inicio: str, fim: str) -> list:

    caminho = {}
    noh_adjacentes = {}
    fila = []

    for noh in g.lista_adjacencia:
        caminho[noh] = float("inf")
        noh_adjacentes[noh] = None
        fila.append(noh)

    caminho[inicio] = 0

    while fila:
        key_min = fila[0]
        min_val = caminho[key_min]
        for n in range(1, len(fila)):
            if caminho[fila[n]] < min_val:
                key_min = fila[n]
                min_val = caminho[key_min]
        u = key_min
        fila.remove(u)

        for v in g.lista_adjacencia[u]:
            alternate = g.lista_adjacencia[u][v] + caminho[u]
            if caminho[v] > alternate:
                caminho[v] = alternate
                noh_adjacentes[v] = u

    noh = fim
    caminho = []
    caminho.append(fim)
    while True:
        noh = noh_adjacentes[noh]
        if noh is None:
            break
        caminho.append(noh)

    return caminho



from sys import stdin


def main() -> None:

    entrada = stdin.read()
    linhas = entrada.splitlines()

    saida = []

    instancia = 0

    linha_atual = 0
    while linha_atual < len(linhas):
        instancia += 1
        n, m = map(int, linhas[linha_atual].split(maxsplit=1))
        linha_atual += 1
        grafo = Grafo(n)
        for _ in range(m):
            u, v, p = linhas[linha_atual].split(maxsplit=2)
            linha_atual += 1
            grafo.inserirAresta(u, v, int(p))
            grafo.inserirAresta(v, u, int(p))
        pessoas, vagas = map(int, linhas[linha_atual].split(maxsplit=1))
        linha_atual += 1
        saida.append("Instancia " + str(instancia) + '\n' + calcularCusto(pessoas, vagas, grafo, "1", str(n)))

    for i in range(instancia):
        print(saida[i])
        if i < instancia - 1:
            print()


main()