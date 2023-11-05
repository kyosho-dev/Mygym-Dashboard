import PySimpleGUI as sg


import layout_style 
import layout_function


class Tela:

   def __init__(self):
      custum_size = (400, 100)
      layout_main = layout_style.set_layout('layout_principal')
        
      #create the main program window
      self.janela = sg.Window("Manipulador de dados", layout_main)
      
   def Init(self):
      func = layout_function.fc()
        
      while True:
         #starts the program functionality
         if func.function_main(self) == False:
            break



iniciar = Tela()
iniciar.Init()


