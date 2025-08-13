def translate(text):

    def _translate(word):
        for vowel in ['a', 'e', 'i', 'o', 'u', 'xr', 'yt']:
            if word.startswith(vowel):
                return word + 'ay'
        
        for consonant in ['squ', 'sch', 'thr', 'qu', 'ch', 'th', 'y', 'rh']:
            if word.startswith(consonant):
                return word[len(consonant):] + consonant + 'ay'

        return word[1:] + word[0] + 'ay'
   
    return ' '.join( [ _translate(word) for word in text.split() ])