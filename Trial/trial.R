# สร้าง data frame
library(ggplot2)
library(GAD)

results <- c(25,    19, 15, 15, 19, 23, 18, 35, 14, 35, 38, 25, 30, 28, 17, 16, 17, 24, 21, 27, 15, 21, 54, 29, 26, 20, 14, 13, 14, 21, 17, 25, 20, 24, 50, 33)
batch <- as.random(rep(seq(1,4),9))
obs <- as.fixed(c(rep(1,12),rep(2,12),rep(3,12)))
process <- as.fixed(rep(c(rep(1,4),rep(2,4),rep(3,4)),3))
dafr <- data.frame(process,batch,obs,results)
model <- lm(results~process+batch%in%process)
gad(model)
data <- data.frame(
  Process = rep(c("Process 1", "Process 2", "Process 3"), each = 4),
  Batch = rep(1:4, 3),
  Value = c(25, 19, 15, 15, 19, 23, 18, 35, 14, 35, 38, 25, 
            30, 28, 17, 16, 17, 24, 21, 27, 15, 21, 54, 29,
            26, 20, 14, 13, 14, 21, 17, 25, 20, 24, 50, 33)
)

ggplot(data, aes(x = Process, y = Value, fill = Process)) +
  geom_boxplot() +
  facet_wrap(~ Batch, nrow = 2, labeller = label_value) +
  labs(x = "กระบวนการ", y = "ค่า", fill = "กระบวนการ") +
  ggtitle("Box Plot เปรียบเทียบค่าของแต่ละกระบวนการ แยกตาม Batch") +
  theme_bw()

ggplot(data, aes(x = Process, y = Value, fill = Process)) +
  geom_boxplot() + ggtitle("Box Plot เปรียบเทียบค่าของแต่ละกระบวนการ") +
  theme_bw()
