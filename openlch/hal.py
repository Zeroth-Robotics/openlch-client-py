import grpc
from typing import List, Tuple, Dict, Union
from . import hal_pb_pb2
from . import hal_pb_pb2_grpc

__all__ = ['HAL']

__pdoc__ = {}
__pdoc__["hal_pb_pb2"] = None
__pdoc__["hal_pb_pb2_grpc"] = None

class HAL:
    """
    Hardware Abstraction Layer for interacting with the MilkV board.

    Args:
        host (str): The IP address of the MilkV board. Defaults to '192.168.42.1'.
        port (int): The port number for gRPC communication. Defaults to 50051.
    """

    def __init__(self, host: str = '192.168.42.1', port: int = 50051) -> None:
        self.__channel = grpc.insecure_channel(f'{host}:{port}')
        self.__stub = hal_pb_pb2_grpc.ServoControlStub(self.__channel)
        self.servo = self.Servo(self.__stub)
        self.system = self.System(self.__stub)
        self.imu = self.IMU(self.__stub)

    def close(self) -> None:
        """Close the gRPC channel."""
        self.__channel.close()

    class Servo:
        """Class for servo-related operations."""

        def __init__(self, stub):
            self.__stub = stub

        def get_positions(self) -> List[Tuple[int, float, float]]:
            """
            Get current positions and speeds of all servos.

            Returns:
                List[Tuple[int, float, float]]: A list of tuples containing servo IDs, their positions, and speeds.
            """
            response = self.__stub.GetPositions(hal_pb_pb2.Empty())
            return [(pos.id, pos.position, pos.speed) for pos in response.positions]

        def set_positions(self, positions: List[Tuple[int, float]]) -> None:
            """
            Set positions for multiple servos.

            Args:
                positions (List[Tuple[int, float]]): A list of tuples, each containing a servo ID and its target position.
            """
            joint_positions = [
                hal_pb_pb2.JointPosition(id=id, position=position, speed=0)
                for id, position in positions
            ]
            request = hal_pb_pb2.JointPositions(positions=joint_positions)
            self.__stub.SetPositions(request)

        def get_servo_info(self, servo_id: int) -> Dict[str, Union[int, float]]:
            """
            Get detailed information about a specific servo.

            Args:
                servo_id (int): The ID of the servo to query.

            Returns:
                Dict[str, Union[int, float]]: A dictionary containing servo information:

                    id: The ID of the servo

                    temperature: Current temperature of the servo (in degrees Celsius)

                    current: Current draw of the servo (in mAmps)

                    voltage: Voltage supplied to the servo (in volts)

                    speed: Current speed of the servo (in degrees per second)

                    current_position: Current position of the servo (in degrees)

                    min_position: Minimum allowed position of the servo (in degrees)

                    max_position: Maximum allowed position of the servo (in degrees)

            Raises:
                Exception: If there's an error retrieving the servo information.
            """
            request = hal_pb_pb2.ServoId(id=servo_id)
            response = self.__stub.GetServoInfo(request)
            if response.HasField('info'):
                info = response.info
                return {
                    'id': info.id,
                    'temperature': info.temperature,
                    'current': info.current,
                    'voltage': round(info.voltage, 2),
                    'speed': info.speed,
                    'current_position': info.current_position,
                    'min_position': info.min_position,
                    'max_position': info.max_position
                }
            else:
                raise Exception(f"Error: {response.error.message} (Code: {response.error.code})")

        def scan(self) -> List[int]:
            """
            Scan for connected servos.

            Returns:
                List[int]: A list of IDs of the connected servos.
            """
            response = self.__stub.Scan(hal_pb_pb2.Empty())
            return list(response.ids)

        def change_id(self, old_id: int, new_id: int) -> bool:
            """
            Change the ID of a servo.

            Args:
                old_id (int): The current ID of the servo.
                new_id (int): The new ID to assign to the servo.

            Returns:
                bool: True if the ID change was successful, False otherwise.

            Raises:
                Exception: If there's an error changing the servo ID.
            """
            request = hal_pb_pb2.IdChange(old_id=old_id, new_id=new_id)
            response = self.__stub.ChangeId(request)
            if response.HasField('success'):
                return response.success
            else:
                raise Exception(f"Error: {response.error.message} (Code: {response.error.code})")

        def start_calibration(self, servo_id: int) -> bool:
            """
            Start calibration for a specific servo.

            Args:
                servo_id (int): The ID of the servo to calibrate.

            Returns:
                bool: True if calibration started successfully, False otherwise.

            Raises:
                Exception: If there's an error starting the calibration.
            """
            request = hal_pb_pb2.ServoId(id=servo_id)
            response = self.__stub.StartCalibration(request)
            if response.HasField('success'):
                return response.success
            else:
                raise Exception(f"Error: {response.error.message} (Code: {response.error.code})")

        def cancel_calibration(self, servo_id: int) -> bool:
            """
            Cancel ongoing calibration for a specific servo.

            Args:
                servo_id (int): The ID of the servo to cancel calibration for.

            Returns:
                bool: True if calibration was successfully cancelled, False otherwise.

            Raises:
                Exception: If there's an error cancelling the calibration.
            """
            request = hal_pb_pb2.ServoId(id=servo_id)
            response = self.__stub.CancelCalibration(request)
            if response.HasField('success'):
                return response.success
            else:
                raise Exception(f"Error: {response.error.message} (Code: {response.error.code})")

        def get_calibration_status(self) -> Dict[str, Union[bool, int]]:
            """
            Get the current calibration status.

            Returns:
                Dict[str, Union[bool, int]]: A dictionary containing calibration status information.

            Raises:
                Exception: If there's an error retrieving the calibration status.
            """
            response = self.__stub.GetCalibrationStatus(hal_pb_pb2.Empty())
            return {
                'is_calibrating': response.is_calibrating,
                'calibrating_servo_id': response.calibrating_servo_id
            }

        def set_torque(self, torque_settings: List[Tuple[int, float]]) -> None:
            """
            Set torque for multiple servos.

            Args:
                torque_settings (List[Tuple[int, float]]): A list of tuples, each containing a servo ID and its target torque.
            """
            settings = [
                hal_pb_pb2.TorqueSetting(id=id, torque=torque)
                for id, torque in torque_settings
            ]
            request = hal_pb_pb2.TorqueSettings(settings=settings)
            self.__stub.SetTorque(request)

        def set_torque_enable(self, enable_settings: List[Tuple[int, bool]]) -> None:
            """
            Enable or disable torque for multiple servos.

            Args:
                enable_settings (List[Tuple[int, bool]]): A list of tuples, each containing a servo ID and a boolean indicating whether to enable torque.
            """
            settings = [
                hal_pb_pb2.TorqueEnableSetting(id=id, enable=enable)
                for id, enable in enable_settings
            ]
            request = hal_pb_pb2.TorqueEnableSettings(settings=settings)
            self.__stub.SetTorqueEnable(request)

    class System:
        """Class for system-related operations."""

        def __init__(self, stub):
            self.__stub = stub

        def set_wifi_info(self, ssid: str, password: str) -> None:
            """
            Set WiFi credentials for the MilkV board.

            Args:
                ssid (str): The SSID of the WiFi network.
                password (str): The password for the WiFi network.
            """
            request = hal_pb_pb2.WifiCredentials(ssid=ssid, password=password)
            self.__stub.SetWifiInfo(request)

        def start_video_stream(self) -> None:
            """Start the video stream."""
            self.__stub.StartVideoStream(hal_pb_pb2.Empty())

        def stop_video_stream(self) -> None:
            """Stop the video stream."""
            self.__stub.StopVideoStream(hal_pb_pb2.Empty())

        def get_video_stream_urls(self) -> Dict[str, List[str]]:
            """
            Get the URLs for various video stream formats.

            Returns:
                Dict[str, List[str]]: A dictionary containing lists of URLs for different stream formats:

                    webrtc: List of WebRTC stream URLs

                    hls: List of HTTP Live Streaming (HLS) URLs

                    hls_ll: List of Low-Latency HLS URLs

                    mse: List of Media Source Extension (MSE) URLs

                    rtsp: List of Real-Time Streaming Protocol (RTSP) URLs

            Each list may contain one or more URLs depending on the available streams.
            """
            response = self.__stub.GetVideoStreamUrls(hal_pb_pb2.Empty())
            return {
                'webrtc': list(response.webrtc),
                'hls': list(response.hls),
                'hls_ll': list(response.hls_ll),
                'mse': list(response.mse),
                'rtsp': list(response.rtsp)
            }

    class IMU:
        """Class for IMU-related operations."""

        def __init__(self, stub):
            self.__stub = stub

        def get_data(self) -> Dict[str, Dict[str, float]]:
            """
            Get current IMU sensor data including gyroscope and accelerometer readings.

            Returns:
                Dict[str, Dict[str, float]]: A dictionary containing gyroscope and accelerometer data:
                    {
                        'gyro': {'x': float, 'y': float, 'z': float},  # Angular velocity in degrees/second
                        'accel': {'x': float, 'y': float, 'z': float}  # Linear acceleration in g
                    }
            """
            response = self.__stub.GetImuData(hal_pb_pb2.Empty())
            return {
                'gyro': {'x': response.gyro.x, 'y': response.gyro.y, 'z': response.gyro.z},
                'accel': {'x': response.accel.x, 'y': response.accel.y, 'z': response.accel.z}
            }
