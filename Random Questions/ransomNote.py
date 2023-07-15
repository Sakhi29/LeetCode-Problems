from collections import Counter
def ransomNote(ransom,magazine):
    str1, str2 = Counter(ransom), Counter(magazine)
    if str1 & str2 == str1:
        return True
    return False

if __name__ == "__main__":
    print(ransomNote("a","b"))
