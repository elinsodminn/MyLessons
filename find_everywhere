
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        lst_words = []
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower().split()
                while text:
                    lst_words.extend(text)
                    file.read().split()
                    all_words = {file_name: lst_words}
                    return all_words


    def find(self, word):
        w = word.lower()
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            if w in words:
                result[file_name] = words.index(w)+1

        return result

    def count(self, word):
        w = word.lower()
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            result[file_name] = words.count(w)

        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
