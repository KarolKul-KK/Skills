# make a script which take radius and computing circuit and field
x = readline("Put radius here: ")
circuit <- as.numeric(x) * 3.14
field <- as.numeric(x) * as.numeric(x)
print(paste("Circuit is: ", circuit))
print(paste("Field is: ", field))

# make a script which take values of rectangle
a = readline("Put first value: ")
b = readline("Put second value: ")
rec_field = as.numeric(a) * as.numeric(b)
rec_circuit = 2 *  as.numeric(a) + 2* as.numeric(b)
print(paste("Field of rectangle is: ", rec_field))
print(paste("Circuit of rectangle is: ", rec_circuit))
