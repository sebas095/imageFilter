import scipy
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

l = scipy.misc.ascent()
l = l[230:290, 220:320]

noisy = l + 0.4 * l.std() * np.random.random(l.shape)
max_denoised = ndimage.filters.maximum_filter(noisy, 3)
min_denoised = ndimage.filters.minimum_filter(noisy, 3)

plt.figure(figsize=(12,2.8))

plt.subplot(131)
plt.imshow(noisy, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('Noisy', fontsize=20)

plt.subplot(132)
plt.imshow(min_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('Min filter', fontsize=20)

plt.subplot(133)
plt.imshow(max_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
plt.axis('off')
plt.title('Max filter', fontsize=20)

plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,
                    right=1)
plt.show()
