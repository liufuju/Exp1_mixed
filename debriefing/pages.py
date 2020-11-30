from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Debriefing(Page):
    def vars_for_template(self):
        exp_theme = '回忆' if self.session.config['mode'] == 0 else '想象'
        return dict(
            theme=exp_theme
        )

    form_model = 'player'
    form_fields = ['difficulty_debrief', 'purpose_debrief', 'imagination_diff', 'disturbance']


class Video(Page):
    pass


page_sequence = [Debriefing, Video]
