import itertools
import random
from src.tools.cli_tools import get_user_input, print_command
from src.tools.constants import PRONOUNS
import pydash as _


class Word:

    part_of_speech = None

    def __init__(self, word):
        self.value = word
        self.translation = get_user_input(f"What does '{word}' mean?")
        self.data = None

    def test(self):
        # Make this just test
        pass


class Verb(Word):

    part_of_speech = "verb"

    def __init__(self, verb):
        super(Verb, self).__init__(verb)

        self.data = {}
        for tense in ["present", "past", "future"]:
            print_command(f"Fill out the information for '{self.value}' in the {tense} tense:")
            self.data[tense] = {f"{article} {input('{0} '.format(article))}": None for article in PRONOUNS}

        print_command("Please translate each of the following into English.")
        for tense in self.data:
            print_command(f"{tense.capitalize()} Tense:")
            self.data[tense] = {latvian: input(f"{latvian} > ") for latvian in self.data[tense]}

        self.data["infinitive"] = {self.value: self.translation}

        self.all_conjugations = _.flatten([list(tense.items()) for tense in self.data.values()])

    def test(self):
        random.shuffle(self.all_conjugations)

        answers = {
            lv: {"actual": input(f"{lv} > "), "correct": en} for en, lv in self.all_conjugations
        }

        total_correct = len([answer for answer in answers.values() if answer["correct"] == answer["actual"]])
        print(f"You scored {total_correct} out of {len(answers)}: {(total_correct/len(answers)) * 100} %")



class Noun(Word):

    part_of_speech = "noun"

    def __init__(self, noun):
        super(Noun, self).__init__(noun)
        pass

    def test(self):
        pass
