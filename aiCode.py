import random
from modules import wow_vars

def character_printer():
    character_bucket = []
    name_bucket = []
    name_odds = random.randint(2, 3)

    random_class = random.choice(wow_vars.class_dict["wow_classes"])
    random_race = random.choice(random_class["races"])

    character_bucket.append(wow_vars.wow_races[random_race])
    character_bucket.append(random_class["wow_class"])

    for _ in range(name_odds):
        name_select = random.choice(wow_vars.name_chunks)
        name_bucket.append(name_select)

    name_result = "".join(name_bucket)
    character_bucket.append(name_result)

    result = " ".join(character_bucket)
    return result


character = character_printer()

print(character)
