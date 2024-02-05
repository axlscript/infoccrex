from xy import*
import time, os, random
from systemofdownaa import completarcc
from cores import Vermelho, Verde, Reset

systemX = str(input(f"Login{Vermelho}:{Reset} "))
systemY = str(input(f"Password{Vermelho}:{Reset} "))

if systemX == x():
    if systemY == y():
        print(f"{Verde}[!]- {Reset}User: {Verde}{x()} {Reset}logado com sucesso, aguarde...")
        time.sleep(5)
        os.system('clear')
        timesleep = random.randint(4,15)
        completarcc()

    else:
        print(f"{Vermelho}[!]- {Reset}Senha incorreta, tente novamente.")
else:
    print(f"{Vermelho}[!]- {Reset}Username incorreto")