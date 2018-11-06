import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

data_y = '''1 514.2 521.3 11 514.9 518.5\
 2 522.9 521.4 12 514.0 527.0\
 3 516.2 523.2 13 515.4 521.1\
 4 518.2 516.7 14 515.1 532.7\
 5 512.1 521.2 15 515.8 520.4\
 6 515.8 514.3 16 516.5 528.1\
 7 513.0 517.3 17 516.7 516.7\
 8 518.7 517.2 18 513.6 515.8\
 9 513.1 512.1 19 521.5 513.2\
 10 518.4 513.7 20 518.2 515.0'''

y = data_y.split(' ')
index = []
nums = []
y_data = []
z_data = []

def func(x):
    return int(x)

for i in range(0, len(y)):
    if len(y[i])<=2:
        index.append(y[i])
    if len(y[i])==5:
        nums.append(y[i])

for n in range(0,len(nums)):
    if n%2==0:
        y_data.append(nums[n])
    else:
        z_data.append(nums[n])
        
index.sort(key=func)

ints_y = [float(t) for t in y_data]
ints_z = [float(t) for t in z_data]

y_mean = np.mean(ints_y)
z_mean = np.mean(ints_z)
y_stdev = np.std(ints_y)
z_stdev = np.std(ints_z)

z_high = (530-z_mean)/z_stdev #these 4 lines are z-scores
z_low = (520-z_mean)/z_stdev
y_high = (530-y_mean)/y_stdev 
y_low = (520-y_mean)/y_stdev

prob_new_520_530 = scipy.stats.norm.cdf(z_high) - scipy.stats.norm.cdf(z_low)
prob_old_520_530 = scipy.stats.norm.cdf(y_high) - scipy.stats.norm.cdf(y_low)

t_val, p_val = scipy.stats.ttest_ind(ints_y, ints_z)

print('One sided t-test results:\n','t_val:', t_val, '\np_val:', p_val/2)

bins = [i for i in range(510,535)]

plt.bar(x=0, height=y_mean, color = 'r', width=0.2)
plt.bar(x=1, height=z_mean, color = 'g', width=0.2)
plt.show()
        
        
    
        
        

