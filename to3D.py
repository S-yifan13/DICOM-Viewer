from dicomUtil import Dicom
import os
import cv2
import pydicom
import numpy as np
from matplotlib import pyplot as plt
from skimage import measure, morphology

from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import time


dicom = Dicom('data/data')
pixel = dicom.pixelRectTranAll()
img_shape = pixel.shape
pixel = np.zeros(img_shape)
img3d = []
for frame in pixel:
     img3d.append(cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY))
img3d = np.array(img3d)
img3d.transpose((1, 2, 0))

img3d = np.zeros(img_shape)
verts, faces, _, _ = measure.marching_cubes(img3d, 500)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# Fancy indexing: `verts[faces]` to generate a collection of triangles
mesh = Poly3DCollection(verts[faces], alpha=0.70)
face_color = [0.45, 0.45, 0.75]
mesh.set_facecolor(face_color)
ax.add_collection3d(mesh)

ax.set_xlim(0, img3d.shape[0])
ax.set_ylim(0, img3d.shape[1])
ax.set_zlim(0, img3d.shape[2])

plt.show()