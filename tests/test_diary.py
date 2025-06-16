import pytest
from lib.diary_entry import *  

def test_count_words_counts_title_and_contents():
    entry = DiaryEntry("Hello World", "This is a test diary entry.")
    assert entry.count_words() == 8 # "Hello World" = 2 words, contents = 6 words, total = 8

def test_reading_time_rounded_up():
    entry = DiaryEntry("Hello", "word " * 9)  # 1 word title + 9 words = 10 words total
    assert entry.reading_time(3) == 4 # Reading speed = 3 wpm, so 10/3 = 3.333.. minutes, rounded up to 4

def test_reading_chunk_returns_correct_chunk_and_advances():
    content = "one two three four five six seven eight nine ten"
    entry = DiaryEntry("Title", content)  # 1 word title + 10 words contents = 11 words total

    # Read 4 words at 2 wpm for 2 minutes: 2*2=4 words per chunk
    chunk1 = entry.reading_chunk(2, 2)
    expected_chunk1 = "Title one two three"  # first 4 words including title
    assert chunk1 == expected_chunk1

    # Next chunk should start where previous ended, next 4 words
    chunk2 = entry.reading_chunk(2, 2)
    expected_chunk2 = "four five six seven"
    assert chunk2 == expected_chunk2

    # Next chunk 4 words again, only 3 left so it returns those
    chunk3 = entry.reading_chunk(2, 2)
    expected_chunk3 = "eight nine ten"
    assert chunk3 == expected_chunk3

    # Next chunk resets to beginning
    chunk4 = entry.reading_chunk(2, 2)
    assert chunk4 == expected_chunk1

def test_reading_chunk_handles_zero_words_read_so_far():
    entry = DiaryEntry("Test", "")
    # Read with zero words in contents and title has one word "Test"
    chunk = entry.reading_chunk(1, 1)
    assert chunk == "Test"

def test_reading_chunk_resets_after_all_words_read():
    entry = DiaryEntry("a b c", "d e f")
    total_words = entry.count_words()
    wpm = 2
    minutes = 1
    # Read chunks until all words are read
    read_words = 0
    while read_words < total_words:
        chunk = entry.reading_chunk(wpm, minutes)
        read_words += len(chunk.split())

    # After reading all words, next chunk should reset to start
    first_chunk = entry.reading_chunk(wpm, minutes)
    expected_first_chunk = "a b"
    assert first_chunk == expected_first_chunk
