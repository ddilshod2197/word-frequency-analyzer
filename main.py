from collections import Counter

def word_frequency_analyzer(text):
    # Textni kichik harflarga va belgilardan tozalash
    text = text.lower()
    text = ''.join(e for e in text if e.isalnum() or e.isspace())

    # So'zlarni ajratib olish
    words = text.split()

    # So'zlar sonini hisoblash
    frequency = Counter(words)

    return frequency

# Test ma'lumoti
text = "This is a test text. This text is just a test. Testing 1, 2, 3."

# Analyzer ishlatish
frequency = word_frequency_analyzer(text)

# Natija chiqarish
for word, count in frequency.items():
    print(f"{word}: {count}")
```

Kodni ishlatish uchun, siz text deb ataladigan string ni o'zgartiring va print() funksiyasidan foydalanib natijani chiqarishingiz kerak.
