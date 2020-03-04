import xml.etree.ElementTree as ElT

tree = ElT.parse("newsafr.xml")

all_words = []
words_count = dict()

root = tree.getroot()

items = root.findall("channel/item")
for item in items:
    words = item.find("description").text.split()
    for word in words:
        if len(word) > 6 and word.isalpha():
            all_words.append(word.lower())

unique_words = set(all_words)

for word in unique_words:
    words_count[word] = all_words.count(word)

print("Топ-10 самых часто встречающихся в новостях слов длиннее 6 символов:\n")
for i, key in enumerate(sorted(words_count, key=words_count.get, reverse=True)[:10], 1):
    print(f"Топ-{i}. Слово \"{key.capitalize()}\" встречается {words_count[key]} раз.")

