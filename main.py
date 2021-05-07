import random
import art
import replit

turn = True
computer_turn = True

playing = True
while playing == True:
  play = input('Would you like to play a game of Blackjack? Type "y" to play or "n" to quit\n')

  #quits app if n pressed
  if play == "y":
    replit.clear()
  elif play == "n":
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
  while turn == True:
    player_cards = "  Your cards are : "
    for card in player_hand:
      player_cards += str(card) + " "
    player_score_is = (f" and your score is {get_score(player_hand)}")
    print(player_cards + player_score_is)

    score = get_score(player_hand)
    if score > 21:
      if cards[0] in player_hand:
        index = player_hand.index(11)
        player_hand[index] = 1
        print(" Converting an ace from 11 to 1!")
      else: 
        turn = False

    draw = input('  Would you like to draw another card? Type "y" to draw or "n" to pass\n')
    if draw == "y":
      draw_card(player_hand)
    else:
      turn = False
  
  #computer turn

  while computer_turn == True:
    if get_score(computer_hand) > 16:
      if score > 21:
        if cards[0] in computer_hand:
          index = computer_hand.index(11)
          computer_hand[index] = 1
          print(" Converting computer's ace from 11 to 1!")
      else: 
        computer_turn = False
        computer_cards = "  The computer's cards are : "
        for card in computer_hand:
          computer_cards += str(card) + " "
          print(computer_cards)
    else:
      draw_card(computer_hand)

  #compare scores

  computer_score = get_score(computer_hand)
  player_score = get_score(player_hand)

  print(f"  Your final score is {player_score}")
  print(f"  The computer's final score is {computer_score}")
  if player_score > 21 and computer_score > 21:
    print(" Both your scores were over 21. You both lose!")
  elif player_score > 21:
    print("  Bust! Computer wins")
  elif computer_score > 21:
    print(" Bust! Player wins")
  elif player_score > computer_score:
    print(" Congratulations, you win!")
  elif computer_score > player_score:
    print("  Unlucky, computer wins!")
  elif computer_score == player_score:
    print(" Both have the same score. Draw!")