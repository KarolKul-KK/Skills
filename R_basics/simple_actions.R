# make 2 matrix and so some stuff with them 
A = matrix(c(1, 3, 4, 4), nrow = 2, ncol = 2, byrow = TRUE)
B = matrix(c(2, 7, 12, 2), nrow = 2, ncol = 2, byrow = TRUE)
print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(A %% B)
print(A %/% B)
print(A ^ B)

# try
print(A > B)
print(A < B)
print(A == B)
print(A <= B)
print(A >= B)
print(A != B)

# more!
print(A & B)
print(A | B)
print(A && B)
print(A || B)