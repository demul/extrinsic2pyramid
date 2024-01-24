import os
import glob
import matplotlib as plt
import plotly.graph_objects as go

from util.camera_pose_visualizer import CameraPoseVisualizer
from util.camera_parameter_loader import CameraParameterLoader


def plot_scenewise(plotly_viz=False):
    loader = CameraParameterLoader()
    visualizer = CameraPoseVisualizer([-50, 50], [-50, 50], [0, 100])
    list_scene = list(filter(os.path.isdir, glob.glob(os.path.join('dataset', '*', 'trajectory'))))
    dts_name = [os.path.split(os.path.split(i)[0])[-1] for i in list_scene]
    if plotly_viz:
        final_layout = go.Figure()
        final_layout.add_annotation(dict(font=dict(color='black', size=40),
                                         x=0.4,
                                         y=0,
                                         showarrow=False,
                                         text='Scenewise visualization',
                                         xanchor='left'))
        final_layout.update_layout(
            scene=dict(
                xaxis=dict(nticks=4, range=[-50, 50], ),
                yaxis=dict(nticks=4, range=[-50, 50], ),
                zaxis=dict(nticks=4, range=[0, 100], ), ),
            legend=dict(x=0.7, y=0.5, font=dict(color='black', size=20)))

    for idx_scene, scene in enumerate(list_scene):
        show_legend = True
        list_frame_annotation = glob.glob(os.path.join(scene, '[0-9][0-9][0-9][0-9][0-9][0-9].json'))
        for idx_frame, frame_annotation in enumerate(list_frame_annotation):
            if idx_frame % 10 == 0:
                extrinsic = loader.get_extrinsic(frame_annotation)
                visualizer.extrinsic2pyramid(extrinsic, (idx_scene / len(list_scene)), 10,
                                             plotly_viz=plotly_viz, legend_group=dts_name[idx_scene],
                                             name=dts_name[idx_scene], show_legend = show_legend)
                show_legend = False

                if plotly_viz:
                    final_layout.add_trace(visualizer.plotly_data)

    visualizer.customize_legend(dts_name)
    visualizer.show()
    if plotly_viz:
        final_layout.show()



def plot_framewise(plotly_viz=False):
    loader = CameraParameterLoader()
    visualizer = CameraPoseVisualizer([-50, 50], [-50, 50], [0, 100])
    list_scene = list(filter(os.path.isdir, glob.glob(os.path.join('dataset', '*', 'trajectory'))))
    if plotly_viz:
        final_layout = go.Figure()
        final_layout.add_annotation(dict(font=dict(color='black', size=40),
                                         x=0.4,
                                         y=0,
                                         showarrow=False,
                                         text='Framewise visualization',
                                         xanchor='left'))
        final_layout.update_layout(
            scene=dict(
                xaxis=dict(nticks=4, range=[-50, 50], ),
                yaxis=dict(nticks=4, range=[-50, 50], ),
                zaxis=dict(nticks=4, range=[0, 100], ), ),
            legend=dict(x=0.7, y=0.5, font=dict(color='black', size=20)))

    max_frame_length = 0
    for idx_scene, scene in enumerate(list_scene):
        list_frame_annotation = glob.glob(os.path.join(scene, '[0-9][0-9][0-9][0-9][0-9][0-9].json'))
        max_frame_length = max(max_frame_length, len(list_frame_annotation))

    for idx_scene, scene in enumerate(list_scene):
        list_frame_annotation = glob.glob(os.path.join(scene, '[0-9][0-9][0-9][0-9][0-9][0-9].json'))
        for idx_frame, frame_annotation in enumerate(list_frame_annotation):
            if not idx_scene:
                show_legend = True
            else:
                show_legend = False
            if idx_frame % 10 == 0:
                extrinsic = loader.get_extrinsic(frame_annotation)
                visualizer.extrinsic2pyramid(extrinsic, (idx_frame / max_frame_length), 10,
                                             plotly_viz=plotly_viz, legend_group=idx_frame,
                                             name=idx_frame, show_legend=show_legend)

                if plotly_viz:
                    final_layout.add_trace(visualizer.plotly_data)


    visualizer.colorbar(max_frame_length)
    visualizer.show()
    if plotly_viz:
        final_layout.show()

plot_scenewise(plotly_viz=True)
plot_framewise(plotly_viz=True)