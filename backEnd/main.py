from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UsuarioLogin(BaseModel):
    user: str
    password: str

@app.get("/")
def rota_inicial():
    return {"message": "API rodando!"}

@app.post("/login")
def login(data: UsuarioLogin):
    user_pred = "Admin"
    password_pred = "SuperSenha@123"

    if data.user == user_pred and data.password == password_pred:
        return {"message": "Login bem-sucedido!",
                "status": "sucess",
                "code": 200}
    else: 
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")