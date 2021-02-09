temp_changer <- function(Cel, Kel){
  C = Kel - 273.15 
  K = Cel + 273.15
  print(paste("Temperature in C is:", C))
  print(paste("Temperature in K is:", K))
}
temp_changer(29, 140)