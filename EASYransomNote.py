class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #convert magazine to list
        magList = list(magazine)
        #go through ransomNote, remove letters from magList 1 by 1
        for i in ransomNote:
            if i in magList:
                magList.remove(i)
        #if letter not present in magList, must be false
            else:
                return False
        #if it goes through the whole thing, and removes 1 every time, must be true
        return True
        