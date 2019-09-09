from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        sorted_dic = sorted(char_count, key=char_count.get, reverse=True)
        result = ""
        for count in sorted_dic:
            result += count * (char_count[count])
        return result