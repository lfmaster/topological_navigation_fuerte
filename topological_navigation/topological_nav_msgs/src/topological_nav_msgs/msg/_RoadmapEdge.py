"""autogenerated by genpy from topological_nav_msgs/RoadmapEdge.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class RoadmapEdge(genpy.Message):
  _md5sum = "7bf8e455ec51d9b3f4f5b22c80145710"
  _type = "topological_nav_msgs/RoadmapEdge"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Info stored with an edge in the roadmap

# Id of this edge in the roadmap.
uint32 id

# Grid this edge lives on
uint32 grid

# Source node of the edge; must belong to the grid.
uint32 src

# Target node of the edge; must belong to the grid.
uint32 dest

# Cost of this edge
float32 cost
"""
  __slots__ = ['id','grid','src','dest','cost']
  _slot_types = ['uint32','uint32','uint32','uint32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,grid,src,dest,cost

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(RoadmapEdge, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.grid is None:
        self.grid = 0
      if self.src is None:
        self.src = 0
      if self.dest is None:
        self.dest = 0
      if self.cost is None:
        self.cost = 0.
    else:
      self.id = 0
      self.grid = 0
      self.src = 0
      self.dest = 0
      self.cost = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_4If.pack(_x.id, _x.grid, _x.src, _x.dest, _x.cost))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 20
      (_x.id, _x.grid, _x.src, _x.dest, _x.cost,) = _struct_4If.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_4If.pack(_x.id, _x.grid, _x.src, _x.dest, _x.cost))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 20
      (_x.id, _x.grid, _x.src, _x.dest, _x.cost,) = _struct_4If.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4If = struct.Struct("<4If")
