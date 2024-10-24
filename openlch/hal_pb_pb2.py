# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: hal_pb.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'hal_pb.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0chal_pb.proto\x12\x06hal_pb\"\x07\n\x05\x45mpty\"<\n\rJointPosition\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x01(\x02\x12\r\n\x05speed\x18\x03 \x01(\x02\":\n\x0eJointPositions\x12(\n\tpositions\x18\x01 \x03(\x0b\x32\x15.hal_pb.JointPosition\"1\n\x0fWifiCredentials\x12\x0c\n\x04ssid\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x15\n\x07ServoId\x12\n\n\x02id\x18\x01 \x01(\x05\"\xa3\x01\n\tServoInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x02\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x02\x12\x0f\n\x07voltage\x18\x04 \x01(\x02\x12\r\n\x05speed\x18\x05 \x01(\x02\x12\x18\n\x10\x63urrent_position\x18\x06 \x01(\x02\x12\x14\n\x0cmin_position\x18\x07 \x01(\x02\x12\x14\n\x0cmax_position\x18\x08 \x01(\x02\"d\n\x11ServoInfoResponse\x12!\n\x04info\x18\x01 \x01(\x0b\x32\x11.hal_pb.ServoInfoH\x00\x12\"\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hal_pb.ErrorInfoH\x00\x42\x08\n\x06result\"S\n\x10\x43hangeIdResponse\x12\x11\n\x07success\x18\x01 \x01(\x08H\x00\x12\"\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hal_pb.ErrorInfoH\x00\x42\x08\n\x06result\"*\n\tErrorInfo\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\"\x17\n\x08ServoIds\x12\x0b\n\x03ids\x18\x01 \x03(\x05\"*\n\x08IdChange\x12\x0e\n\x06old_id\x18\x01 \x01(\x05\x12\x0e\n\x06new_id\x18\x02 \x01(\x05\"Y\n\x0fVideoStreamUrls\x12\x0e\n\x06webrtc\x18\x01 \x03(\t\x12\x0b\n\x03hls\x18\x02 \x03(\t\x12\x0e\n\x06hls_ll\x18\x03 \x03(\t\x12\x0b\n\x03mse\x18\x04 \x03(\t\x12\x0c\n\x04rtsp\x18\x05 \x03(\t\"V\n\x13\x43\x61librationResponse\x12\x11\n\x07success\x18\x01 \x01(\x08H\x00\x12\"\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x11.hal_pb.ErrorInfoH\x00\x42\x08\n\x06result\"I\n\x11\x43\x61librationStatus\x12\x16\n\x0eis_calibrating\x18\x01 \x01(\x08\x12\x1c\n\x14\x63\x61librating_servo_id\x18\x02 \x01(\x05\"9\n\x0eTorqueSettings\x12\'\n\x08settings\x18\x01 \x03(\x0b\x32\x15.hal_pb.TorqueSetting\"+\n\rTorqueSetting\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06torque\x18\x02 \x01(\x02\"E\n\x14TorqueEnableSettings\x12-\n\x08settings\x18\x01 \x03(\x0b\x32\x1b.hal_pb.TorqueEnableSetting\"1\n\x13TorqueEnableSetting\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06\x65nable\x18\x02 \x01(\x08\x32\xac\x06\n\x0cServoControl\x12\x35\n\x0cGetPositions\x12\r.hal_pb.Empty\x1a\x16.hal_pb.JointPositions\x12\x35\n\x0cSetPositions\x12\x16.hal_pb.JointPositions\x1a\r.hal_pb.Empty\x12\x35\n\x0bSetWifiInfo\x12\x17.hal_pb.WifiCredentials\x1a\r.hal_pb.Empty\x12:\n\x0cGetServoInfo\x12\x0f.hal_pb.ServoId\x1a\x19.hal_pb.ServoInfoResponse\x12\'\n\x04Scan\x12\r.hal_pb.Empty\x1a\x10.hal_pb.ServoIds\x12\x36\n\x08\x43hangeId\x12\x10.hal_pb.IdChange\x1a\x18.hal_pb.ChangeIdResponse\x12@\n\x10StartCalibration\x12\x0f.hal_pb.ServoId\x1a\x1b.hal_pb.CalibrationResponse\x12\x41\n\x11\x43\x61ncelCalibration\x12\x0f.hal_pb.ServoId\x1a\x1b.hal_pb.CalibrationResponse\x12\x30\n\x10StartVideoStream\x12\r.hal_pb.Empty\x1a\r.hal_pb.Empty\x12/\n\x0fStopVideoStream\x12\r.hal_pb.Empty\x1a\r.hal_pb.Empty\x12<\n\x12GetVideoStreamUrls\x12\r.hal_pb.Empty\x1a\x17.hal_pb.VideoStreamUrls\x12@\n\x14GetCalibrationStatus\x12\r.hal_pb.Empty\x1a\x19.hal_pb.CalibrationStatus\x12\x32\n\tSetTorque\x12\x16.hal_pb.TorqueSettings\x1a\r.hal_pb.Empty\x12>\n\x0fSetTorqueEnable\x12\x1c.hal_pb.TorqueEnableSettings\x1a\r.hal_pb.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hal_pb_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=24
  _globals['_EMPTY']._serialized_end=31
  _globals['_JOINTPOSITION']._serialized_start=33
  _globals['_JOINTPOSITION']._serialized_end=93
  _globals['_JOINTPOSITIONS']._serialized_start=95
  _globals['_JOINTPOSITIONS']._serialized_end=153
  _globals['_WIFICREDENTIALS']._serialized_start=155
  _globals['_WIFICREDENTIALS']._serialized_end=204
  _globals['_SERVOID']._serialized_start=206
  _globals['_SERVOID']._serialized_end=227
  _globals['_SERVOINFO']._serialized_start=230
  _globals['_SERVOINFO']._serialized_end=393
  _globals['_SERVOINFORESPONSE']._serialized_start=395
  _globals['_SERVOINFORESPONSE']._serialized_end=495
  _globals['_CHANGEIDRESPONSE']._serialized_start=497
  _globals['_CHANGEIDRESPONSE']._serialized_end=580
  _globals['_ERRORINFO']._serialized_start=582
  _globals['_ERRORINFO']._serialized_end=624
  _globals['_SERVOIDS']._serialized_start=626
  _globals['_SERVOIDS']._serialized_end=649
  _globals['_IDCHANGE']._serialized_start=651
  _globals['_IDCHANGE']._serialized_end=693
  _globals['_VIDEOSTREAMURLS']._serialized_start=695
  _globals['_VIDEOSTREAMURLS']._serialized_end=784
  _globals['_CALIBRATIONRESPONSE']._serialized_start=786
  _globals['_CALIBRATIONRESPONSE']._serialized_end=872
  _globals['_CALIBRATIONSTATUS']._serialized_start=874
  _globals['_CALIBRATIONSTATUS']._serialized_end=947
  _globals['_TORQUESETTINGS']._serialized_start=949
  _globals['_TORQUESETTINGS']._serialized_end=1006
  _globals['_TORQUESETTING']._serialized_start=1008
  _globals['_TORQUESETTING']._serialized_end=1051
  _globals['_TORQUEENABLESETTINGS']._serialized_start=1053
  _globals['_TORQUEENABLESETTINGS']._serialized_end=1122
  _globals['_TORQUEENABLESETTING']._serialized_start=1124
  _globals['_TORQUEENABLESETTING']._serialized_end=1173
  _globals['_SERVOCONTROL']._serialized_start=1176
  _globals['_SERVOCONTROL']._serialized_end=1988
# @@protoc_insertion_point(module_scope)
