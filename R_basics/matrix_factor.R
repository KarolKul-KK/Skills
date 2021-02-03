# make a list
list1 <- list(c(2, 5, 3), 21, 3, sin)
print(list1)

# make a matrix
M = matrix(c('a', 'a', 'b', 'c', 'b', 'a'), nrow = 2, ncol = 3, byrow = TRUE)
print(M)

# make a table
a <- array(c('green', 'yellow'), dim = c(3, 3, 2))
print(a)

# make a vector and check levels of them
apple_colors <- c('green', 'green', 'yellow', 'red', 'red', 'green')
factor_apple <- factor(apple_colors)
print(factor_apple)
print(nlevels(factor_apple))