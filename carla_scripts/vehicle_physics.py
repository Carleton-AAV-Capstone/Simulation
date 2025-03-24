import carla

def main():
    # Connect to client
    client = carla.Client('localhost', 2000)
    client.set_timeout(2.0)

    # Get World and Actor
    world = client.get_world()
    actors = world.get_actors()

    # Get ego vehicle
    vehicle = [actor for actor in actors if 'vehicle.micro.microlino' in actor.type_id][0]

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
