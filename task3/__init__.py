from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'task3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    answer = models.IntegerField()
    t3_rawscore = models.IntegerField()

    compchoice = models.IntegerField(
        label='When you are ready, please make your selection below.',
        widget=widgets.RadioSelect,
        choices=[
            [1, 'Task 1 (Piece rate) scheme'],
            [2, 'Task 2 (Tournament) scheme'], ])

    # a function to add tentative earnings to the build-in payff variable
    def add_payoff(self):
        self.payoff += round(self.session.config['real_world_currency_per_point'] * self.t3_rawscore)


# FUNCTIONS
# PAGES
class Instructions(Page):
    form_model = 'player'


class Task3(Page):
    form_model = 'player'
    form_fields = ['answer',
                   't3_rawscore']
    timeout_seconds = 60

    def before_next_page(player, timeout_happened):
        player.add_payoff()


class Choice(Page):
    form_model = 'player'
    form_fields = ['compchoice']


page_sequence = [Instructions, Choice, Task3]