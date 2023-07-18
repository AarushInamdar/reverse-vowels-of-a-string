def reverseVowels(s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelsList = []

        for char in s:
            if char.lower() in vowels:
                vowelsList.append(char)
        
        print('Vowels list before: ', vowelsList)
        vowelsList = list(reversed(vowelsList))
        print('Vowels list after: ', vowelsList)
        
        res = ''

        for char in s:
            if char not in vowels:
                res += char
            else:
                
                res += vowelsList[0]
                vowelsList.pop(0)
        
        return res


print(reverseVowels('aA'))