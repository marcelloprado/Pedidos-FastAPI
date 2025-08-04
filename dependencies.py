from fastapi import Depends, HTTPException
from main import SECRET_KEY, ALGORITHM, oauth2_scheme
from models import db, Usuario
from sqlalchemy.orm import sessionmaker, Session
from jose import jwt, JWTError


def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()
        

def verificar_token(token: str = Depends(oauth2_scheme), session: Session = Depends(pegar_sessao)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM) # type: ignore
        id_usuario = int(dic_info.get("sub")) # type: ignore
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado, Verifique a validade do token")
    #^ Verifica se o token é válido
    #^ Extrair o ID do usuário do token
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()  # type: ignore
    if not usuario:
        raise HTTPException(status_code=401, detail="Acesso Inválido")
    return usuario