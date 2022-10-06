from characters.races.npc_races import Bear, Raccoon, Hedgehog
from functions.range_dictionary import RangeDict

monsters_dict = {
    'Forest_animal': [Bear, Raccoon, Hedgehog]
}

hostility_dict = RangeDict({
    range(0, 10): 'Very calm and friendly',
    range(10, 20): 'Calm and friendly',
    range(20, 30): 'Rather calm and friendly',
    range(30, 40): 'Alert but rather harmless',
    range(40, 50): 'Probably fight-averse',
    range(50, 60): 'Alert and rather hostile',
    range(60, 70): 'Alert and hostile',
    range(70, 80): 'Angry and hostile',
    range(80, 90): 'Very hostile and angry',
    range(90, 100): 'Extremely angry'
})

animal_adjectives_dict = RangeDict({
    range(0, 5): 'Small',
    range(5, 15): 'Medium',
    range(15, 30): 'Grand',
    range(30, 45): 'Gigantic',
    range(45, 60): 'Colossal'
})

level_differences_dict = RangeDict({
    range(-5, 5): 'You seem to be more or less equally strong',
    range(-10, -5): 'He seems to be stronger than you',
    range(-20, -10): 'He definitely is stronger than you',
    range(-100, -20): 'He will probably squash you',
    range(5, 10): 'You seem to be stronger than him',
    range(10, 20): 'You are definitely stronger than him',
    range(20, 100): 'You will probably squash him'

})
