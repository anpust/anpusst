import re

def remove_text_in_brackets(text):
    pattern = r"\([^)]*\)"
    return re.sub(pattern, "", text)

text = "Это (текст), в котором нужно удалить (часть текста, заключенную) в скобки."
cleaned_text = remove_text_in_brackets(text)
print(cleaned_text)