import PySimpleGUI as sg
import layout_style as est
import SQL

#import SQL

class fc:
    
    def __init__(self) -> None:
        self.sql = SQL.SQL()
        print(self.sql.mycursor)

    #main window flow 
    def function_main(self, window):
        contr = True
        window.event, window.values = window.janela.Read()
        



        #if the user pressed a button
        if window.event == 'Cadastre um novo usuario':
            self.open_new_window(window, 'layout_cadastro_usuarios', 'fc.function_cadastro_usuarios')

        if window.event == 'Cadastre um novo treinador':
            self.open_new_window(window, 'layout_cadastro_treinadores', 'fc.function_cadastro_treinadores')

        if window.event == 'Puxar tabela':
            self.open_new_window(window, 'layout_puxar_tabela', 'fc.function_puxar_tabela')
        
        if window.event == 'Buscar nos usuario':
            self.open_new_window(window, 'layout_Buscar_usuarios', 'fc.function_Buscar_usuarios')

        if window.event == 'Buscar nos treinadores':
            self.open_new_window(window, 'layout_Buscar_treinadores', 'fc.function_Buscar_treinadores')
        
        if window.event == 'Atualizar usuario':
            self.open_new_window(window, 'layout_atualizar_usuario', 'fc.function_atualizar_usuario')
    
        if window.event == 'Atualizar treinador':
            self.open_new_window(window, 'layout_atualizar_treinadores', 'fc.function_atualizar_treinadores')
        
        
        
        if window.event == 'Excluir':
            self.open_new_window(window, 'layout_excluir', 'fc.function_excluir')
        
        if window.event == 'Sair':
            contr = False


        if window.event == sg.WIN_CLOSED:
            self.sql.close()
            contr = False

        
        return contr


    #flow from other windows
    def function_cadastro_usuarios(self , window, event, values):
        self.sql.cadastrar_usuario(values['Usuario'], values['Idade'], values['Sexo'], values['Endereço'], values['Telefone'])
        
    def function_cadastro_treinadores(self, window, event, values):
        self.sql.cadastrar_treinadores(values['Treinador'], values['Especialização'], values['Experiência'], values['NR'])
  
    def function_puxar_tabela(self, window, event, values):
        text = self.sql.buscar_tabela(values['Tabela'])
        window.new_window['out put'].update(text)

    def function_Buscar_usuarios(self, window, event, values):
        user = self.sql.buscar_usuarios(values['Usuario'], 'clientes')

        if str(user) == 'None':
            window.new_window['ID'].update('ID: None')
            window.new_window['Idade'].update('Idade: None')
            window.new_window['Sexo'].update('Sexo: None')
            window.new_window['Endereço'].update('Endereço: None')
            window.new_window['Telefone'].update('Telefone: None')
            return ''
        else:
            window.new_window['ID'].update('ID: ' + str(user[0]))
            window.new_window['Idade'].update('Idade: ' + str(user[2]))
            window.new_window['Sexo'].update('Sexo: ' + user[3])
            window.new_window['Endereço'].update('Endereço: ' + user[4])
            window.new_window['Telefone'].update('Telefone: ' + str(user[5]))

    def function_Buscar_treinadores(self, window, event, values):
        user = self.sql.buscar_usuarios(values['Treinador'], 'treinadores')

        if str(user) == 'None':
            window.new_window['ID'].update('ID: None')
            window.new_window['Especialização'].update('Especialização: None')
            window.new_window['Experiência'].update('Experiência: None')
            window.new_window['Número de registro'].update('Número de registro: None')
            return ''
        else:
            window.new_window['ID'].update('ID: ' + str(user[0]))
            window.new_window['Especialização'].update('Especialização: ' + user[2])
            window.new_window['Experiência'].update('Experiência: ' + str(user[3]))
            window.new_window['Número de registro'].update('Número de registro: ' + str(user[4]))
            
    def function_atualizar_usuario(self, window, event, values):
        self.sql.update_usuario(values['Usuario'], values['Idade'], values['Sexo'], values['Endereço'], values['Telefone'])
    
    def function_atualizar_treinadores(self, window, event, values):
        self.sql.update_treinadores(values['Treinador'], values['Especialização'], values['Experiência'], values['NR'])

    def function_excluir(self, window, event, values):
        self.sql.delete_field( values['Entidade'], values['ID'])
        
    def open_new_window(self, window, layout, function):
        window.new_window = sg.Window("New window", est.set_layout(layout))

        while True:
            event, values = window.new_window.read()

            if event == sg.WIN_CLOSED:
                window.new_window.close()
                break

            f = eval(function)
            f(self, window, event, values)

            