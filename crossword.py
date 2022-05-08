class CrosswordApp:
    def __init__(self):
        print("crossword app running")


    def get_words_of_length_n(self, file, n):
        words = []
        fin = open(file)
        for line in fin:
            word = line.strip()
            if len(word) == n:
                words.append(word)
        return words


    def check_crossword(self, file, clue):
        possible_words = []
        clue = clue.lower()
        words_of_same_length = self.get_words_of_length_n(file, len(clue))
        for w in words_of_same_length:
            if self.contains_letters(w, clue):
                possible_words.append(w)
        return possible_words


    def contains_letters(self, word_to_check, clue):
        for l in range(len(clue)):
            if clue[l] != '_':
                if clue[l] != word_to_check[l]:
                    return False
        return True



#print(	
#check_crossword('words_and_nouns.txt', 
#'c_u_t'
#))

# User enters the word with gaps as underscores and presses submit

# w = input("enter word: \n")
# print(
# check_crossword(
# 'words_and_nouns.txt',
# w
# ))
