class Diary:
    def __init__(self):
        self._entries = []

    def add(self, entry):
        self._entries.append(entry)

    def all(self):
        return self._entries

    def count_words(self): #better to use unique name - eg. count_entries_words
        total = 0
        for entry in self._entries:
            total += entry.count_words()
        return total

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if self._entries== []:
            raise Exception("No entries added yet")
        content_words = len(self._contents.split())

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self._entries== []:
            raise Exception("No entries added yet")
        words_the_user_could_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for entry in self._entries:
            if entry.count_words() <= words_the_user_could_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable