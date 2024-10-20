"""Defines the CLI for the OpenLCH project."""

import subprocess
import click
from .hal import HAL

DEFAULT_IP = "192.168.42.1"

@click.group()
def cli() -> None:
    """OpenLCH CLI tool for interacting with MilkV boards.

    Available commands:
    - ping: Ping the MilkV board
    - get-positions: Get current positions of all servos
    - set-position: Set position for a specific servo
    - set-wifi: Set WiFi credentials for the MilkV board
    - get-servo-info: Get information about a specific servo
    - scan-servos: Scan for connected servos
    - change-servo-id: Change the ID of a servo
    - start-calibration: Start calibration for a specific servo
    - cancel-calibration: Cancel ongoing calibration for a specific servo
    - get-calibration-status: Get the current calibration status
    - start-video-stream: Start the video stream
    - stop-video-stream: Stop the video stream
    - get-video-stream-urls: Get the URLs for various video stream formats

    Use 'openlch COMMAND --help' for more information on a specific command.
    """
    pass

@cli.command()
@click.argument("ip", default=DEFAULT_IP)
def ping(ip: str) -> None:
    """Ping the MilkV board at the specified IP address."""
    try:
        result = subprocess.run(["ping", "-c", "1", ip], capture_output=True, text=True, check=False)
        if result.returncode == 0:
            click.echo(f"Successfully pinged {ip}")
            click.echo(result.stdout)
        else:
            click.echo(f"Failed to ping {ip}")
            click.echo(result.stderr)
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")

@cli.command()
@click.argument("ip", default=DEFAULT_IP)
def get_positions(ip: str) -> None:
    """Get current positions of all servos."""
    hal = HAL(ip)
    try:
        positions = hal.servo.get_positions()
        click.echo("Current positions:")
        for id, position in positions:
            click.echo(f"Servo {id}: {position}")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("id", type=int)
@click.argument("position", type=float)
@click.argument("ip", default=DEFAULT_IP)
def set_position(id: int, position: float, ip: str) -> None:
    """Set position for a specific servo."""
    hal = HAL(ip)
    try:
        hal.servo.set_positions([(id, position)])
        click.echo(f"Position set for servo {id} to {position}")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("ssid")
@click.argument("password")
@click.argument("ip", default=DEFAULT_IP)
def set_wifi(ssid: str, password: str, ip: str) -> None:
    """Set WiFi credentials for the MilkV board."""
    hal = HAL(ip)
    try:
        hal.system.set_wifi_info(ssid, password)
        click.echo("WiFi credentials set successfully")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("id", type=int)
@click.argument("ip", default=DEFAULT_IP)
def get_servo_info(id: int, ip: str) -> None:
    """Get information about a specific servo."""
    hal = HAL(ip)
    try:
        info = hal.servo.get_servo_info(id)
        click.echo(f"Servo {id} info:")
        for key, value in info.items():
            click.echo(f"{key}: {value}")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("ip", default=DEFAULT_IP)
def scan_servos(ip: str) -> None:
    """Scan for connected servos."""
    hal = HAL(ip)
    try:
        servo_ids = hal.servo.scan()
        click.echo("Found servo IDs:")
        for id in servo_ids:
            click.echo(id)
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("old_id", type=int)
@click.argument("new_id", type=int)
@click.argument("ip", default=DEFAULT_IP)
def change_servo_id(old_id: int, new_id: int, ip: str) -> None:
    """Change the ID of a servo."""
    hal = HAL(ip)
    try:
        success = hal.servo.change_id(old_id, new_id)
        if success:
            click.echo(f"Successfully changed servo ID from {old_id} to {new_id}")
        else:
            click.echo("Failed to change servo ID")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("servo_id", type=int)
@click.argument("ip", default=DEFAULT_IP)
def start_calibration(servo_id: int, ip: str) -> None:
    """Start calibration for a specific servo."""
    hal = HAL(ip)
    try:
        success = hal.servo.start_calibration(servo_id)
        if success:
            click.echo(f"Calibration started for servo {servo_id}")
        else:
            click.echo(f"Failed to start calibration for servo {servo_id}")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("servo_id", type=int)
@click.argument("ip", default=DEFAULT_IP)
def cancel_calibration(servo_id: int, ip: str) -> None:
    """Cancel ongoing calibration for a specific servo."""
    hal = HAL(ip)
    try:
        success = hal.servo.cancel_calibration(servo_id)
        if success:
            click.echo(f"Calibration cancelled for servo {servo_id}")
        else:
            click.echo(f"Failed to cancel calibration for servo {servo_id}")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("ip", default=DEFAULT_IP)
def get_calibration_status(ip: str) -> None:
    """Get the current calibration status."""
    hal = HAL(ip)
    try:
        status = hal.servo.get_calibration_status()
        if status['is_calibrating']:
            click.echo(f"Calibration in progress for servo {status['calibrating_servo_id']}")
        else:
            click.echo("No calibration in progress")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("ip", default=DEFAULT_IP)
def start_video_stream(ip: str) -> None:
    """Start the video stream."""
    hal = HAL(ip)
    try:
        hal.system.start_video_stream()
        click.echo("Video stream started")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("ip", default=DEFAULT_IP)
def stop_video_stream(ip: str) -> None:
    """Stop the video stream."""
    hal = HAL(ip)
    try:
        hal.system.stop_video_stream()
        click.echo("Video stream stopped")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

@cli.command()
@click.argument("ip", default=DEFAULT_IP)
def get_video_stream_urls(ip: str) -> None:
    """Get the URLs for various video stream formats."""
    hal = HAL(ip)
    try:
        urls = hal.system.get_video_stream_urls()
        click.echo("Video stream URLs:")
        for format, url_list in urls.items():
            click.echo(f"{format.upper()}:")
            for url in url_list:
                click.echo(f"  - {url}")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
    finally:
        hal.close()

if __name__ == "__main__":
    cli()
