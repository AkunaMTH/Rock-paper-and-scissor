# import serve para importar uma livraria para o código
import random

# Função para recolher as escolhas do jogador
def get_choices():
  # [] serve para criar uma lista de itens
  items = ["pedra", "papel", "tesoura"]
  player_choice = input("Pedra, papel ou tesoura? ")
  computer_choice = random.choice(items)
  # {} serve para criar um "dictionary", sendo capaz de armazenar valores
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

# Função para determinar o vencedor do jogo
def check_win(player, computer):
  if player == computer:
    return "Foi um empate"
  elif player == "pedra":
    if computer == "tesoura":
      return "Você ganhou!"
    else:
      return "Você perdeu."
  elif player == "papel":
    if computer == "pedra":
      return "Você ganhou!"
    else:
      return "Você perdeu."
  elif player == "tesoura":
    if computer == "papel":
      return "Você ganhou!"
    else:
      return "Você perdeu."

# Variáveis para rodar o jogo
choice = get_choices()
computador = choice["computer"]

# Aplicando a função check_win para verificar o ganhador da função get_choices atribuida à variavel choice
result = check_win(choice["player"], choice["computer"])

print(f"O computador escolheu {computador}. {result}")
