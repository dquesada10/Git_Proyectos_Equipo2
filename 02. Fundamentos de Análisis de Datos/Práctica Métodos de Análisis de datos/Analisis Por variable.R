

library(dplyr)
library(ggplot2)
library(ggcorrplot)
library(fBasics)
library(tidyr)
library(gridExtra)
library(caret)
library(readxl)

Cv <- function(mean, sd){(sd/mean)*100}


Breast_Cancer <- read_excel("Breast_Cancer.xlsx")

Breast_Cancer<-rename(Breast_Cancer,Regional_Node_Positive=Reginol_Node_Positive)
str(as.data.frame(Breast_Cancer$Regional_Node_Positive))

Breast_Cancer[sapply(Breast_Cancer, is.character)] <- lapply(Breast_Cancer[sapply(Breast_Cancer, is.character)],as.factor)
str(Breast_Cancer[,sapply(Breast_Cancer, is.factor)])

Breast_Cancer_limpio<-Breast_Cancer %>% filter(is.na(Regional_Node_Positive)==FALSE)


set.seed(1)

particion <- sample(1:nrow(Breast_Cancer_limpio), size = 0.7 * nrow(Breast_Cancer_limpio))

Breast_Cancer_train <- Breast_Cancer_limpio[particion, ]

Breast_Cancer_test <- Breast_Cancer_limpio[-particion, ]

Breast_Cancer_train.columns

#numericas - edad

#Analisis de las variables propias  - PARA NOSOTROS
summary(Breast_Cancer_train_num$Age)
sd(Breast_Cancer_train_num$Age)
Cv(mean(Breast_Cancer_train_num$Age), sd(Breast_Cancer_train_num$Age))

normalTest(Breast_Cancer_train_num$Age, method = c("sw", "jb"))
qqnorm(Breast_Cancer_train_num$Age, pch = 1, frame = FALSE)
qqline(Breast_Cancer_train_num$Age, col = "steelblue", lwd = 2)

ggplot(data = Breast_Cancer_train, aes(x = Age))+
  geom_histogram(bins=20,fill="lavender", color="black",alpha = 0.9)+
  xlab("Age")+  
  theme_minimal()


Breast_Cancer_train %>%
  ggplot(aes(y = Age)) +
  geom_boxplot() +
  ggtitle("Age")


Breast_Cancer_train %>%
ggplot(aes(x = Age, y = Tumor_Size)) +  geom_point()+
labs(title="Age vs Tumor Size", x="Age", y="Tumor Size")+ 
theme(plot.title=element_text(hjust=0.5), plot.subtitle=element_text(hjust=0.5)) + 
geom_smooth(method='lm')

# Codigo para volver variable numerica en rangos
Breast_Cancer_train$Age_range <- cut(Breast_Cancer_train$Age, breaks = c(29, 40, 50, 60, 70))

a<-Breast_Cancer_train %>% group_by(Age_range) %>% summarise(conteo=n(),media=mean(Tumor_Size))
a


ggplot(a,aes(x = Age_range)) + 
  geom_col(aes(y = conteo), fill="yellow",alpha=0.7) + 
  geom_line(aes(y=media*10 , group=), group = 1,color="red") + 
  geom_text(aes(y = media*10, label = round(media,2)),
            vjust = 1.4, color = "red", size = 2) +
  scale_y_continuous(sec.axis = sec_axis(~./10, name = "media")) 


# Cuantitativa con cualitativa
y<-"Race"
lables <-levels(Breast_Cancer_train[,"Age"])
total<-length(Breast_Cancer_train[,"Age"])

Breast_Cancer_train %>%
  # mutate(variabl = factor(get(y) , labels = levels(Breast_Cancer_train[,y]))) %>%
  ggplot(aes(x = get(x), fill = get(y))) +
  geom_density(alpha = .3) +
  ggtitle(x)



      
