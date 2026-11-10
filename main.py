class Node:

    def __init__(self,valor):
        self.valor=valor
        self.esquerda=None
        self.direita=None

class Arvore:

    def __init__(self):
        self.raiz=None

    def inserir(self,dado:int):
        novo = Node(dado)

        if self.raiz == None:
            self.raiz=novo
            return

        atual=self.raiz
        while True:
            if dado< atual.valor:
                if atual.esquerda is None:
                    atual.esquerda= novo
                    return
                atual=atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita=novo
                    return
                atual = atual.direita

    def remover(self,valor:int):
        pai = None
        atual=self.raiz
        while atual and atual.valor != valor:
            pai=atual
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        if not atual:
            print("Elemento nao encontrado")
            return 

        if atual.esquerda and atual.direita:
            pai_suc=atual
            suc=atual.direita

            while suc.esquerda:
                pai_suc=suc
                suc= suc.esquerda

                atual.valor= suc.valor
                pai=pai_suc
                atual=suc

        filho = atual.esquerda or atual.direita
        if pai is None:
            self.raiz=filho
        elif pai.esquerda == atual:
            pai.esquerda=filho
        else:
            pai.direita=filho
        return True


    def buscar(self, valor):
        atual = self.raiz
        while atual:
            if valor == atual.valor:
                print(f"valor encontrado: {valor}")
                return True
            if valor < atual.valor:
                atual=atual.esquerda
            else:
                atual = atual.direita
        print('valor nao encontrado')

    
    def altura(self,no):
        if no is None:
            return 0
        alt_esquerda = self.altura(no.esquerda)
        alt_direita = self.altura(no.direita)

        return 1 + max(alt_esquerda, alt_direita)

    def pre_ordem(self,no):
        if no is not None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def in_ordem(self,no):
        if no is not None:
            self.in_ordem(no.esquerda)
            print(no.valor)
            self.in_ordem(no.direita)

    def pos_ordem(self,no):
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)
    
        

def main():
    opcao=0
    arv = Arvore()

    while opcao != 8:
        print('1 -- Inserir elemento')
        print('2 -- Excluir elemento')
        print('3 -- Buscar elemento')
        print('4 -- Altura da arvore')
        print('5 -- Mostrar in-ordem')
        print('6 -- Mostrar pre-ordem')
        print('7 -- Mostrar pos-ordem')
        print('8 -- Sair')



        opcao=int(input("Opcao: "))

        if opcao == 1:
            dado=int(input("Insira o valor: "))
            arv.inserir(dado)

        elif opcao == 2:
            dado=int(input("Insira o valor: "))
            arv.remover(dado)

        elif opcao == 3:
            dado = int(input("Digite o valor para buscar: "))
            arv.buscar(dado)

        elif opcao == 4:
            print(f"Altura: {arv.altura(arv.raiz)}")

        elif opcao ==5:
            arv.in_ordem(arv.raiz)
        elif opcao==6:
            arv.pre_ordem(arv.raiz)
        elif opcao==7:
            arv.pos_ordem(arv.raiz)


if __name__ == "__main__":
    main()