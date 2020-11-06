from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Debriefing(Page):
    form_model = 'player'
    form_fields = ['difficulty_debrief', 'purpose_debrief', 'imagination_diff', 'disturbance']


class Video(Page):
    pass


page_sequence = [Debriefing, Video]
