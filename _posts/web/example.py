import re 

pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
text = "今天是 2025-08-02"
match = pattern.search(text)
print(match.group())  # 2025-08-02