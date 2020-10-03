import sys
import inspect
import cv2, os
import matplotlib.pyplot as plt
import numpy as np


# PATH = os.path.join(os.path.dirname('/Users/kevin/Documents/ML Related/Dataset/'), 'MMI_selected')
PATH = os.path.join(os.path.dirname('/Users/kevin/Documents/ML Related/Dataset/'), 'KDEF')
# PATH = os.path.join(os.path.dirname('/Users/kevin/Documents/ML Related/Dataset/'), 'CK+_add')

os.chdir('/Users/kevin/Documents/ML Related/Dataset/')
print(os.getcwd())
#image = cv2.imread()
arr = os.listdir(PATH)



ax = plt.figure().add_subplot(111)
ax.set_title('Histogram plot for KDEF dataset')

    # f.append(plt.figure())
    # ax = f[k].add_subplot(111)
    # ax.set_title('Histogram plot for ' + arr[k] + ' in CK+ dataset')
histr = 0
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    for k in range(len(arr)):
        arr1 = os.listdir(PATH + '/' + arr[k])
        for j in range(len(arr1)):
            img = cv2.imread(PATH + '/' + arr[k] + '/' + arr1[j], 1)
            # print(PATH + '/' + arr[k] + '/' + arr1[j])
            # print(img.shape)
            histr += cv2.calcHist([img], [i], None, [256], [0,256]) / len(arr1)
    ax.plot(histr, color = color[i])
    ax.set_xlim([0,256])
    ax.set_ylim([0,150000])


plt.savefig('KDEF_RGB.png')
plt.show()