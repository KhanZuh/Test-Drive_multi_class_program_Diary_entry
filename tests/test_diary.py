from lib.diary import Diary
from lib.diary_entry import DiaryEntry  

def test_find_best_entry_exact_fit():
    diary = Diary()
    # Adjusted to account for title words: "Medium" (1) + content (5) = 6 total
    entry1 = DiaryEntry("Short", "two three")  # 1 + 2 = 3 words
    entry2 = DiaryEntry("Medium", "two three four five six")  # 1 + 5 = 6 words  
    entry3 = DiaryEntry("Long", "two three four five six seven eight nine")  # 1 + 8 = 9 words

    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)

    # wpm = 2, minutes = 3 => max_words = 6
    result = diary.find_best_entry_for_reading_time(wpm=2, minutes=3)

    assert result == entry2
    assert result.title == "Medium"

def test_find_best_entry_under_limit():
    diary = Diary()
    entry1 = DiaryEntry("Tiny", "two")  # 1 + 1 = 2 words
    entry2 = DiaryEntry("Smaller", "")  # 1 + 0 = 1 word
    
    diary.add(entry1)
    diary.add(entry2)

    # wpm = 1, minutes = 3 => max_words = 3
    result = diary.find_best_entry_for_reading_time(wpm=1, minutes=3)

    assert result == entry1
    assert result.title == "Tiny"

def test_find_best_entry_none_fit():
    diary = Diary()
    entry1 = DiaryEntry("Too", "long one two three four")  # 1 + 5 = 6 words
    diary.add(entry1)

    # wpm = 1, minutes = 2 => max_words = 2
    result = diary.find_best_entry_for_reading_time(wpm=1, minutes=2)

    assert result is None

def test_find_best_entry_with_multiple_equal_entries():
    diary = Diary()
    entry1 = DiaryEntry("Entry1", "two three")  # 1 + 2 = 3 words
    entry2 = DiaryEntry("Entry2", "five six")   # 1 + 2 = 3 words

    diary.add(entry1)
    diary.add(entry2)

    # Both entries have 3 words, which fits max_words
    result = diary.find_best_entry_for_reading_time(wpm=1, minutes=3)

    # Should return the first one it encounters
    assert result == entry1

def test_find_best_entry_no_entries():
    diary = Diary()

    result = diary.find_best_entry_for_reading_time(wpm=10, minutes=1)

    assert result is None