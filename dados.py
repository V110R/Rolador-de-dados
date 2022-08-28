from PySimpleGUI import PySimpleGUI as sg
import time
import random
#Layout


sg.theme('Black')
dados = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd10%', 'd100']
layout = [
    [sg.Text('Dados'), sg.Combo(dados, key= str('dado_escolhido'))],
    [sg.Text('quantos dados deseja rolar'), sg.Input(key='ndados', size=('2'))],
    [sg.Button('rolar')],
    [sg.Output(size=(30, 2))]
]


#janela
janela = sg.Window('rolador de dados', layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    valores['ndados'] = int(valores['ndados'])
    valores['ndados'] = valores['ndados'] + 1
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'rolar':
        if valores['dado_escolhido'] == '':
            print('escolha um dado')
        if valores['dado_escolhido'] == 'd4' or 'd6' or 'd8' or 'd10' or 'd12' or 'd20' or 'd10%' or 'd100':



            if valores['dado_escolhido'] == 'd4':
                counter = 0
                valor = 0
                while counter != valores['ndados']:
                    valor = random.randint(1, 4) + valor
                    if counter != valores['ndados']:
                        counter = counter + 1
                    if counter == valores['ndados'] - 1:
                        print(f'\n{valor}')




            if valores['dado_escolhido'] == 'd6':
                counter = 0
                valor = 0
                while counter != valores['ndados']:
                    valor = random.randint(1, 6) + valor
                    if counter != valores['ndados']:
                        counter = counter + 1
                    if counter == valores['ndados'] - 1:
                        print(f'\n{valor}')




            if valores['dado_escolhido'] == 'd8':
                counter = 0
                valor = 0
                while counter != valores['ndados']:
                    valor = random.randint(1, 8) + valor
                    if counter != valores['ndados']:
                        counter = counter + 1
                    if counter == valores['ndados'] - 1:
                        print(f'\n{valor}')



            if valores['dado_escolhido'] == 'd10':
                counter = 0
                valor = 0
                while counter != valores['ndados']:
                    valor = random.randint(1, 10) + valor
                    if counter != valores['ndados']:
                        counter = counter + 1
                    if counter == valores['ndados'] - 1:
                        print(f'\n{valor}')




            if valores['dado_escolhido'] == 'd12':
                counter = 0
                valor = 0
                while counter != valores['ndados']:
                    valor = random.randint(1, 12) + valor
                    if counter != valores['ndados']:
                        counter = counter + 1
                    if counter == valores['ndados'] - 1:
                        print(f'\n{valor}')




            if valores['dado_escolhido'] == 'd20':
                counter = 0
                valor = 0
                while counter != valores['ndados']:
                    valor = random.randint(1, 20) + valor
                    if counter != valores['ndados']:
                        counter = counter + 1
                    if counter == valores['ndados'] - 1:
                        print(f'\n{valor}')






            if valores['dado_escolhido'] == 'd10%':
                counter = 0
                valor = 0
                while counter != valores['ndados']:
                    valor = random.randrange(00, 100, 10) + valor
                    if counter != valores['ndados']:
                        counter = counter + 1
                    if counter == valores['ndados'] - 1:
                        print(f'\n{valor}')




            if valores['dado_escolhido'] == 'd100':
                counter = 0
                valor = 0
                while counter != valores['ndados']:
                    valor = random.randrange(00, 100, 10) + valor
                    valor = random.randint(1, 10) + valor
                    if counter != valores['ndados']:
                        counter = counter + 1
                    if counter == valores['ndados'] - 1:
                        print(f'\n{valor}')

