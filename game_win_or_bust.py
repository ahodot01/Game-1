def play_game():
    limit = 238
    team_a_score = 0
    team_b_score = 0
    team_a_inputs = 0
    team_b_inputs = 0
    winning_team = None

# INTRODUCTION AND RULES
    print('\nWelcome to WIN OR BUST game!')
    print('\nRules: There are 2 teams: A and B. Each team has 3 players. \nEach player has one attempt to enter a number, three per team, six altogether.\nNumber must be between 1 and 200.')
    print('\nWinner allocation: All entered numbers from each team members \nwill be added up. Team with higher number wins, but sum must be lower than 238.\nOtherwise team, which exceeded this number will go BUST.')
    print('\nPrize distribution: Prize paid in GBP. Prize will equal winning \nnumber amount. But if other team went BUST, then prize will be made via also \nadding losing team score to the prize.')
    print('\nGame starts NOW!')

# MAIN LOOP WITH LIMITER OF 3 INPUTS PER TEAM. OTHERWISE: AUTOMATIC INPUT ASSIGNATION.
    while team_a_inputs < 3 or team_b_inputs < 3:
        for i in range(1, 7):
            while True:
                try:
                    player_num = int(input(f'\nEnter a number: '))
                    if 1 <= player_num <= 200:
                        while True:
                            if team_a_inputs < 3 and team_b_inputs < 3:
                                player_team = input("Add to Team A or B: ").upper()
                                if player_team not in ['A', 'B']:
                                    print("Invalid input! Please enter A or B!")
                                    continue
                            elif team_a_inputs >= 3:
                                print("Team A has already 3 inputs, automatically assigning to Team B.")
                                player_team = 'B'
                            else:
                                print("Team B has already 3 inputs, automatically assigning to Team A.")
                                player_team = 'A'

                            if player_team != 'A' and player_team != 'B':
                                pass
                            else:
                                break
                        break
                    else:
                        print('Error! Number must be between 1 and 200!')
                except ValueError:
                    pass

# BOTH TEAMS INPUTS CHECKER AND COUNTER
            if player_team == 'A' and team_a_inputs < 3:
                team_a_score += player_num
                team_a_inputs += 1
            elif player_team == 'B' and team_b_inputs < 3:
                team_b_score += player_num
                team_b_inputs += 1

# CHECK IF BOTH TEAMS HAVE 3 INPUTS
            if team_a_inputs == 3 and team_b_inputs == 3:
                break

# DRAW: BOTH BUSTED. RESTART.
        if team_a_score > limit and team_b_score > limit:
            print('\nBoth Teams busted. Draw! \nGame restarts...')
            team_a_score = 0
            team_b_score = 0
        elif team_a_score > limit:
            winning_team = 'B'
            prize = team_a_score + team_b_score
            print(f"\nScore of Team A is {team_a_score} and Score of Team B is {team_b_score}.")
            print(f'Team A busted! Team {winning_team} won! The prize is £{prize}.')
            print('\nMASSIVE CONGRATULATIONS! You earned a monster prize!!!')
            break
        elif team_b_score > limit:
            winning_team = 'A'
            prize = team_a_score + team_b_score
            print(f"\nScore of Team A is {team_a_score} and Score of Team B is {team_b_score}.")
            print(f'Team B busted! Team {winning_team} won. The prize is £{prize}.')
            print('\nMASSIVE CONGRATULATIONS! You earned a monster prize!!!')
            break

# DRAW: SAME SCORE. NOT BUSTED. RESTART.
        elif team_a_score == team_b_score:
            print('\nTeam A and B draw. Game restarts...')
            team_a_score = 0
            team_b_score = 0

# NOT DRAW:
        else:
            if team_a_score > team_b_score:
                winning_team = 'A'
                prize = team_a_score
                print(f"\nScore of Team A is {team_a_score} and Score of Team B is {team_b_score}.")
                print(f'Team {winning_team} won. The prize is £{prize}.')
                print('\nCONGRATULATIONS!')
                break
            else:
                winning_team = 'B'
                prize = team_b_score
                print(f"\nScore of Team A is {team_a_score} and Score of Team B is {team_b_score}.")
                print(f'Team {winning_team} won. The prize is £{prize}.')
                print('\nCONGRATULATIONS!')
                break

# "PLAY AGAIN" FUNCTION IN CASE OF:
# 1. NOT DRAW
# 2. NOT DRAW WHEN BOTH TEAM BUSTED
def main():
    playing = True
    while playing:
        play_game()
        while True:
            play_again = input("\nPlay again? (Y/Yes/N/No/...): ").lower()
            if play_again in ['y', 'yes']:
                break
            elif play_again in ['n', 'no']:
                playing = False
                print("\nThank you for playing! Bye!")
                break
            else:
                print("Invalid input. Please enter Y/yes or N/no!")

main()