""" DUNGEON CRAWLER INFINITO """
from DungeonPy.scripts import desafios, jogador
from DungeonPy.scripts.jogador import personagem
from stringcolor import *
# ------------------------------------------- INICIA O JOGO ------------------------------------------------------------
print('----- Seja bem vindo ao DUNGEON CRAWLER 1.0 -------')

jogador.instrucao()
jogador.inicio()

escolha = None
fim = False

while escolha != 'INICIAR':
    escolha = input('Digite: ').upper()
    if escolha == 'INICIAR':
        break

personagem.status()
desafios.gerar_desafio()

# --------------------------------------------- MENUS ------------------------------------------------------------------
while fim is False:
    if fim:
        break
    # ======================================= MORTE JOGADOR: FINALIZA O JOGO ===========================================
    if personagem.vida <= 0:
        fim = True
        print(cs('\n#################### Você morreu! ####################\n', 'red').bold() +
              f'Você atingiu nível: {personagem.nivel}\n' +
              f'Você coletou: {personagem.coletados} items\n' +
              f'Você derrotou: {personagem.derrotados} monstros!\n' +
              cs('#################### Aplicação finalizada ####################', 'red').bold())
        break
    # ======================================== LOOP MENU ===============================================================
    if fim is False:
        jogador.continuar()
        escolha = input('Digite: ').upper()
    if escolha == '1':
        desafios.gerar_desafio()
    if escolha == '2':
        jogador.instrucao()
    if escolha == '3':
        print(f'\nVocê atingiu nível: {personagem.nivel}\n'
              f'Você derrotou: {personagem.derrotados} monstros!\n'
              '------------- Aplicação finalizada -------------')
        break
    if escolha == 'STATUS':
        personagem.status()
    if escolha == 'MOCHILA':
        personagem.ver_mochila()
    if escolha == 'POT':
        personagem.usar_pocao()