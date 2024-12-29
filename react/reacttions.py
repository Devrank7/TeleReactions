from enum import Enum
from typing import Optional


class React(Enum):
    LIKE = {"index": 0, "type": "👍"}
    DISLIKE = {"index": 1, "type": "👎"}
    HEART = {"index": 2, "type": "❤"}
    FIRE = {"index": 3, "type": "🔥"}
    IN_LOVE = {"index": 4, "type": "🥰"}
    CLAP = {"index": 5, "type": "👏"}
    GRINNING = {"index": 6, "type": "😁"}
    THINKING = {"index": 7, "type": "🤔"}
    MINDBLOWN = {"index": 8, "type": "🤯"}
    SCREAM = {"index": 9, "type": "😱"}
    RAGING = {"index": 10, "type": "🤬"}
    CRYING = {"index": 11, "type": "😢"}
    PARTY = {"index": 12, "type": "🎉"}
    STARSTRUCK = {"index": 13, "type": "🤩"}
    NAUSEATED = {"index": 14, "type": "🤮"}
    POOP = {"index": 15, "type": "💩"}
    PRAY = {"index": 16, "type": "🙏"}
    OK_HAND = {"index": 17, "type": "👌"}
    DOVE = {"index": 18, "type": "🕊"}
    CLOWN = {"index": 19, "type": "🤡"}
    YAWNING = {"index": 20, "type": "🥱"}
    WOOZY = {"index": 21, "type": "🥴"}
    LOVESTRUCK = {"index": 22, "type": "😍"}
    WHALE = {"index": 23, "type": "🐳"}
    HEART_ON_FIRE = {"index": 24, "type": "❤‍🔥"}
    MOON_FACE = {"index": 25, "type": "🌚"}
    HOTDOG = {"index": 26, "type": "🌭"}
    HUNDRED = {"index": 27, "type": "💯"}
    ROFL = {"index": 28, "type": "🤣"}
    LIGHTNING = {"index": 29, "type": "⚡"}
    BANANA = {"index": 30, "type": "🍌"}
    TROPHY = {"index": 31, "type": "🏆"}
    BROKEN_HEART = {"index": 32, "type": "💔"}
    SKEPTICAL = {"index": 33, "type": "🤨"}
    NEUTRAL = {"index": 34, "type": "😐"}
    STRAWBERRY = {"index": 35, "type": "🍓"}
    CHAMPAGNE = {"index": 36, "type": "🍾"}
    KISS = {"index": 37, "type": "💋"}
    MIDDLE_FINGER = {"index": 38, "type": "🖕"}
    DEVIL = {"index": 39, "type": "😈"}
    SLEEPY = {"index": 40, "type": "😴"}
    SOBBING = {"index": 41, "type": "😭"}
    NERD = {"index": 42, "type": "🤓"}
    GHOST = {"index": 43, "type": "👻"}
    CODER = {"index": 44, "type": "👨‍💻"}
    EYES = {"index": 45, "type": "👀"}
    PUMPKIN = {"index": 46, "type": "🎃"}
    SEE_NO_EVIL = {"index": 47, "type": "🙈"}
    ANGEL = {"index": 48, "type": "😇"}
    ANXIOUS = {"index": 49, "type": "😨"}
    HANDSHAKE = {"index": 50, "type": "🤝"}
    WRITING = {"index": 51, "type": "✍"}
    HUGGING = {"index": 52, "type": "🤗"}
    SANTA = {"index": 53, "type": "🎅"}
    CHRISTMAS_TREE = {"index": 54, "type": "🎄"}
    SNOWMAN = {"index": 55, "type": "☃"}
    NAIL_POLISH = {"index": 56, "type": "💅"}
    ZANY = {"index": 57, "type": "🤪"}
    MOAI = {"index": 58, "type": "🗿"}
    COOL = {"index": 59, "type": "🆒"}
    HEART_ARROW = {"index": 60, "type": "💘"}
    HEAR_NO_EVIL = {"index": 61, "type": "🙉"}
    UNICORN = {"index": 62, "type": "🦄"}
    KISSING = {"index": 63, "type": "😘"}
    PILL = {"index": 64, "type": "💊"}
    SPEAK_NO_EVIL = {"index": 65, "type": "🙊"}
    SUNGLASSES = {"index": 66, "type": "😎"}
    ALIEN = {"index": 67, "type": "👾"}
    SHRUG_MAN = {"index": 68, "type": "🤷‍♂"}
    SHRUG = {"index": 69, "type": "🤷"}
    SHRUG_WOMAN = {"index": 70, "type": "🤷‍♀"}
    ANGRY = {"index": 71, "type": "😡"}

    @staticmethod
    def get_reactions_by_index(index: int) -> Optional['React']:
        for reaction in React:
            if reaction.value["index"] == index:
                return reaction
        return None
