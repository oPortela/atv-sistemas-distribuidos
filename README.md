## Atividade Sistemas Distribuidos


API simples para validação de requisição de Login

## Tecnologias Usadas
* Python
* FastAPI
* Uvicorn

## Passo a Passo

1. Validar se o python está instalado em sua máquina
2. Ative o ambiente virtual
    ```bash
    venv\Scripts\activate
    ```
3. Intale as bibliotecas do Python
    ```bash
    pip install fastApi "uvicorn[standard]" 
    ```
4. Inicie o Uvicorn
    ```bash
    uvicorn main:app --reload
    ```