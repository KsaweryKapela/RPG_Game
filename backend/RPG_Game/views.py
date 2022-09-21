from rest_framework.response import Response
from rest_framework.decorators import api_view
from RPG_Game.game_content.classes import Character


@api_view(['POST'])
def update_stats(request):
    if request.method == 'POST':
        new_character = Character()
        print(new_character.attributes)
        new_character.update_stats(request.data)
        print(new_character.attributes)
        return Response(request.data)


