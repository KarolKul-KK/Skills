library(reshape2)
library(ggplot2)

# LOAD DATA
delim = ";" 
dec = ","    
rice <- read.csv("ceny_ryżu.csv", header=TRUE, sep=delim, dec=dec, stringsAsFactors=FALSE)

# Change columns names to more clearly
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

# Drop useless columns
rice
rice = subset(rice, select = -c(Kod,X) )
rice

# Let's see closer on metrics by years
summary(rice)

# The function melt reshapes it from wide to long
df <- melt(rice)
df  

#add a rowid identifying variable
df$rowid <- 1:17
head(df, 17)

# make a line plot
ggplot(df, aes(variable, value, group=factor(rowid))) + geom_line(aes(color=factor(Nazwa)))
  