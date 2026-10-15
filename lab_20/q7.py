"""7. Word Frequency Counter
Concepts: dictionaries, split(), strip(), lower(), get(), items()
Read a paragraph. Count how often each word appears, ignoring case and stripping
surrounding punctuation (.,!?;:). Print the words alphabetically with their counts. Then
print the most frequent word. If several words tie, print all of them."""
text=input("Enter your text")
counts={}
for word in text.lower().split():
    word=word.strip(".,?:;")
    if word=="":
        continue
    counts[word]=counts.get(word,0)+1
if not counts:
    print("No words found.")
else:
    for word,count in sorted(counts.items()):
        print(f"{word}:{count}")

    highest=max(counts.values())
    top_words=[]
    for word,count in sorted(counts.items()):
        if count==highest:
            top_words.append(word)
    print(f"Most frequent({highest}):{','.join(top_words)}")


