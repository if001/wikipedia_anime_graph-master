
library(maptools)

data <- read.csv("mds_plot_prog.dat")

print(data)
png("output.png")


plot(data$x,data$y,cex=2,col="red")

CC <- c("Bash","C","C++","Emacs Lisp","Go","HTML","Java","JavaScript","Julia","MATLAB","Mathematica","Perl","PHP","Python","Ruby","Scala","Swift","Haskell")
#CC <- c(Bash,C,C++,C Sharp,Emacs Lisp,Go,HyperText Markup Language,Java,JavaScript,Julia,MATLAB,Mathematica,Perl,PHP,Python,Ruby,Scala,Swift,Haskell,Lua )

pointLabel(x=data$x, y=data$y, labels=CC)







