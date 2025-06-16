# Digital Diary System 📚

A Python program to manage diary entries with smart reading features and time-based entry selection.

## What It Does

This digital diary system can:
- Store multiple diary entries with titles and content
- Count words across all entries
- Calculate reading times based on reading speed
- Find the best entry to read based on available time
- Track reading progress through long entries

## Classes Overview

### DiaryEntry
Represents a single diary page with:
- Title and content storage
- Word counting (title + content)
- Reading time calculation
- Chunked reading with progress tracking

### Diary
Main diary container that:
- Stores multiple DiaryEntry objects
- Aggregates data from all entries
- Finds optimal entries based on reading time constraints

## Key Features

Smart Entry Selection: Finds the longest entry that fits within available reading time
Reading Progress Tracking: Remembers reading position across multiple sessions
Accurate Word Counting: Includes both title and content words for precise reading estimates
Comprehensive Testing: Full test coverage with unit and integration tests

## Installation

Clone the repository
Ensure Python 3.x is installed
Install pytest: pip install pytest
Run tests to verify setup: pytest

## License
This project is open source and available under the MIT License.
RetryClaude does not have the ability to run the code it generates yet.Claude can make mistakes. Please double-check responses.

## Usage Example

```python
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

# Create diary entries
entry1 = DiaryEntry("Monday", "Went to school and had lunch")
entry2 = DiaryEntry("Tuesday", "Played games all day")

# Create diary and add entries
my_diary = Diary()
my_diary.add(entry1)
my_diary.add(entry2)

# Get total word count
total_words = my_diary.count_words()

# Find best entry for 5 minutes at 2 words per minute
best_entry = my_diary.find_best_entry_for_reading_time(wpm=2, minutes=5)

# Read an entry in chunks
chunk = entry1.reading_chunk(wpm=3, minutes=2)  # Read for 2 minutes at 3 wpm


# Run all tests
pytest

# Run specific test files
pytest tests/test_diary.py
pytest tests/test_diary_entry.py
pytest tests/test_integration_diary.py

# Run with verbose output
pytest -v
