from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import os, random, pandas
import paramiko


class Instructions_main(Page):
    def is_displayed(self):
        return self.round_number == 2


class Instructions_prac(Page):
    def is_displayed(self):
        return self.round_number == 1


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
        person = self.participant.vars['combinations']['persons'][self.round_number - 1]
        place = self.participant.vars['combinations']['places'][self.round_number - 1]

        return dict(
            emotion=emotion,
            emo_dscp=emo_dscp,
            age=age,
            city=city,
            round_number=self.round_number - 1,
            person=person,
            place=place
        )

    def js_vars(self):
        emo = self.participant.vars['emotions'][self.round_number - 1]
        if emo in ['relaxation', 'desire']:
            emotion_type = 'positive'
        elif emo in ['anger', 'sadness']:
            emotion_type = 'negative'
        else:
            emotion_type = 'none'
        return dict(
            round_number=self.round_number,
            time_mode=self.session.config['mode'],
            emotion_type=emotion_type
        )

    def before_next_page(self):
        self.player.emo = self.participant.vars['emotions'][self.round_number - 1]
        self.player.alpha = 'practice' if self.round_number == 1 else self.participant.vars['alphas'][self.round_number - 2]

        rasp_number = self.session.config['rasp_number']
        client = ssh_connect(rasp_number)
        work_on_my_video(client, 'sudo rm -rf /var/log/motion/motion.log')
        work_on_my_video(client, 'sudo service motion start')
        work_on_my_video(client, 'sudo rm -rf /var/log/motion/motion.log')
        work_on_my_video(client, 'sudo service motion start')
        work_on_my_video(client, 'sudo motion')
        client.close()

    form_model = 'player'
    form_fields = ['short_dscp', 'exact_time', 'event_core', 'event_specification']


class Imagination(Page):
    def vars_for_template(self):
        event = self.player.short_dscp
        event_core = self.player.event_core
        if self.round_number == 1:
            sound = 'practice'
        else:
            sound = 'forehead_{}'.format(self.player.alpha)
        action_sound = 'sound/{}.mp3'.format(sound)

        return dict(
            event=event,
            event_core=event_core,
            action_sound=action_sound
        )

    def before_next_page(self):
        rasp_number = self.session.config['rasp_number']
        client = ssh_connect(rasp_number)
        work_on_my_video(client, 'sudo service motion stop')
        client.close()


class Question_filling(Page):
    def vars_for_template(self):
        gotcha_num = random.choice(range(1, 8))
        gotcha_drct = random.choice([0, 1])
        drct_str = ['左数第{}项', '右数第{}项']
        self.player.gotcha_ans = abs(8 * gotcha_drct - gotcha_num)

        return dict(
            gotcha_label=drct_str[gotcha_drct].format(gotcha_num),
        )


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


class Description(Page):
    def vars_for_template(self):
        event = self.player.short_dscp
        event_core = self.player.event_core
        return dict(
            event=event,
            event_core=event_core,
        )

    def js_vars(self):
        return dict(
            round_number=self.round_number
        )

    form_model = 'player'
    form_fields = ['dscp_emo']


def ssh_connect(rasp_number):
    HOST = '39.105.99.86'
    USER = 'pi'
    PWD = 'horace13940349!!'
    PORTs = [6000, 5000, 4000]

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=HOST, port=PORTs[rasp_number - 1], username=USER, password=PWD)

    return client


def work_on_my_video(client, command):
    (stdin, stdout, stderr) = client.exec_command(command)


page_sequence = [Instructions_main, Instructions_prac, Emo_evoketion, Composition, Imagination,
                 Question_filling, Description]
