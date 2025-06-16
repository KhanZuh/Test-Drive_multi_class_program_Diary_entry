class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries


    def count_words(self):
        return sum(entry.count_words() for entry in self.entries)


    def reading_time(self, wpm):
        return sum(entry.reading_time(wpm) for entry in self.entries)


    def find_best_entry_for_reading_time(self, wpm, minutes):
        max_words = wpm * minutes # Figure out the most words the person can read in the given time
        best_entry = None
        best_word_count = 0

        for entry in self.entries:
            entry_word_count = entry.count_words()
            if entry_word_count <= max_words and entry_word_count > best_word_count:
                best_entry = entry
                best_word_count = entry_word_count

        return best_entry



