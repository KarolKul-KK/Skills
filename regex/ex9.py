import re
salaries = "120000    140000   10000    1000    200"

result_list = re.findall(r"\d{5,6}", salaries)
print(result_list)