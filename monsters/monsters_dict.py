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
    range(80, 90): 'Very hostile and ready to fight',
    range(90, 100): 'Raging like a demon'
})

animal_adjectives_dict = RangeDict({
    range(0, 5): 'Small',
    range(5, 15): 'Medium',
    range(15, 30): 'Grand',
    range(30, 45): 'Gigantic',
    range(45, 60): 'Colossal'
})
