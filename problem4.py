# def count_duplicates(word):
#     char_count = {}
#     duplicates = 0

#     for char in word:
#         char_lower = char.lower()

#         if char_lower.isalpha():
#             if char_lower in char_count:
#                 char_count[char_lower] += 1
#                 if char_count[char_lower] == 2:
#                     duplicates += 1
#             else:
#                 char_count[char_lower] = 1

#     return duplicates


# word = input("enter the word: ")
# result = count_duplicates(word)

# print(f"{word} - {result} duplicates")

def count_duplicates(word):
    count = {}
    duplicates = 0

    for i in word:
        lower = i.lower()

        if lower.isalpha():
            if lower in count:
                count[lower] += 1
                if count[lower] == 2:
                    duplicates += 1
            else:
                count[lower] = 1

    return duplicates


word = input("Enter the word: ")
result = count_duplicates(word)

print(f"{word} - {result} duplicates")
