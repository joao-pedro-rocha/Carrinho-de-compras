import PySimpleGUI as sg
import os

carrinho = []

# Criar janelas e estilos
def janela_menu():
    sg.theme('Reddit')
    
    layout = [
        [sg.B('Adicionar item'), sg.B('Ver carrinho')],
        [sg.B('Editar', size = (12, 0)), sg.B('Excluir', size = (10, 0))]
    ]
    
    return sg.Window('Menu', layout = layout, finalize = True)

def janela_adicionar():
    sg.theme('Reddit')
    
    layout = [
        [sg.Text('Item')],
        [sg.Input(size = (20, 0), key = '-adc_item-')],
        [sg.B('Cancelar'), sg.B('Confirmar')]
    ]
    
    return sg.Window('Adicionar item', layout = layout, finalize = True)

def janela_visualizar():
    sg.theme('Reddit')
    
    layout = [
        [sg.Text('Seu carrinho:')],
        [sg.Output(size  = (30, 10))],
        [sg.B('Voltar')]
    ]
    
    return sg.Window('Ver carrinho', layout = layout, finalize = True)

def janela_editar():
    sg.theme('Reddit')
    
    layout = [
        [sg.Text('Número do item \na ser removido'), sg.Input(size = (20, 0), key = '-tirar-')],
        [sg.Text('Item de troca', size = (14, 0)), sg.Input(size = (20, 0), key = '-trocar-')],
        [sg.B('Cancelar'), sg.B('Confirmar')]
    ]
    return sg.Window('Editar itens', layout = layout, finalize = True)

def janela_excluir():
    sg.theme('Reddit')
    
    layout = [
        [sg.Text('Número do item')],
        [sg.Input(size = (20, 0), key = '-exc_item-')],
        [sg.B('Cancelar'), sg.B('Confirmar')]
    ]
    
    return sg.Window('Excluir', layout = layout, finalize = True)
    
# Criar janelas iniciais
janela1, janela2, janela3, janela4, janela5 = janela_menu(), None, None, None, None

# Criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    
    # Quando a janela for fechada
    if event == sg.WIN_CLOSED:
        break
    
    # Quando quisermos ir para a proxima janela
    # Menu
    if window == janela1 and event == 'Adicionar item':
        janela1.hide()
        janela2 = janela_adicionar()
        
    # Eventos da janela 2 
    if window == janela2 and event == 'Confirmar':
        carrinho.append(values['-adc_item-'])
        
        sg.popup(f'*{values["-adc_item-"].upper()}* foi adicionado ao seu carrinho!')
        
    if window == janela2 and event == 'Cancelar':
        janela2.hide()
        janela1.un_hide()
        janela2 = None
    # Menu 
    if window == janela1 and event == 'Ver carrinho':
        janela1.hide()
        janela3 = janela_visualizar()
    
    # Eventos da janela 3    
        for c, i in enumerate(carrinho):
            print(c, '-', i.capitalize())
        
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()
        janela3 = None
        
    # Menu
    if window == janela1 and event == 'Editar':
        janela1.hide()
        janela4 = janela_editar()
        
    # Eventos da janela 4
    if window == janela4 and event == 'Cancelar':
        janela4.hide()
        janela1.un_hide()
        janela4 = None
        
    if window == janela4 and event == 'Confirmar':
        tirar = int(values['-tirar-'])
        carrinho[tirar] = values['-trocar-']
        
        sg.popup(f'Troca realizada com sucesso!')
    
    # Menu
    if window == janela1 and event == 'Excluir':
        janela1.hide()
        janela5 = janela_excluir()
        
    # Eventos da janela 5
    if window == janela5 and event == 'Cancelar':
        janela5.hide()
        janela1.un_hide()
        janela5 = None
        
    if window == janela5 and event == 'Confirmar':
        exc = int(values['-exc_item-'])
        carrinho.pop(exc)
        
        sg.popup('Item excluído com sucesso!')
        
window.close()
