text = readline("Insert a sentence: ")
x = nchar(text)
while (x > 0) {
  print(substr(text, x, x))
  x = x - 1
}

