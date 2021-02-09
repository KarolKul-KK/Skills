library(ggplot2)
library(tidyverse)

rice <- read.csv("ceny_ryżu.csv", sep=';', header = TRUE)
rice


rice_matrix[1,]

rice <- rice %>% 
  rename(
    '2006' = styczeń.ryż...za.1kg.cena.2006..zł.,
    '2007' = styczeń.ryż...za.1kg.cena.2007..zł.,
    '2008' = styczeń.ryż...za.1kg.cena.2008..zł.,
    '2009' = styczeń.ryż...za.1kg.cena.2009..zł.,
    '2010' = styczeń.ryż...za.1kg.cena.2010..zł.,
    '2011' = styczeń.ryż...za.1kg.cena.2011..zł.,
    '2012' = styczeń.ryż...za.1kg.cena.2012..zł.,
    '2013' = styczeń.ryż...za.1kg.cena.2013..zł.,
    '2014' = styczeń.ryż...za.1kg.cena.2014..zł.,
    '2015' = styczeń.ryż...za.1kg.cena.2015..zł.,
    '2016' = styczeń.ryż...za.1kg.cena.2016..zł.,
    '2017' = styczeń.ryż...za.1kg.cena.2017..zł.,
    '2018' = styczeń.ryż...za.1kg.cena.2018..zł.,
    '2019' = styczeń.ryż...za.1kg.cena.2019..zł.,
    )

max(rice[, 3])
price_poland <-ggplot(data=rice[, 3], aes(x=colnames(rice[, 3])), y=rice[, 3])) +
  geom_bar(stat="identity")
price_poland

length(rice[2,])
length(colnames(rice))
length(rice)
max(rice[,3])

