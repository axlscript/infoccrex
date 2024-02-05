from bin import escolherbin
import random, time, os
from nmae import *
from cpsystem import *
from checker import checkerTrue
from banner_init import *
from aprovacao import *
from main import*
from bannerinfocc import bannerInfoCC



def completarcc():
    bin = escolherbin()
    matriz = random.randint(1345222340, 9132344962)
    ccMatriz = (str(bin) + str(matriz))
    os.system('clear')

    cvv = random.randint(100, 900)
    # DATA DA CC
    data_dia = random.randint(10, 30)
    data_ano = random.randint(2025, 2030)

    # CC FORMADA
    if bin == 557675:
        os.system('clear')
        print(f"{Vermelho}[!]- {Reset}Buscando CC na base de dados{Vermelho}...{Reset}")
        time.sleep(5)
        os.system('clear')
        print(bannerInfoCC)
        print("="*30)
        print("Nome:", gerar_nome_completo())
        exibircpf()
        print(f'''CC: {ccMatriz}
Data: {data_dia}|{data_ano}
CVV: {cvv}
Nível: Platinum
Status: {checkerTrue()}''')
        print("="*30)
    

    elif bin == 511477:
        print(f"{Vermelho}[!]- {Reset}Buscando CC na base de dados{Vermelho}...{Reset}")
        time.sleep(8)
        os.system('clear')
        print(bannerInfoCC)
        print("="*30)
        print("Nome:", gerar_nome_completo())
        exibircpf()
        print(f'''CC: {ccMatriz}
Data: {data_dia}|{data_ano}
CVV: {cvv}
Nível: Standart
Bandeira: Mastercard
Status: {checkerTrue()}''')
        print("="*30)
    elif bin == 549630:
        print(f"{Vermelho}[!]- {Reset}Buscando CC na base de dados{Vermelho}...{Reset}")
        time.sleep(8)
        os.system('clear')
        print(bannerInfoCC)
        print("="*30)
        print("Nome:", gerar_nome_completo())
        exibircpf()
        print(f'''CC: {ccMatriz}
Data: {data_dia}|{data_ano}
CVV: {cvv}
Nível: Prepaid
Bandeira: Mastercard
Status: {checkerTrue()}''')
        print("="*30)


    elif bin == 548049:
        print(f"{Vermelho}[!]- {Reset}Buscando CC na base de dados{Vermelho}...{Reset}")
        time.sleep(9)
        os.system('clear')
        print(bannerInfoCC)
        print("="*30)
        print("Nome:", gerar_nome_completo())
        exibircpf()
        print(f'''CC: {ccMatriz}
Data: {data_dia}|{data_ano}
CVV: {cvv}
Nível: World Elite
Bandeira: Mastercard''')


    elif bin == 457601:
        print(f"{Vermelho}[!]- {Reset}Buscando CC na base de dados{Vermelho}...{Reset}")
        time.sleep(12)
        os.system('clear')
        print (bannerInfoCC)
        print("="*30)
        print("Nome:", gerar_nome_completo())
        exibircpf()
        print(f'''CC: {ccMatriz}
Data: {data_dia}|{data_ano}
CVV: {cvv}
Nível: Business
Bandeira: Visa
Status: {checkerTrue()} ''')
        print("="*30)

    elif bin == 417401:

        print(f"{Vermelho}[!]- {Reset}Buscando CC na base de dados{Vermelho}...{Reset}")
        time.sleep(4)
        os.system('clear')
        print (bannerInfoCC)
        print("="*30)
        print("Nome:", gerar_nome_completo())
        exibircpf()
        print(f'''CC: {ccMatriz}
Data: {data_dia}|{data_ano}
CVV: {cvv}
Nível: Classic
Bandeira: Visa
Status: {checkerTrue()} ''')
        print("="*30)


        
    else:
        print(f"Bin não reconhecida: {bin}")



