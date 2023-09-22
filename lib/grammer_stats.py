class GrammarStats:
    def __init__(self):
        self.passed = 0
        self.total_count = 0

    def check(self, text):
        self.total_count += 1
        result = text[0].isupper() and text[-1] in ".?!"
        if result:
            self.passed += 1
        return result

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        try:
            result = round((self.passed / self.total_count) * 100)
        except ZeroDivisionError:
                return 0
        return result