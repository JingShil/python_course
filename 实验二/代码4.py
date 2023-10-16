import numpy as np

def kmeans(data, k, max_iterations=100):
    # 随机初始化k个聚类中心
    centroids = data[np.random.choice(range(len(data)), k, replace=False)]
    
    for _ in range(max_iterations):
        # 分配数据点到最近的聚类中心
        labels = np.argmin(np.linalg.norm(data[:, np.newaxis] - centroids, axis=-1), axis=-1)
        
        # 更新聚类中心为各簇的均值
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])
        
        # 如果聚类中心不再变化，提前结束迭代
        if np.all(centroids == new_centroids):
            break
        
        centroids = new_centroids
    
    return labels, centroids