from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'demographics'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    RACE = [dict(name='isWhite', label="White"),
            dict(name='isBlack', label="Black or African American"),
            dict(name='isNative', label="American Indian or Alaskan Native"),
            dict(name='isAsian', label="Asian or Native Hawaiian or Pacific Islander"),
            dict(name='isOther', label="Some other race"),
            dict(name='isNone', label="Prefer not to say")]
    GENDER = [dict(name='isMale', label="Cis male"),
              dict(name='isFemale', label="Cis female"),
              dict(name='isTrans', label="Nonbinary/Trans/Other"),
              dict(name='isNoneGender', label="Prefer not to say")]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    isWhite = models.BooleanField(blank=True)
    isBlack = models.BooleanField(blank=True)
    isNative = models.BooleanField(blank=True)
    isAsian = models.BooleanField(blank=True)
    isOther = models.BooleanField(blank=True)
    isNone = models.BooleanField(blank=True)

    isMale = models.BooleanField(blank=True)
    isFemale = models.BooleanField(blank=True)
    isTrans = models.BooleanField(blank=True)
    isNoneGender = models.BooleanField(blank=True)

    isHispanic = models.IntegerField(
        label='Are you of Hispanic, Latino, or Spanish origin?',
        widget=widgets.RadioSelect,
        choices=[
            [1, 'Yes'],
            [2, 'No'],
            [3, 'Prefer not to say']])
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )

    answer = models.IntegerField(
        label=""
    )


# FUNCTIONS
# PAGES
class Instructions(Page):
    form_model = 'player'


class Race(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return [r['name'] for r in C.RACE]

    @staticmethod
    def error_message(player: Player, values):
        # print('values is', values)
        num_selected = 0
        for r in C.RACE:
            if values[r['name']]:
                num_selected += 1
        if num_selected < 1:
            return "You must select at least 1 race."


class Hispanic(Page):
    form_model = 'player'
    form_fields = ['isHispanic']


class Gender(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return [g['name'] for g in C.GENDER]

    @staticmethod
    def error_message(player: Player, values):
        # print('values is', values)
        num_selected = 0
        for g in C.GENDER:
            if values[g['name']]:
                num_selected += 1
        if num_selected < 1:
            return "You must select at least 1 gender."


class Debrief(Page):
    form_model = 'player'


page_sequence = [Instructions, Race, Hispanic, Gender, Debrief]
