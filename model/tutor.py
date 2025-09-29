from sqlalchemy import Column, String, Integer, DateTime, Float 
from sqlalchemy.orm import relationship
from typing import Union, Optional, List

from datetime import datetime
from model import Base

class Tutor(Base):
    __tablename__ = 'tutor'

    id = Column("pk_tutor", Integer, primary_key=True)
    nome = Column(String(140), unique=True, nullable=False)
    telefone = Column(String(20))

    data_insercao = Column(DateTime, default=datetime.now(), nullable=True)

    # Relacionamento: um tutor para muitos pets
    pets = relationship("Pet", back_populates="tutor")

    def __init__(self, nome: str, telefone: str,
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria um Tutor

        Arguments:
            nome: nome do tutor.
            telefone: telefone de contato do tutor.
        """
        self.nome = nome
        self.telefone = telefone

        if data_insercao:
            self.data_insercao = data_insercao