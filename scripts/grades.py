"""
BSc University Grade Viewer.

Usage:
    grades.py [--y1] [--y2] [--y3] [--y4] [--pause]
    grades.py -h | --help | -v | --version

Options:
    -h --help         Show this screen.
    -v --version      Show version.
    -p --pause        Pause between each graph
    --y1              Show year one
    --y2              Show year two
    --y3              Show year three
    --y4              Show year four

Dependencies:
   pip install matplotlib
   pip install docopt

Examples:
    
"""
from matplotlib import pyplot as plot
from docopt import docopt

year_one = {
    "2D Graphics Programming": 81,
    "Computing Systems": 60.03,
    "Mathematics of Space & Change": 79,
    "Introduction to Programming": 65,
    "Intro to Games Development": 74,
    "Creative Computing Profession": 61.5
}

year_two = {
    "Real Time 3D Graphics": 81.08,
    "Interactive Physical Modelling": 68,
    "Computing Project": 84,
    "Structures and Algorithms": 75.8,
    "Computer Games Design": 73,
    "Game Engine Design": 82.2
}

year_three = {
    "Computer Game AI": 85,
    "Games Technology Project": 81.6,
    "Mobile Games Development": 87.83,
    "Games Project : Design and Plan": 71.4,
    "Advanced Games Programming": 92.8,
    "Algorithms and Collections": 79.2
}

year_four = {
    "Games Console Development": 85.8,
    "Serious Games": 81, 
    "GPGPU & Accelerator Programming": 86,
    "Computing Honours Project": 80, 
    "3D Level Design": 90
}

def next_figure():
  next_figure.counter += 1
  return next_figure.counter
next_figure.counter = 0

def show_year(graph_title, year, pause):
    grades = list(year.values())
    grade_count = len(grades)
    labels = list(range(grade_count))
    average = sum(grades) / grade_count

    plot.rcParams["figure.figsize"] = (12, 6)

    fig = plot.figure(next_figure())
    fig.canvas.set_window_title('University Grades')

    plot.title(graph_title)
    plot.plot(labels, list(year.values()))
    plot.plot(labels, list(year.values()), 'gs')
    plot.plot([-1] + labels + [grade_count+1], [average] * (2 + grade_count))
    plot.axis([-1, len(grades), 0, 100])
    plot.xticks(labels, list(year.keys()), fontsize=5)
    plot.ylabel('Grades %')

    if pause:
        plot.show()

def main():
    config = docopt(__doc__, version='0.1')
    pause = config['--pause']

    if config['--y1']:
        show_year("Year One", year_one, pause)
    if config['--y2']:
        show_year("Year Two", year_two, pause)
    if config['--y3']:
        show_year("Year Three", year_three, pause)
    if config['--y4']:
        show_year("Year Four", year_four, pause)

    if not pause:
        plot.show()
    

if __name__ == "__main__":
    main()