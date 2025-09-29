from pydantic import BaseModel
from typing import Union, Optional, List
from model.tutor import Tutor


# -------------------------------------------------------------------------
# 1. Schema para Inserção (POST)
# -------------------------------------------------------------------------
class TutorSchema(BaseModel):
    nome: str 
    telefone: str


# -------------------------------------------------------------------------
# 2. Schema para Busca por Nome (GET por parâmetro)
# -------------------------------------------------------------------------
class TutorBuscaSchema(BaseModel):
    nome: str = "Maria Oliveira"


# -------------------------------------------------------------------------
# 3. Schema para Visualização (Retorno de um único Tutor)
# -------------------------------------------------------------------------
class TutorViewSchema(BaseModel):
    """ Define como um tutor será retornado, incluindo o ID e a data de criação.
        Aqui estamos incluindo a contagem de pets, similar à contagem de comentários no seu produto.
    """
    id: int = 1
    nome: str = "Ana Souza"
    telefone: Optional[str] = "(11) 99887-7665"
    data_insercao: str
    total_pets: int = 2


# -------------------------------------------------------------------------
# 4. Schema para Listagem (Retorno de múltiplos Tutores)
# -------------------------------------------------------------------------
class ListagemTutoresSchema(BaseModel):
    """ Define como uma listagem de tutores será retornada.
    """
    tutores: List[TutorViewSchema]


# -------------------------------------------------------------------------
# 5. Schema para Deleção (Retorno após DELETE)
# -------------------------------------------------------------------------
class TutorDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção.
    """
    message: str = "Tutor removido com sucesso!"
    nome: str = "Tutor a ser removido"

    
# -------------------------------------------------------------------------
# 6. Função de Serialização/Aprensentação (Model -> Schema)
# -------------------------------------------------------------------------
def apresenta_tutor(tutor: Tutor):
    """ Retorna uma representação do tutor seguindo o schema definido em
        TutorViewSchema.
    """
    return {
        "id": tutor.id,
        "nome": tutor.nome,
        "telefone": tutor.telefone,
        "data_insercao": tutor.data_insercao.strftime("%d/%m/%Y %H:%M:%S"),
        "total_pets": len(tutor.pets)
    }

def apresenta_tutores(tutores: List[Tutor]):
    """ Retorna uma representação da listagem de tutores.
    """
    result = []
    for tutor in tutores:
        result.append(apresenta_tutor(tutor))

    return {"tutores": result}