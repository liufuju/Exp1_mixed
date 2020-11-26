from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import os, json, pandas

class Alignment_info(Page):
    form_model = 'player'
    form_fields = ['name', 'student_id', 'exp_date']


class Instruction(Page):
    def before_next_page(self):
        pwd = os.getcwd()
        emo_order_file = self.session.config['order_file']
        dscp_file = 'emo_dscp_future.js'

        folder = 'reference'
        dscp_path = os.path.join(pwd, folder, dscp_file)
        order_path = os.path.join(pwd, folder, emo_order_file)

        with open(dscp_path, 'r', encoding='utf-8') as file_object:
            dscp_data = json.load(file_object)

        if self.session.config['mode'] == 0:
            order, order_code = order_retrieval(order_path)
        elif self.session.config['mode'] == 1:
            order, order_code = order_retrieval_future(order_path)

        emotions = order
        emo_dscp = [dscp_data[i] for i in emotions]

        self.participant.vars['emotions'] = emotions
        self.participant.vars['emo_dscp'] = emo_dscp

        self.player.emo_order = '_'.join(emotions)
        self.player.emo_order_code = order_code

    def vars_for_template(self):
        exp_theme = '回忆' if self.session.config['mode'] == 0 else '想象'
        return dict(
            exp_theme=exp_theme
        )


page_sequence = [Instruction, Alignment_info]


def order_retrieval(order_path):
    order_data = pandas.read_table(order_path, sep='\t')
    for i in range(24):
        used = order_data['used'].iloc[i]
        get = used == 0
        if get:
            order_data.iloc[i, 1] = 1
            order = [
                order_data['0'].iloc[i],
                order_data['1'].iloc[i],
                order_data['2'].iloc[i],
                order_data['3'].iloc[i],
                order_data['4'].iloc[i]
            ]
            order_code = order_data['code'].iloc[i]
            break
        continue

    order_data.to_csv(order_path, sep='\t', index=False)

    return order, order_code


def order_retrieval_future(order_path):
    order_data = pandas.read_table(order_path, sep='\t')
    for i in range(108):
        used = order_data['used'].iloc[i]
        get = used == 0
        if get:
            order_data.iloc[i, 1] = 1
            order = [
                order_data['0'].iloc[i],
                order_data['1'].iloc[i],
                order_data['2'].iloc[i]
            ]
            order_code = order_data['code'].iloc[i]
            break
        continue

    order_data.to_csv(order_path, sep='\t', index=False)

    return order, order_code