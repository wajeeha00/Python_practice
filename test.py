class MercedesBenz:
  name="benz"
  color=""
  def __init__(self, color):
    self._color = color

  @property
  def color(self):
    return self._color
  
  @color.setter
  def color(self,val):
    self._color = val
  
  def drive(self):
    return self
  
mb = MercedesBenz("red")

mb.color="blue"

print(mb.color)