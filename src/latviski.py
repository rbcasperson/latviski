from src.tools.db_entries import Noun, Verb, Word
import shelve
import random



class Latviski:

    def run_command(self, options):
        """Parse the options from the CLI input and run the appropriate command."""
        with shelve.open("./vārdi") as db:
            self.db = db

            if options["add"]:
                self.add_word(options["<word>"], options["<part-of-speech>"])

            if options["test"]:
                word = options["<word>"]
                if word in self.db:
                    self.db[word].test()
                else:
                    print(f"There is no word '{word}' in your dictionary!")

    def add_word(self, word, part_of_speech):
        if part_of_speech == "verb":
            self.db[word] = Verb(word)
        elif part_of_speech == "noun":
            self.db[word] = Noun(word)
        else:
            self.db[word] = Word(word)

    def test_verb(self, verb):
        try:
            translations = list(self.db[verb]["present"].items())
            translations += list(self.db[verb]["past"].items())
            translations += list(self.db[verb]["future"].items())
            random.shuffle(translations)

            answers = {latvian: {"actual": input(f"{latvian} > "), "correct": english} for english, latvian in translations}

            total_correct = len([answer for answer in answers.values() if answer["correct"] == answer["actual"]])
            print(f"You scored {total_correct} out of {len(answers)}: {(total_correct/len(answers)) * 100} %")
        except KeyError:
            print("no!!")

