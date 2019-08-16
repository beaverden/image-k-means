import os
import shutil
import sys
from scipy import ndimage
from sklearn.cluster import KMeans

greeting = """
# usage: cluster <dir_path> <cluster_size1> ... <cluster_sizeN>
# will create N folders, for each n_clusters that you specified
# with images copied inside their respective cluster index
#
# example: cluster.py icons 5 10
#   will create a folder named 5_clusters with subfolders 0, 2, ..., 4
#   also creates a folder named 10_cluster with subfolders 0, 2, ..., 9
"""

def main():
    if len(sys.argv) == 1:
        print(greeting)
        exit(0)

    images = []
    names = []
    images_path = sys.argv[1]
    clusters_list = map(int, sys.argv[2:])
    for name in os.listdir(images_path):
        full = os.path.join(images_path, name)
        image = ndimage.imread(full)
        x, y, z = image.shape
        image_2d = image.reshape(x * y * z)
        images.append(image_2d)
        names.append(full)

    print('Nr images: ', len(images))
    for n_clusters in clusters_list:
        # inertia_data = []
        kmeans_cluster = KMeans(n_clusters=n_clusters)
        kmeans_cluster.fit(images)

        inertia = kmeans_cluster.inertia_
        # inertia_data.append(inertia)
        print('Computing for %d - %f' % (n_clusters, inertia))

        # cluster_centers = kmeans_cluster.cluster_centers_
        cluster_labels = kmeans_cluster.labels_
        for i, im in enumerate(images):
            cluster = cluster_labels[i]
            folder = os.path.join(images_path, '..', '%d_clusters' % n_clusters, str(cluster))
            item = os.path.join(folder, os.path.basename(names[i]))
            if not os.path.exists(folder):
                os.makedirs(folder, 777, True)
            shutil.copy(names[i], item)
    """
    plt.plot(range(20, 40), inertia_data, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()
    """


if __name__ == '__main__':
    main()
