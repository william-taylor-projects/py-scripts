
import matplotlib.pyplot as plot

xbar = [ 0, 1, 2 ]
ybar = [ 85, 75, 90 ]

fig = plot.figure(1)
fig.canvas.set_window_title('University Grades')

plot.title('Grades')
plot.plot(xbar, ybar)
plot.xticks(xbar, ['A', 'B', 'C' ])
plot.ylabel('Grade %')
plot.show()