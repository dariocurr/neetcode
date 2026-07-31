from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            word_dict = defaultdict(lambda: 0)
            for char in word:
                word_dict[char] += 1
            word_id = ""
            for key in "qwertyuiopasdfghjklzxcvbnm":
                value = word_dict[key]
                word_id += f"{key}{value}"
            anagrams[word_id].append(word)
        print(anagrams)
        return list(anagrams.values())