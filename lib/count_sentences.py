#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        if not self.value.strip():
            return 0
        cleaned_value = self.value.replace("...", ".")
        # Split by `.`, `?`, `!` and count non-empty parts
        sentences = [s.strip() for s in re.split(r'[.?!]', cleaned_value) if s.strip()]
        return len(sentences)


