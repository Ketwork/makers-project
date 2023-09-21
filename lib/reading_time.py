def estimated_reading_time(text):
    if text == "":
        raise Exception("can't estimate reading time for empty text.")
    else:
        print(len(text))
        words = text.split()
        return len(words) / 200