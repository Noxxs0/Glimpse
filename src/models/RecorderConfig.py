from models.FPS import FPS

class RecorderConfig:
  def __init__(self, fps: FPS) -> None:
    self.fps = fps

  # def __init__(self, name: str, location: str, fileRouteDestination: str) -> None:
    # self.name = name
    # self.location = location
    # self.fileRouteDestination = fileRouteDestination
    # pass