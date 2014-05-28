"""autogenerated by genpy from graph_mapping_msgs/ConstraintGraphMessage.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import graph_mapping_msgs.msg

class ConstraintGraphMessage(genpy.Message):
  _md5sum = "cda8ffff59a7c01fc6f86d350d17f4c7"
  _type = "graph_mapping_msgs/ConstraintGraphMessage"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """Node[] nodes
Edge[] edges
================================================================================
MSG: graph_mapping_msgs/Node
uint32 id

# This array has length 1 if the node has an optimized pose; 0 otherwise
geometry_msgs/Pose[] optimized_pose


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

================================================================================
MSG: graph_mapping_msgs/Edge
uint32 id
GraphConstraint constraint

================================================================================
MSG: graph_mapping_msgs/GraphConstraint
uint32 src
uint32 dest
PoseWithPrecision constraint
================================================================================
MSG: graph_mapping_msgs/PoseWithPrecision
geometry_msgs/Pose pose
float64[36] precision
"""
  __slots__ = ['nodes','edges']
  _slot_types = ['graph_mapping_msgs/Node[]','graph_mapping_msgs/Edge[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       nodes,edges

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ConstraintGraphMessage, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.nodes is None:
        self.nodes = []
      if self.edges is None:
        self.edges = []
    else:
      self.nodes = []
      self.edges = []

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
      length = len(self.nodes)
      buff.write(_struct_I.pack(length))
      for val1 in self.nodes:
        buff.write(_struct_I.pack(val1.id))
        length = len(val1.optimized_pose)
        buff.write(_struct_I.pack(length))
        for val2 in val1.optimized_pose:
          _v1 = val2.position
          _x = _v1
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v2 = val2.orientation
          _x = _v2
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.edges)
      buff.write(_struct_I.pack(length))
      for val1 in self.edges:
        buff.write(_struct_I.pack(val1.id))
        _v3 = val1.constraint
        _x = _v3
        buff.write(_struct_2I.pack(_x.src, _x.dest))
        _v4 = _v3.constraint
        _v5 = _v4.pose
        _v6 = _v5.position
        _x = _v6
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v7 = _v5.orientation
        _x = _v7
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_struct_36d.pack(*_v4.precision))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.nodes is None:
        self.nodes = None
      if self.edges is None:
        self.edges = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.nodes = []
      for i in range(0, length):
        val1 = graph_mapping_msgs.msg.Node()
        start = end
        end += 4
        (val1.id,) = _struct_I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.optimized_pose = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v8 = val2.position
          _x = _v8
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v9 = val2.orientation
          _x = _v9
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.optimized_pose.append(val2)
        self.nodes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.edges = []
      for i in range(0, length):
        val1 = graph_mapping_msgs.msg.Edge()
        start = end
        end += 4
        (val1.id,) = _struct_I.unpack(str[start:end])
        _v10 = val1.constraint
        _x = _v10
        start = end
        end += 8
        (_x.src, _x.dest,) = _struct_2I.unpack(str[start:end])
        _v11 = _v10.constraint
        _v12 = _v11.pose
        _v13 = _v12.position
        _x = _v13
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v14 = _v12.orientation
        _x = _v14
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 288
        _v11.precision = _struct_36d.unpack(str[start:end])
        self.edges.append(val1)
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
      length = len(self.nodes)
      buff.write(_struct_I.pack(length))
      for val1 in self.nodes:
        buff.write(_struct_I.pack(val1.id))
        length = len(val1.optimized_pose)
        buff.write(_struct_I.pack(length))
        for val2 in val1.optimized_pose:
          _v15 = val2.position
          _x = _v15
          buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
          _v16 = val2.orientation
          _x = _v16
          buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
      length = len(self.edges)
      buff.write(_struct_I.pack(length))
      for val1 in self.edges:
        buff.write(_struct_I.pack(val1.id))
        _v17 = val1.constraint
        _x = _v17
        buff.write(_struct_2I.pack(_x.src, _x.dest))
        _v18 = _v17.constraint
        _v19 = _v18.pose
        _v20 = _v19.position
        _x = _v20
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
        _v21 = _v19.orientation
        _x = _v21
        buff.write(_struct_4d.pack(_x.x, _x.y, _x.z, _x.w))
        buff.write(_v18.precision.tostring())
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.nodes is None:
        self.nodes = None
      if self.edges is None:
        self.edges = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.nodes = []
      for i in range(0, length):
        val1 = graph_mapping_msgs.msg.Node()
        start = end
        end += 4
        (val1.id,) = _struct_I.unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.optimized_pose = []
        for i in range(0, length):
          val2 = geometry_msgs.msg.Pose()
          _v22 = val2.position
          _x = _v22
          start = end
          end += 24
          (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
          _v23 = val2.orientation
          _x = _v23
          start = end
          end += 32
          (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
          val1.optimized_pose.append(val2)
        self.nodes.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.edges = []
      for i in range(0, length):
        val1 = graph_mapping_msgs.msg.Edge()
        start = end
        end += 4
        (val1.id,) = _struct_I.unpack(str[start:end])
        _v24 = val1.constraint
        _x = _v24
        start = end
        end += 8
        (_x.src, _x.dest,) = _struct_2I.unpack(str[start:end])
        _v25 = _v24.constraint
        _v26 = _v25.pose
        _v27 = _v26.position
        _x = _v27
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        _v28 = _v26.orientation
        _x = _v28
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _struct_4d.unpack(str[start:end])
        start = end
        end += 288
        _v25.precision = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
        self.edges.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_36d = struct.Struct("<36d")
_struct_4d = struct.Struct("<4d")
_struct_2I = struct.Struct("<2I")
_struct_3d = struct.Struct("<3d")
