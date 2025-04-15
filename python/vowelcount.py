def count_each_vowel(text):
    vowels = 'aeiou'
    counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    total = 0

    for char in text.lower():
        if char in counts:
            counts[char] += 1
            total += 1
    for vowel, count in counts.items():
        print(f"{vowel} = {count}")
    print(f"Total vowels = {total}")
        

user_input = input("Enter a sentance: ")
count_each_vowel(user_input)