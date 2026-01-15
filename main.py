#pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# Passo 1: Entrar no sistema da empresa
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')


pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)


# Passo 2: Fazer Login
pyautogui.click(x=771, y=376)
pyautogui.write('seuemailfavorito@gmail.com')
pyautogui.press('tab')
pyautogui.write('suasenhamuitodificil')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2.5)


# Passo 3: Abrir a base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')
for linha in tabela.index: #linha da tabela
    # Passo 4: Cadastrar 1 produto
    #codigo
    pyautogui.click(x=730, y=261)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    pyautogui.press('tab')

    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')

    #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    #preco
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')

    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')

    #voltar para o inicio da tela
    pyautogui.scroll(5000)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos