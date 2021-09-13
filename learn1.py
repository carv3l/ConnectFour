# -*- coding: utf-8 -*-
import sys
import os
import Tkinter
import sqlite3
from colorama import init, Fore, Style
from random import randint
from itertools import groupby, chain
init(autoreset=True)

conn = sqlite3.connect('scores.db')

c = conn.cursor()

try:
    c.execute('Select * from Leaderboard')
except:
    c.execute('''CREATE TABLE Leaderboard
            (Name text, Wins int, Draws int, Defeats int, Points int)''')
    

class menu():
    def main_menu_options(self):
        "This is going to display the main menu"

        introtext =""" 
        .----.                              .-.   .----.               
        : .--'                             .' '.  : .--'              
        : :    .--. ,-.,-.,-.,-. .--.  .--.`. .'  : `;.--. .-..-..--. 
        : :__ ' .; :: ,. :: ,. :' '_.''  ..': :   : :' .; :: :; :: ..'
        `.__.'`.__.':_;:_;:_;:_;`.__.'`.__.':_;   :_;`.__.'`.__.':_;  
        """
        print introtext
        print(chr(201)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(187))
        print(chr(186)+' Welcome to Connect Four '+ chr(186))
        print(chr(186)+ Fore.LIGHTBLUE_EX + ' 1'+ Fore.RESET + ' --> Start Game        '+ Fore.RESET + chr(186))
        print(chr(186)+ Fore.BLUE + ' 2'+ Fore.RESET + ' --> LeaderBoards      '+ Fore.RESET + chr(186))
        print(chr(200)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(188))
        print(Fore.GREEN + 'Press e to exit the game \n')
        return None

    def matrix_options(self,opcao_jogo,name1,name2):
        "This display all board sizes"
        if opcao_jogo == '1':
            print (Fore.YELLOW + name1 + Fore.RESET + ' and '+ Fore.YELLOW + name2 + Fore.RESET + ' CHOOSE THE LEVEL TO PLAY:')

        if opcao_jogo == '2':
            print (Fore.YELLOW + name1 + Fore.RESET + ' CHOOSE THE LEVEL TO PLAY:')

        print(chr(201)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(187))
        print(chr(186)+ Fore.BLUE +'   1'+ Fore.RESET + '--> 7 X 6 ='+ Fore.CYAN +' rookie   ' + Fore.RESET + chr(186))
        print(chr(186)+Fore.BLUE + '   2'+ Fore.RESET + '--> 8 X 7 ='+ Fore.CYAN +' basic    '+ Fore.RESET + chr(186))
        print(chr(186)+Fore.BLUE + '   3'+ Fore.RESET + '--> 9 X 7 ='+ Fore.CYAN +' normal   '+ Fore.RESET + chr(186))
        print(chr(186)+Fore.BLUE + '   4'+ Fore.RESET + '--> 8 X 8 ='+ Fore.CYAN +' medium   '+ Fore.RESET + chr(186))
        print(chr(186)+Fore.BLUE + '   5'+ Fore.RESET + '--> 10 X 7 ='+ Fore.CYAN +' hard    '+ Fore.RESET + chr(186))
        print(chr(200)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(188))
        print(Fore.GREEN + 'Press e to exit this sub menu\n')
        opcao_tabuleiro = raw_input('$: ')
        return opcao_tabuleiro

        #return None
        
    def game_options(self):
        "This display all game modes"
        print(chr(201)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(187))
        print(chr(186)+ '       All Game Modes Available      '+ Fore.RESET + chr(186))
        print(chr(186)+Fore.BLUE + ' 1'+ Fore.RESET + ' --> Play mano A mano              '+ Fore.RESET + chr(186))
        print(chr(186)+Fore.BLUE + ' 2'+ Fore.RESET + ' --> Play with an Heartless machine'+ Fore.RESET + chr(186))
        print(chr(200)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(188))
        print(Fore.GREEN + 'Press e to exit this sub menu\n')
        modo_jogo = raw_input('$: ')
        return modo_jogo 

    def leaderboard_option(self):
        "This displays the LeaderBoard"
        print '  Place = Name : W - T - D - P'
        print(chr(201)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(187))
        count = 1
        for  linha_leaderboard in c.execute('SELECT * FROM Leaderboard ORDER BY Points DESC LIMIT 10'):
            row = ' '.join(str(linha_leaderboard))
            row = row.replace(" ", "")
            row = row.replace("'", "")
            row = row.replace("(", "")
            row = row.replace(")", "")
            row = row.replace("u", "", 1)
            row = row.replace(",", " : ", 1)
            row = row.replace(",", " - ")
            print '  ', count, chr(248), ' = ', row
            count += 1
        print(chr(200)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(205)+' '+chr(188))
        print ('W = Wins')
        print ('T = Ties')
        print ('D = Defeats')
        print ('P = Points')
        print(Fore.GREEN + 'Press e to exit this sub menu\n')
        opcoes_leaderboard = raw_input('$: ')
        return opcoes_leaderboard



    def halp_option(self):
        "This display the help"
        print('Coming Soon ...œœ◄')
        print('Coming Soon ...')
        print(Fore.GREEN + 'Press e to exit this sub menu')
        return None

    def exit_option(self,mode):
        "This will exit the game"
        exittext =""" 
                 ___   __    __  ____  ____  _  _  ____ 
                / __) /  \  /  \(    \(  _ \( \/ )(  __)
               ( (_ \(  O )(  O )) D ( ) _ ( )  /  ) _) 
                \___/ \__/  \__/(____/(____/(__/  (____)
                """

        if mode == 1:
            print exittext
            sys.exit(0)
            exit()
        if mode == 2:
            os.system("learn1.py")
        return None

class jogador:
    def insere_jogador(self,player1,player2):

        getplayer1 = c.execute('Select Name from Leaderboard Where Name=?',[player1]).fetchone()
        player1_resultado = ' '.join(str(getplayer1))
        player1_resultado = player1_resultado.replace(" ", "")
        player1_resultado = player1_resultado.replace("'", "")
        player1_resultado = player1_resultado.replace("(", "")
        player1_resultado = player1_resultado.replace(")", "")
        player1_resultado = player1_resultado.replace("u", "", 1)
        player1_resultado = player1_resultado.replace(",", "")
        getplayer2 = c.execute('Select Name from Leaderboard Where Name=?',[player2]).fetchone()
        player2_resultado = ' '.join(str(getplayer2))
        player2_resultado = player2_resultado.replace(" ", "")
        player2_resultado = player2_resultado.replace("'", "")
        player2_resultado = player2_resultado.replace("(", "")
        player2_resultado = player2_resultado.replace(")", "")
        player2_resultado = player2_resultado.replace("u", "", 1)
        player2_resultado = player2_resultado.replace(",", "")
        #print player1_resultado
        #print player2_resultado
        if player1_resultado != player1:
            item = [(player1,0,0,0,0)]
            c.executemany("INSERT INTO Leaderboard VALUES (?,?,?,?,?)",item)
            conn.commit()
        else:
            pass
        if player2_resultado != player2:
            item = [(player2,0,0,0,0)]
            c.executemany("INSERT INTO Leaderboard VALUES (?,?,?,?,?)",item)
            conn.commit()
        else:
            pass
    def insere_pontuacao(self,nome,modo_resultado,nomeadversario):
        #vitorias = 1
        #empates  = 0
        #derrotas = 0
        #print modo_resultado

        if modo_resultado == 1:

            get_wins = c.execute('SELECT Wins from Leaderboard WHERE Name=?', [nome]).fetchone()
            wins = ' '.join(map(str, (get_wins)))
            vitorias = int(wins)+1
            c.execute("""UPDATE Leaderboard SET Wins = ? WHERE Name = ? """, (vitorias, nome))

            self.pontuacao_total(nome)

            get_loser = c.execute('SELECT Defeats from Leaderboard WHERE Name=?', [nomeadversario]).fetchone()
            losses = ' '.join(map(str, (get_loser)))
            derrotas = int(losses)+1
            c.execute("""UPDATE Leaderboard SET Defeats = ? WHERE Name = ? """, (derrotas, nomeadversario))
            conn.commit()

            self.pontuacao_total(nomeadversario)

        if modo_resultado == 2:
            
            get_draws = c.execute('SELECT Draws from Leaderboard WHERE Name=?', [nome]).fetchone()
            Ties = ' '.join(map(str, (get_draws)))
            empates = int(Ties)+1
            c.execute("""UPDATE Leaderboard SET Draws = ? WHERE Name = ?""",(empates, nome))
            conn.commit()
                    
            self.pontuacao_total(nome)

            get_draws = c.execute('SELECT Draws from Leaderboard WHERE Name=?', [nomeadversario]).fetchone()
            Ties = ' '.join(map(str, (get_draws)))
            empates = int(Ties)+1
            c.execute("""UPDATE Leaderboard SET Draws = ? WHERE Name = ?""",(empates,nomeadversario))
            conn.commit()

            self.pontuacao_total(nomeadversario)

    def pontuacao_total(self,nome):
        get_wins = c.execute('SELECT Wins from Leaderboard WHERE Name=?', [nome]).fetchone()
        pontos_wins = ' '.join(map(str, (get_wins)))
        get_draws = c.execute('SELECT Draws from Leaderboard WHERE Name=?', [nome]).fetchone()
        pontos_draws = ' '.join(map(str, (get_draws)))
        pontos_total = ((int(pontos_wins)*3)+(int(pontos_draws)*1))
        #print 'Pontos:',pontos_total
        c.execute("""UPDATE Leaderboard SET Points = ? WHERE Name = ? """, (pontos_total, nome))
        conn.commit()

class tabuleiro:
    jogador = jogador()
    menu = menu()

    def __init__(self, opcao = 0):
        """Settings"""
        self.opcao =  opcao

    def build_tabuleiro(self,resultm):
        self.opcao = resultm
        if resultm == '1':
            self.grid = [['_' for x in range(7)] for y in range(6)]
        if resultm == '2':
            self.grid = [['_' for x in range(8)] for y in range(7)]
        if resultm == '3':
            self.grid = [['_' for x in range(9)] for y in range(7)]
        if resultm == '4':
            self.grid = [['_' for x in range(8)] for y in range(8)]
        if resultm == '5':
            self.grid = [['_' for x in range(10)] for y in range(7)]


    def size_opcao(self):
        opcao = self.opcao
        if opcao == '1':
            linhas = 6
            colunas = 7
            return linhas, colunas
        if opcao == '2':
            linhas = 7
            colunas = 8
            return linhas, colunas
        if opcao == '3':
            linhas = 7
            colunas = 9
            return linhas, colunas
        if opcao == '4':
            linhas = 8
            colunas = 8
            return colunas, linhas
        if opcao == '5':
            linhas = 10
            colunas = 7
            return colunas, linhas



    def diagonalsPos (self,tabuleiro,linhas, colunas):
        """Get positive diagonals, going from bottom-left to top-right."""
        for di in ([(j, i - j) for j in range(linhas)] for i in range(linhas + colunas -1)):
            yield [tabuleiro[i][j] for i, j in di if i >= 0 and j >= 0 and i < linhas and j < colunas]

    def diagonalsNeg (self,tabuleiro,linhas, colunas):
        """Get negative diagonals, going from top-left to bottom-right."""
        for di in ([(j, i - linhas + j + 1) for j in range(colunas)] for i in range(linhas + colunas - 1)):
            yield [tabuleiro[i][j] for i, j in di if i >= 0 and j >= 0 and i < linhas and j < colunas]



    def getWinner(self, linhas, colunas, game_type):
        grid = self.grid
        lines = (
                grid, # columns
                zip(*grid), # rows
                self.diagonalsPos(grid, linhas, colunas), # positive diagonals
                self.diagonalsNeg(grid, linhas, colunas) # negative diagonals
        )
        if game_type == 2:
            for line in chain(*lines):
                for signal_player, group in groupby(line):
                    if signal_player != '_' and len(list(group)) >= 4:
                        signal_player = 'a'
                        return signal_player
            try:          
                er = next(x for x in grid[0] if x == '_' )
            except:
                signal_player = 'f'
                return signal_player

       
        if game_type == 1:
            for line in chain(*lines):
                for signal_player, group in groupby(line):
                    if signal_player != '_' and len(list(group)) >= 4:
                        signal_player = 'a'
                        return signal_player


    def getplayerjogada(self, linhas, colunas):
        grid = self.grid
        machine_next_move = 0
        lines = (
                grid, # columns
                zip(*grid), # rows
                self.diagonalsPos(grid, linhas, colunas), # positive diagonals
                self.diagonalsNeg(grid, linhas, colunas) # negative diagonals
        )
        for line in chain(*lines):
                for signal_player, group in groupby(line):
                    #print 'ARRAY:', line
                    for i in groupby(line):
                        if (signal_player != '_') and (signal_player == chr(254)) and (len(list(group)) >= 3):
                            #print 'ARRAY:', line
                            #print 'ARRAY1:', line.index(chr(254))
                            try:
                                if line[len(line) - 1 - line[::-1].index(chr(254))+1] == '_':
                                    #line[len(line) - 1 - line[::-1].index(chr(254))+1] = chr(207)
                                    machine_next_move = 1
                                    return machine_next_move
                            except:
                            
                                    if line[line.index(chr(254)) -1] == '_':
                                        #line[line.index(chr(254)) -1] = chr(207)
                                        machine_next_move = 2
                                        return machine_next_move
 
    def case_option(self, x):
        """Alternative to Switch Case"""       
        if x.isupper():# Check if is upper and if it is ,turn to lowercase
            x = x.lower()
        try:
            return {
                'a': 0,
                'b': 1,
                'c': 2,
                'd': 3,
                'e': 4,
                'f': 5,
                'g': 6,
                'h': 7,
                'i': 8,
                'j': 9,
                }[x]
        except:
            x = 'error'
            return x

    def print_tabuleiro(self):
        opcao = self.opcao
        for i, coluna in enumerate(self.grid):
            if int(opcao) == 1:
                print Fore.MAGENTA + '  A  B  C  D  E  F  G'
                opcao = 0
            if (int(opcao) == 2) or (int(opcao) == 4):
                print Fore.MAGENTA + '  A  B  C  D  E  F  G  H '
                opcao = 0
            if int(opcao) == 3:
                print Fore.MAGENTA + '  A  B  C  D  E  F  G  H  I'
                opcao = 0
            if int(opcao) == 5:
                print Fore.MAGENTA + '  A  B  C  D  E  F  G  H  I  J'
                opcao = 0
            print ' ', '  '.join(coluna)

    def verifica_jogada (self,nome,game_type,nomeadversario):
        """Check the current board for a winner."""
        linhas_tabuleiro, colunas_tabuleiro = self.size_opcao()
        estado = self.getWinner(linhas_tabuleiro,colunas_tabuleiro,game_type)
        acabar_jogo = False
        if estado == 'a':
            print(nome + ' won!')

            jogador.insere_pontuacao(nome,1,nomeadversario)
            acabar_jogo = True
        if estado == 'f':
            print 'DRAW !!!'
            jogador.insere_pontuacao(nome,2,nomeadversario)
            acabar_jogo = True

        return acabar_jogo

    def machine_move (self,nome):
        """Check the current board a possible connection."""
        linhas_tabuleiro, colunas_tabuleiro = self.size_opcao()
       #Get player1 last move to calc the machine next move
        machine_next_move = self.getplayerjogada(linhas_tabuleiro,colunas_tabuleiro)
        next_move = 0
        if machine_next_move == 1:
            #print 'move is next'

            next_move = 1
            return next_move

        elif machine_next_move == 2:
           # print 'move is up'
            next_move = 2
            return next_move
        else:
            return next_move
       

    def coloca_peca(self,player, nomeatual ,nomeadversario, coordenada):
        gameover = True
    ##### PLAYER 1
        grid = self.grid

        if player == 'p1':
            posY= len(grid) -1
            if grid[1][coordenada] != '_':
                self.print_tabuleiro()
                print(Fore.LIGHTRED_EX + 'COLUMN IS FULL!!!')
            try:
                while grid[posY][coordenada] != '_':
                        posY -= 1
                grid[posY][coordenada] = chr(254)
            except:
                print(Fore.LIGHTRED_EX + 'COLUMN IS FULL!!! YOU\'VE LOST YOUR TURN')
            self.print_tabuleiro()
            resultado = self.verifica_jogada(nomeatual,2,nomeadversario)
            if resultado:
                print(Fore.GREEN + 'GAMEOVER!!!')
                resposta = menu.leaderboard_option()
                if resposta == 'e':
                    menu.exit_option(2)
                gameover = False
            return gameover
            
    ##### PLAYER 2
        if player == 'p2':
            posY= len(grid) -1
            if grid[1][coordenada] != '_':
                self.print_tabuleiro()
                print(Fore.LIGHTRED_EX + 'COLUMN IS FULL!!!')
            try:
                while grid[posY][coordenada] != '_':
                        posY -= 1
                grid[posY][coordenada] = chr(207)
            except:
                print(Fore.LIGHTRED_EX + 'COLUMN IS FULL!!! YOU\'VE LOST YOUR TURN')
            self.print_tabuleiro()
            resultado1 = self.verifica_jogada(nomeatual,2,nomeadversario)
            if resultado1:
                print(Fore.GREEN + 'GAMEOVER!!!')
                resposta = menu.leaderboard_option()
                if resposta == 'e':
                    menu.exit_option(2)
                gameover = False
            return gameover        

    def machine_coloca_peca(self,playerturn,playeratual,playeradversario,player_move,):
        #menu = menu()
        gameover = True
        grid = self.grid
        coordenada = player_move
       # print(randint(0,1))
        if playerturn == 'p1':
                posY= len(grid) -1
                if grid[1][coordenada] != '_':
                    self.print_tabuleiro()
                    print(Fore.LIGHTRED_EX + 'COLUMN IS FULL!!!')
                try:
                    while grid[posY][coordenada] != '_':
                            posY -= 1
                    grid[posY][coordenada] = chr(254)
                except:
                    print(Fore.LIGHTRED_EX + 'COLUMN IS FULL!!! YOU\'VE LOST YOUR TURN')
                self.print_tabuleiro()
                resultado = self.verifica_jogada(playeratual,1,playeradversario)
                if resultado:
                    print(Fore.GREEN + 'GAMEOVER!!!')
                    resposta = menu.leaderboard_option()
                    if resposta == 'e':
                        menu.exit_option(2)
                    gameover = False
                return gameover
        
        if playerturn == 'cpu':
                response = self.machine_move(playeratual)
                #print 'Response',response

                if response == 1:
                    posY= len(grid) -1
                    player_move +=1
                    try:      
                        while grid[posY][player_move] != '_':
                            posY -= 1
                        try:
                            grid[posY][player_move] = chr(207)
                        except:
                            player_move -=2
                            grid[posY][player_move] = chr(207)
                    except:
                        print(Fore.LIGHTRED_EX + 'COLUMN IS FULL!!! YOU\'VE LOST YOUR TURN')
                    self.print_tabuleiro()
                    resultado1 = self.verifica_jogada(playeratual,1,playeradversario)
                    if resultado1:
                        print(Fore.GREEN + 'GAMEOVER!!!')
                        resposta = menu.leaderboard_option()
                        if resposta == 'e':
                            menu.exit_option(2)
                        gameover = False
                    return gameover
                    

                elif response == 2:
                    posY= len(grid) -1
                    try:      
                        while grid[posY][player_move] != '_':
                            posY -= 1
                        try:
                            grid[posY][player_move] = chr(207)
                        except:
                            grid[posY][coordenada] = chr(207)
                    except:
                        print(Fore.LIGHTRED_EX + 'COLUMN IS FULL!!!')
                    self.print_tabuleiro()
                    resultado1 = self.verifica_jogada(playeratual,1,playeradversario)
                    if resultado1:
                        print(Fore.GREEN + 'GAMEOVER!!!')
                        #menu.main_menu_options()
                        resposta = menu.leaderboard_option()
                        if resposta == 'e':
                            menu.exit_option(2)

                        gameover = False
                    return gameover

                elif response == 0:
                    posY= len(grid) -1
                    random_choice = randint(0,2)
                    if random_choice == 0:
                        player_move +=1
                    elif random_choice == 1:
                        player_move -=1
                    else:
                        player_move = player_move
                    try:      
                        while grid[posY][player_move] != '_':
                            posY -= 1
                        try:
                            grid[posY][player_move] = chr(207)
                        except:
                            grid[posY][coordenada] = chr(207)
                    except:
                        print(Fore.LIGHTRED_EX + 'COLUMN IS FULL!!!')
                    self.print_tabuleiro()
                    resultado1 = self.verifica_jogada(playeratual,1,playeradversario)
                    if resultado1:
                        print(Fore.GREEN + 'GAMEOVER!!!')
                        resposta = menu.leaderboard_option()
                        if resposta == 'e':
                            menu.exit_option(2)
                        gameover = False
                return gameover

def multi_player():
    print Fore.GREEN + 'To exit while playing press the (x) key, no score will be saved'
    tabuleiro.opcao = opcao_tabuleiro
    tabuleiro.print_tabuleiro()
    estado_jogo = True
    turn = True
    while estado_jogo == True:
        if turn == True:
            print (Fore.YELLOW + player1 + '\'s TURN:')
            coordinate = raw_input('::')
            coordinate = ''.join(coordinate.split())
            if (not coordinate) or (coordinate.isdigit()) or (len(coordinate) > 1):
                print Fore.RED + 'WAKE UP... WRONG INPUT !!! YOU NEITHER CAN\'T USE NUMBERS HERE NEITHER LEAVE IT BLANK !!!'
            elif coordinate == 'x':
                estado_jogo = False
                menu.main_menu_options()
            else:
                coor = tabuleiro.case_option(coordinate)
                if coor == 'error':
                    print Fore.RED + 'WAKE UP... WRONG INPUT !!!'
                    turn = True
                else:
                    status = tabuleiro.coloca_peca('p1', player1, player2 , coor)
                    turn = False
                    estado_jogo = status
        elif turn == False:
            print (Fore.YELLOW + player2 + '\'s TURN:')
            coordinate = raw_input('::')
            coordinate = ''.join(coordinate.split())
            if (not coordinate) or (coordinate.isdigit()) or (len(coordinate) > 1):
                print Fore.RED + 'WAKE UP... WRONG INPUT !!! YOU NEITHER CAN\'T USE NUMBERS HERE NEITHER LEAVE IT BLANK !!!'
            elif coordinate == 'x':
                estado_jogo = False
                menu.main_menu_options()
            else:
                coor = tabuleiro.case_option(coordinate)
                if coor == 'error':
                    print Fore.RED + 'WAKE UP... WRONG INPUT !!!'
                    turn = False
                else:
                    status = tabuleiro.coloca_peca('p2', player2, player1 , coor)   ### Estado e para saber se o jogo acabou ou continua
                    turn = True
                    estado_jogo = status


def single_player():
    #menu = menu()
    tabuleiro.opcao = opcao_tabuleiro
    tabuleiro.print_tabuleiro()
    estado_jogo = True
    turn = True
    cpu = 'CPU'
    while estado_jogo == True:
        if turn == True:
            print (Fore.YELLOW + player1 + '\'s TURN:')
            coordinate = raw_input('::')
            coordinate = ''.join(coordinate.split())
            if (not coordinate) or (coordinate.isdigit()) or (len(coordinate) > 1):
               print Fore.RED + 'WAKE UP... WRONG INPUT !!! YOU NEITHER CAN\'T USE NUMBERS HERE NEITHER LEAVE IT BLANK !!!'
            elif coordinate == 'x':
                estado_jogo = False
                menu.main_menu_options()
            else:
                coor = tabuleiro.case_option(coordinate)
                if coor == 'error':
                    print Fore.RED + 'WAKE UP... WRONG INPUT !!!'
                    turn = True
                else:
                    status = tabuleiro.machine_coloca_peca('p1', player1 ,cpu, coor)
                    turn = False
                    estado_jogo = status
        elif turn == False:
            print (Fore.YELLOW + cpu + '\'s TURN:')
            status = tabuleiro.machine_coloca_peca('cpu',cpu, player1, coor)
            turn = True
            estado_jogo = status

########### START ALL THING ###########
tabuleiro = tabuleiro()
jogador = jogador()
menu = menu()
spell_check = False
menu.main_menu_options()
opcao_menu= raw_input('$:')
if opcao_menu == '1':
    opcao_jogo = menu.game_options()
    if opcao_jogo == '1':
         player1 = raw_input(Fore.YELLOW + "Name of Player 1:")
         player2 = raw_input(Fore.YELLOW + "Name of Player 2:")

         if ( not player1) or ( not player2) :
             print(Fore.RED + 'Both Players must have a name !!!')
         else:
                jogador.insere_jogador(player1,player2)
                while spell_check == False:
                    opcao_tabuleiro = menu.matrix_options(opcao_jogo,player1,player2)
                    if opcao_tabuleiro.isdigit():
                        tabuleiro.build_tabuleiro(opcao_tabuleiro)
                        multi_player()
                        spell_check == True
                    elif opcao_tabuleiro == 'e':
                        spell_check == True
                        menu.exit_option(2)
                    else:
                        print Fore.RED + 'NOT A VALID INPUT TRY AGAIN !!!'
                        spell_check == False

    elif opcao_jogo == '2':
        player1 = raw_input(Fore.YELLOW + "Name of Player 1:")
        if not player1:
             print(Fore.RED + 'Player must have a name !!!')
        else:
              jogador.insere_jogador(player1,'CPU')
              while spell_check == False:
                opcao_tabuleiro = menu.matrix_options(opcao_jogo,player1,None)
                if opcao_tabuleiro.isdigit():
                        spell_check == True
                        tabuleiro.build_tabuleiro(opcao_tabuleiro)
                        single_player()
                elif opcao_tabuleiro == 'e':
                    spell_check == True
                    menu.exit_option(2)
                else:
                    print Fore.RED + 'NOT A VALID INPUT TRY AGAIN !!!'
                    spell_check == False
              
    elif opcao_jogo == 'e':
        menu.exit_option(2)
elif opcao_menu == '2':
      #  print(Fore.RED + 'Something is Wrong !!!')
        #menu.leaderboard_option()
        resposta = menu.leaderboard_option()
        if resposta == 'e':
            menu.exit_option(2)

elif opcao_menu == 'e':
        menu.exit_option(1)