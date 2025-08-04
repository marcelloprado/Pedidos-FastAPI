from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
# from sqlalchemy_utils.types import ChoiceType

#^ Cria a conexão do seu banco
db = create_engine("sqlite:///banco.db")

#^ Cria a base do banco de dados
Base = declarative_base()

#^ Cria as classes/Tabelas do Banco
#* Usuario
class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)
    
    def __init__(self, nome, email, senha, ativo=True, admin=False):
           self.nome = nome
           self.email = email
           self.senha = senha
           self.ativo = ativo
           self.admin = admin


#* Pedido
class Pedido(Base):
    __tablename__ = "pedidos"
    
    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) #Pendente, Cancelado, Finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id"))
    preco = Column("preco", Float)
    itens = relationship("ItemPedido", cascade= "all, delete")
    
    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.status = status
        self.usuario = usuario
        self.preco = preco
        
    def calcular_preco(self):
        #^ Percorrer todos os itens do pedido
        #^ somar todos os precos de todos os itens do pedido
        #^ editar no campo "preco" o valor total do pedido
        #~ listcomprehension
        self.preco = sum(item.preco_unitario * item.quantidade for item in self.itens)
            
  

#* itensPedido
class ItemPedido(Base):
    __tablename__ = "itens_pedido"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id"))
    
    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

#^ Executa a criação dos MetaDados do seu banco (Cria efetivamente o banco de dados)

#^ criar a migração: alembic revision --autogenerate -m "nome da migração"
#^Executar a migração: alembic upgrade head