# Blackjack
Python tutorial for creating a blackjack game

This is for an exercise on Angela Yu's Python course. It is a 'capstone' project, incorporating every element learned on the course so far.

I have not included dicts in the program. I am in the process of determining the best way to implement them. I have decided that they
should be used in place of the string concatenation. Currently I am using a mix of fstrings and string variables to print the player
and computer scores. This is incredibly janky, and stems from the fact that I did not want to use dicts whatsoever. On the other hand,
I should probably use them because it will make me a better programmer in the long run. So I am going to find a way to incorporate them
and do away with the hacky score reporting. 

Changelog:

I have included dicts in the program. I recently found out that dicts correlate [roughly] to maps and/or structs in GML. They are in effect
'key/value pairs'. I have used structs extensively in GML so was quite happy to find this out. However, their implementation in the project is 
more tacked on than essential. I wanted to use them in order to make sure I had used everything I had hitherto learned, and I am glad that I did,
although their implementation is unnecessary. If I had understood their relation to gml structs earlier, then I would have found a better use for them.
As it is, I didn't want to rewrite a working program in order to shoehorn them in, so I sort of tacked them on as an afterthought.

The score reporting is still incredibly hacky. Code in question:

    #tab is there to help the player distinguish between menu commands and game text [game text is indented]
    player_cards = "  Your cards are : "
    
    for card in player_hand:
      #adds card value and a space onto the end of player_cards for each card in hand
      player_cards += str(card) + " "
      
    #the exercise required score reporting for each card the player drew, so score updates accordingly
    player_score_is = (f"and your score is {get_score(player_hand)}")
    #prints player card string and their score
    print(player_cards + player_score_is)
    
It's not too bad all things considered. But it is hacky. I'm kind of happy with the way the program turned out, it was accomplished one step above the 'expert difficulty' [with no reference whatsoever to the exercise hints] so while it is true that dicts are tacked on, I had no reference to go by except what I'd learned in GML previously. Granted my experience does include a survival solitaire card game engine 🤔 with animations, a deck, discard pile, library of different cards... I should probably go back to it sometime
