import itertools
import shelve
import random


PRONOUNS = ["Es", "Tu", "Viņš/Viņa", "Mēs", "Jūs", "Viņi/Viņas"]


class Latviski:

    def run_command(self, options):
        """Parse the options from the CLI input and run the appropriate command."""
        with shelve.open("./vārdi") as db:
            self.db = db

            if options["add"]:
                if options["<part-of-speech>"] == "verb":
                    self.add_verb(options["<word>"])
                elif options["<part-of-speech>"] == "noun":
                    self.add_noun(options["<word>"])
                else:
                    print("Invalid part of speech.")

            if options["test"]:
                self.test_verb(options["<word>"])

    def add_verb(self, verb):
        print(f"Please provide the necessary information about '{verb}'")
        db_entry = {}

        for tense in ["present", "past", "future"]:
            print(f"{tense.capitalize()} Tense:")
            db_entry[tense] = {f"{article} {input('{0} > '.format(article))}": None for article in PRONOUNS}

        print("Please translate each of the following into English.")
        for tense in db_entry:
            db_entry[tense] = {latvian: input(f"{latvian} > ") for latvian in db_entry[tense]}

        self.db[verb] = db_entry

    def test_verb(self, verb):
        try:
            translations = list(self.db[verb]["present"].items())
            translations += list(self.db[verb]["past"].items())
            translations += list(self.db[verb]["future"].items())
            random.shuffle(translations)

            answers = {english: {"actual": input(f"{english} > "), "correct": latvian} for english, latvian in translations}

            total_correct = len([answer for answer in answers.values() if answer["correct"] == answer["actual"]])
            print(f"You scored {total_correct} out of {len(answers)}: {(total_correct/len(answers)) * 100} %")
        except KeyError:
            print("no!!")

    def add_noun(self, noun):
        pass

