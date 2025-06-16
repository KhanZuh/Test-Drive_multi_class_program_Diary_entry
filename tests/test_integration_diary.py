from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_add_and_retrieve_entries():
    diary = Diary()
    entry1 = DiaryEntry("Day 1", "I went for a walk")
    entry2 = DiaryEntry("Day 2", "It rained all day")

    diary.add(entry1)
    diary.add(entry2)

    # Should return a list of entries in the order added
    assert diary.all() == [entry1, entry2]

def test_count_words_across_entries():
    diary = Diary()
    entry1 = DiaryEntry("Hello", "One two three")  # 1 + 3 = 4 words
    entry2 = DiaryEntry("World", "Four five")      # 1 + 2 = 3 words

    diary.add(entry1)
    diary.add(entry2)

    # Total should be 4 + 3 = 7 words
    assert diary.count_words() == 7

def test_reading_time_calculation():
    diary = Diary()
    entry1 = DiaryEntry("Hi", "One two three four")  # 1 + 4 = 5 words
    entry2 = DiaryEntry("Bye", "Five six")           # 1 + 2 = 3 words

    diary.add(entry1)
    diary.add(entry2)

    wpm = 2

    # Entry1: 5 words, reading time = ceil(5 / 2) = 3 minutes
    # Entry2: 3 words, reading time = ceil(3 / 2) = 2 minutes
    # Total reading time = 3 + 2 = 5 minutes
    assert diary.reading_time(wpm) == 5

def test_find_best_entry_integration():
    diary = Diary()
    entry1 = DiaryEntry("Short", "One two")                    # 1 + 2 = 3 words
    entry2 = DiaryEntry("Medium", "One two three four")        # 1 + 4 = 5 words
    entry3 = DiaryEntry("Long", "One two three four five six seven") # 1 + 7 = 8 words

    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)

    wpm = 2
    minutes = 2
    # Max words readable = 2 * 2 = 4 words

    # entry1 = 3 words -> fits
    # entry2 = 5 words -> too long
    # entry3 = 8 words -> too long
    # Expect entry1 as best fit
    best_entry = diary.find_best_entry_for_reading_time(wpm, minutes)
    assert best_entry == entry1

def test_methods_with_no_entries():
    diary = Diary()

    assert diary.count_words() == 0
    assert diary.reading_time(5) == 0
    assert diary.find_best_entry_for_reading_time(5, 5) is None

def test_diary_entry_reading_chunk_with_multiple_calls():
    """Test that DiaryEntry maintains state across multiple reading_chunk calls"""
    entry = DiaryEntry("Title", "one two three four five six")
    
    # First chunk: read 3 words
    chunk1 = entry.reading_chunk(wpm=3, minutes=1)
    assert chunk1 == "Title one two"
    
    # Second chunk: read next 3 words
    chunk2 = entry.reading_chunk(wpm=3, minutes=1)
    assert chunk2 == "three four five"
    
    # Third chunk: only 1 word left
    chunk3 = entry.reading_chunk(wpm=3, minutes=1)
    assert chunk3 == "six"
    
    # Fourth chunk: should reset and start from beginning
    chunk4 = entry.reading_chunk(wpm=3, minutes=1)
    assert chunk4 == "Title one two"

def test_diary_and_entry_integration_complex():
    """Complex integration test combining multiple Diary and DiaryEntry features"""
    diary = Diary()
    
    entry1 = DiaryEntry("Morning", "Had breakfast with coffee")     # 1 + 4 = 5 words
    entry2 = DiaryEntry("Afternoon", "Went to the park for lunch") # 1 + 6 = 7 words
    entry3 = DiaryEntry("Evening", "Watched a movie")              # 1 + 3 = 4 words
    
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)
    
    # Test total word count
    assert diary.count_words() == 16  # 5 + 7 + 4 = 16
    
    # Test total reading time at 4 wpm
    # entry1: ceil(5/4) = 2 minutes
    # entry2: ceil(7/4) = 2 minutes  
    # entry3: ceil(4/4) = 1 minute
    # Total: 5 minutes
    assert diary.reading_time(4) == 5
    
    # Test finding best entry for 6 words (1.5 minutes at 4 wpm)
    best = diary.find_best_entry_for_reading_time(wpm=4, minutes=1.5)
    assert best == entry1  # 5 words fits, 7 and 4 don't optimize as well