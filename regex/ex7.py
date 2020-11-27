import re


text = """John Doe
            Jane Doe
            Jin Du
            Chin Doe"""

results = re.split(r"\n+", text)

print(results)