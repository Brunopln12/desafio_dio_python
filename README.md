# Sistema Bancário Simples

Um sistema bancário simples implementado em Python, que permite aos usuários realizar operações básicas como depósito, saque, criação de contas e cadastro de usuários.

## Funcionalidades

- Depositar dinheiro na conta.
- Sacar dinheiro da conta (com limite de saque e contagem de número de saques).
- Ver extrato da conta.
- Criar uma nova conta.
- Listar contas existentes.
- Criar um novo usuário.
- Sair do sistema.

## Uso

Para executar o programa, basta rodar o script `sistema_bancario.py`. O programa apresentará um menu com as opções disponíveis. Basta selecionar a operação desejada digitando a letra correspondente e seguir as instruções na tela.

### Menu de Operações

```
================ MENU ================
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q]  Sair
=>

```

## Funcionamento

- Ao selecionar a opção "Depositar", o usuário pode informar o valor a ser depositado na conta. O saldo será atualizado e o depósito será registrado no extrato.
- Ao selecionar a opção "Sacar", o usuário pode informar o valor a ser sacado da conta. Serão verificados se o valor é válido, se há saldo suficiente, se o valor está dentro do limite de saque e se o número de saques não excede o limite estabelecido. Se todas as condições forem atendidas, o saque será realizado com sucesso e registrado no extrato.
- Ao selecionar a opção "Extrato", o usuário pode visualizar o extrato da conta, que contém o registro de todas as operações realizadas.
- Ao selecionar a opção "Nova conta", o usuário pode criar uma nova conta, informando o CPF do titular.
- Ao selecionar a opção "Listar contas", o usuário pode ver todas as contas existentes, mostrando detalhes como agência, número da conta e titular.
- Ao selecionar a opção "Novo usuário", o usuário pode criar um novo usuário informando dados como CPF, nome, data de nascimento e endereço.
- Ao selecionar a opção "Sair", o programa será encerrado.

## Limitações

- O sistema não possui funcionalidades avançadas, como autenticação de usuários, persistência de dados ou interface gráfica.
- O limite de saques é fixo em 3 saques.
- O limite de saque por transação é fixo em R$ 500.00.
- Não há tratamento de erros abrangente para entradas inválidas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue caso encontre algum problema ou para propor melhorias ao projeto.

## Autor

Este projeto foi desenvolvido por Bruno Nascimento.
