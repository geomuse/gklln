import re 

pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
text = "今天是 2025-08-02 2025-08-05"
match = pattern.findall(text)
print(match)  # 2025-08-02