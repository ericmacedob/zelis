dictionary = ['albums', 'barely', 'befoul', 'convex', 'hereby', 'jigsaw', 'tailor', 'weaver']

pieces = ['al', 'bums', 'bar', 'ely', 'be', 'foul', 'con', 'vex', 'here', 'by', 'jig', 'saw', 'tail', 'or', 'we', 'aver']

six_letter_words = []
failed_attempts = []

for piece1 in pieces:
    for piece2 in pieces:
        if piece1 != piece2:
            word = piece1 + piece2
            if word in dictionary and len(word) == 6 and word not in six_letter_words:
                six_letter_words.append(word)
            else:
                failed_attempts.append(word)

print("# --- Printing successful operations:")
for word in six_letter_words:
    print(word)
print("# --- Printing failed attempts:")
for word in failed_attempts:
    print(word)
