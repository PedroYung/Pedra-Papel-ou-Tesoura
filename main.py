# Importação do Tkinter
import tkinter
from tkinter import *
from tkinter import ttk

# Importação do Pillow
from PIL import Image, ImageTk

# Importação do Random
import random

# global app_PC

# Cores ----------------------
co0   = '#FFFFFF'    # Branco
co1   = '#333333'    # Cinza + Escuro
co2   = '#FF9B33'    # Laranja
co3   = '#BA1030'    # Vermelho
co4   = '#008646'    # Verde
fundo = '#3b3b3b'    # Cinza


# Formatação de janela;
janela = Tk()
janela.title('Pedra, Papel ou Tesoura')
janela.geometry('329x400')
janela.resizable(False, False)
janela.iconbitmap('Imagens\Tesoura_icone.ico') # Se estiver testando o código sem ser pelo executável nos "Imagens\'imagem.png/texto.ico' adicionar antes de "Imagens" a localização, exemplo: Jogo_PedraPapelTesoura\Imagens\'imagem.png/texto.ico'
janela.configure(bg= fundo)


# Divisão da Janela;
frame_cima = Frame(janela, width= 330, height= 110, bg= co1, relie = 'raised')
frame_cima.grid(row= 0, column= 0, sticky= NW)

frame_baixo = Frame(janela, width= 330, height= 380, bg= co0, relief= 'flat')
frame_baixo.grid(row= 1, column= 0, sticky= NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Configuranção do frame_cima;

# Pontos do Jogador e barra lateral esquerda:
app_1 = Label(frame_cima, text= "Jogador", height= 1, anchor= 'center', font=('Ivy 10 bold'), bg= co1, fg= co0)
app_1.place(x= 29, y= 70)
app_1_linha = Label(frame_cima, text= "", height= 12, width= 1, anchor= 'center', font=('Ivy 10 bold'), bg= co0, fg= co0)
app_1_linha.place(x= 0, y= 0)
app_1_pontos = Label(frame_cima, text= "0", height= 1, anchor= 'center', font=('Ivy 30 bold'), bg= co1, fg= co0)
app_1_pontos.place(x= 55, y= 20)

# Divisão entre Jogador e Computador:
app_ = Label(frame_cima, text= ":", height= 1, anchor= 'center', font=('Ivy 30 bold'), bg= co1, fg= co0)
app_.place(x= 155, y= 20)

# Pontos do Computador e barra lateral direita:
app_2_pontos = Label(frame_cima, text= "0", height= 1, anchor= 'center', font=('Ivy 30 bold'), bg= co1, fg= co0)
app_2_pontos.place(x= 245, y= 20)
app_2 = Label(frame_cima, text= "PC", height= 1, anchor= 'center', font=('Ivy 10 bold'), bg= co1, fg= co0)
app_2.place(x= 275, y= 70)
app_2_linha = Label(frame_cima, text= "", height= 12, width= 1, anchor= 'center', font=('Ivy 10 bold'), bg= co0, fg= co0)
app_2_linha.place(x= 315, y= 0)

# Linha de baixo dos pontos:
app_linha = Label(frame_cima, text= "", width= 325, height= 2, anchor= 'center', font=('Ivy 1 bold'), bg= co0, fg= co0)
app_linha.place(x= 0, y= 100)

# Linha de cima dos pontos:
app_linha_2 = Label(frame_cima, text= "", width= 325, height= 2, anchor= 'center', font=('Ivy 1 bold'), bg= co0, fg= co0)
app_linha_2.place(x= 0, y= 0)

# Indicador das escolhas do Computador:
app_PC = Label(frame_baixo, text= "", height= 1, anchor= 'center', font=('Ivy 13 bold'), bg= co0, fg= co0)
app_PC.place(x= 90, y= 10)

# Indicador das escolhas do Computador:
app_Player_Escolha = Label(frame_baixo, text= "", height= 1, anchor= 'center', font=('Ivy 13 bold'), bg= co0, fg= fundo)
app_Player_Escolha.place(x= 50, y= 60)

# Definição de variáveis globais:
global player
global computer
global rodadas
global player_points
global computer_points


# Definição de pontos e rodadas iniciais:
player_points = 0
computer_points = 0
rodadas = 3


# Função da logica do jogo:
def jogar(i):
    global rodadas
    global player_points
    global computer_points
    global app_PC
    global app_Player_Escolha

    # Definindo as rodadas:
    if rodadas != 0:
        print (rodadas)
        escolhas = ['Pedra', 'Papel', 'Tesoura']
        computer = random.choice(escolhas)
        player = i # Isto chama a escolha do jogador.


        # Indicação da escolha do PC:
        app_PC['text'] = "PC escolheu: " + computer
        app_PC['fg'] = co1


        # print (player, computer)

        # Escolhas iguais:
        if player == 'Pedra' and computer == 'Pedra':
            print ('Empate')
            app_linha  ['bg'] = co2
            app_linha_2['bg'] = co0
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
        
        elif player == 'Papel' and computer == 'Papel':
            print ('Empate')
            app_linha  ['bg'] = co2
            app_linha_2['bg'] = co0
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
        
        elif player == 'Tesoura' and computer == 'Tesoura':
            print ('Empate')
            app_linha  ['bg'] = co2
            app_linha_2['bg'] = co0
            app_1_linha['bg'] = co0
            app_2_linha['bg'] = co0
        
        # Escolhas diferentes:
        # Vitória do PC:
        elif player == 'Pedra' and computer == 'Papel':
            print ('PC Ganhou')
            app_linha  ['bg'] = co0
            app_linha_2['bg'] = co0
            app_1_linha['bg'] = co3
            app_2_linha['bg'] = co4
            computer_points += 1 

        elif player == 'Papel' and computer == 'Tesoura':
            print ('PC Ganhou')
            app_linha  ['bg'] = co0
            app_linha_2['bg'] = co0
            app_1_linha['bg'] = co3
            app_2_linha['bg'] = co4
            computer_points += 1

        elif player == 'Tesoura' and computer == 'Pedra':
            print ('PC Ganhou')
            app_linha  ['bg'] = co0
            app_linha_2['bg'] = co0
            app_1_linha['bg'] = co3
            app_2_linha['bg'] = co4
            computer_points += 1

        

        # Vitória do Jogador:
        elif player == 'Pedra' and computer == 'Tesoura':
            print ('Jogador Ganhou')
            app_linha  ['bg'] = co0
            app_linha_2['bg'] = co0
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co3
            player_points += 1

        elif player == 'Papel' and computer == 'Pedra':
            print ('Jogador Ganhou')
            app_linha  ['bg'] = co0
            app_linha_2['bg'] = co0
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co3
            player_points += 1

        elif player == 'Tesoura' and computer == 'Papel':
            print ('Jogador Ganhou')
            app_linha  ['bg'] = co0
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co3
            player_points += 1


    # Atualização da Pontuação:
        # Pontos do jogador:
        app_1_pontos['text'] = player_points

        # Pontos do computador:
        app_2_pontos['text'] = computer_points

    # Atualização das Rodadas:
        rodadas -= 1

    else:
        app_1_pontos['text'] = player_points
        app_2_pontos['text'] = computer_points

        fim_de_jogo()


# Função iniciação do jogo:
def iniciar_jogo():
    global app_PC
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3
    global app_Player_Escolha

    b_jogar.destroy()

    # Indicação para Player escolher:
    app_Player_Escolha['text'] = "Escolha sua jogada abaixo:"

    # Botão de escolha: Pedra;
    icon_1 = Image.open("Imagens\Pedra.png") # Se estiver testando o código sem ser pelo executável nos "Imagens\'imagem.png/texto.ico' adicionar antes de "Imagens" a localização, exemplo: Jogo_PedraPapelTesoura\Imagens\'imagem.png/texto.ico'
    icon_1 = icon_1.resize((60,60)) #, Image.ANTIALIAS
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda: jogar('Pedra'), width= 60, image= icon_1, compound= CENTER, bg= co0, fg= co0, font=('Ivy 10 bold'), anchor= CENTER, relief= FLAT, overrelief= RIDGE)
    b_icon_1.place(x= 20, y= 120)

    # Botão de escolha: Papel;
    icon_2 = Image.open('Imagens\Papel.png') # Se estiver testando o código sem ser pelo executável nos "Imagens\'imagem.png/texto.ico' adicionar antes de "Imagens" a localização, exemplo: Jogo_PedraPapelTesoura\Imagens\'imagem.png/texto.ico'
    icon_2 = icon_2.resize((60,60)) #, Image.ANTIALIAS
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar('Papel'), width= 60, image= icon_2, compound= CENTER, bg= co0, fg= co0, font=('Ivy 10 bold'), anchor= CENTER, relief= FLAT, overrelief= RIDGE)
    b_icon_2.place(x= 127, y= 120)

    # Botão de escolha: Tesoura;
    icon_3 = Image.open('Imagens\Tesoura_icone.ico') # Se estiver testando o código sem ser pelo executável nos "Imagens\'imagem.png/texto.ico' adicionar antes de "Imagens" a localização, exemplo: Jogo_PedraPapelTesoura\Imagens\'imagem.png/texto.ico'
    icon_3 = icon_3.resize((60,60)) #, Image.ANTIALIAS
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar('Tesoura'), width= 60, image= icon_3, compound= CENTER, bg= co0, fg= co0, font=('Ivy 10 bold'), anchor= CENTER, relief= FLAT, overrelief= RIDGE)
    b_icon_3.place(x= 244, y= 120)


