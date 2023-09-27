import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")
        self._title = title
        self._contents = contents
        self._read_so_far = 0

    def format(self):
        return self._title + ": " + self._contents 

    def count_words(self):
        words = self._contents.split()
        return len(words)
        
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time with wpm of 0")
        content_words = len(self._contents.split())
        return math.ceil(content_words / wpm)

    def reading_chunk(self, wpm, minutes):
        words = self._contents.split()
        if self._read_so_far >= len(words):
            self._read_so_far = 0
        words_user_can_read = wpm * minutes
        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + words_user_can_read
        readable_chunk = " ".join(words[chunk_start:chunk_end])
        self._read_so_far = chunk_end
        return  readable_chunk