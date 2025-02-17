from abc import ABC, abstractmethod

class IScreenRecorder(ABC):
  @abstractmethod
  def getLocations(self):
    pass