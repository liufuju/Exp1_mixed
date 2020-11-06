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
    name_in_url = 'debriefing'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    difficulty_debrief = models.LongStringField(label='')
    imagination_diff = models.LongStringField(label='')
    disturbance = models.LongStringField(label='')
    purpose_debrief = models.LongStringField(label='')

