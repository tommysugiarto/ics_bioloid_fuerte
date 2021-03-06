"""autogenerated by genpy from arm_navigation_msgs/WorkspaceParameters.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import arm_navigation_msgs.msg
import geometry_msgs.msg
import std_msgs.msg

class WorkspaceParameters(genpy.Message):
  _md5sum = "1487490edff0df276863abf2cf221de5"
  _type = "arm_navigation_msgs/WorkspaceParameters"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# This message contains a set of parameters useful in
# setting up the workspace for planning
arm_navigation_msgs/Shape  workspace_region_shape
geometry_msgs/PoseStamped    workspace_region_pose


================================================================================
MSG: arm_navigation_msgs/Shape
byte SPHERE=0
byte BOX=1
byte CYLINDER=2
byte MESH=3

byte type


#### define sphere, box, cylinder ####
# the origin of each shape is considered at the shape's center

# for sphere
# radius := dimensions[0]

# for cylinder
# radius := dimensions[0]
# length := dimensions[1]
# the length is along the Z axis

# for box
# size_x := dimensions[0]
# size_y := dimensions[1]
# size_z := dimensions[2]
float64[] dimensions


#### define mesh ####

# list of triangles; triangle k is defined by tre vertices located
# at indices triangles[3k], triangles[3k+1], triangles[3k+2]
int32[] triangles
geometry_msgs/Point[] vertices

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

"""
  __slots__ = ['workspace_region_shape','workspace_region_pose']
  _slot_types = ['arm_navigation_msgs/Shape','geometry_msgs/PoseStamped']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       workspace_region_shape,workspace_region_pose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WorkspaceParameters, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.workspace_region_shape is None:
        self.workspace_region_shape = arm_navigation_msgs.msg.Shape()
      if self.workspace_region_pose is None:
        self.workspace_region_pose = geometry_msgs.msg.PoseStamped()
    else:
      self.workspace_region_shape = arm_navigation_msgs.msg.Shape()
      self.workspace_region_pose = geometry_msgs.msg.PoseStamped()

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
      buff.write(_struct_b.pack(self.workspace_region_shape.type))
      length = len(self.workspace_region_shape.dimensions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.pack(pattern, *self.workspace_region_shape.dimensions))
      length = len(self.workspace_region_shape.triangles)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.workspace_region_shape.triangles))
      length = len(self.workspace_region_shape.vertices)
      buff.write(_struct_I.pack(length))
      for val1 in self.workspace_region_shape.vertices:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_struct_3I.pack(_x.workspace_region_pose.header.seq, _x.workspace_region_pose.header.stamp.secs, _x.workspace_region_pose.header.stamp.nsecs))
      _x = self.workspace_region_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.workspace_region_pose.pose.position.x, _x.workspace_region_pose.pose.position.y, _x.workspace_region_pose.pose.position.z, _x.workspace_region_pose.pose.orientation.x, _x.workspace_region_pose.pose.orientation.y, _x.workspace_region_pose.pose.orientation.z, _x.workspace_region_pose.pose.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.workspace_region_shape is None:
        self.workspace_region_shape = arm_navigation_msgs.msg.Shape()
      if self.workspace_region_pose is None:
        self.workspace_region_pose = geometry_msgs.msg.PoseStamped()
      end = 0
      start = end
      end += 1
      (self.workspace_region_shape.type,) = _struct_b.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.workspace_region_shape.dimensions = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.workspace_region_shape.triangles = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.workspace_region_shape.vertices = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.workspace_region_shape.vertices.append(val1)
      _x = self
      start = end
      end += 12
      (_x.workspace_region_pose.header.seq, _x.workspace_region_pose.header.stamp.secs, _x.workspace_region_pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.workspace_region_pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.workspace_region_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.workspace_region_pose.pose.position.x, _x.workspace_region_pose.pose.position.y, _x.workspace_region_pose.pose.position.z, _x.workspace_region_pose.pose.orientation.x, _x.workspace_region_pose.pose.orientation.y, _x.workspace_region_pose.pose.orientation.z, _x.workspace_region_pose.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
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
      buff.write(_struct_b.pack(self.workspace_region_shape.type))
      length = len(self.workspace_region_shape.dimensions)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.workspace_region_shape.dimensions.tostring())
      length = len(self.workspace_region_shape.triangles)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.workspace_region_shape.triangles.tostring())
      length = len(self.workspace_region_shape.vertices)
      buff.write(_struct_I.pack(length))
      for val1 in self.workspace_region_shape.vertices:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_struct_3I.pack(_x.workspace_region_pose.header.seq, _x.workspace_region_pose.header.stamp.secs, _x.workspace_region_pose.header.stamp.nsecs))
      _x = self.workspace_region_pose.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_7d.pack(_x.workspace_region_pose.pose.position.x, _x.workspace_region_pose.pose.position.y, _x.workspace_region_pose.pose.position.z, _x.workspace_region_pose.pose.orientation.x, _x.workspace_region_pose.pose.orientation.y, _x.workspace_region_pose.pose.orientation.z, _x.workspace_region_pose.pose.orientation.w))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.workspace_region_shape is None:
        self.workspace_region_shape = arm_navigation_msgs.msg.Shape()
      if self.workspace_region_pose is None:
        self.workspace_region_pose = geometry_msgs.msg.PoseStamped()
      end = 0
      start = end
      end += 1
      (self.workspace_region_shape.type,) = _struct_b.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      end += struct.calcsize(pattern)
      self.workspace_region_shape.dimensions = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.workspace_region_shape.triangles = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.workspace_region_shape.vertices = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.workspace_region_shape.vertices.append(val1)
      _x = self
      start = end
      end += 12
      (_x.workspace_region_pose.header.seq, _x.workspace_region_pose.header.stamp.secs, _x.workspace_region_pose.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.workspace_region_pose.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.workspace_region_pose.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 56
      (_x.workspace_region_pose.pose.position.x, _x.workspace_region_pose.pose.position.y, _x.workspace_region_pose.pose.position.z, _x.workspace_region_pose.pose.orientation.x, _x.workspace_region_pose.pose.orientation.y, _x.workspace_region_pose.pose.orientation.z, _x.workspace_region_pose.pose.orientation.w,) = _struct_7d.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_b = struct.Struct("<b")
_struct_7d = struct.Struct("<7d")
_struct_3d = struct.Struct("<3d")
