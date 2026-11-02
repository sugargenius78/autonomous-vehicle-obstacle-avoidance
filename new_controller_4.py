from controller import Robot

if __name__ == "__main__":

    # create the Robot instance.
    robot = Robot()
    
    # get the time step of the current world.
    timestep = 64
    max_speed = 6.28
    
    # get motor devices
    left_front_motor = robot.getDevice('motor_1')
    left_rear_motor = robot.getDevice('motor_2')
    right_front_motor = robot.getDevice('motor_3')
    right_rear_motor = robot.getDevice('motor_4')
    
    left_front_motor.setPosition(float('inf'))
    left_rear_motor.setPosition(float('inf'))
    right_front_motor.setPosition(float('inf'))
    right_rear_motor.setPosition(float('inf'))
    
    left_front_motor.setVelocity(0.0)
    left_rear_motor.setVelocity(0.0)
    right_front_motor.setVelocity(0.0)
    right_rear_motor.setVelocity(0.0)
    
    # Initialize the IR sensors
    ir_left = robot.getDevice("ir_left")
    ir_left_1 = robot.getDevice("ir_left_1")
    ir_right = robot.getDevice("ir_right")
    ir_right_1 = robot.getDevice("ir_right_1")
    ir_front = robot.getDevice('ir_front')
    
    # Enable the IR sensors with timestep
    ir_left.enable(timestep)
    ir_left_1.enable(timestep)
    ir_right.enable(timestep)
    ir_right_1.enable(timestep)
    ir_front.enable(timestep)
    
    ir_thresholder = 1000
    
    # Initialize the GPS
    gps = robot.getDevice('gps')
    gps.enable(timestep)
    
    # Target coordinates
    target_position = [1.16869, 1.34784, 0.00472]
    
    # Main loop:
    while robot.step(timestep) != -1:
    
        gps_value = gps.getValues()
        # Print the GPS values
        msg = "GPS values: "
        for each_val in gps_value:
            msg += " {0:0.5f}".format(each_val)
        print(msg)
        
        tolerance = 0.01  
        if (abs(gps_value[0] - target_position[0]) < tolerance and
            abs(gps_value[1] - target_position[1]) < tolerance and
            abs(gps_value[2] - target_position[2]) < tolerance):
            print("Target position reached! Stopping the robot.")
            # Stop the robot if the target is reached
            left_front_motor.setVelocity(0.0)
            left_rear_motor.setVelocity(0.0)
            right_front_motor.setVelocity(0.0)
            right_rear_motor.setVelocity(0.0)
            break  # Exit the loop, stopping the robot
    
        # Get IR sensor values
        ir_left_value = ir_left.getValue()
        ir_left_1_value = ir_left_1.getValue()
        ir_right_value = ir_right.getValue()
        ir_right_1_value = ir_right_1.getValue()
        ir_front_value = ir_front.getValue()
        
        print(f"IR Left Sensor Value:, {ir_left_value}")
        print(f"IR Left_1 Sensor Value:, {ir_left_1_value}")
        print(f"IR Right Sensor Value:, {ir_right_value}")
        print(f"IR Right_1 Sensor Value:, {ir_right_1_value}")
        print(f"IR Front Sensor Value:, {ir_front_value}")
        
        # Handle IR sensor values and robot movement
        if ir_left_value < ir_thresholder:
            print("Object detected on the left. Turning right.")
            left_front_speed = max_speed * 0.0
            left_rear_speed = max_speed * 0.0
            right_rear_speed = max_speed * 1.0
            right_front_speed = max_speed * 1.0
        elif ir_right_value < ir_thresholder:
            print("Object detected on the right. Turning left.")
            left_front_speed = max_speed * 1.0
            left_rear_speed = max_speed * 1.0
            right_front_speed = max_speed * 0.0
            right_rear_speed = max_speed * 0.0
        else:
            print("No object detected. Moving forward.")
            left_front_speed = 0.5 * -max_speed
            left_rear_speed = 0.5 * -max_speed
            right_front_speed = 0.5 * -max_speed
            right_rear_speed = 0.5 * -max_speed    
            
        # Set motor speeds
        left_front_motor.setVelocity(left_front_speed)
        left_rear_motor.setVelocity(left_rear_speed)
        right_front_motor.setVelocity(right_front_speed)
        right_rear_motor.setVelocity(right_rear_speed)
    
    # Enter here exit cleanup code.
