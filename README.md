# Sistema de Filas para Hospitais

Este projeto é um trabalho acadêmico com o objetivo de criar um sistema de filas para hospitais. O sistema gerencia a fila de pacientes utilizando uma lista encadeada, onde pacientes com cartões de cores diferentes têm prioridades distintas no atendimento.

## Contexto do Projeto

O sistema de filas foi desenvolvido para simular o gerenciamento de pacientes em um hospital. Pacientes com cartão vermelho ('V') têm menor prioridade e são inseridos no final da fila, enquanto pacientes com cartão amarelo ('A') têm maior prioridade e são inseridos no início da fila ou antes dos pacientes com cartão vermelho.

## Estrutura do Código

O código consiste em duas classes principais:

1. **Nodo**: Representa cada paciente na fila.
2. **ListaEncadeada**: Gerencia a lista de espera e implementa as operações de inserção e atendimento de pacientes.

### Classe Nodo

A classe `Nodo` representa cada paciente na fila e contém as seguintes propriedades:

- `numero`: Número do cartão do paciente.
- `cor`: Cor do cartão do paciente ('A' para amarelo, 'V' para vermelho).
- `proximo`: Referência para o próximo nodo na lista.

### Classe ListaEncadeada

A classe `ListaEncadeada` gerencia a lista de espera de pacientes e contém os seguintes métodos:

- `inserirSemPrioridade(nodo)`: Insere um paciente no final da fila (paciente com cartão vermelho).
- `inserirComPrioridade(nodo)`: Insere um paciente com prioridade (paciente com cartão amarelo).
- `inserir()`: Solicita ao usuário as informações do paciente e o insere na fila conforme a prioridade.
- `imprimirListaEspera()`: Exibe a lista de espera de pacientes.
- `atenderPaciente()`: Atende o paciente no início da fila.
- `menu()`: Exibe um menu interativo para o usuário selecionar as ações desejadas.

## Execução

Para executar o sistema de filas, basta rodar o script Python. O usuário será apresentado com um menu interativo com as seguintes opções:

1. Adicionar paciente à fila
2. Mostrar pacientes na fila
3. Chamar paciente
4. Sair

### Passos de Execução

1. Clone o repositório.
2. Navegue até o diretório do projeto.
3. Execute o script Python:
   ```bash
   python sistema_filas.py
