import logging
from collections import defaultdict

from peewee import *

logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

db = SqliteDatabase('todo_app.db')


class BaseModel(Model):
    class Meta:
        database = db


class Card(BaseModel):
    id = CharField(primary_key=True, unique=True)
    name = CharField()

    @staticmethod
    def get_all():
        """
        return : Cards with corresponding items{
            <card_id> : {
                "name": string,
                "items": [
                    {
                        "id": int,
                        "name": string,
                        "completed": boolean
                    }
                ]
            },
            ...
        }
        """
        cards = Card.select(
            Card.id.alias('card_id'), Card.name.alias('card_name')).dicts()
        items = Items.select(Card.id.alias('card_id'), Items.id, Items.name, Items.completed) \
            .join(Card).dicts()
        ret = defaultdict(dict)
        for c in cards:
            ret[c['card_id']]['name'] = c['card_name']
            ret[c['card_id']]['items'] = []
        for item in items:
            if "id" in item:
                ret[item['card_id']]['items'].append({
                    "id": item['id'],
                    "name": item['name'],
                    "completed": item['completed']
                })
        return ret


class Items(BaseModel):
    id = AutoField()
    name = CharField()
    completed = BooleanField(default=False)
    card = ForeignKeyField(Card, backref='items')
