"""This is an integration of everything I have learned about programming
through python."""

__author__ = "Kevin Rodriguez"

# any code using try and except I learned through the class website, w3schools
# and this website:
# https://betterprogramming.pub/handling-errors-in-python-9f1b32952423


def main():
    """This is the starting point of the program, and it contains most of
    the code in the program apart from function definitions."""

    print("Welcome to my integration program, I hope you find it interesting!")

    # NBA themed lines of code about certain players
    curry = ("Steph Curry! " * 3)
    print("My favorite sport is basketball and my favorite player is", curry)
    print("Steph Curry is currently", 20 + 12, "years old.")

    # This code will quiz you on what has happened in the program so far
    print("Pop quiz time! I'm going to test you to see if "
          "you have been paying attention!")
    pop_quiz = False
    while not pop_quiz:
        print("A. Chris Paul, B. Stephen Curry, C. Lebron James")
        fav_player = input("Who is my favorite player from the "
                           "above list(input letter option): ")
        player_age = input("How old is this player: A. 32, B. 27, C. 30: ")
        print((fav_player == "B") and (player_age == "A"))
        if fav_player == "B" and player_age == "A":
            print("Congratulations, you passed!")
            pop_quiz = True
        else:
            print("You have failed the pop quiz, please try again "
                  "I'm sure you will get it this time.")
    print("Done!")
    # introduces which team Steph plays for
    print("From the below choices, pick the team you "
          "think Steph plays for by picking a number from 1 - 5 "
          "or pick number 6 if you do not know the answer.")
    team_selection = False
    while not team_selection:
        try:

            print("1. Golden State Warriors")
            print("2. Miami Heat")
            print("3. Los Angeles Lakers")
            print("4. Dallas Mavericks")
            print("5. Portland Trail Blazers")
            print("6. I do not know the answer to this.")
            team_pick = int(input("Choose a number:"))
            if team_pick == 1:
                print("Correct! Curry does indeed play for the", team_pick,
                      "as their main superstar player.")
                team_selection = True
            elif team_pick == 6:
                print("It's okay if you didn't know the answer, thank you "
                      "for trying.")
                print("Steph Curry plays for the Golden State Warriors as "
                      "their top superstar player.")
                team_selection = True
            elif team_pick != 1:
                print("Not quite correct. You might have to freshen up "
                      "on your NBA knowledge. Please try again.")
            else:
                print("Incorrect input.")
        except ValueError:
            print("Incorrect input, please try again.")

    # program gives more information about Steph
    print("Let's talk about what kind of player Steph is.")
    print("First up, let's find out how many points "
          "Steph is averaging this NBA season.")
    print("You will be given three tries to guess correctly or "
          "close enough to the correct answer. After three tries you will be "
          "given the right answer.")
    number_tries = 0
    while number_tries < 3:
        try:
            ave_points = int(input("How many points do you think Steph is "
                                   "currently averaging in this "
                                   "season (give a rough estimate):"))
            print((ave_points >= 28) and (ave_points <= 30))
            if 28 <= ave_points <= 30:
                number_tries = 3
            elif ave_points <= 27 or ave_points >= 31:
                print("Your guess wasn't close enough to the correct answer.")
                number_tries += 1
            else:
                print("Not a valid input, please try again.")
        except ValueError:
            print("Incorrect input, please try again")
    print(
        "If your guess was either 29 or between numbers 28-30, good "
        "job because Steph is averaging 29 points per game! "
        "If it wasn't, thank your trying. ")
    print("Done!")

    # gives user more information about the type of player steph is
    print("Next is to learn what position Steph plays.")
    print("In basketball there are 5 different positions a player can "
          "play depending on the players height, physical attributes and "
          "skill set which include: \n1. Point Guard "
          "\n2. Shooting Guard \n3. Small Forward "
          "\n4. Power Forward \n5. Center")
    print("Hint: Steph is 6'3 in.")
    position_tries = False
    while not position_tries:
        try:
            position_guess = int(input("What position do you think Steph plays"
                                       " (input either number digit 1-5):"))
            if position_guess == 1:
                print("Correct! Steph is a point guard. In fact, Steph "
                      "is considered the best point guard in the NBA!")
                position_tries = True
            elif position_guess == 2:
                print("Incorrect! While Steph could play as a shooting guard "
                      "since their average height is 6'5 in, he is still "
                      "not considered a shooting guard.")
            elif position_guess == 3:
                print("Incorrect! Steph is too small to play small "
                      "forward because their average height is 6'8 in.")
            elif position_guess == 4:
                print("Incorrect! The average height for power forwards is "
                      "around 6'8 - 7'0 inches which is a "
                      "huge difference from Steph height.")
            elif position_guess == 5:
                print("Incorrect! Centers are usually 7'0 - 7'3, "
                      "and they definitely can't shoot as well as Steph.")
            else:
                print("Not a valid input, please try again.")
        except ValueError:
            print("Error due to wrong input, please try again.")

    print("Done!")

    print("Next let's do a quick fun fact question.")
    fun_fact_question = input("Do you think Steph has ever scored more than "
                              "62 points in a game. Answer with yes or no:")
    if fun_fact_question == "yes":
        print(not (fun_fact_question == "no"))
        print("Correct, Steph has actually scored up to "
              "62 points which he did earlier this season.")
    else:
        print(not 'no')
        print("Incorrect, Steph has actually scored up to "
              "62 points which he did earlier this season.")

    # code needed for the def calc_ave_points program
    print("The next program will allow you to calculate average "
          "points Steph has scored after x amount of \ngames and y "
          "amount of points which you will input.")
    # the following code I learned through the website
    # https://betterprogramming.pub/handling-errors-in-python-9f1b32952423
    # as well as the class website and w3schools.
    program_cont = False
    while not program_cont:
        try:
            tot_games = 0
            pts_game = 0
            amt_games_input = int(input("Input how many games Steph played to "
                                        "calculate average points per game:"))
            total_average_ppg = calc_ave_points(tot_games, pts_game,
                                                amt_games_input)
            print("Steph averaged", format(total_average_ppg, '0.2f'),
                  end=' points per game in a total of ' + str(
                      amt_games_input) + ' games.')
            program_cont = True
        except ValueError:
            print("Error due to wrong input, please try again.")
        except ZeroDivisionError:
            print("Error due to wrong input, please try again.")

    # code needed for the def calc_seasonal_ave_points program
    print("\nSimilar to the previous program, this "
          "program will calculate average points per \nseason after x amount "
          "of games and y amount of points per season.")
    program_cont2 = False
    while not program_cont2:
        try:
            total_seasons = 0
            total_points_in_season = 0
            amount_seasons_played = int(
                input("\nInput the total amount of seasons "
                      "Steph has played:"))
            total_ave_pps = calc_seasonal_ave_points(total_seasons,
                                                     total_points_in_season,
                                                     amount_seasons_played)
            print("Steph averaged", format(total_ave_pps, '0.2f'),
                  end=' points per season in a total of ' + str(
                      amount_seasons_played) + ' seasons played. ')
            average_ppg_in_season = total_ave_pps / 81
            total_games_played = amount_seasons_played * 81
            print("\nThere are 81 games in a season, which means Steph "
                  "averaged",
                  format(average_ppg_in_season, '0.2f'),
                  end=' points per game \neach season in a total of ' + str(
                      total_games_played) + ' games played.')
            program_cont2 = True
        except ValueError:
            print("Error due to wrong input, please try again.")
        except ZeroDivisionError:
            print("Error due to wrong input, please try again.")

    # code needed for def calculate_salary
    program_cont3 = False
    while not program_cont3:
        try:
            seasonal_payment = 40.23
            print("\nCurry is currently getting paid around",
                  format(seasonal_payment, "0.2f"), sep=' $',
                  end=' million per season due to his great level of play. ')
            print("\nCalculate how much Steph would make after x amount "
                  "of seasons.")
            salary_seasons = int(
                input("\nEnter amount of seasons for salary calculation: "))
            total_salary_made = calculate_salary(seasonal_payment,
                                                 salary_seasons)
            print("After " + str(salary_seasons) + " seasons, Steph will "
                                                   "have been paid ""close to",
                  format(total_salary_made, "0.2f"), sep=' $',
                  end=' million, which is one \nof the highest '
                      'paid contracts in the entire league!')
            program_cont3 = True
        except ValueError:
            print("Error due to wrong input, please try again.")

    # allows user to calculate average points after x amount
    # of games and y amount of points in each game


