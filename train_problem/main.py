from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy
import pandas
import pylab

# a - угол наклона в радианах
class line:
    def __init__(self, x0, y0, x1, y1, a):
        self.len = numpy.sqrt((x1 - x0)**2 + (y1 - y0)**2)
        self.x = numpy.linspace(x0 ,x1, self.len)
        self.y = numpy.linspace(y0, y1, self.len)
        self.z = self.x * numpy.sin(a)

    def print(self):
        fig = pyplot.figure()
        ax = Axes3D(fig)

        ax.scatter(self.x , self.y, self.z)
        pyplot.show()

class road:
    def __init__(self):
        self.x = []
        self.y = []
        self.z = []


    def add_line(self, l):
        for i in l.x:
            self.x.append(i)

        for i in l.y:
            self.y.append(i)

        for i in l.z:
            self.z.append(i)


    def print(self):
        fig = pyplot.figure()
        ax = Axes3D(fig)

        ax.scatter(self.x , self.y, self.z)

        pyplot.show()

r = road()

c = pandas.read_csv('coordinates', header=None).as_matrix()
for i in c:
    r.add_line(line(i[0],i[1],i[2],i[3],i[4]))

r.print()

