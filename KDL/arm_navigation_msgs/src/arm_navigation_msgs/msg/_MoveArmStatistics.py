"""autogenerated by genpy from arm_navigation_msgs/MoveArmStatistics.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import arm_navigation_msgs.msg

class MoveArmStatistics(genpy.Message):
  _md5sum = "d83dee1348791a0d1414257b41bc161f"
  _type = "arm_navigation_msgs/MoveArmStatistics"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int32 request_id
string result
arm_navigation_msgs/ArmNavigationErrorCodes error_code

float64 planning_time
float64 smoothing_time
float64 ik_time
float64 time_to_execution
float64 time_to_result

bool preempted

float64 num_replans
float64 trajectory_duration

string planner_service_name

================================================================================
MSG: arm_navigation_msgs/ArmNavigationErrorCodes
int32 val

# overall behavior
int32 PLANNING_FAILED=-1
int32 SUCCESS=1
int32 TIMED_OUT=-2

# start state errors
int32 START_STATE_IN_COLLISION=-3
int32 START_STATE_VIOLATES_PATH_CONSTRAINTS=-4

# goal errors
int32 GOAL_IN_COLLISION=-5
int32 GOAL_VIOLATES_PATH_CONSTRAINTS=-6

# robot state
int32 INVALID_ROBOT_STATE=-7
int32 INCOMPLETE_ROBOT_STATE=-8

# planning request errors
int32 INVALID_PLANNER_ID=-9
int32 INVALID_NUM_PLANNING_ATTEMPTS=-10
int32 INVALID_ALLOWED_PLANNING_TIME=-11
int32 INVALID_GROUP_NAME=-12
int32 INVALID_GOAL_JOINT_CONSTRAINTS=-13
int32 INVALID_GOAL_POSITION_CONSTRAINTS=-14
int32 INVALID_GOAL_ORIENTATION_CONSTRAINTS=-15
int32 INVALID_PATH_JOINT_CONSTRAINTS=-16
int32 INVALID_PATH_POSITION_CONSTRAINTS=-17
int32 INVALID_PATH_ORIENTATION_CONSTRAINTS=-18

# state/trajectory monitor errors
int32 INVALID_TRAJECTORY=-19
int32 INVALID_INDEX=-20
int32 JOINT_LIMITS_VIOLATED=-21
int32 PATH_CONSTRAINTS_VIOLATED=-22
int32 COLLISION_CONSTRAINTS_VIOLATED=-23
int32 GOAL_CONSTRAINTS_VIOLATED=-24
int32 JOINTS_NOT_MOVING=-25
int32 TRAJECTORY_CONTROLLER_FAILED=-26

# system errors
int32 FRAME_TRANSFORM_FAILURE=-27
int32 COLLISION_CHECKING_UNAVAILABLE=-28
int32 ROBOT_STATE_STALE=-29
int32 SENSOR_INFO_STALE=-30

# kinematics errors
int32 NO_IK_SOLUTION=-31
int32 INVALID_LINK_NAME=-32
int32 IK_LINK_IN_COLLISION=-33
int32 NO_FK_SOLUTION=-34
int32 KINEMATICS_STATE_IN_COLLISION=-35

# general errors
int32 INVALID_TIMEOUT=-36


"""
  __slots__ = ['request_id','result','error_code','planning_time','smoothing_time','ik_time','time_to_execution','time_to_result','preempted','num_replans','trajectory_duration','planner_service_name']
  _slot_types = ['int32','string','arm_navigation_msgs/ArmNavigationErrorCodes','float64','float64','float64','float64','float64','bool','float64','float64','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       request_id,result,error_code,planning_time,smoothing_time,ik_time,time_to_execution,time_to_result,preempted,num_replans,trajectory_duration,planner_service_name

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(MoveArmStatistics, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.request_id is None:
        self.request_id = 0
      if self.result is None:
        self.result = ''
      if self.error_code is None:
        self.error_code = arm_navigation_msgs.msg.ArmNavigationErrorCodes()
      if self.planning_time is None:
        self.planning_time = 0.
      if self.smoothing_time is None:
        self.smoothing_time = 0.
      if self.ik_time is None:
        self.ik_time = 0.
      if self.time_to_execution is None:
        self.time_to_execution = 0.
      if self.time_to_result is None:
        self.time_to_result = 0.
      if self.preempted is None:
        self.preempted = False
      if self.num_replans is None:
        self.num_replans = 0.
      if self.trajectory_duration is None:
        self.trajectory_duration = 0.
      if self.planner_service_name is None:
        self.planner_service_name = ''
    else:
      self.request_id = 0
      self.result = ''
      self.error_code = arm_navigation_msgs.msg.ArmNavigationErrorCodes()
      self.planning_time = 0.
      self.smoothing_time = 0.
      self.ik_time = 0.
      self.time_to_execution = 0.
      self.time_to_result = 0.
      self.preempted = False
      self.num_replans = 0.
      self.trajectory_duration = 0.
      self.planner_service_name = ''

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
      buff.write(_struct_i.pack(self.request_id))
      _x = self.result
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_i5dB2d.pack(_x.error_code.val, _x.planning_time, _x.smoothing_time, _x.ik_time, _x.time_to_execution, _x.time_to_result, _x.preempted, _x.num_replans, _x.trajectory_duration))
      _x = self.planner_service_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.error_code is None:
        self.error_code = arm_navigation_msgs.msg.ArmNavigationErrorCodes()
      end = 0
      start = end
      end += 4
      (self.request_id,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result = str[start:end].decode('utf-8')
      else:
        self.result = str[start:end]
      _x = self
      start = end
      end += 61
      (_x.error_code.val, _x.planning_time, _x.smoothing_time, _x.ik_time, _x.time_to_execution, _x.time_to_result, _x.preempted, _x.num_replans, _x.trajectory_duration,) = _struct_i5dB2d.unpack(str[start:end])
      self.preempted = bool(self.preempted)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planner_service_name = str[start:end].decode('utf-8')
      else:
        self.planner_service_name = str[start:end]
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
      buff.write(_struct_i.pack(self.request_id))
      _x = self.result
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_i5dB2d.pack(_x.error_code.val, _x.planning_time, _x.smoothing_time, _x.ik_time, _x.time_to_execution, _x.time_to_result, _x.preempted, _x.num_replans, _x.trajectory_duration))
      _x = self.planner_service_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.error_code is None:
        self.error_code = arm_navigation_msgs.msg.ArmNavigationErrorCodes()
      end = 0
      start = end
      end += 4
      (self.request_id,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.result = str[start:end].decode('utf-8')
      else:
        self.result = str[start:end]
      _x = self
      start = end
      end += 61
      (_x.error_code.val, _x.planning_time, _x.smoothing_time, _x.ik_time, _x.time_to_execution, _x.time_to_result, _x.preempted, _x.num_replans, _x.trajectory_duration,) = _struct_i5dB2d.unpack(str[start:end])
      self.preempted = bool(self.preempted)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.planner_service_name = str[start:end].decode('utf-8')
      else:
        self.planner_service_name = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
_struct_i5dB2d = struct.Struct("<i5dB2d")
