winner_found= 0 #Global variable is 0 unitl a winner is found.

def main():
	print("Welcome to Tic Tac Toe!")
	player_1= input("Player 1, enter your name: ")
	player_2= input("Player 2, enter your name: ")

	print(f"\n{player_1}, you'll be X. You make the first move.")
	print(f"{player_2}, you'll be O. You go after {player_1}.\n")
	in_game(player_1, player_2)

	while True:
	    winner_found= 0
	    replay_the_game= input("Do you want to replay?\nEnter 'Y' or 'N' for 'yes' and 'no' respectively.")
	    if replay_the_game== 'Y':
	        in_game(player_1, player_2)
	    else:
	        print("Thank you!")
	        break


def check_winner(d, player_1= 'Rakhshanda', player_2= 'Raqeeba'):
    '''
    This function is going to help us check for winners.
    
    INPUT: dict
    OUTPUT: Displays the winner or concludes a draw for the round.
    '''
    list_of_values= list(d.values())
    diagonal_list_1= list_of_values[0::4]
    diagonal_list_2= list_of_values[2:7:2] 
    winner_X= ['X']*3
    winner_O= ['O']*3
    
    if (diagonal_list_1== winner_X or diagonal_list_2== winner_X):
        return 'X'
    elif (diagonal_list_1== winner_O or diagonal_list_2== winner_O):
        return 'O'
    
    for i in range(0, len(list_of_values)-1,3):
        if list_of_values[i:i+3:1]==winner_X:  
            return 'X'
        elif list_of_values[i:i+3:1]==winner_O:
            return 'O'
        else: 
            continue

    for i in range(0, len(list_of_values)-1,1):
        if list_of_values[i:i+7:3]==winner_X:   
            return 'X'
        elif list_of_values[i:i+7:3]==winner_O:
            return 'O'
        else: 
            continue
    
    return 'Draw'


def game_board(d, total_turns, player_1= 'Rakhshanda', player_2= 'Raqeeba'):
    '''
    This is going to print the game board with all the inputs
    given in form of X's and O's by each player. 
    
    INPUT: int 
    OUTPUT: 
                 |     |     
              7  |  8  | 9  
            _____|_____|_____
                 |     |     
              4  |  5  | 6  
            _____|_____|_____
                 |     |     
              1  |  2  | 3 
                 |     |     
    '''
    global winner_found
    
    for i in range(9,2,-3):
        print("     |     |     ")
        print(f"  {d[i-2]}  |  {d[i-1]}  | {d[i]}  ")
        if(i!=3):
            print("_____|_____|_____")
        elif(i==3):
            print("     |     |     ")

    result= check_winner(d, player_1, player_2)
    if result== 'X':
        winner_found+=1
        print(f"\n{player_1}, congratultions!\nYou won the game!")
    elif result== 'O':
        winner_found+=1
        print(f"\n{player_2}, congratultions!\nYou won the game!")
    elif result== 'Draw'and total_turns== 9:
        print("\nIt's a draw!")


def in_game(player_1= 'Rakhshanda', player_2= 'Raqeeba'):
    '''
    This is the main game function. It takes the user input and
    deals with the replay option accordingly.
    '''
    global winner_found
      
    #Variables counting each player's turns
    turn_player_1= 0
    turn_player_2= 0
      
    #Creating a default dictionary with keys and corresponding 
    #values values ranging from 1-9.
    inputs_given= {x: f"{x}" for x in range(1, 10)}  
      
    #Calling game_board() to print the number pad for giving players 
    #the needed instructions. 
    game_board(inputs_given,turn_player_1)
    print("\nThat is how the number pad looks like.")
    print("You must enter values between 1 and 9.")
    
    #Replacing all values with blank spaces to be later occupied by X's and O's.
    inputs_given= {x: " " for x in range(1, 10)}  
    
    while ((turn_player_1<5 and turn_player_2<=4) and not winner_found):
        if(turn_player_1==0 or turn_player_1<=turn_player_2):
            player_1_input= int(input(f"\n{player_1}, you want to place your X at?"))
            
            #Checking for valid inputs. No duplicates allowed.
            #No number except in range 1-9 allowed.
            if(player_1_input in range (1,10) and inputs_given[player_1_input]== " "): 
                inputs_given[player_1_input]= 'X'
                turn_player_1+=1
            else:
                print("Invalid input given. Try again\n")
                continue
        else:  
            player_2_input= int(input(f"\n{player_2}, you want to place your O at?"))           
            if(player_2_input in range (1,10) and inputs_given[player_2_input]== " "): 
                inputs_given[player_2_input]= 'O'
                turn_player_2+=1
            else:
                print("Invalid input given. Try again\n")
                continue

        #Calling the game_board() where the actual board will be displayed and 
        #the result will be calculated within it using the check_winner().
        game_board(inputs_given, turn_player_1+turn_player_2, player_1, player_2)

if __name__ == '__main__':
	main()