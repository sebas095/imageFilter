import scipy
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

l = scipy.misc.ascent()
l = l[230:290, 220:320]

noisy = l + 0.4 * l.std() * np.random.random(l.shape)
gauss_denoised = ndimage.gaussian_filter(noisy, 2)

plt.subplot(121)
plt.imshow(noisy, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.xticks([]), plt.yticks([])
plt.title('Noisy', fontsize=20)

plt.subplot(122)
plt.imshow(gauss_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.xticks([]), plt.yticks([])
plt.title('Gaussian filter', fontsize=20)

plt.show()
