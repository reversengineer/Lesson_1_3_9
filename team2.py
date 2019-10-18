####
# Each team's file must define four tokens:
#     team_name: 
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Tyler' # Only 10 chars displayed.
strategy_name = 'Commit to Master'
strategy_description = "It doesn't decide, the master does."
    
def move(my_history, their_history, my_score, their_score):
    real_result = move(my_history, their_history, my_score, their_score)
    
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False
    
