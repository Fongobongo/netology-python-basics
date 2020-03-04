import json

all_words = []
words_count = dict()

with open("newsafr.json", encoding="utf-8") as file:
    json_data = json.load(file)

for news in json_data["rss"]["channel"]["items"]:
    words = news["description"].split()
    for word in words:
        if len(word) > 6 and word.isalpha():
            all_words.append(word.lower())

unique_words = set(all_words)

for word in unique_words:
    words_count[word] = all_words.count(word)

print("Топ-10 самых часто встречающихся в новостях слов длиннее 6 символов:\n")
for i, key in enumerate(sorted(words_count, key=words_count.get, reverse=True)[:10], 1):
    print(f"Топ-{i}. Слово \"{key.capitalize()}\" встречается {words_count[key]} раз.")
