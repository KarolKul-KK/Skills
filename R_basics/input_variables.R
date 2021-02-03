# make a dataframe
BMI <- data.frame(
  gender = c("Male", "Male", "Female"),
  height = c(152, 171.5, 165),
  weight = c(81, 93, 78),
  Age = c(42, 38, 26)
)
print(BMI)

# input some data
name = readline(prompt = "Input your name: ")
age = readline(prompt = "Input your age")
print(paste("My name is",name,"and I am",age,"years old"))