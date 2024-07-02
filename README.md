# API de Saque de Caixa Eletrônico

## Visão Geral

Esta API simula o funcionamento de um caixa eletrônico. Ela recebe um valor de saque desejado e retorna a quantidade de cédulas de cada valor necessárias para compor esse saque, utilizando a menor quantidade de cédulas possível.

## Requisitos

- Python 3.x
- Flask

## Estrutura do Projeto
```
api-saque/
├── código/
│   ├── .idea/
│   ├── app/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_routes.py
│   ├── app.py
│   ├── main.py
│   └── requirements.txt
├── README.md
```

## Executando o Projeto

#### Instale as Dependências:

Com o ambiente virtual ativado, instale as dependências listadas no requirements.txt:

```
pip install -r código/requirements.txt
```
ou 
```
pip install flask
```
### Execute a Aplicação:

No terminal, vá para o diretório:
```
cd código
python app.py
```
Se tudo estiver correto, você verá a mensagem ```Running on http://127.0.0.1:5000/.```

### Teste a API:

Use o curl ou um cliente REST como Postman para fazer uma requisição POST:

```
curl -X POST -H "Content-Type: application/json" -d '{"valor": 524}' http://127.0.0.1:5000/api/saque
```

Você deve ver a resposta JSON com a distribuição de cédulas.
### Rodar os Testes:

Para executar os testes, no terminal, vá para o diretório código e execute:
```
python -m unittest discover -s tests
```
### Usando o Postman
Para testar a API usando o Postman:

Abra o Postman.
Crie uma nova requisição.

Selecione o método POST.

Insira a URL ```http://localhost:5000/api/saque.```

Vá para a aba Body, selecione raw e JSON.

Insira o seguinte JSON no corpo da requisição:


```
{
    "valor" : 524
}
```
Resposta esperada:
```
{
    "2": 2,
    "5": 0,
    "10": 0,
    "20": 1,
    "50": 0,
    "100": 5
}
```
Clique em Send.
Você deve ver a resposta JSON com a distribuição de cédulas.
