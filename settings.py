from os import environ

SESSION_CONFIGS = [
    dict(
        name='Exp1_mixed_future',
        display_name="Exp1_mixed_future",
        num_demo_participants=3,
        app_sequence=['instructions', 'main', 'debriefing'],
        mode=1,
        order_file='order.txt'
    ),
    dict(
        name='Exp1_mixed_past',
        display_name="Exp1_mixed_past",
        num_demo_participants=3,
        app_sequence=['instructions', 'main', 'debriefing'],
        mode=0,
        order_file='order.txt'
    ),
    dict(
        name='Exp1_mixed_past_female',
        display_name="Exp1_mixed_past_female",
        num_demo_participants=3,
        app_sequence=['instructions', 'main', 'debriefing'],
        mode=0,
        order_file='order_past_female.txt'
    ),
    dict(
        name='Exp1_mixed_past_male',
        display_name="Exp1_mixed_past_male",
        num_demo_participants=3,
        app_sequence=['instructions', 'main', 'debriefing'],
        mode=0,
        order_file='order_past_male.txt'
    ),
    dict(
        name='Exp2_future',
        display_name='Exp2_future',
        num_demo_participants=3,
        app_sequence=['instructions', 'novel_combination', 'novel_future', 'debriefing'],
        mode=1,
        order_file='order_future.txt'
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'zh-hans'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'b+%cj3b*wx5bc_yz_zig0n8zi!yy=@t54erpy40d2*_iwv)p5c'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
