# DungeonPy
Simple Dungeon Crawler game made with python.
Um Dungeon Crawler simples feito em Python.
####### COMANDOS
STATUS -> Vizualiza seus STATUS (NíVEL, VIDA, POÇÕES, etc...)
MOCHILA -> Vizualiza seus itens
POT -> Usar poção
SAIR -> Finaliza a aplicação

####### SISTEMA DE EXPERIENCIA
O jogador começa nivel 1 e a cada criatura derrotada ganha experiência.
Os níveis contam como pontuação, assim como as criaturas derrotadas.
Ao final da partida será impresso na tela quantas criaturas derrotou, seu nível e quantos itens coletou.
O nível pode ser vizualizado através do comando STATUS.
Toda vez que o jogador sobe de nível, a vida volta ao seu valor máximo (10)

####### SISTEMA DE COMBATE
O sistema de combate simula o jogar de dados
A dificuldade é definida semi-aleatoriamente.
As criaturas geradas contam com valores máximos e mínimos de vida e de ataque/defesa.
Os locais são escolhidos a partir de uma lista pré-definida utilizando random.choice()
A cada turno os dados são jogados, apresentando se você sofreu, causou ou se o dano foi anulado.
O jogador conta com 10 pontos de vida.
Cada uso de poção restaura 2 pontos de vida, elas podem ser usadas após/entre os combates, mas não durante.

####### SISTEMA DE ITEMS
Os itens são divididos em ATAQUE e DEFESA.
Cada criatura derrotada tem a chance de deixar cair um item, e ele será enviado para sua mochila e aumentará o respectivo atributo.
A mochila pode conter infinitos itens.
Os valores de ATAQUE e DEFESA são somados no tirar dos dados.
