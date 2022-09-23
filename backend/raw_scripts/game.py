from backend.raw_scripts.character_creation import MainCharacter


new_character = MainCharacter()
new_character.create_character()
print(new_character.attributes)
new_character.spend_attribute_points()
print(new_character.attributes)
