# Tic Tac Toe game using Python

- User will be presented with the layout
- Users are X and O (upper case O)
- Game will print when a player wins or if it ends in a tie and then end the game
- Player will not be able to overwrite an already played spot. User will be prompted to try again before game moves to the next player
- If player enters a number outside of the range 0, 8 then a message will be shown and player will be prompted to try again.

## Assumption

- Not applicable in this verions as there is a check done for this. <<Player will always enter a valid spot to make the next move (in this case from 0 till 8)>>
- If user enters a negative or invalid number greater than 8 then the program cannot handle this situation.

## Improvement in this version

- When the game begins, it will ask player 1's and player 2's name.
- While declaring the result, it will declare using the name of the player instead of saying X won/O won like in previous version of the game.
- If player provides input for example alphabet(resulting in ValueError), then game will ask the user to provide input again.

## Wanted Improvement

- When player enters some garbage value then the program displays the string "<PlayerName's> turn". A good experience should be not display this string because we are already asking the same player to give the input.
