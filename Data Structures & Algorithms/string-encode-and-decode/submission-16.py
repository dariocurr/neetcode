class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([f"{len(string)}#{string}" for string in strs])

    def decode(self, s: str) -> List[str]:
        i = s.find("#")
        words = []
        while i != -1:
            str_len = int(s[0:i])
            end = i + 1 + str_len
            word = s[i+1:end]
            words.append(word)
            s = s[end:]
            i = s.find("#")
        return words
