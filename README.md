<h1 style="color:#CF72F2; font-size:1.95em">Mygym</h1>

Mygym é um projeto feito em Python com a finalidade de automatizar consultas em bancos de dados com a intermediação de um dashboard.

⚙ Funcionalidades dentro do programa:

- `Cadastre um novo usuario` cadastra um novo usuario no banco de dados.
- `Cadastre um novo treinador` cadastra um novo treinador no banco de dados.
- `Puxar tabela` seleciona uma tabela dentro do banco de dados e retorna todas as informações.
- `Buscar nos usuarios` busca por usuario no banco de dados pelo seu nome.
- `Buscar nos treinadores` busca por um treinador dentro do banco de dados pelo seu nome.
- `Atualizar usuario` atualiza as informações de um usuario.
- `Atualizar treinador` atualia as informações de um treinador.
- `Excluir` deleta um campo em uma tabela pelo seu ID.

<h1 style="color:#CF72F2; font-size:1.5em">Iniciando a aplicação</h1>
- Abra o arquivo `\sql_diagram.mwb` e execute no Mysql para iniciar o banco de dados.
- Use os comandos `pip install mysql.connector` , `pip install PySimpleGUI`.
- em seguida va para arquivo `\Main.py` e execute o arquivo.

<span style="color:#CF72F2; font-size:1.5em"> </h1>
<h1 style="color:#CF72F2; font-size:1.5em">Sobre a aplicação</h1>

📜 Organização do codigo:


- `\Main.py` é onde  programa é iniciado, ele apenas serve para criar a janela inicial. 
- `layout_style.py` é o script que armazena todo o layout do programa junto com as suas keys de cada componente da tela que serão chamadas posteriormente no script layout_function.py.
- `\layout_function.py` é o script que corderna todo o fluxo das funcionalidade do programa, sempre que o usuario interagir com algum campo do layout ele sera processado aqui.
- `\SQL.py` é o script que realiza as consultas no banco de dados, ele é um modulo que é chamado pelo layout_function.py quando necessario.

⚡ Organização do Mysql:


- `clientes` é a tabela que fica registrado cada cliente da academia, a tabela e composta por ID, Nome,
Idade, Sexo, Endereco e Telefone.
- `treinadores` é a tabela que fica registrado cada treinador da academia, a tabela e composta por ID, Nome, Especialização, Experiencia e NumeroRegistro. 
<span style="color:#CF72F2; font-size:1.5em"> </h1>
<h1 style="color:#CF72F2; font-size:1.5em">Tecnologias usadas </h1>

![python](https://img.shields.io/badge/python-000?style=for-the-badge&logo=python&logoColor=CF72F2)
![python](https://img.shields.io/badge/Mysql-000?style=for-the-badge&logo=Mysql&logoColor=CF72F2)







  