# Função de terminar jogo:
def fim_de_jogo():
    global rodadas
    global player_points
    global computer_points
    global app_PC
    global app_Player_Escolha

    # Reinicialização das variáveis:
    player_points = 0
    computer_points = 0
    rodadas = 3

    # Destruição dos botões de escolha do jogador:
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()
    app_Player_Escolha['text'] = ''

    # Definição do vencedor:
    jogador_player = int(app_1_pontos['text'])
    jogador_computer = int(app_2_pontos['text'])

    # Se o player ganhoar:
    if jogador_player > jogador_computer:
        app_vencedor = Label(frame_baixo, text= "Parábens você ganhou!!! | 👌😎😁", height= 1, anchor= 'center', font=('Ivy 13 bold'), bg= co0, fg= co4)
        app_vencedor.place(x= 5, y= 60)
        app_linha  ['bg'] = co4
        app_linha_2['bg'] = co4
        app_1_linha['bg'] = co4
        app_2_linha['bg'] = co4

    # Se o computador ganhar:
    elif jogador_player < jogador_computer:
        app_vencedor = Label(frame_baixo, text= "Infelizmente você perdeu. | 😢😰😭", height= 1, anchor= 'center', font=('Ivy 13 bold'), bg= co0, fg= co3)
        app_vencedor.place(x= 5, y= 60)
        app_linha  ['bg'] = co3
        app_linha_2['bg'] = co3
        app_1_linha['bg'] = co3
        app_2_linha['bg'] = co3

    # Se empatar:
    else:
       app_vencedor = Label(frame_baixo, text= "É foi um empate. | 😒😑😴", height= 1, anchor= 'center', font=('Ivy 13 bold'), bg= co0, fg= co1)
       app_vencedor.place(x= 5, y= 60) 
       app_linha  ['bg'] = co2
       app_linha_2['bg'] = co2
       app_1_linha['bg'] = co2
       app_2_linha['bg'] = co2

    # Jogar novamente:
    def jogar_novamente():
        app_1_pontos['text'] = '0'
        app_2_pontos['text'] = '0'
        app_vencedor.destroy()
        app_PC['text'] = ''
        app_1_linha['bg'] = co0
        app_2_linha['bg'] = co0
        app_linha  ['bg'] = co0
        app_linha_2['bg'] = co0
        

        b_jogar_novamente.destroy()

        iniciar_jogo()

    b_jogar_novamente= Button(frame_baixo, command= jogar_novamente, width= 30, text= 'Jogar novamente', bg= co4, fg= co0, font=('Ivy 11 bold'), anchor= CENTER, relief= RAISED, overrelief= RIDGE)
    b_jogar_novamente.place(x= 25, y= 240)

# Botão de jogar;

b_jogar= Button(frame_baixo, command= iniciar_jogo, width= 30, text= 'Jogar', bg= co4, fg= co0, font=('Ivy 11 bold'), anchor= CENTER, relief= RAISED, overrelief= RIDGE)
b_jogar.place(x= 25, y= 240)




janela.mainloop()