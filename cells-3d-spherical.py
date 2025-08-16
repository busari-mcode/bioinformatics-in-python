import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

# Grid size
N = 64
x, y, z = np.indices((N, N, N))

# Cell parameters
center = np.array([N//2, N//2, N//2])
cell_radius = N//2 - 4
membrane_thickness = 2

# Nucleus parameters
nucleus_radius = N//5

# Helper to create spheres/ellipsoids
def sphere(cx, cy, cz, r):
    return (x - cx)**2 + (y - cy)**2 + (z - cz)**2 <= r**2

def ellipsoid(cx, cy, cz, rx, ry, rz):
    return ((x - cx)/rx)**2 + ((y - cy)/ry)**2 + ((z - cz)/rz)**2 <= 1

# Cell body & membrane shell
cell = sphere(*center, cell_radius)
inner_cell = sphere(*center, cell_radius - membrane_thickness)
membrane = cell & ~inner_cell

# Nucleus
nucleus = sphere(*center, nucleus_radius)

# Cytoplasm (cell interior minus nucleus)
cytoplasm = inner_cell & ~nucleus

# Mitochondria: scattered ellipsoids
rng = np.random.default_rng(42)
mito = np.zeros_like(cell, dtype=bool)
num_mito = 18
for _ in range(num_mito):
    cx, cy, cz = rng.integers(
        N//2 - nucleus_radius - 6,
        N//2 + nucleus_radius + 6,
        size=3
    )
    rx, ry, rz = rng.integers(2, 4), rng.integers(2, 4), rng.integers(5, 8)
    candidate = ellipsoid(cx, cy, cz, rx, ry, rz)
    mito |= candidate & cytoplasm

# Endoplasmic reticulum (ER): sinusoidal sheets
xx = x / N * 2*np.pi
yy = y / N * 2*np.pi
zz = z / N * 2*np.pi
er_pattern = np.sin(2*xx + 0.5*np.sin(3*yy)) + np.cos(2*yy + 0.5*np.sin(3*zz))
er = (np.abs(er_pattern) < 0.15) & cytoplasm

# Golgi: stacked ellipsoids near nucleus
golgi_center = center + np.array([nucleus_radius + 6, -4, 0])
golgi = np.zeros_like(cell, dtype=bool)
for k in range(-2, 3):
    layer = ellipsoid(*(golgi_center + np.array([0, 0, k*2])),
                      6, 3, 0.7 + 0.2*abs(k))
    golgi |= layer
golgi &= cytoplasm

# Combine components into volume
volume = np.zeros((N, N, N), dtype=np.uint8)
volume[membrane] = 1
volume[cytoplasm] = 2
volume[nucleus] = 3
volume[mito] = 4
volume[er] = 5
volume[golgi] = 6

# Prepare voxel mask and colors
mask = volume > 0
facecolors = np.zeros((*volume.shape, 4), dtype=float)
facecolors[volume == 1] = [0.7, 0.7, 0.7, 0.6]  # membrane
facecolors[volume == 2] = [0.8, 0.8, 0.8, 0.1]  # cytoplasm
facecolors[volume == 3] = [0.3, 0.5, 0.9, 0.6]  # nucleus
facecolors[volume == 4] = [0.9, 0.4, 0.1, 0.8]  # mitochondria
facecolors[volume == 5] = [0.2, 0.8, 0.6, 0.6]  # ER
facecolors[volume == 6] = [0.8, 0.6, 0.2, 0.8]  # Golgi

# Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.voxels(mask, facecolors=facecolors, edgecolor=None)

ax.set_box_aspect([1, 1, 1])
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_title("3D Voxel Mammalian Cell")


plt.show()
