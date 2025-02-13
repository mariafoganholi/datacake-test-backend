## DataCake 🎂 Test API
API implementada utilizando Django com os seguintes endpoints:
- GET /todo: lista todas as tarefas
- POST /todo: cria uma nova tarefa
- DELETE /todo/<pk>: exclui uma tarefa específica
- PUT /todo/<pk>: edita uma tarefa específica 

## Dependências
- Python 3
- Virtual Env

## Como usar

1. Crie um ambiente virtual Python.

```
python -m venv env
```

2. Ative o ambiente virtual.

```
.\env\Scripts\activate
```

3. Instale as dependências rodando o seguinte comando no terminal. 

```
pip install -r requirements.txt
```

4. Crie o banco de dados.

```
python manage.py migrate
```

5. Rode o servidor.

```
python manage.py runserver
```

Agora a API está pronta respondendo na porta 8000.