from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Background(Page):
    def before_next_page(self):
        self.participant.vars['age'] = self.player.age
        self.participant.vars['city'] = self.player.city

    form_model = 'player'
    form_fields = ['age', 'city']


class Novel_combination(Page):
    def vars_for_template(self):
        age = self.participant.vars['age']
        city = self.participant.vars['city']

        return dict(
            age=age,
            city=city,
        )

    def before_next_page(self):
        persons = [self.player.person1, self.player.person2, self.player.person3, self.player.person4, self.player.person5]
        places = [self.player.place1, self.player.place2, self.player.place3, self.player.place4, self.player.place5]

        two_persons = random.sample(persons, 3)
        two_places = random.sample(places, 3)

        self.participant.vars['combinations'] = dict(
            persons=two_persons,
            places=two_places
        )

    form_model = 'player'
    form_fields = [
        'person1', 'person2', 'person3', 'person4', 'person5',
        'place1', 'place2', 'place3', 'place4', 'place5'
    ]


page_sequence = [Background, Novel_combination]
