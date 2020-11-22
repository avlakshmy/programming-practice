def uniqueMorseRepresentations(words)
    morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    transformations = set()
    for word in words:
        morse = []
        for ch in word:
            morse.append(morseCode[ord(ch) - ord('a')])
        transformations.add(''.join(morse))
    return len(transformations)
