from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'elicitation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    rating = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[1, 2, 3, 4]
    )


# FUNCTIONS
# PAGES
class Instructions(Page):
    form_model = 'player'


class Rating(Page):
    form_model = 'player'
    form_fields = ['rating']


page_sequence = [Instructions, Rating]
