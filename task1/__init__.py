from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'task1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField()
    t1_rawscore = models.IntegerField()

    # a function to add tentative earnings to the build-in payff variable
    def add_payoff(self):
        self.payoff += round(self.session.config['real_world_currency_per_point'] * self.t1_rawscore)


# FUNCTIONS
# PAGES
class Instructions(Page):
    pass


class Task1(Page):
    form_model = 'player'
    form_fields = ['answer',
                   't1_rawscore']
    timeout_seconds = 60

    def before_next_page(player, timeout_happened):
        player.add_payoff()


page_sequence = [Instructions, Task1]
