import numpy as np
from util.camera_pose_visualizer import CameraPoseVisualizer

if __name__ == '__main__':
    # argument : the minimum/maximum value of x, y, z
    visualizer = CameraPoseVisualizer([-50, 50], [-50, 50], [0, 50])

    # argument : extrinsic matrix, color, scaled focal length(z-axis length of frame body of camera
    visualizer.extrinsic2pyramid(np.eye(4), 'c', 10)

    visualizer.show()
