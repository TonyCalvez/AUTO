import numpy as np
import time
import random
import sonar_filter
import rob1a_v01 as rob1a


class RobotControl:
    def __init__(self):
        self.rb = rob1a.Rob1A()
        self.distBetweenWheels = 0.12
        self.nTicksPerRevol = 720
        self.wheelDiameter = 0.06
        self.biasValueFront = self.bias(0.87, "front")
        self.biasValueRight = 0
        self.loopIterTime = 0.050

    def testMove(self, rb: object, speedLeft: object, speedRight: object, duration: object) -> object:
        # forward motion
        rb.set_speed(speedLeft, speedRight)
        tStart = time.time()
        while time.time() - tStart < duration:
            time.sleep(self.loopIterTime)
        # stop the robot
        rb.stop()

    def testInfiniteObstacle(self, rb):
        legTimeMax = 5.0  # always turn after 5s (even if no obsctacle)
        distObstacle = 0.3  # stops and change direction if obstacle
        # at less than 30 cm
        while True:  # infinite loop : stop by typing ctrl-C
            rb.set_speed(90, 90)
            tStartLeg = time.time()
            while True:
                t0 = time.time()
                if time.time() - tStartLeg >= legTimeMax:
                    break
                distFront = rb.get_sonar("front")
                # print ("distFront :",distFront)
                if distFront != 0.0 and distFront < distObstacle:
                    break
                t1 = time.time()
                dt = self.loopIterTime - (t1 - t0)
                if dt > 0:
                    time.sleep(dt)  # wait for end of iteration
            # in the case the robot is trapped in front of a wall
            # go back at speed 40 for 0.5 seconds
            rb.set_speed(-40, -40)
            time.sleep(0.5)
            # set random orientation by setting rotation duration
            # minimum time is 0.2 seconds, max is 1.5 seconds
            rotationTime = 0.2 + 1.3 * random.random()
            rotationDirection = random.random()
            if rotationDirection < 0.5:
                self.testMove(rb, 40, -40, rotationTime)
            else:
                self.testMove(rb, -40, 40, rotationTime)

    def inPlaceTurnRight(self, ang=90, speed=5):
        n = 1440 / 360
        impulsions = n * ang
        offsetLeft, offsetRight = self.rb.get_odometers()
        x = 0
        t0 = 0
        self.rb.set_speed(-speed, speed)
        while x < impulsions:
            t0 = time.time()
            odoLeft, odoRight = self.rb.get_odometers()
            x = odoRight - offsetRight
            t1 = time.time()
            dt = np.abs(self.loopIterTime - (t1 - t0))
            time.sleep(dt)
        self.rb.stop()

    def inPlaceTurnLeft(self, ang=90, speed=5):  # ang in degrees
        n = 1440 / 360
        impulsions = n * ang
        offsetLeft, offsetRight = self.rb.get_odometers()
        x = 0
        t0 = 0
        self.rb.set_speed(speed, -speed)
        while x < impulsions:
            t0 = time.time()
            odoLeft, odoRight = self.rb.get_odometers()
            x = odoLeft - offsetLeft
            t1 = time.time()
            dt = np.abs(self.loopIterTime - (t1 - t0))
            time.sleep(dt)
        self.rb.stop()

    def goLineOdometer(self, dist, speed=100):
        perim_roue = 0.1885 * 2
        dist = (dist) / perim_roue
        impulsions = dist * 1440
        offsetRight, offsetLeft = self.rb.get_odometers()
        x = 0
        t0 = 0
        distFront = self.rb.get_sonar("front") + self.biasValueFront

        self.rb.set_speed(speed, speed)

        fltFront = sonar_filter.SonarFilter()
        fltFront.set_iir_a(0.7)
        fltFront.reset_iir()
        fltFront.set_bias(self.biasValueFront)

        while x < impulsions or (distFront > 0.45 or distFront == 0):
            t0 = time.time()
            odoRight, odoLeft = self.rb.get_odometers()
            x = odoLeft - offsetLeft
            distFrontCompute = self.rb.get_sonar("front")
            if distFrontCompute != 0:
                distFront = fltFront.median_filter(distFrontCompute)
                distFront = fltFront.iir_filter(distFront)

            t1 = time.time()
            dt = np.abs(self.loopIterTime - (t1 - t0))
            time.sleep(dt)
        self.rb.stop()

    def wallFollower(self, dist=0, wall="null", setPoint=0.5, nominalSpeed=100, timer=0):

        # INIT FILTER
        fltFront = sonar_filter.SonarFilter()
        fltFront.set_iir_a(0.7)
        fltFront.reset_iir()
        fltFront.set_bias(self.biasValueFront)
        flt = sonar_filter.SonarFilter()
        flt.set_iir_a(0.7)
        flt.reset_iir()
        flt.set_bias(self.biasValueRight)
        # END FILTER

        # COEFF
        kp = 10
        kd = 1000

        # INIT ODOMETER
        perim_roue = 0.1885 * 2
        dist = (dist) / perim_roue
        impulsions = dist * 1440
        offsetRight, offsetLeft = self.rb.get_odometers()
        impulsionscal = 0

        # INIT SONAR
        distFront = self.rb.get_sonar("front")
        distRight = self.rb.get_sonar("right")
        distLeft = self.rb.get_sonar("left")

        # INIT BOUCLE
        deltaSpeedMax = 20
        derivOk = False
        lastError = 0

        if wall == "null":
            if distRight < 1.5 and distRight != 0:
                wall = "right"
            elif distLeft < 1.5 and distLeft != 0:
                wall = "left"
            else:
                wall = "null"

        print("MUR:" + wall)

        while distFront > 0.45 or distFront == 0 or impulsionscal < impulsions:
            distFrontCompute = self.rb.get_sonar("front")
            if distFrontCompute !=0:
                distFront = fltFront.median_filter(distFrontCompute)
                distFront = fltFront.iir_filter(distFront)

            odoRight, odoLeft = self.rb.get_odometers()
            if dist == 0:
                impulsionscal = 0
            else:
                impulsionscal = odoLeft - offsetLeft

            distWallCompute = self.rb.get_sonar(wall)
            distWall = flt.median_filter(distWallCompute)
            distWall = flt.iir_filter(distWall)
            ControlError = setPoint - distWall

            if distWallCompute !=0:
                if derivOk:
                    derivError = ControlError - lastError
                    deltaSpeed = kp * ControlError + kd * derivError
                else:
                    deltaSpeed = kp * ControlError

                if deltaSpeed > deltaSpeedMax:
                    deltaSpeed = deltaSpeedMax
                if deltaSpeed < - deltaSpeedMax:
                    deltaSpeed = - deltaSpeedMax

                if wall == "right":
                    self.rb.set_speed(nominalSpeed - deltaSpeed, nominalSpeed + deltaSpeed)
                elif wall == "left":
                    self.rb.set_speed(nominalSpeed + deltaSpeed, nominalSpeed - deltaSpeed)
                lastError = ControlError
                derivOk = True

            else:
                self.rb.stop()
                break
        # while distFront > 0.5 or distFront == 0:
        #     t0 = time.time()
        #
        #     print(distFront)
        #
        #     if wall == "left" or wall == "right":
        #         distcomputelateral = self.rb.get_sonar(wall)
        #     else:
        #         distcomputelateral = 0
        #
        #     if True:
        #         distWall = flt.iir_filter(flt.median_filter(self.rb.get_sonar(distcomputelateral)))
        #         ControlError = setPoint - distWall
        #
        #         if derivOk:
        #             derivError = ControlError - lastError
        #             deltaSpeed = kp * ControlError + kd * derivError
        #         else:
        #             deltaSpeed = kp * ControlError
        #
        #         if deltaSpeed > deltaSpeedMax:
        #             deltaSpeed = deltaSpeedMax
        #
        #         if deltaSpeed < - deltaSpeedMax:
        #             deltaSpeed = - deltaSpeedMax
        #
        #         if wall == "right":
        #             self.rb.set_speed(nominalSpeed - deltaSpeed, nominalSpeed + deltaSpeed)
        #             print("Le robot va a gauche")
        #
        #         elif wall == "left":
        #             self.rb.set_speed(nominalSpeed + deltaSpeed, nominalSpeed - deltaSpeed)
        #             print("Le robot va a gauche")
        #
        #         lastError = ControlError
        #         derivOk = True
        #
        #     else:
        #         self.rb.set_speed(nominalSpeed, nominalSpeed)
        #
        #     distFront = fltFront.iir_filter(fltFront.median_filter(self.rb.get_sonar("front")))
        #
        #     t1 = time.time()
        #     dt = np.abs(self.loopIterTime - (t1 - t0))
        #     time.sleep(dt)
        self.rb.stop()

    def bias(self, distTheorique, direction, n=50):
        ts = np.zeros(n)
        loop_time = 0.100  # 100 ms (or 10 Hz)
        distfront = 0
        flt = sonar_filter.SonarFilter()
        flt.set_iir_a(0.7)
        flt.reset_iir()
        flt.set_bias(0)
        for i in range(n):
            t0 = time.time()
            distWallCompute = self.rb.get_sonar(direction)
            distWall = flt.median_filter(distWallCompute)
            distWall = flt.iir_filter(distWall)
            ts[i] = distWall
            t1 = time.time()
            dt = loop_time - (t1 - t0)
            if dt > 0:
                time.sleep(dt)
            else:
                print("overtime !!")
        self.rb.stop()
        bias = distTheorique - distWall
        return -bias

    def stopItNow(self):
        self.rb.set_speed(0, 0)
        self.rb.stop()
        self.rb.log_file_off()  # end log
        self.rb.full_end()
