library(ggplot2)

filename = "regrex1.csv"

dataset = read.csv(filename)

dataset

model = lm(formula = y~x, data=dataset)

ggplot() +
  geom_point(aes(x = dataset$x, y = dataset$y),
             colour = 'red') +
  ggtitle('y vs x') +
  xlab('x') +
  ylab('y')

ggsave("R_linear_regression_scatter.png", width=4, height=4)

dev.off()