import robot_control

if __name__ == "__main__":
    robot = robot_control.RobotControl()

    robot.goLineOdometer(0.5)
    robot.inPlaceTurnLeft()
    robot.goLineOdometer(0.5)
    robot.inPlaceTurnRight()
    robot.goLineOdometer(0.6)
    robot.wallFollower(wall="left", nominalSpeed=10)
    robot.inPlaceTurnLeft()
    robot.wallFollower(wall="left")
    robot.inPlaceTurnLeft()
    robot.wallFollower(wall="left")
    robot.inPlaceTurnLeft(ang=100)
    robot.goLineOdometer(dist=0.75)
    robot.wallFollower(setPoint=0.6, nominalSpeed=30)
    robot.inPlaceTurnLeft(ang=45)
    robot.goLineOdometer(dist=0.20)
    robot.inPlaceTurnLeft(ang=80)
    robot.goLineOdometer(dist=0.40)
    robot.wallFollower(wall="right", setPoint=0.6, nominalSpeed=30)
    robot.inPlaceTurnLeft(ang=40)
    robot.wallFollower(wall="left", nominalSpeed=30)

    robot.stopItNow()
