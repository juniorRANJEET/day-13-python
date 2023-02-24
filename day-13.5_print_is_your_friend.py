#print is your friend:
pages = 0
word_per_page = 0
pages = int(input("number of pages : "))
word_per_page = int(input("number of word per pages "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"word_per_pages = {word_per_page}")
print(f"total word in the pages = {total_words}")
