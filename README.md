# O que é a rede neural adaline?
"Adaline" é um acrônimo em inglês para "Adaptative Linear Element", ou seja, "Elemento Linear Adaptável". A Adaline é uma rede que se parece bastante com a rede Perceptron de camada única em nível de simplicidade. Ela também possui apenas 1 neurônio. A diferença entre as duas está no algoritmo de treinamento. Ao passo que a Perceptron de camada única utiliza a regra de Hebb para encontrar algum hiperplano que divida duas classes linearmente separáveis, a Adaline utiliza a regra delta, que é baseada em minimizar o erro quadrático médio entre as saídas desejadas e as saídas da rede. 
Para mais informações sobre o funcionamento da Adaline, consultar o livro "Redes neurais artificias para  engenharia e ciências aplicadas" dos altores Ivan Nunes da Silva, Danilo Hernane Spatti e Rogério Andrade Flauzino.
# Para que serve?
Ela é capaz de aprender a separar classes linearmente separáveis. Um exemplo comum de uso é para realizar as operações lógicas "e" e "ou".
# Como utilizar a rede presente nesse repositório?
A rede presente neste repositório está com os pesos sinápticos e limiar de ativação (presentes no arquivo pesos.txt da pasta treinamento) treinados para realizar a operação "e" lógico. Isso pode ser observado pelos arquivos "entradas.txt" e "saidas.txt" presentes na pasta de treinamento.
Algo como:
Entrada: -1,1,1
Saída: 1
Pode ser observado nesses arquivos de treinamento. Indicando a operação "e" lógica, que no caso da entrada -1,1,1 efetua a operação tendo a saída 1. Vale ressaltar que o "-1" presente na primeira posição em todas as linhas da entrada serve para adicionar o viés à rede. Para mais informações sobre viéses em redes neurais, consultar o livro "Redes neurais artificias para  engenharia e ciências aplicadas" dos altores Ivan Nunes da Silva, Danilo Hernane Spatti e Rogério Andrade Flauzino.
Para testar a rede nestas condições, basta executar o arquivo main presente na pasta raiz e digitar entradas de dois dígitos separados por vírgula, como por exemplo:
Digite: 1,1 
True
Digite: 1,0
False
# Como treinar a rede para executar outra tarefa?
Para treinar a rede para a execução de outra tarefa, basta alterar os dados presentes nos arquivos de entradas e saidas para que eles contenham um conjunto de entradas e saídas para o problema a ser resolvido. Vale lembrar que a rede perceptron só consegue resolver problemas de classificação que envolvam apenas duas classes linearmente separáveis. Como no exemplo do "e" lógico, onde a saída é "True" ou "False".
Após trocar as entradas e saídas basta abrir o arquivo "treinamento.py" na pasta de treinamento e executar o algoritmo de treinamento.
Após executado o algoritmo de treinamento, basta reexecutar o main.py.
Vale ressaltar: caso o problema não seja mapeável em duas classes linearmente separáveis, pode ser que o treinamento execute um número limite de épocas sem conseguir encontrar os pesos sinápticos corretos. Também é importante adicionar o viés nas linhas do arquivo de entrada.
