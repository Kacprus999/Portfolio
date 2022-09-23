import numpy as np
import matplotlib.pylab as plt
from scipy import misc
from scipy.stats import norm

data1 = 1.0 * np.random.randn(100) + 3.0
data2 = 2.0 * np.random.randn(100) + 1.0


mu1 = np.mean(data1)
std1 = np.std(data1)
mu2 = np.mean(data2)
std2 = np.std(data2)

thres = (std1*mu2+std2*mu1)/(std1+std2)
data1_below_thres = sum(data1 < thres)
data2_above_thres = sum(data2 > thres)
data1_overlap = data1_below_thres/len(data1)
data2_overlap = data2_above_thres/len(data2)
missclassfication_rate = (data1_overlap+data2_overlap)/2

print(missclassfication_rate)

plt.hist(data1,alpha=0.5,density=True)
#plt.hist(data2,alpha=0.5)


xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
pdf = norm.pdf(x,mu1,std1)
plt.plot(x,pdf,'k',linewidth=1)


mu = np.zeros(100)
for i in range(100):
    data = np.random.normal(3.0,1.0,100)
    mu[i] = np.mean(data)

plt.show()