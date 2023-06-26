class Automato:
    def __init__(self, estados, alfabeto, transicoes, estado_inicial, estados_finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais

    def verificar_entrada(self, palavra):
        estado_atual = self.estado_inicial

        for simbolo in palavra:
            if simbolo not in self.alfabeto:
                return False

            estado_atual = self.transicoes.get((estado_atual, simbolo))

            if estado_atual is None:
                return False

        return estado_atual in self.estados_finais


# Função para construir um autômato definido pelo usuário
def construir_automato():
    print('#################################################################################################')
    print(' ')
    print('== SIMULADOR DE AUTOMATOS - FABIO, MARCIO, GREGORY, XXXXX ==')
    print('===                  MONTE SEU AUTOMATO                  ===')
    print(' ')
    estados = input("Informe os estados separados por vírgula: ").split(",")
    alfabeto = input("Informe os simbolos que compõem o alfabeto separados por vírgula: ").split(",")
    estado_inicial = input("Informe o estado inicial: ")
    estados_finais = input("Informe os estados finais separados por vírgula: ").split(",")

    transicoes = {}
    print("Digite as transições no formato: 'estado atual,simbolo,estado destino' ")
    print("Digite 'fim' para finalizar a entrada das transições.")
    print(' ')
    
    while True:
        entrada = input("Transição: ")
        if entrada == 'fim':
            break

        estado_atual, simbolo, estado_destino = entrada.split(",")
        transicoes[(estado_atual, simbolo)] = estado_destino

    automato = Automato(estados, alfabeto, transicoes, estado_inicial, estados_finais)
    return automato


# Função para testar uma palavra no autômato definido pelo usuário
def testar_palavra(automato):
    opcao = ''
    while opcao != '0':
        print(' ')
        print('SELECIONE UMA OPÇÃO:')
        print('1. Definir palavra')        
        print('0. Encerrar')
        opcao = input('')

        if opcao == '1':
            palavra = input('Digite sua palavra: ')
            if automato.verificar_entrada(palavra):
                print("A palavra foi reconhecida pelo autômato.")
            else:
             print("A palavra não foi reconhecida pelo autômato.")
            print('')
        elif opcao == '0':
            print('Encerrando o programa...')
        else:
            print(' ')
            print('Opção inválida. Tente novamente.')
            print(' ')



# Construir o autômato
automato = construir_automato()

# Testar palavras no autômato
testar_palavra(automato)
