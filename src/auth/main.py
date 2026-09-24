from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from datetime import datetime, timedelta

app = FastAPI(title="Auth Service")
SECRET_KEY = "my_super_secret_key"
ALGORITHM = "HS256"

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == "admin" and form_data.password == "admin":
        payload = {"sub": form_data.username, "exp": datetime.utcnow() + timedelta(hours=24)}
        token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Incorrect username or password")
