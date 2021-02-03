# checking data types
print(class(TRUE))
print(class(12))
print(class(12.1))
print(class(0L))
print(class('a'))

# change data types
print(class(as.character(12)))

# make a vector and check class of them 
apple <-c('red', 'green', 'yellow')
print(apple)
print(length(apple))