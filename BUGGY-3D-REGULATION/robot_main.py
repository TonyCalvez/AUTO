import robot_control

if __name__ == "__main__":
    robot = robot_control.RobotControl()

    robot.goLineOdometer(0.5)
    robot.inPlaceTurnLeft()
    robot.goLineOdometer(0.5)
    robot.inPlaceTurnRight()
    # robot.goLineOdometer(1.5)
    robot.wallFollower()
    robot.inPlaceTurnLeft()
    robot.wallFollower()

    robot.inPlaceTurnLeft()

    robot.wallFollower()
    robot.stopItNow()
