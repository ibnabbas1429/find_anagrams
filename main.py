# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    
    are_words_anagrams = True
    
    if (sorted(word) == sorted(anagram)):
        return are_words_anagrams
    else:
        return False

    
    
