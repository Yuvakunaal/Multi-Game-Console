import random
def game(number):
    if number == 1:
        print("---------- Rock, Paper & Scissor ---------")
        rules = '''
        Rock + Scissor -> Rock wins
        Scissor + Paper -> Scissor wins
        paper + Rock -> Paper wins
        '''
        print("Rules :", rules)

        win1 = 0
        win2 = 0
        count = 1
        while True:
            print("Game :", count)
            print("Choose any one you wish :\n1 - Rock \n2 - Scissor \n3 - Paper")
            person_choice = int(input("Enter your choice : "))
            while person_choice > 3 or person_choice < 1:
                person_choice = int(input("Enter valid choice : "))
            if person_choice == 1:
                choice = "Rock"
                print("User choice :", choice)
            elif person_choice == 2:
                choice = "Scissor"
                print("User choice :", choice)
            else:
                choice = "Paper"
                print("User choice :", choice)
            print("Now its computer turn !!!")
            comp_choice = random.randint(1, 3)
            while comp_choice == person_choice:
                comp_choice = random.randint(1, 3)
            if comp_choice == 1:
                choice1 = "Rock"
                print("Computer choice :", choice1)
            elif comp_choice == 2:
                choice1 = "Scissor"
                print("Computer choice :", choice1)
            else:
                choice1 = "Paper"
                print("Computer choice :", choice1)
            if person_choice == comp_choice:
                result = "Draw"
            elif (person_choice == 1 and comp_choice == 2):
                result = choice
            elif (person_choice == 2 and comp_choice == 1):
                result = choice1

            if (person_choice == 2 and comp_choice == 3):
                result = choice
            elif (person_choice == 3 and comp_choice == 2):
                result = choice1

            if (person_choice == 3 and comp_choice == 1):
                result = choice
            elif (person_choice == 1 and comp_choice == 3):
                result = choice1
            if result is choice:
                win1 += 1
                print("<<<<<<<* You won !!! *>>>>>>>")
            elif result is choice1:
                win2 += 1
                print("<<<<<<<* Computer won !!! *>>>>>>>")
            print()
            print("Do you want to play again ? (y/n) :", end=" ")
            a = input().lower()
            print()
            if a == "n":
                break
            else:
                count += 1
        print("---------------------------------------\nFinal Stats (Rock, Paper & Scissors) :-")
        print("You won : ", win1, "/", count)
        print("Computer won : ", win2, "/", count,"\n---------------------------------------")

    elif number == 2:
        print("---------- Snakes & Ladder ---------")

        print("---> Rules :-\n\n1. To roll die click on anything on keyboard(including enter button).")
        print("2. To quit the game click n.\n")
        print("3. Ladder : 3 -> 25")
        print("          : 33 -> 48")
        print("          : 38 -> 59")
        print("          : 71 -> 90")
        print("          : 79 -> 99\n")
        print("4. Snake : 31 -> 29")
        print("         : 41 -> 22")
        print("         : 66 -> 56")
        print("         : 92 -> 69")
        print("         : 98 -> 35 <---\n")
        print("Give the names of players :-")

        count = 1
        name_1 = input("Player-1 name : ")
        name_2 = input("Player-2 name : ")
        win1 = 0
        win2 = 0
        while True:
            print("*** Game : ", count, "***")
            p1_score = 1
            p2_score = 1
            print(name_1, "at : ", p1_score)
            print(name_2, "at : ", p2_score)
            print("Game starts now !!!\n")
            while True:
                print(name_1 + "'s turn", end="")
                p1 = input(" spin (yes or no) : ")
                if p1 == "n":
                    print(name_1, "quitted\n", name_2, "won !!!!")
                    break
                else:
                    spin = random.randint(1, 6)
                    print("🎲 : ", spin)
                    p1_score += spin
                    if p1_score < 100:
                        print(name_1, "at : ", p1_score)
                        if p1_score == 3:
                            print("<<< Ladder >>>")
                            p1_score = 25
                            print(name_1, "at : ", p1_score, "\n")
                        elif p1_score == 38:
                            print("<<< Ladder >>>")
                            p1_score = 59
                            print(name_1, "at : ", p1_score, "\n")
                        elif p1_score == 33:
                            print("<<< Ladder >>>")
                            p1_score = 48
                            print(name_1, "went to : ", p1_score, "\n")
                        elif p1_score == 79:
                            print("<<< Ladder >>>")
                            p1_score = 99
                            print(name_1, "went to : ", p1_score, "\n")
                        elif p1_score == 71:
                            print("<<< Ladder >>>")
                            p1_score = 90
                            print(name_1, "went to : ", p1_score, "\n")
                        elif p1_score == 41:
                            print("<<< Snake >>>")
                            p1_score = 22
                            print(name_1, "went to : ", p1_score, "\n")
                        elif p1_score == 31:
                            print("<<< Snake >>>")
                            p1_score = 29
                            print(name_1, "went to : ", p1_score, "\n")
                        elif p1_score == 98:
                            print("<<< Snake >>>")
                            p1_score = 35
                            print(name_1, "went to : ", p1_score, "\n")
                        elif p1_score == 92:
                            print("<<< Snake >>>")
                            p1_score = 69
                            print(name_1, "went to : ", p1_score, "\n")
                        elif p1_score == 66:
                            print("<<< Snake >>>")
                            p1_score = 56
                            print(name_1, "went to : ", p1_score, "\n")
                    elif p1_score == 100:
                        print(name_1, "won !!! (by reaching 100)")
                        win1 += 1
                        break
                    else:
                        p1_score -= spin
                        print(name_1, "at : ", p1_score)
                        print("------------------------------------------------")
                print(name_2 + "'s turn", end="")
                p2 = input(" spin (yes or no) : ")
                if p2 == "n":
                    print(name_2, "quitted\n", name_1, "won !!!!")
                    break
                else:
                    spin = random.randint(1, 6)
                    print("🎲 : ", spin)
                    p2_score += spin
                    if p2_score < 100:
                        print(name_2, "at : ", p2_score)
                        if p2_score == 3:
                            print("<<< Ladder >>>")
                            p2_score = 25
                            print(name_2, "went to : ", p2_score, "\n")
                        elif p2_score == 38:
                            print("<<< Ladder >>>")
                            p2_score = 59
                            print(name_2, "went to : ", p2_score, "\n")
                        elif p2_score == 33:
                            print("<<< Ladder >>>")
                            p2_score = 48
                            print(name_2, "went to : ", p2_score, "\n")
                        elif p2_score == 79:
                            print("<<< Ladder >>>")
                            p2_score = 99
                            print(name_2, "went to : ", p2_score, "\n")
                        elif p2_score == 71:
                            print("<<< Ladder >>>")
                            p2_score = 90
                            print(name_2, "went to : ", p2_score, "\n")
                        elif p2_score == 41:
                            print("<<< Snake >>>")
                            p2_score = 22
                            print(name_2, "went to : ", p2_score, "\n")
                        elif p2_score == 31:
                            print("<<< Snake >>>")
                            p2_score = 29
                            print(name_2, "went to : ", p2_score, "\n")
                        elif p2_score == 98:
                            print("<<< Snake >>>")
                            p2_score = 35
                            print(name_2, "went to : ", p2_score, "\n")
                        elif p2_score == 92:
                            print("<<< Snake >>>")
                            p2_score = 69
                            print(name_2, "went to : ", p2_score, "\n")
                        elif p2_score == 66:
                            print("<<< Snake >>>")
                            p2_score = 56
                            print(name_2, "went to : ", p2_score, "\n")
                        print("------------------------------------------------")
                    elif p2_score == 100:
                        print(name_2, "won !!! (by reaching 100)")
                        win2 += 1
                        break
                    else:
                        p2_score -= spin
                        print(name_2, "at :", p2_score)
                        print("------------------------------------------------")
            print("\nDo you want to play again ? (y/n) :", end=" ")
            a = input().lower()
            print()
            if a == "n":
                break
            else:
                count += 1
                continue
        print("---------------------------------------\nFinal Stats (Snakes & Ladder):-")
        print(name_1, "won :", win1, "/", count)
        print(name_2, "won :", win2, "/", count,"\n---------------------------------------")

    elif number == 3:
        l = [["a", "b", "c"],
             ["d", "e", "f"],
             ["g", "h", "i"]]
        print("---------- TIC - TAC - TOE ---------")
        print(
            "Rules :-\nObserve the box given below, When you're asked to enter position of X or O.\nYou have to enter these positions (in terms of alphabets given below) as per your specification...")
        print("|", l[0][0][0], l[0][1][0], l[0][2][0], "|\n" + "|", l[1][0][0], l[1][1][0], l[1][2][0], "|\n" + "|",
              l[2][0][0], l[2][1][0], l[2][2][0], "|")
        print()
        print(
            "InGame rules :-\nPerson-1 takes X,Person-2 takes O\nWho gets the first vertical or horizontal or cross matching elements (X or O) will win the game...")
        print()
        count = 1
        win1 = 0
        win2 = 0
        draw = 0
        while True:
            print("Game :", count, ":-")
            l1 = [[[" "], [" "], [" "]],
                  [[" "], [" "], [" "]],
                  [[" "], [" "], [" "]]]
            el1 = []
            el2 = []
            a = 0
            user1 = input("Person-1's turn, Enter position : ")
            user1.lower()
            while user1 not in ("a", "b", "c", "d", "e", "f", "g", "h", "i"):
                user1 = input(
                    "Warning !!! Given wrong / position given before...\nPerson-1's turn, Enter position again : ")
            if user1 == "a":
                user1 = [0, 0]
            elif user1 == "b":
                user1 = [0, 1]
            elif user1 == "c":
                user1 = [0, 2]
            elif user1 == "d":
                user1 = [1, 0]
            elif user1 == "e":
                user1 = [1, 1]
            elif user1 == "f":
                user1 = [1, 2]
            elif user1 == "g":
                user1 = [2, 0]
            elif user1 == "h":
                user1 = [2, 1]
            elif user1 == "i":
                user1 = [2, 2]
            l1[user1[0]][user1[1]] = ("X")
            el2.append(user1[0])
            el2.append(user1[1])
            el1.append(el2)
            print("|", l1[0][0][0], l1[0][1][0], l1[0][2][0], "|                             |", l[0][0][0], l[0][1][0],
                  l[0][2][0], "|\n|", l1[1][0][0], l1[1][1][0], l1[1][2][0], "|                             |",
                  l[1][0][0], l[1][1][0], l[1][2][0], "|\n|", l1[2][0][0], l1[2][1][0], l1[2][2][0],
                  "|                             |", l[2][0][0], l[2][1][0], l[2][2][0], "|")
            print()
            for i in range(4):
                user2 = input("Person-2's turn, Enter position : ")
                user2.lower()
                while user2 not in ("a", "b", "c", "d", "e", "f", "g", "h", "i"):
                    user2 = input(
                        "Warning !!! Given wrong / position given before...\nPerson-2's turn, Enter position again : ")
                if user2 == "a":
                    user2 = [0, 0]
                elif user2 == "b":
                    user2 = [0, 1]
                elif user2 == "c":
                    user2 = [0, 2]
                elif user2 == "d":
                    user2 = [1, 0]
                elif user2 == "e":
                    user2 = [1, 1]
                elif user2 == "f":
                    user2 = [1, 2]
                elif user2 == "g":
                    user2 = [2, 0]
                elif user2 == "h":
                    user2 = [2, 1]
                elif user2 == "i":
                    user2 = [2, 2]
                while user2 in el1:
                    user2 = input(
                        "Warning !!! Given wrong / position given before...\nPerson-2's turn, Enter position again : ")
                    if user2 == "a":
                        user2 = [0, 0]
                    elif user2 == "b":
                        user2 = [0, 1]
                    elif user2 == "c":
                        user2 = [0, 2]
                    elif user2 == "d":
                        user2 = [1, 0]
                    elif user2 == "e":
                        user2 = [1, 1]
                    elif user2 == "f":
                        user2 = [1, 2]
                    elif user2 == "g":
                        user2 = [2, 0]
                    elif user2 == "h":
                        user2 = [2, 1]
                    elif user2 == "i":
                        user2 = [2, 2]
                l1[user2[0]][user2[1]] = ("O")
                el2 = []
                el2.append(user2[0])
                el2.append(user2[1])
                el1.append(el2)
                print("|", l1[0][0][0], l1[0][1][0], l1[0][2][0], "|                             |", l[0][0][0],
                      l[0][1][0], l[0][2][0], "|\n|", l1[1][0][0], l1[1][1][0], l1[1][2][0],
                      "|                             |", l[1][0][0], l[1][1][0], l[1][2][0], "|\n|", l1[2][0][0],
                      l1[2][1][0], l1[2][2][0], "|                             |", l[2][0][0], l[2][1][0], l[2][2][0],
                      "|")

                print()
                if l1[0][0] == l1[0][1] == l1[0][2] == 'X' or l1[1][0] == l1[1][1] == l1[1][2] == 'X' or l1[2][0] == \
                        l1[2][1] == l1[2][2] == 'X' or l1[0][0] == l1[1][0] == l1[2][0] == 'X' or l1[0][1] == l1[1][
                    1] == l1[2][1] == 'X' or l1[0][2] == l1[1][2] == l1[2][2] == 'X' or l1[0][0] == l1[1][1] == l1[2][
                    2] == 'X' or l1[2][0] == l1[1][1] == l1[0][2] == 'X':
                    win1 += 1
                    print("Hurrah!!!\n<<<< Person-1 won >>>>")
                    a = 1
                    break
                elif l1[0][0] == l1[0][1] == l1[0][2] == 'O' or l1[1][0] == l1[1][1] == l1[1][2] == 'O' or l1[2][0] == \
                        l1[2][1] == l1[2][2] == 'O' or l1[0][0] == l1[1][0] == l1[2][0] == 'O' or l1[0][1] == l1[1][
                    1] == l1[2][1] == 'O' or l1[0][2] == l1[1][2] == l1[2][2] == 'O' or l1[0][0] == l1[1][1] == l1[2][
                    2] == 'O' or l1[2][0] == l1[1][1] == l1[0][2] == 'O':
                    win2 += 1
                    print("Hurrah!!!\n<<<< Person-2 won >>>>")
                    a = 2
                    break

                user1 = input("Person-1's turn, Enter position : ")
                user1.lower()
                while user1 not in ("a", "b", "c", "d", "e", "f", "g", "h", "i"):
                    user1 = input(
                        "Warning !!! Given wrong / position given before...\nPerson-1's turn, Enter position again : ")
                if user1 == "a":
                    user1 = [0, 0]
                elif user1 == "b":
                    user1 = [0, 1]
                elif user1 == "c":
                    user1 = [0, 2]
                elif user1 == "d":
                    user1 = [1, 0]
                elif user1 == "e":
                    user1 = [1, 1]
                elif user1 == "f":
                    user1 = [1, 2]
                elif user1 == "g":
                    user1 = [2, 0]
                elif user1 == "h":
                    user1 = [2, 1]
                elif user1 == "i":
                    user1 = [2, 2]
                while user1 in el1:
                    user1 = input(
                        "Warning !!! Given wrong / position given already...\nPerson-1's turn, Enter position again : ")
                    if user1 == "a":
                        user1 = [0, 0]
                    elif user1 == "b":
                        user1 = [0, 1]
                    elif user1 == "c":
                        user1 = [0, 2]
                    elif user1 == "d":
                        user1 = [1, 0]
                    elif user1 == "e":
                        user1 = [1, 1]
                    elif user1 == "f":
                        user1 = [1, 2]
                    elif user1 == "g":
                        user1 = [2, 0]
                    elif user1 == "h":
                        user1 = [2, 1]
                    elif user1 == "i":
                        user1 = [2, 2]
                l1[user1[0]][user1[1]] = ("X")
                el2 = []
                el2.append(user1[0])
                el2.append(user1[1])
                el1.append(el2)
                print("|", l1[0][0][0], l1[0][1][0], l1[0][2][0], "|                             |", l[0][0][0],
                      l[0][1][0], l[0][2][0], "|\n|", l1[1][0][0], l1[1][1][0], l1[1][2][0],
                      "|                             |", l[1][0][0], l[1][1][0], l[1][2][0], "|\n|", l1[2][0][0],
                      l1[2][1][0], l1[2][2][0], "|                             |", l[2][0][0], l[2][1][0], l[2][2][0],
                      "|")

                print()
                if l1[0][0] == l1[0][1] == l1[0][2] == 'X' or l1[1][0] == l1[1][1] == l1[1][2] == 'X' or l1[2][0] == \
                        l1[2][1] == l1[2][2] == 'X' or l1[0][0] == l1[1][0] == l1[2][0] == 'X' or l1[0][1] == l1[1][
                    1] == l1[2][1] == 'X' or l1[0][2] == l1[1][2] == l1[2][2] == 'X' or l1[0][0] == l1[1][1] == l1[2][
                    2] == 'X' or l1[2][0] == l1[1][1] == l1[0][2] == 'X':
                    win1 += 1
                    print("Hurrah!!!\n<<<< Person-1 won 😎 >>>>")
                    a = 1
                    break
                elif l1[0][0] == l1[0][1] == l1[0][2] == 'O' or l1[1][0] == l1[1][1] == l1[1][2] == 'O' or l1[2][0] == \
                        l1[2][1] == l1[2][2] == 'O' or l1[0][0] == l1[1][0] == l1[2][0] == 'O' or l1[0][1] == l1[1][
                    1] == l1[2][1] == 'O' or l1[0][2] == l1[1][2] == l1[2][2] == 'O' or l1[0][0] == l1[1][1] == l1[2][
                    2] == 'O' or l1[2][0] == l1[1][1] == l1[0][2] == 'O':
                    win2 += 1
                    print("Hurrah!!!\n<<<< Person-2 won 😎 >>>>")
                    a = 2
                    break

            if a == 0:
                draw += 1
                print("\n<<<< Its a Draw 🤝🏻 >>>>")
            print("Do you want to play again ? (y/n) :", end=" ")
            a = input().lower()
            print()
            if a == "n":
                break
            else:
                print("Same game rules every time....\n")
                count += 1
                continue

        print("---------------------------------------\nFinal Stats (Tic-Tac-Toe) :-")
        print("Person-1 won : ", win1, "/", win1 + win2 + draw, "games")
        print("Person-2 won : ", win2, "/", win1 + win2 + draw, "games")
        print("Drawn : ", draw, "/", win1 + win2 + draw, "games","\n---------------------------------------")

    else:
        print("Invalid game code...re-enter game code which you want to play...")
        game_ = int(input("Enter game code : "))
        return game(game_)

print("Games:-")
games='''
| Code |        Game           |
|------------------------------|
| 1    | Rock, Paper & Scissor |
| 2    | Snake & Ladder        |
| 3    | Tic-Tac-Toe           |
'''
print(games)
while True:
    print("Click on game code which you want to play...")
    game_ = int(input("Enter game code : "))
    game(game_)
    ch = input("Do you wanna play another game (y/n) : ")
    if ch=="y":
        print("Click on game code which you want to play...")
        game_ = int(input("Enter game code : "))
        game(game_)
    else:
        print("\n  😊 THANK YOU 😊")
        break