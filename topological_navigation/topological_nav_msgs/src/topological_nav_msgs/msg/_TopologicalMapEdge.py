"""autogenerated by genpy from topological_nav_msgs/TopologicalMapEdge.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class TopologicalMapEdge(genpy.Message):
  _md5sum = "dff6569149701e0971e585b9fd6fe1e7"
  _type = "topological_nav_msgs/TopologicalMapEdge"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Info stored with an edge in 2d topological map

# Id of this edge in the topological map
uint32 id

# Id of the source node
uint32 src

# Id of the destination node
uint32 dest

# Pose of origin of destination node's coordinate frame
# represented in the source node's coordinate frame
geometry_msgs/Pose offset

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['id','src','dest','offset']
  _slot_types = ['uint32','uint32','uint32','geometry_msgs/Pose']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,src,dest,offset

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TopologicalMapEdge, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.src is None:
        self.src = 0
      if self.dest is None:
        self.dest = 0
      if self.offset is None:
        self.offset = geometry_msgs.msg.Pose()
    else:
      self.id = 0
      self.src = 0
      self.dest = 0
      self.offset = geometry_msgs.msg.Pose()

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
      buff.write(_struct_3I7d.pack(_x.id, _x.src, _x.dest, _x.offset.position.x, _x.offset.position.y, _x.offset.position.z, _x.offset.orientation.x, _x.offset.orientation.y, _x.offset.orientation.z, _x.offset.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.offset is None:
        self.offset = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 68
      (_x.id, _x.src, _x.dest, _x.offset.position.x, _x.offset.position.y, _x.offset.position.z, _x.offset.orientation.x, _x.offset.orientation.y, _x.offset.orientation.z, _x.offset.orientation.w,) = _struct_3I7d.unpack(str[start:end])
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
      buff.write(_struct_3I7d.pack(_x.id, _x.src, _x.dest, _x.offset.position.x, _x.offset.position.y, _x.offset.position.z, _x.offset.orientation.x, _x.offset.orientation.y, _x.offset.orientation.z, _x.offset.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.offset is None:
        self.offset = geometry_msgs.msg.Pose()
      end = 0
      _x = self
      start = end
      end += 68
      (_x.id, _x.src, _x.dest, _x.offset.position.x, _x.offset.position.y, _x.offset.position.z, _x.offset.orientation.x, _x.offset.orientation.y, _x.offset.orientation.z, _x.offset.orientation.w,) = _struct_3I7d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I7d = struct.Struct("<3I7d")
