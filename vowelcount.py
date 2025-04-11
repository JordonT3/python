def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
        

user_input = input("Enter a sentance: ")
vowel_count = count_vowels(user_input)
print(f"There are {vowel_count} vowels in this text.")