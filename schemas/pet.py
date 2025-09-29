from pydantic import BaseModel
from typing import Union, Optional, List
from model.pet import Pet, EspeciePet # Importa Pet e o Enum EspeciePet

# -------------------------------------------------------------------------
# 1. Schema para INSERÇÃO (POST)
# -------------------------------------------------------------------------
class PetSchema(BaseModel):
    """ Define como um novo pet a ser inserido deve ser representado.
        Recebe o ID do tutor selecionado no frontend.
    """
    nome: str = "Max"
    especie: str = "CACHORRO" 
    raca: str = "Poodle"
    tutor_id: int = 1

# -------------------------------------------------------------------------
# 2. Schemas de BUSCA (GET/DELETE Query)
# -------------------------------------------------------------------------
class PetBuscaIdSchema(BaseModel):
    """ Define o schema de busca por ID (usado em GET ou DELETE).
    """
    id: int = 1

# -------------------------------------------------------------------------
# 3. Schemas de VISUALIZAÇÃO (Retorno - GET/POST)
# -------------------------------------------------------------------------
class PetViewSchema(BaseModel):
    """ Define como um pet será retornado, incluindo o nome do tutor.
    """
    id: int = 1
    nome: str = "Tobi"
    especie: str = "Felina"
    raca: str = "Siamês"
    tutor_nome: str = "João da Silva"
    tutor_telefone: str = "12987654321",
    data_insercao: str

class ListagemPetsSchema(BaseModel):
    """ Define como uma listagem de pets será retornada.
    """
    pets: List[PetViewSchema]

# -------------------------------------------------------------------------
# 4. Função de Serialização/Aprensentação (Model -> Schema)
# -------------------------------------------------------------------------
def apresenta_pet(pet: Pet):
    """ Retorna uma representação do pet seguindo o schema definido em
        PetViewSchema, incluindo o nome do tutor associado.
    """
    return {
        "id": pet.id,
        "nome": pet.nome,
        "especie": pet.especie.value if isinstance(pet.especie, EspeciePet) else pet.especie,
        "raca": pet.raca,
        "tutor_nome": pet.tutor.nome,
        "tutor_telefone": pet.tutor.telefone,
        "data_insercao": pet.data_insercao.strftime("%d/%m/%Y %H:%M:%S")
    }


def apresenta_pets(pets: List[Pet]):
    """ Retorna uma representação da listagem de pets.
    """
    result = []
    for pet in pets:
        result.append(apresenta_pet(pet))

    return {"pets": result}