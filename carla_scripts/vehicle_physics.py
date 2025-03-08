import carla

def main():
    # Connect to client
    client = carla.Client('127.0.0.1', 2000)
    client.set_timeout(2.0)

    # Get World and Actors
    world = client.get_world()

    # Get ego vehicle
    vehicle = world.get_blueprint_library().find('vehicle.micro.microlino') 

    # Create Wheels Physics Control
    front_left_wheel  = carla.WheelPhysicsControl(tire_friction=2.0, damping_rate=1.5, max_steer_angle=20.0, long_stiff_value=1000)
    front_right_wheel = carla.WheelPhysicsControl(tire_friction=2.0, damping_rate=1.5, max_steer_angle=20.0, long_stiff_value=1000)
    rear_left_wheel   = carla.WheelPhysicsControl(tire_friction=3.0, damping_rate=1.5, max_steer_angle=0.0,  long_stiff_value=1000)
    rear_right_wheel  = carla.WheelPhysicsControl(tire_friction=3.0, damping_rate=1.5, max_steer_angle=0.0,  long_stiff_value=1000)

    wheels = [front_left_wheel, front_right_wheel, rear_left_wheel, rear_right_wheel]

    # Change Vehicle Physics Control parameters of the vehicle
    physics_control = vehicle.get_physics_control()

    physics_control.mass = 272.155
    physics_control.wheels = wheels

    # Apply Vehicle Physics Control for the vehicle
    vehicle.apply_physics_control(physics_control)
    print(physics_control)

if __name__ == '__main__':
    main()
