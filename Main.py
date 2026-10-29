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
teams=[]
# Loop that many times according to user input for example if user typed 3 then ask user "what''s team 1 what's team 2 what's team 3?", create the teams and set all scores to 0, then append it to your list of teams
for number in range(1,numteams+1):
    name=input(f"What is the name of team #{number}?")
    team=[name,0,0,0,0,0,0,0]
    teams.append(team)

for i in range(len(teams)):
    print(teams[i][0])
# Start an infinite loop for main menu, make a menu first then user input
choice=0
while choice!=1:
    print("MENU")
    print("[4] score")
    print("[3] team stats")
    print("[2] team score")
    print("[1] quit")

    choice = int(input("Enter your choice(1-4):"))


    if choice == 4:
        print("teams:")
        for count, team in enumerate(teams, start=1):
            print(f"Team #{count}: {team}")
        while True:
            t1_num = int(input("Enter your team number:"))
            t2_num = int(input("Enter your team number:"))

            team1 = teams[t1_num - 1]
            team2 = teams[t2_num - 1]

            while True:
                t1_goals = int(input(f"Enter goals scored by {team1[0]}:"))
                     t2_goals = int(input(f"Enter goals scored by {team2[0]}:"))
                     team1[1] = team1[1] + 1
                     team2[1] = team2[1] + 1

                     team1[5] = team1[5] + t1_goals
                     team1[6] = team1[6] + t2_goals
                     team2[5] = team2[5] + t1_goals
                     team2[6] = team2[6] + t2_goals

                     if t1_goals > t2_goals:
                         team1[2] = team1[2] + 1
                         team2[3] = team2[3] + 1
                        print(f"{team1} won by {t1_goals}-{t2_goals}")
                     elif t1_goals < t2_goals:
                         team2[3] = team2[3] + 1
                         team1[2] = team1[2] + 1
                         print(f"{team2} won by {t2_goals}-{t1_goals}")
                     else:
                     team1[4] = team1[4] + 1
                     team2[4] = team2[4] + 1
                       print(f"The match ended in a {t1_goals}-{t2_goals} tie!")

                        team1[7] = (team1[2] * 2) + (team1[4] * 1)
                        team2[7] = (team2[2] * 2) + (team2[4] * 1)

    elif choice == 3:
        pass

    elif choice == 2:
        pass

    elif choice == 1:
        print("goodbye.")
        break

    else:
        print("Invalid choice")


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