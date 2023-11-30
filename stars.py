import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
file = pyfits.open('~/Desktop/v523cas60s-001.fit')
data = file[0].data

y0 = 1656
x0 = 670
r = 42
x = []
value1 = []
for i in range(x0 - r, x0 + r):  #срез по у
    x.append(i)
    value1.append(data[y0][i])

y = []
value2 = []
for i in range(y0 - r, y0 + r):  #срез по х
    y.append(i)
    value2.append(data[i][x0])
file.close()

plt.subplot(1, 3, 1)
plt.plot(x, value1)
plt.xlabel('Координаты х')
plt.title('Срез по у')

plt.subplot(1, 3, 3)
plt.plot(y, value2)
plt.xlabel('Координаты y')
plt.title('Срез по х')

plt.show()
