from abc import ABC, abstractmethod

from db.mongodb.connect import get_collection


class MongoService(ABC):
    @abstractmethod
    def commit(self):
        raise NotImplementedError


class CreateChanel(MongoService):

    def __init__(self, chat_id: int):
        self.chat_id = chat_id

    def get_default_document(self):
        return {
            "_id": self.chat_id,
            "data": [
                {
                    "index": 0,
                    "rarity": 0.33
                },
                {
                    "index": 5,
                    "rarity": 0.33
                },
                {
                    "index": 7,
                    "rarity": 0.34
                }
            ]
        }

    def commit(self):
        collections = get_collection()
        docx = collections.find_one({"_id": self.chat_id})
        if docx is None:
            collections.insert_one(self.get_default_document())
            return self.get_default_document()
        return docx


class AddReactions(MongoService):
    def __init__(self, chat_id: int, reaction_id: int, rarity: float):
        self.chat_id = chat_id
        self.reaction_id = reaction_id
        self.rarity = rarity

    def commit(self):
        collection = get_collection()
        collection.update_one(
            {
                "_id": self.chat_id,
                "data.index": {"$ne": self.reaction_id}
            },
            {
                "$push": {"data": {"index": self.reaction_id, "rarity": self.rarity}}
            }
        )


class RemoveReactions(MongoService):
    def __init__(self, chat_id: int, reaction_id: int):
        self.chat_id = chat_id
        self.reaction_id = reaction_id

    def commit(self):
        collection = get_collection()
        collection.update_one(
            {"_id": self.chat_id},
            {"$pull": {"data": {"index": self.reaction_id}}}
        )


class GetReact(MongoService):
    def __init__(self, chat_id: int):
        self.chat_id = chat_id

    def commit(self):
        react = get_collection().find_one({"_id": self.chat_id})
        if react is None:
            return CreateChanel(self.chat_id).commit()
        return react
