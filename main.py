from collections import Counter
import sys

solution = []

def find_anagrams(word_list, input_word):
    with open(word_list) as f:
        for line in f.readlines():
            if line[:len(line) - 1] == "":
                continue
            if is_anagram(input_word, line[:len(line) - 1]):
                solution.append(line[:len(line) - 1])


def is_anagram(cli_input, word):
    if cli_input == word:
        return False
    input_counter, word_counter = Counter(cli_input), Counter(word)
    return all(input_counter[char] >= word_counter[char]
               for char in word_counter)


if __name__ == '__main__':
    find_anagrams(sys.argv[1], sys.argv[2])
    print(solution)