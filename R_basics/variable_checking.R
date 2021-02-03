# variable checking
print(ls())
print(ls(pattern = "var"))
print(ls(all.name = TRUE))

# variable removing
rm(age)
print(x)

rm(list = ls())
print(ls())
