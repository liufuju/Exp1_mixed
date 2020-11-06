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
    name_in_url = 'instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label='您的姓名')
    student_id = models.StringField(label='您的学号', max_length=12)
    exp_date = models.StringField(label='实验日期（年/月/日）')
    emo_order = models.StringField()
    emo_order_code = models.StringField()


