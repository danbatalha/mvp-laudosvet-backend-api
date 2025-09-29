from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union, Optional, List
from model import Base

from enum import Enum as PyEnum
class EspeciePet(PyEnum):
    CACHORRO = "Cachorro"
    GATO = "Gato"

class Pet(Base):
    __tablename__ = 'pet'

    id = Column(Integer, primary_key=True)
    nome = Column(String(140), nullable=False)
    especie = Column(Enum(EspeciePet, name='especies_pet'), nullable=False)
    raca = Column(String(100), nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())

    tutor_id = Column(Integer, ForeignKey("tutor.pk_tutor"), nullable=False)

    tutor = relationship("Tutor", back_populates="pets") 

    def __init__(self, nome: str, especie: EspeciePet, tutor_id: int, raca: Union[str, None] = None,
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria um Pet

        Arguments:
            nome: nome do pet.
            especie: cachorro ou gato.
            tutor_id: id do Tutor associado (chave estrangeira).
            raca: raça do pet.
            data_insercao: data de quando o pet foi inserido à base.
        """
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.tutor_id = tutor_id

        if data_insercao:
            self.data_insercao = data_insercao