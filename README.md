### Cadastro de Alunos

Este projeto é uma aplicação simples de cadastro de alunos que permite realizar operações de CRUD (Create, Read, Update, Delete) em um banco de dados armazenado em um arquivo JSON. A aplicação é executada via console.

### Funcionalidades

1. **Registrar Aluno**
    - Permite a inserção de novos alunos no sistema.
    - Informações necessárias: Nome, Idade, Matrícula, Curso.
    - Após o cadastro, os dados são salvos no arquivo JSON.

2. **Consultar Aluno**
    - Permite a consulta de alunos cadastrados no sistema.
    - O usuário pode buscar um aluno específico pela matrícula.
    - Exibe informações detalhadas do aluno: Nome, Idade, Curso.

3. **Atualizar Cadastro de Aluno**
    - Permite a atualização das informações de um aluno existente.
    - O usuário pode modificar Nome, Idade e Curso do aluno.
    - As alterações são salvas no arquivo JSON.

4. **Excluir Cadastro de Aluno**
    - Permite a exclusão de um aluno do sistema.
    - O usuário deve confirmar a exclusão antes que o aluno seja removido do arquivo JSON.

5. **Sair do Sistema**
    - Encerra a execução da aplicação.

### Como Usar

1. **Clone o repositório**

   ```bash
   git clone https://github.com/Virto003/repo-cadastro-alunos.git
   cd repo-cadastro-alunos
   ```

2. **Execute o script**

   ```bash
   python cadastro_alunos.py
   ```

3. **Navegue pelas opções do menu**
    - O menu principal apresenta cinco opções:
        1. Registrar aluno
        2. Consultar aluno
        3. Atualizar cadastro de aluno
        4. Excluir cadastro de aluno
        5. Sair do sistema

### Estrutura do Projeto

- `cadastro_alunos.py`: Arquivo principal da aplicação, contendo toda a lógica do sistema.
- `alunos.json`: Arquivo JSON usado como banco de dados para armazenar os dados dos alunos.

### Exemplo de Uso

```plaintext
*** Cadastro de Alunos ***
1. Registrar aluno
2. Consultar aluno
3. Atualizar cadastro de aluno
4. Excluir cadastro de aluno
5. Sair do sistema
Escolha uma opção: 1
Digite o nome do aluno: João Silva
Digite a idade do aluno: 20
Digite a matrícula do aluno: 12345
Digite o curso do aluno: Engenharia
O aluno(a), João Silva da matrícula 12345 foi cadastrado com sucesso.
```

### Contribuição

Para contribuir com este projeto, siga os passos abaixo:

1. **Fork o repositório**
2. **Crie um branch para sua feature/bug fix**

   ```bash
   git checkout -b feature/nova-feature
   ```

3. **Commit suas alterações**

   ```bash
   git commit -m "Adiciona nova feature"
   ```

4. **Faça o push para o branch**

   ```bash
   git push origin feature/nova-feature
   ```

5. **Abra um Pull Request**
