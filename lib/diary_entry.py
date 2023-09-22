import math

class DiaryEntry:
    def __init__(self, title, contents):
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")
        self._title = title
        self._contents = contents
        self._read_so_far = 0
        pass

    def format(self):
        return self._title + ": " + self._contents 

    def count_words(self):
        words = self.format().split()
        return len(words)
        
    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot calculate reading time with wpm of 0")
        content_words = len(self._contents.split())
        return math.ceil(content_words / wpm)

    def reading_chunk(self, wpm, minutes):
        words_user_can_read = wpm * minutes
        words = self._contents.split()
        chunk_start = self._read_so_far
        chunk_end = self._read_so_far + words_user_can_read
        chunk_words = words[chunk_start:chunk_end]
        self._read_so_far = chunk_end
        return  " ".join(chunk_words)
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        pass