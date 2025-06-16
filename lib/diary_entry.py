import math

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words_read_so_far = 0


    def count_words(self):
        title_words = self.title.split()
        content_words = self.contents.split()
        return len(title_words) + len(content_words)
    
    def reading_time(self, wpm):
        total_words = self.count_words()
        minutes = total_words/wpm
        return math.ceil(minutes)
    
    def reading_chunk(self, wpm, minutes):
        words_list = (self.title + " " + self.contents).split() # Combine title and contents into one string, then split into words
        total_words_can_read = int(minutes * wpm) # Calculate the total number of words the user can read in the given time

        if self.words_read_so_far >= len(words_list): # If we've already read all words, reset to start from the beginning
            self.words_read_so_far = 0

        chunk = words_list[self.words_read_so_far:self.words_read_so_far + total_words_can_read] # Select the next chunk of words to read based on how many words can be read
        self.words_read_so_far += len(chunk) # Update the position to mark these words as read for next time

        return " ".join(chunk) # Join the chunk list back into a string and return it
