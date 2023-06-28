import random
from IPython.display import clear_output
import art
import game_data


def calculate_result(first_person_follower_count, second_person_follower_count):
    if first_person_follower_count > second_person_follower_count:
        return "A"
    else:
        return "B"


listed_persons = []
actual_choices = []
free_persons = game_data.data


def show_choices(score):
    if score == 0:
        person_a = free_persons[random.randint(0, len(free_persons) - 1)]
        free_persons.remove(person_a)
        listed_persons.append(person_a)

        person_b = free_persons[random.randint(0, len(free_persons) - 1)]
        free_persons.remove(person_b)
        listed_persons.append(person_b)

        actual_choices.clear()
        actual_choices.append(person_a)
        actual_choices.append(person_b)
    else:
        person_a = listed_persons[len(listed_persons) - 1]

        person_b = free_persons[random.randint(0, len(free_persons) - 1)]
        free_persons.remove(person_b)
        listed_persons.append(person_b)

        actual_choices.clear()
        actual_choices.append(person_a)
        actual_choices.append(person_b)

    print(f"Compare A: {person_a['name']}, {person_a['description']}, from {person_a['country']}.")
    print(art.vs)
    print(f"Against B: {person_b['name']}, {person_b['description']}, from {person_b['country']}.")

    return actual_choices


def game():
    print(art.logo)
    score = 0
    game_over = False

    while not game_over:
        clear_output()
        options = show_choices(score)
        person_a_follower_count = options[0]['follower_count']
        person_b_follower_count = options[1]['follower_count']

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        if answer == calculate_result(person_a_follower_count, person_b_follower_count):
            score += 1
            print(f"You are right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong! Final score: {score}.")
            game_over = True

game()
