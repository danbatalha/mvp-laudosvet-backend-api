from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Tutor, Pet
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="LaudosVet", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
tutor_tag = Tag(name="Tutor", description="Adição e listagem de tutores")
pet_tag = Tag(name="Pet", description="Adição, listagem e remoção de pets")

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/tutor', tags=[tutor_tag],
          responses={"200": TutorViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_tutor(body: TutorSchema):
    """Adiciona um novo tutor.

    Retorna uma representação do tutor cadastrado.
    """
    tutor = Tutor(
        nome=body.nome,
        telefone=body.telefone)
    logger.debug(f"Adicionando tutor de nome: '{tutor.nome}'")
    try:
        session = Session()
        session.add(tutor)
        session.commit()
        logger.debug(f"Adicionado tutor de nome: '{tutor.nome}'")
        return apresenta_tutor(tutor), 200

    except IntegrityError as e:
        error_msg = "Tutor de mesmo nome já salvo na base."
        logger.warning(f"Erro ao adicionar tutor '{tutor.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        error_msg = f"Não foi possível salvar novo tutor: {e}"
        logger.warning(f"Erro ao adicionar tutor '{tutor.nome}'. {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/tutores', tags=[tutor_tag],
          responses={"200": ListagemTutoresSchema, "404": ErrorSchema})
def get_tutores():
    """Faz a busca por todos os tutores cadastrados.

    Retorna uma representação da listagem de tutores.
    """
    logger.debug(f"Coletando tutores")
    session = Session()
    tutores = session.query(Tutor).all()

    if not tutores:
        return {"tutores": []}, 200
    else:
        logger.debug(f"%d tutores encontrados" % len(tutores))
        return apresenta_tutores(tutores), 200

@app.post('/pet', tags=[pet_tag],
          responses={"200": PetViewSchema, "404": ErrorSchema, "400": ErrorSchema})
def add_pet(body: PetSchema):
    """Adiciona um novo pet, associando-o a um tutor existente.

    Retorna uma representação do pet cadastrado, incluindo o nome do tutor.
    """
    session = Session()
    
    tutor = session.query(Tutor).filter(Tutor.id == body.tutor_id).first()
    if not tutor:
        error_msg = "Tutor não encontrado. Não é possível cadastrar um pet sem tutor válido."
        logger.warning(f"Tentativa falha de cadastro de pet. Tutor ID: {body.tutor_id}")
        return {"mesage": error_msg}, 404
    
    pet = Pet(
        nome=body.nome,
        especie=body.especie,
        raca=body.raca,
        tutor_id=body.tutor_id
    )
    logger.debug(f"Adicionando pet de nome: '{pet.nome}' para o Tutor ID: {pet.tutor_id}")

    try:
        session.add(pet)
        session.commit()
        logger.debug(f"Adicionado pet de nome: '{pet.nome}'")
        
        return apresenta_pet(pet), 200

    except Exception as e:
        error_msg = f"Não foi possível salvar novo pet: {e}"
        logger.warning(f"Erro ao adicionar pet '{pet.nome}'. {error_msg}")
        return {"mesage": error_msg}, 400

@app.get('/pets', tags=[pet_tag],
          responses={"200": PetViewSchema, "404": ErrorSchema})
def get_pets():
    """Faz a busca por todos os pets cadastrados.

    Retorna uma representação da listagem de pets.
    """
    logger.debug(f"Coletando pets")
    session = Session()
    pets = session.query(Pet).all()

    if not pets:
        return {"pets": []}, 200
    else:
        logger.debug(f"%d pets encontrados" % len(pets))
        return apresenta_pets(pets), 200


@app.delete('/pet', tags=[pet_tag],
            responses={"200": TutorDelSchema, "404": ErrorSchema})
def del_pet(query: PetBuscaIdSchema):
    """Deleta um pet a partir do ID informado.

    Retorna uma mensagem de confirmação da remoção.
    """
    pet_id = query.id
    logger.debug(f"Deletando dados sobre pet #{pet_id}")
    session = Session()
    
    count = session.query(Pet).filter(Pet.id == pet_id).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado pet #{pet_id}")
        return {"message": "Pet removido com sucesso", "id": pet_id}
    else:
        error_msg = "Pet não encontrado na base."
        logger.warning(f"Erro ao deletar pet #'{pet_id}', {error_msg}")
        return {"mesage": error_msg}, 404