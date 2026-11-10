🌳 Árvore Binária de Busca (ABB) em Python
📌 Sobre o projeto

Este projeto implementa uma Árvore Binária de Busca (ABB) utilizando a linguagem Python.

Uma Árvore Binária de Busca é uma estrutura de dados não linear em que cada nó possui, no máximo, dois filhos: um à esquerda e outro à direita.

A organização dos valores segue a seguinte regra:

Valores menores que o nó atual são inseridos à esquerda.
Valores maiores ou iguais ao nó atual são inseridos à direita.

O programa oferece um menu interativo que permite realizar operações de inserção, remoção, busca, cálculo de altura e diferentes tipos de percurso na árvore.

🚀 Funcionalidades

O programa possui as seguintes funcionalidades:

Opção	Funcionalidade	Descrição
1	Inserir elemento	Adiciona um novo valor à árvore.
2	Excluir elemento	Remove um valor existente da árvore.
3	Buscar elemento	Verifica se determinado valor está presente.
4	Altura da árvore	Calcula a altura da árvore.
5	Percurso In-ordem	Exibe os valores na ordem crescente.
6	Percurso Pré-ordem	Exibe primeiro a raiz, depois a esquerda e a direita.
7	Percurso Pós-ordem	Exibe primeiro os filhos e depois a raiz.
8	Sair	Encerra o programa.
🧱 Estrutura do código

O código é dividido em duas classes principais:

1. Classe Node

Responsável por representar cada nó da árvore.

Cada nó possui três atributos:

valor: armazena o valor do elemento.
esquerda: referência para o filho esquerdo.
direita: referência para o filho direito.
2. Classe Arvore

Responsável por implementar as operações da Árvore Binária de Busca.

Seus principais métodos são:

inserir(dado): insere um novo elemento respeitando as regras da árvore binária de busca.
remover(valor): remove um elemento da árvore, considerando os diferentes casos de remoção.
buscar(valor): procura um elemento na árvore.
altura(no): calcula a altura da árvore ou de uma subárvore.
pre_ordem(no): realiza o percurso pré-ordem.
in_ordem(no): realiza o percurso in-ordem.
pos_ordem(no): realiza o percurso pós-ordem.
🔄 Tipos de percurso

O programa implementa três formas de percorrer os elementos da árvore:

In-ordem (Esquerda → Raiz → Direita)

Visita primeiro a subárvore esquerda, depois o nó atual e, por último, a subárvore direita.

Em uma Árvore Binária de Busca, esse percurso apresenta os valores em ordem crescente.

Pré-ordem (Raiz → Esquerda → Direita)

Visita primeiro o nó atual, depois a subárvore esquerda e, por último, a subárvore direita.

Pós-ordem (Esquerda → Direita → Raiz)

Visita primeiro a subárvore esquerda, depois a direita e, por último, o nó atual.

💻 Como executar o projeto
Pré-requisitos
Python 3 instalado.
Um editor de código ou terminal.
Execução
Clone o repositório:
bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

Entre na pasta do projeto:
bash
cd SEU-REPOSITORIO

Execute o arquivo Python:
bash
python main.py

📋 Exemplo de utilização

Considere a inserção dos seguintes valores:

text
50, 30, 70, 20, 40, 60, 80


A árvore será organizada da seguinte maneira:

text
          50
        /    \
      30      70
     /  \    /  \
    20  40  60  80


Os percursos apresentarão os seguintes resultados:

In-ordem:

text
20
30
40
50
60
70
80


Pré-ordem:

text
50
30
20
40
70
60
80


Pós-ordem:

text
20
40
30
60
80
70
50

⏱️ Complexidade das operações

Considerando uma árvore com n elementos:

Operação	Caso médio	Pior caso
Inserção	O(log n)	O(n)
Busca	O(log n)	O(n)
Remoção	O(log n)	O(n)
Percursos	O(n)	O(n)
Cálculo da altura	O(n)	O(n)

A complexidade depende da organização da árvore. Quando ela está equilibrada, as operações de busca, inserção e remoção tendem a ser mais eficientes. Quando está degenerada, seu comportamento pode se aproximar de uma lista encadeada.

🎯 Objetivo acadêmico

O objetivo deste projeto é aplicar os conceitos de estruturas de dados não lineares, especialmente Árvores Binárias de Busca, utilizando Python.

Por meio da implementação, são trabalhados conceitos como:

Estruturas de dados dinâmicas.
Classes e objetos.
Referências entre nós.
Algoritmos de busca e inserção.
Remoção de elementos em árvores.
Recursividade.
Algoritmos de percurso.
🛠️ Tecnologias utilizadas
Linguagem: Python 3.
Conceitos: Estrutura de Dados, Árvore Binária de Busca e Recursividade.
📄 Licença

Este projeto foi desenvolvido para fins educacionais e de estudo sobre estruturas de dados.