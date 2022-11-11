summary(Breast_Cancer)
head(Breast_Cancer)
Breast_Cancer$`Tumor Size`[is.na(Breast_Cancer$`Tumor Size`)] <- 0
Breast_Cancer$`Regional Node Examined`[is.na(Breast_Cancer$`Regional Node Examined`)] <- 0
Breast_Cancer$`Reginol Node Positive`[is.na(Breast_Cancer$`Reginol Node Positive`)] <- 0
Breast_Cancer$`Survival Months`[is.na(Breast_Cancer$`Survival Months`)] <- 0

mest<-Breast_Cancer[1:3220,]
mval<-Breast_Cancer[3221:4024,]

predict(Breast_Cancer,datospred = Breast_Cancer[4025:4300,])
View(Breast_Cancer)
str(Breast_Cancer)
names(Breast_Cancer)

