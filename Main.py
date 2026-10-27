# Create an Intramural score tracker
score = 0
# Each team entry is a list that includes
#   - Name
#   - Games Played
#   - Wins
#   - Losses
#   - Ties
#   - Goals For
#   - Goals Against

# You will ask how many teams are playing.
numteams=int(input("How many teams are playing? "))
# Loop that many times according to user input for example if user typed 3 then ask user "what''s team 1 what's team 2 what's team 3?", create the teams and set all scores to 0, then append it to your list of teams
for number in range(1,numteams+1):
    teamname=input(f"What is the name of team #{number}?")
# Start an infinite loop for main menu, make a menu first then user input
def menu():
    print("[4] score")
    print("[3] team stats")
    print("[2] team score")
    print("[1] quit")

menu()
option = int(input("Enter your choice:"))

while True:
    if option not in menu:
        print('Please enter a valid option')
        continue

     if option == 4:


#   1) Add score
#   2) See Team stats
#   3) See Overall Standings
#   4) Quit
#if goals are the same, look for GF.
#if gf and goals aare the same, look for who has the fewer goals against.

#   1) Enter team 1, team 2, goals for team 1, goals for team 2
#       - Find the teams, update the games played, add the goals for and against, and decide if it's a win, lose or tie

#   2) Print a list of team names.
#       Once the user selects, Print out their stats

#   3) Print out the teams in order from most team points to least
#   - Team points = wins*2 + ties*1
#   - If they have the same points, look for most goals for
#   - If they have the same goals for, take the least goals against.
#   - If those are the same, then just output the teams.

#   4) Say goodbye and break out of the loop