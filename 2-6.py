import re

def remove_text_in_brackets(text):
    pattern = r"\([^()]*\)"
    result = re.sub(pattern, "", text)
    return result

text = "Пример (текста) с (скобками)."
processed_text = remove_text_in_brackets(text)
print(processed_text)
