class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        new_l = []

        translator = s.maketrans('', '', string.punctuation)

        # Remove punctuation
        clean_text = s.translate(translator)
        
        for x in clean_text:
            if x == " ":
                continue

            elif ord(x):
                new_l.append(x.lower())
            
        copy_l =  new_l.copy()
        new_l.reverse()

        if copy_l == new_l:
            return True
        else:
            return False