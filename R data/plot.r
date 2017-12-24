library(ggplot2)
new = read.csv("seaflow_21min.csv",TRUE,",")
y = 1:length(new)
plot(new$time,new$chl_big,pch=16,cex=0.4)