# Determine wordlist
wordlist_input = input("Select word list (n for NLTK, f for freebsd):")
if wordlist_input == 'n':
    import nltk
    from nltk.corpus import words
    wordlist = words.words()
if wordlist_input == 'f':
    import http.client
    from bs4 import BeautifulSoup
    client = http.client.HTTPSConnection("svnweb.freebsd.org", 443)
    client.request("GET", "/csrg/share/dict/words?view=co")
    soup = BeautifulSoup(client.getresponse().read(), "html.parser")
    wordlist = str(soup).split("\n")

# Remove words shorter than 4 letters
long_words = [x for x in wordlist if len(x) > 3]

# Obtain outer letters
outer_letters = []
for i in range(0,6):
    outer_letters.append(input(f"Enter outer letter {i+1}:").lower())

# Obtain middle letter
middle_letter = input("Enter middle letter:").lower()

# Remove words without middle letter
new_valid_words = [x for x in long_words if middle_letter in x]

# Remove words containing non-input letters
accepted_words = []
for word in new_valid_words:
    valid = True
    for c in word:
        if c.lower() not in outer_letters and c.lower() != middle_letter:
            valid = False
    if valid:
        accepted_words.append(word)

# Print all remaining words
print(accepted_words)
