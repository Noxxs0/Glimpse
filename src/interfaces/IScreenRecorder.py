from abc import ABC, abstractmethod

class IScreenRecorder(ABC):
  @abstractmethod
  def startCapture(self):
    pass