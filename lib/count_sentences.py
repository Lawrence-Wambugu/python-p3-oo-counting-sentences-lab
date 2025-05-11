import re

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Triggers setter validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Split on punctuation that typically ends sentences
        sentences = re.split(r'[.!?]+', self._value)
        # Filter out empty strings and whitespace-only strings
        return len([s for s in sentences if s.strip()])
