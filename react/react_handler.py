import random

from db.mongodb.service import GetReact
from react.reacttions import React


class Reactor:
    def weighted_random_choice(self, data) -> dict:
        weights = [item['rarity'] for item in data]
        choices = data
        chosen = random.choices(choices, weights=weights, k=1)
        return chosen[0]

    def get_react(self, chat_id: int):
        react = GetReact(chat_id).commit()
        element = self.weighted_random_choice(react['data'])
        react_type = React.get_reactions_by_index(element['index'])
        return react_type.value['type']
