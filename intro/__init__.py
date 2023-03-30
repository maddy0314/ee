from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pq = models.IntegerField(
        label='Consider the problem above. What is the sum of the five numbers?',
    )

    # a function to add tentative earnings to the build-in payff variable
    def add_payoff(self):
        self.payoff += 5


# FUNCTIONS
# PAGES
class Disclaimer(Page):
    pass


class Intro(Page):
    pass


class PracticeQuestion(Page):
    form_model = 'player'
    form_fields = ['pq']

    def before_next_page(player, timeout_happened):
        player.add_payoff()


page_sequence = [Disclaimer, Intro, PracticeQuestion]
