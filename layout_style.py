import PySimpleGUI as sg
import os

# Obtenha o diretório atual do script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Especifique o diretório relativo ao diretório atual
image_directory = os.path.join(script_dir, 'public', 'image', 'home.png')



sg.theme('Dark Grey 13')
sg.theme_background_color("#161B2E")
sg.theme_button_color(('white', '#3F2F63'))
sg.theme_text_color('white')
sg.theme_text_element_background_color('#161B2E')





# Crie uma cor personalizada com base nos valores RGB










def set_layout(select):

    layout_principal_direita = [
                [sg.Text('Mygym', font=("Helvetica", 25), size=(0,2))],
                [sg.Button('Cadastre um novo usuario',  size=(30,0))],
                [sg.Button('Cadastre um novo treinador', size=(30,0))],
                [sg.Button('Puxar tabela', size=(30,0))],
                [sg.Button('Buscar nos usuario', size=(30,0))],
                [sg.Button('Buscar nos treinadores', size=(30,0))],
                [sg.Button('Atualizar usuario', size=(30,0))],
                [sg.Button('Atualizar treinador', size=(30,0))],
                [sg.Button('Excluir', size=(30,0))],
                [sg.Button('Sair', size=(30,0))] 

    ]

    layout_principal_esquerda = [
        [sg.Image(filename=image_directory, background_color = "#111525" )]
    ]
        
    layout_principal = [        
                [sg.Column(layout_principal_direita), sg.Column(layout_principal_esquerda, background_color='#111525',)],
                
    ]


    layout_login = [        
                [sg.Text('')],
                [sg.Text('', size=(60,10)), sg.Text('Login', size=(30,10), font=("Helvetica", 25))],
                [sg.Text('')],
                [sg.Text('Entre na sua conta')],
                [sg.Text('')],
                [sg.Text('Usuario' , size=(5,0)), sg.Input(key="usuario", size=(20,0))],
                [sg.Text('Senha' , size=(5,0)), sg.Input(key="senha", size=(20,0))],
                [sg.Text('')],

                [sg.Button('Enviar')] 
    ]


    layout_cadastro_usuarios = [
        

                [sg.Text('')],
                [sg.Text('', size=(55,10)), sg.Text('Mygym', size=(30,5), font=("Helvetica", 25))],
                [sg.Text('')],
                [sg.Text('Cadastre um novo usuario')],
                [sg.Text('')],
                [sg.Text('Nome de Usuario' , size=(8,0)), sg.Input(key="Usuario", size=(20,0))],
                [sg.Text('Idade' , size=(8,0)), sg.Input(key="Idade", size=(20,0))],
                [sg.Text('Sexo' , size=(8,0)), sg.Input(key="Sexo", size=(20,0))],
                [sg.Text('Endereço' , size=(8,0)), sg.Input(key="Endereço", size=(20,0))],
                [sg.Text('Telefone' , size=(8,0)), sg.Input(key="Telefone", size=(20,0))],
                [sg.Text('')],

                [sg.Button('Enviar')] 
    ]


    layout_cadastro_treinadores = [
        

                [sg.Text('')],
                [sg.Text('', size=(55,10)), sg.Text('Mygym', size=(30,5), font=("Helvetica", 25))],
                [sg.Text('Cadastre um novo treinador')],
                [sg.Text('')],
                [sg.Text('Nome do treinador' , size=(9,0)), sg.Input(key="Treinador", size=(20,0))],
                [sg.Text('Especialização' , size=(9,0)), sg.Input(key="Especialização", size=(20,0))],
                [sg.Text('Experiência' , size=(9,0)), sg.Input(key="Experiência", size=(20,0))],
                [sg.Text('Número de registro' , size=(9,0)), sg.Input(key="NR", size=(20,0))],
                [sg.Text('')],

                [sg.Button('Enviar')] 
    ]


    layout_puxar_tabela = [
        

                [sg.Text('')],
                [sg.Text('', size=(55,10)), sg.Text('Mygym', size=(30,5), font=("Helvetica", 25))],
                [sg.Text('Escolha a tabela para puxar os dados')],
                [sg.Text('')],
                [sg.Text('Tabela' , size=(9,0)), sg.Combo(['clientes','treinadores'], key='Tabela')],
                [sg.Multiline(size=(80,10), key='out put')],
                [sg.Text('')],

                [sg.Button('Enviar')] 
    ]


    layout_Buscar_usuarios = [
        

                [sg.Text('')],
                [sg.Text('', size=(55,10)), sg.Text('Mygym', size=(30,5), font=("Helvetica", 25))],
                [sg.Text('Buscar dados do usuario')],
                [sg.Text('')],
                [sg.Text('Nome do usuario' , size=(9,0)), sg.Input(key="Usuario", size=(20,0))],
                [sg.Text('')],
                [sg.Text('ID: ', key="ID")],
                [sg.Text('Idade: ', key="Idade")],
                [sg.Text('Sexo: ', key="Sexo")],
                [sg.Text('Endereço: ', key="Endereço")],
                [sg.Text('Telefone: ', key="Telefone")],
                [sg.Text('')],

                [sg.Button('Enviar')] 
    ]


    layout_Buscar_treinadores = [
        

                [sg.Text('')],
                [sg.Text('', size=(55,10)), sg.Text('Mygym', size=(30,5), font=("Helvetica", 25))],
                [sg.Text('Buscar dados do treinador')],
                [sg.Text('')],
                [sg.Text('Nome do treinador' , size=(9,0)), sg.Input(key="Treinador", size=(20,0))],
                [sg.Text('')],
                [sg.Text('ID: ', key="ID")],
                [sg.Text('Especialização: ', key="Especialização")],
                [sg.Text('Experiência: ', key = "Experiência")],
                [sg.Text('Número de registro: ', key= "Número de registro")],
                [sg.Text('')],

                [sg.Button('Enviar')] 
    ]


    layout_atualizar_usuario = [
        

                [sg.Text('')],
                [sg.Text('', size=(55,10)), sg.Text('Mygym', size=(30,5), font=("Helvetica", 25))],
                [sg.Text('')],
                [sg.Text('Atualize um usuario')],
                [sg.Text('')],
                [sg.Text('Nome de Usuario' , size=(8,0)), sg.Input(key="Usuario", size=(20,0))],
                [sg.Text('Idade' , size=(8,0)), sg.Input(key="Idade", size=(20,0))],
                [sg.Text('Sexo' , size=(8,0)), sg.Input(key="Sexo", size=(20,0))],
                [sg.Text('Endereço' , size=(8,0)), sg.Input(key="Endereço", size=(20,0))],
                [sg.Text('Telefone' , size=(8,0)), sg.Input(key="Telefone", size=(20,0))],
                [sg.Text('')],

                [sg.Button('Enviar')] 
    ]


    layout_atualizar_treinadores = [
            

                [sg.Text('')],
                [sg.Text('', size=(55,10)), sg.Text('Mygym', size=(30,5), font=("Helvetica", 25))],
                [sg.Text('Atualize um treinador')],
                [sg.Text('')],
                [sg.Text('Nome do treinador' , size=(9,0)), sg.Input(key="Treinador", size=(20,0))],
                [sg.Text('Especialização' , size=(9,0)), sg.Input(key="Especialização", size=(20,0))],
                [sg.Text('Experiência' , size=(9,0)), sg.Input(key="Experiência", size=(20,0))],
                [sg.Text('Número de registro' , size=(9,0)), sg.Input(key="NR", size=(20,0))],
                [sg.Text('')],

                [sg.Button('Enviar')] 
    ]


    layout_excluir = [
            

                [sg.Text('')],
                [sg.Text('', size=(55,10)), sg.Text('Mygym', size=(30,5), font=("Helvetica", 25))],
                [sg.Text('Exclua um usuario ou treinador pelo seu ID')],
                [sg.Text('')],
                [sg.Text('Entidade' , size=(9,0)), sg.Combo(['clientes','treinadores'], key='Entidade')],
                [sg.Text('ID' , size=(9,0)), sg.Input(key="ID", size=(20,0))],
                [sg.Text('')],

                [sg.Button('Enviar')] 
    ]


    return eval(select)
    




    
    