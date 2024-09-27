from openalea.plantgl.all import Viewer


def saveImage(image_name, scene):
    """ """
    Viewer.frameGL.saveImage(image_name)
    return (scene,)
