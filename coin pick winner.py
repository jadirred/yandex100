
# the major function which calls the minor recursive function
# with additional parameters
def coin_pick_winner(n):
    games = []  # a list of all possible games with a certain n 
    first_win = [] # a list of critical n's  from which the first player wins
    second_win = [] #a list of critical n's  from which the second player wins
    # now we call the additional recursive function with additional parameters
    # in order to make recursive step (step in the game)
    final_list = coin_pick_winner_turns(n, n, 1, games) 
    #here I print the final list in order to show you the format of a
    #final list
    print(final_list)
    # you can see we have the list of lists (each list has 3 elements: 
        #the previous n, the current n, the final number of turns)
    for i in final_list:
        #we check whether the number of turns is odd when the game ends
        #it indicates that the first player wins
        if (i[2]%2)==1:
            #we check whether the winning step comes after the same 
            #previous crucial n in order not to include duplicates
            if i[0] not in first_win:
                first_win.append(i[0])
        else:
                second_win.append(i[0])
    #if we have any winning combinations for the first player
    #we return true and count different n's which comes before the 
    #winning step            
    if len(first_win)>0:
         return(True, len(first_win))
    else:
         return(False, len(second_win))

#the minor recursive function
#parameters: prev - previous n, n - current n, turns - turns counter
#games - the list (empty by default) to which we add the game after the
#winning step    
def coin_pick_winner_turns(prev, n, turns, games):
    #to check that n is positive is crucial in order to avoid
    #endless recursion
    if n>0:
        #the basis state: when n=1 or 2 or 3 from the very beginning
        #of the last winning step
        if n==1 or n==2 or n==4:
           games.append([prev, n, turns])
           #if we put small n's =1,2,4 we still want to check another
           #winning combinations
           if (turns == 1):
               coin_pick_winner_turns(n, n-1, turns+1, games)
               coin_pick_winner_turns(n, n-2, turns+1, games)
               coin_pick_winner_turns(n, n-4, turns+1, games)             
        else:
            #pay attention this is the recursive step
            #we check all three options (1,2,3) ans we always count turns
            coin_pick_winner_turns(n, n-1, turns+1, games)
            coin_pick_winner_turns(n, n-2, turns+1, games)
            coin_pick_winner_turns(n, n-4, turns+1, games)
    #we return the list of lists in order to work with it in the major function
    return(games)

print(coin_pick_winner(3))