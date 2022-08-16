import matplotlib.pyplot as plot

import png

labels = ('Firefox', 'Brave', 'Google Chrome', 'Microsoft edge')
index = (1, 2, 3, 4,)
sales = [15.3, 16.3, 55.8, 12.6]
plot.bar(index, sales, tick_label=labels)
plot.ylabel('percentage(%)')
plot.xlabel('Browsers')
plot.show()
