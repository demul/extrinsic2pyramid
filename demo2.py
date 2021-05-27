import os
import glob
import matplotlib as plt
from util.camera_pose_visualizer import CameraPoseVisualizer
from util.camera_parameter_loader import CameraParameterLoader


def plot_scenewise():
    loader = CameraParameterLoader()
    visualizer = CameraPoseVisualizer([-50, 50], [-50, 50], [0, 100])
    list_scene = list(filter(os.path.isdir, glob.glob(os.path.join('dataset', '*', 'trajectory'))))

    for idx_scene, scene in enumerate(list_scene):
        list_frame_annotation = glob.glob(os.path.join(scene, '[0-9][0-9][0-9][0-9][0-9][0-9].json'))
        for idx_frame, frame_annotation in enumerate(list_frame_annotation):
            if idx_frame % 10 == 0:
                extrinsic = loader.get_extrinsic(frame_annotation)
                visualizer.extrinsic2pyramid(extrinsic, plt.cm.rainbow(idx_scene / len(list_scene)), 10)

    list_scene = [os.path.split(os.path.split(i)[0])[-1] for i in list_scene]
    visualizer.customize_legend(list_scene)
    visualizer.show()


def plot_framewise():
    loader = CameraParameterLoader()
    visualizer = CameraPoseVisualizer([-50, 50], [-50, 50], [0, 100])
    list_scene = list(filter(os.path.isdir, glob.glob(os.path.join('dataset', '*', 'trajectory'))))

    max_frame_length = 0
    for idx_scene, scene in enumerate(list_scene):
        list_frame_annotation = glob.glob(os.path.join(scene, '[0-9][0-9][0-9][0-9][0-9][0-9].json'))
        max_frame_length = max(max_frame_length, len(list_frame_annotation))

    for idx_scene, scene in enumerate(list_scene):
        list_frame_annotation = glob.glob(os.path.join(scene, '[0-9][0-9][0-9][0-9][0-9][0-9].json'))
        for idx_frame, frame_annotation in enumerate(list_frame_annotation):
            if idx_frame % 10 == 0:
                extrinsic = loader.get_extrinsic(frame_annotation)
                visualizer.extrinsic2pyramid(extrinsic, plt.cm.rainbow(idx_frame / max_frame_length), 10)

    visualizer.colorbar(max_frame_length)
    visualizer.show()

plot_scenewise()
plot_framewise()