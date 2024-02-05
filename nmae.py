import random

nomes_brasileiros = list(set([
    "Ana", "Carlos", "Fernanda", "Luiz", "Mariana", 
    "Ricardo", "Camila", "Lucas", "Isabela", "Pedro",
    "Gustavo", "Larissa", "Roberto", "Amanda", "Diego",
    "Leticia", "Bruno", "Juliana", "Alexandre", "Patricia",
    "Gabriel", "Beatriz", "Daniel", "Carolina", "Vinicius",
    "Tatiane", "Felipe", "Leticia", "Rodrigo", "Sabrina",
    "Julio", "Vanessa", "Eduardo", "Thais", "Rafael",
    "Aline", "Fernando", "Natalia", "Leonardo", "Jessica",
    "Renato", "Bianca", "Joao", "Renata", "Henrique",
    "Laura", "Cesar", "Helena", "Adriano", "Monica"
]))

sobrenomes_brasileiros = list(set([
    "Silva", "Oliveira", "Santos", "Souza", "Pereira", 
    "Lima", "Ferreira", "Almeida", "Costa", "Rodrigues",
    "Martins", "Rocha", "Gomes", "Carvalho", "Lopes",
    "Pinto", "Cavalcanti", "Mendes", "Nunes", "Farias",
    "Araujo", "Cardoso", "Goncalves", "Barbosa", "Melo",
    "Castro", "Borges", "Fonseca", "Dias", "Teixeira",
    "Machado", "Correia", "Alves", "Fogaça", "Marques",
    "Pires", "Ramos", "Brito", "Siqueira", "Cordeiro",
    "Lins", "Moreira", "Cruz", "Cunha", "Cavalcante",
    "Sousa", "Lacerda", "Andrade", "Sales", "Nascimento",
    "Dantas", "Lima", "Aragão", "Moraes", "Vasconcelos",
    "Pacheco", "Vieira", "Guedes", "Monteiro", "Xavier",
    "Coutinho", "Figueiredo", "Lemos", "Magalhães", "Peixoto",
    "Diniz", "Leal", "Pessoa", "Ribeiro", "Albuquerque",
    "Guimarães", "Fernandes", "Alves", "Rangel", "Barros"
]))

def gerar_nome_completo():
    nome = random.choice(nomes_brasileiros)
    sobrenome1 = random.choice(sobrenomes_brasileiros)
    sobrenome2 = random.choice(sobrenomes_brasileiros)
    
    nome_completo = f"{nome} {sobrenome1} {sobrenome2}"
    return nome_completo

