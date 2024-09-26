import h5py
import matplotlib.pyplot as plt

path = r"C:\Users\alkrd\Desktop\graduation_project\data.mat"
# path = r"C:\Users\alkrd\Desktop\graduation_project\eSEEd_v2\data_v2.mat"

with h5py.File(path, 'r') as f:
    data = f['Data']
    x = data['video']
    defx = f[x[0].ref]
    print(defx)
    # plt.imshow(data, cmap='viridis')
    # plt.colorbar()
    # plt.show()

# plt.imshow(data, cmap='viridis')
# plt.colorbar()
# plt.show()