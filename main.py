import random
import art
import replit

playing = True
while playing == True:
  
  strings = {
    
    "play" : input('  Would you like to play a game of Blackjack? Type "y" to play or "n" to quit\n'),
    "both_lose" : "  Both your scores were over 21. You both lose!",
    "player_bust" : "  Bust! Computer wins",
    "computer_bust" : "  Bust! Player wins",
    "player_wins" : "  Congratulations, you win!",
    "computer_wins" : "  Unlucky, computer wins!",
    "draw" : "  Both have the same score. Draw!"
  }
  
  print(strings["play"])

  #quits app if n pressed
  if strings["play"] == "y":
    replit.clear()

  else:
    playing = False
    print("Goodbye!")
    quit()

  #prints logo

  print(art.logo)

  #deck

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  #draws a card to hand

  def draw_card(hand):
    card = random.choice(cards)
    hand.append(card)

  #sums values in player or computer hand

  def get_score(hand):
    return sum(hand)

  player_hand = []
  computer_hand = []

  #draw computer's first card

  draw_card(computer_hand)
  print(f"  The computer's first card is {computer_hand[0]}")
  
  #player turn

  draw_card(player_hand)
  draw_card(player_hand)
  def player_turn():
    player_cards = "  Your cards are : "
    for card in player_hand:
      player_cards += str(card) + " "
    player_score_is = (f"and your score is {get_score(player_hand)}")
    print(player_cards + player_score_is)

    score = get_score(player_hand)
    turn = True
    while turn == True:
      score = get_score(player_hand)
      if cards[0] in player_hand and score > 21:
        index = player_hand.index(11)
        player_hand[index] = 1
        print(" Converting an ace from 11 to 1!")
        continue
      if score < 21:
        draw = input('  Would you like to draw another card? Type "y" to draw or any other key to pass\n')
        if draw == "y":
          draw_card(player_hand)
          player_turn()
        else:
          break
      break
  
  #computer turn

  def computer_turn():

    score = get_score(computer_hand)

    turn = True
    while turn == True:
      while score <= 16: 
        draw_card(computer_hand)

        if cards[0] in computer_hand and score > 21:
          index = computer_hand.index(11)
          computer_hand[index] = 1
          print(" Converting computer's ace from 11 to 1!")
        score = get_score(computer_hand)
        computer_cards = "  The computer's cards are : "
        for card in computer_hand:
          computer_cards += str(card) + " "
        computer_score_is = (f"and the computer's score is {score}")
        print(computer_cards + computer_score_is)

      else:
        break
      break

  #compare scores

  def compare_scores():
    computer_score = get_score(computer_hand)
    player_score = get_score(player_hand)

    print(f"  Your final score is {player_score}")
    print(f"  The computer's final score is {computer_score}")
    if player_score > 21 and computer_score > 21:
      print(strings["both_lose"])
    elif player_score > 21:
      print(strings["player_bust"])
    elif computer_score > 21:
      print(strings["computer_bust"])
    elif player_score > computer_score:
      print(strings["player_wins"])
    elif computer_score > player_score:
      print(strings["computer_wins"])
    elif computer_score == player_score:
      print(strings["draw"])

  player_turn()
  computer_turn()
  compare_scores()
  