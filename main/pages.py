from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import os, pandas, random


class Instructions_main(Page):
    def is_displayed(self):
        return self.round_number == 2

    def vars_for_template(self):
        texts = Constants.text
        mode = self.session.config['mode']
        return dict(
            action=texts['action'][mode],
            time=texts['time'][mode]
        )


class Instructions_prac(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        texts = Constants.text
        mode = self.session.config['mode']
        return dict(
            action=texts['action'][mode],
            time=texts['time'][mode]
        )

class Background(Page):
    def before_next_page(self):
        self.participant.vars['age'] = self.player.age
        self.participant.vars['city'] = self.player.city

    def is_displayed(self):
        criterion = self.round_number == 1
        return criterion

    def vars_for_template(self):
        mode = self.session.config['mode']
        texts = Constants.text
        return dict(
            action=texts['action'][mode],
            direction=texts['direction'][mode]
        )

    form_model = 'player'
    form_fields = ['age', 'city']


class Composition(Page):
    def vars_for_template(self):
        pwd = os.getcwd()
        folder = 'reference'
        file_path = os.path.join(pwd, folder, 'composition.xlsx')
        cmp_data = pandas.read_excel(file_path)

        population = list(range(36))
        selection = random.sample(population, 4)
        information = []

        for i in selection:
            information += [[cmp_data['file'].iloc[i], cmp_data['big'].iloc[i], cmp_data['small'].iloc[i]]]

        self.player.cmp_ans1 = information[0][1]
        self.player.cmp_ans2 = information[1][2]
        self.player.cmp_ans3 = information[2][1]
        self.player.cmp_ans4 = information[3][1]

        return dict(
            cmp_pic1='compositions/' + information[0][0],
            cmp_pic2='compositions/' + information[1][0],
            cmp_pic3='compositions/' + information[2][0],
            cmp_pic4='compositions/' + information[3][0]
        )

    def is_displayed(self):
        return self.round_number != 1

    form_model = 'player'
    form_fields = ['cmp_response1', 'cmp_response2', 'cmp_response3', 'cmp_response4']


class Emo_evoketion(Page):
    def vars_for_template(self):
        emotion = self.participant.vars['emotions'][self.round_number - 1]
        emo_dscp = self.participant.vars['emo_dscp'][self.round_number - 1]
        age = self.participant.vars['age']
        city = self.participant.vars['city']
        texts = Constants.text
        mode = self.session.config['mode']

        return dict(
            emotion=emotion,
            emo_dscp=emo_dscp,
            age=age,
            city=city,
            round_number=self.round_number - 1,
            action=texts['action'][mode],
            direction=texts['direction'][mode]
        )

    def js_vars(self):
        return dict(
            round_number=self.round_number,
            time_mode=self.session.config['mode']
        )

    def before_next_page(self):
        self.player.emo = self.participant.vars['emotions'][self.round_number - 1]

    form_model = 'player'
    form_fields = ['short_dscp', 'exact_time', 'event_core']


class Imagination(Page):
    def vars_for_template(self):
        event = self.player.short_dscp
        event_core = self.player.event_core
        texts = Constants.text
        mode = self.session.config['mode']
        return dict(
            event=event,
            event_core=event_core,
            action=texts['action'][mode],
        )


class Question_filling(Page):
    form_model = 'player'
    form_fields = [
        'role_emo',
        'self_emo',
        'clear_emo',
        'isolate_emo',
        'sub_time',
        'vivid_emo',
        'valence_emo',
        'diff_emo',
        'gotcha'
    ]

    def vars_for_template(self):
        gotcha_num = random.choice(range(1, 8))
        gotcha_drct = random.choice([0, 1])
        drct_str = ['左数第{}项', '右数第{}项']
        self.player.gotcha_ans = abs(8 * gotcha_drct - gotcha_num)

        mode = self.session.config['mode']
        texts = Constants.text

        return dict(
            gotcha_label=drct_str[gotcha_drct].format(gotcha_num),
            action=texts['action'][mode],
            time=texts['time'][mode]
        )

class Description(Page):
    def vars_for_template(self):
        event = self.player.short_dscp
        event_core = self.player.event_core
        mode = self.session.config['mode']
        texts = Constants.text
        return dict(
            event=event,
            event_core=event_core,
            action=texts['action'][mode],
        )

    def js_vars(self):
        return dict(
            round_number=self.round_number
        )

    form_model = 'player'
    form_fields = ['dscp_emo']

class Rest(Page):
    def is_displayed(self):
        A = self.round_number == 3
        B = self.round_number != len(self.participant.vars['emotions'])
        return A & B

    def vars_for_template(self):
        return dict(
            left_percentage=round((self.round_number * 100) / 5)
        )


page_sequence = [Instructions_main, Instructions_prac, Background, Emo_evoketion, Composition, Imagination,
                 Question_filling, Description, Rest]
