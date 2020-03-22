
import math
import BrickPi3 as bp

BP = bp.BrickPi()
right_motor = ""
left_motor = ""
RADIUS = 10
ULTRASONIC = ""

def distance_to_angular(distance):
    angular = (distance * 180) / (math.pi * RADIUS)
    return angular


def move_motors(motor_a, motor_b, angle_a, angle_b):

    target_angle_a = BP.get_motor_encoder(motor_a) + angle_a
    target_angle_b = BP.get_motor_encoder(motor_b) + angle_b

    while True:
        BP.set_motor_position(motor_a, target_angle_a)
        BP.set_motor_position(motor_b, target_angle_b)

        current_angle_a = BP.get_motor_encoder(motor_a)
        current_angle_b = BP.get_motor_encoder(motor_b)
        if current_angle_a > target_angle_a:
            break
        if current_angle_b > target_angle_b:
            break


def turn_right():
    move_motors(left_motor, right_motor, -90, 90)

def turn_left():
    move_motors(left_motor, right_motor, 90, -90)

def turn_around():
    move_motors(left_motor, right_motor, -180, 180)

def stop_robot():
    BP.set_motor_power(right_motor, 0)
    BP.set_motor_power(left_motor, 0)

def move_forward_at_speed(speed):

    #set motor to speed
    BP.set_motor_power(right_motor, speed)
    BP.set_motor_power(left_motor, speed)


def move_forward_to(target_distance):

    # giving the motor encoders some buffer to account for lack in precision
    buffer_zone = 1

    #set motor to position
    target_distance = distance_to_angular(target_distance)
    current_position_right = BP.get_motor_encoder(right_motor)
    current_position_left = BP.get_motor_encoder(left_motor)

    target_position_right, target_position_left = current_position_right + target_distance, current_position_left + target_distance

    while True:
        BP.set_motor_position(right_motor, target_position_right)
        BP.set_motor_position(left_motor, target_position_left)

        current_position_right = BP.get_motor_encoder(right_motor)
        current_position_left = BP.get_motor_encoder(left_motor)

        if current_position_right > (target_position_right - buffer_zone):
            break

        if current_position_left > (target_position_left - buffer_zone):
            break


def move_backward_to(distance):
    move_forward_to(-distance)


def get_sensor_value(sensor):

    while True:
        try:
            sensor_value = BP.get_sensor(sensor)
            return sensor_value
        except bp.SensorError as error:
            print(error)


def drive_a_distance():
    while True:
        distance = input("Distance to which the robot should move? Enter a negative distance to end")
        if distance < 0:
            return
        move_forward_to(distance)

def obstacle_aware_drive():
    speed = input("Enter a speed at which to drive. (negative speed for bachwards")
    while True:
        move_forward_at_speed(speed)
        distance_to_obstacle = get_sensor_value(ULTRASONIC)
        if distance_to_obstacle < 30:
            stop_robot()
            break

if __name__ == "__main__":


    try:
        drive_a_distance()

    except KeyboardInterrupt:
        BP.reset_all()






