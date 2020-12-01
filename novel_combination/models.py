from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'novel_combination'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='')
    city = models.StringField(label='')

    person1 = models.StringField(label='')
    person2 = models.StringField(label='')
    person3 = models.StringField(label='')
    person4 = models.StringField(label='')
    person5 = models.StringField(label='')

    place1 = models.StringField(label='')
    place2 = models.StringField(label='')
    place3 = models.StringField(label='')
    place4 = models.StringField(label='')
    place5 = models.StringField(label='')

