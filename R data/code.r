library(ggplot2)
library(rpart)
library(rpart.plot)
library(randomForest)
library(e1071)
new = read.csv("seaflow_21min.csv",TRUE,",")
summary.data.frame(new)
names(new)
class(new[,"pop"])
idx = sample(2,nrow(new),replace=TRUE,prob=c(0.5,0.5))
train = new[idx==1,]
test = new[idx==1,]
class(train)
#qplot(new$pe,new$chl_small,color=new$pop)
fol <- formula(pop ~ fsc_small + fsc_perp + fsc_big + pe + chl_big + chl_small)
model <- rpart(fol, train,method="class")
print(model)
#rpart.plot(model)
p <- predict(model,test,type="class")
t = table(p,test$pop)
acc = sum(diag(t))/sum(t)

# writting code for random forest

model2 <- randomForest(fol, train, method="class")
p2 <- predict(model2,test,type="class")
t2 = table(p2,test$pop)
acc2 = sum(diag(t2))/sum(t2)
im = importance(model2)

# writting code for SVM

model3 = svm(fol,train)
p3 = predict(model3,test,type="class")
t3 = table(p3,test$pop)