def calc_ave_points(total_games, points_game, amount_games_input):
    """

    :param total_games: Holds value of total amount of games Steph has played
    :param points_game: Holds value of total amount of points
    :param amount_games_input: Holds input from user of amount of games user
    wants to calculate
    :return: Returns the average points per game
    """
    for average_points in range(amount_games_input):
        points_in_game = int(input("Enter how many points Steph scored "
                                   "in the game:"))
        total_games += 1
        points_game += points_in_game
        points_game / total_games
    return points_game / total_games

    # allows user to calculate average points after x
    # amount of seasons and y amount of points per season


def calc_seasonal_ave_points(total_seasons2, total_points_in_season2,
                             amount_seasons_played2):
    """

    :param total_seasons2: Holds the value of total seasons played
    :param total_points_in_season2: Holds value of total points in all
    seasons combined
    :param amount_seasons_played2: Holds input from user for amount of
    seasons user wants to calculate
    :return: returns the average amount of points scored per season
    """
    for average_points_per_season in range(amount_seasons_played2):
        points_per_season = int(input("Enter how many points Steph scored in "
                                      "that season:"))
        total_points_in_season2 += points_per_season
        total_seasons2 += 1
        total_points_in_season2 / total_seasons2
    return total_points_in_season2 / total_seasons2

    # program calculates Steph salary


def calculate_salary(seasonal_payment2, salary_seasons2):
    """

    :param seasonal_payment2: holds the value of how much steph gets paid
    every season
    :param salary_seasons2: holds input value from user of total seasons
    user wants to use for calculation
    :return: returns the value of total amount of money steph would make
    after x amount of seasons
    """
    result_salary = seasonal_payment2 * salary_seasons2
    return result_salary


if __name__ == "__main__":
    main()
