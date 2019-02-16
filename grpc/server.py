from concurrent import futures
from threading import Thread, Lock

import RPi.GPIO as GPIO
import time
import datetime
import logging
import math
import grpc

import grpc_pb2
import grpc_pb2_grpc

from collections import deque

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)

bottom_servo = GPIO.PWM(12, 50)
top_servo = GPIO.PWM(33, 50)

mutex = Lock()

queue = deque()

# -------------clockwork------------------- dorick branch BEGIN

#---definitions
def unit():
    return .9875
    # 1 unit is .9875

def down_length():
    return -5*unit()
    #add coordinate to move down

def up_length():
    return 5*unit()
    #give coordinate to move up

def rigth_width():
    return 3*unit()
    #give coordinate to move up

def left_width():
    return -3*unit()
    #give coordinate to move up


#--- Returning our starting positions that we would start at
def goToFirstPosit():
	req = {}
	req['x2'] = (-7*unit())
	req['y2'] = (5*unit())
    #return ((-7*.9875),(5*.9875))
    return req

def goToSecondPosit():
	req = {}
	req['x2'] = (-3*unit())
	req['y2'] = (5*unit())
    #return ((-3*.9875),(5*.9875))
    return req

def goToThirdPosit():
	req = {}
	req['x2'] = unit()
	req['y2'] = (5*unit())
    #return ((.9875),(5*.9875))
    return req

def goToLastPosit():
	req = {}
	req['x2'] = (5*unit())
	req['y2'] = (5*unit())
    #return ((5*.9875),(5*.9875))
    return req

def goToCenter():
	req = {}
	req['x2'] = float(0)
	req['y2'] = float(0)
	return req

#--- Number movement methods

def move_to_coordinates(req):
	pan_angle, tilt_angle = scale_box_to_pan_tilt(req)
    pan_pwm = angle_to_pwm_pan(pan_angle)
    tilt_pwm = angle_to_pwm_tilt(tilt_angle)
    move_servos(pan_pwm, tilt_pwm)

def num_0(position):
    req = {}
    if(position == 0):
    	req = goToFirstPosit()
    elif(position == 1):
    	req = goToSecondPosit()
    elif(position == 2):
    	req = goToThirdPosit()
    else:
    	req = goToLastPosit()

    move_to_coordinates(req)

    laser_on()

    req['y2'] += down_length()
    move_to_coordinates(req)
    req['y2'] += down_length()
    move_to_coordinates(req)
    req['x2'] += rigth_width()
    move_to_coordinates(req)
    req['y2'] += up_length()
    move_to_coordinates(req)
    req['y2'] += up_length()
    move_to_coordinates(req)
    req['x2'] += left_width()
    move_to_coordinates(req)

    laser_off()

    return "0"

def num_1():
    req = {}
    if(position == 0):
    	req = goToFirstPosit()
    elif(position == 1):
    	req = goToSecondPosit()
    elif(position == 2):
    	req = goToThirdPosit()
    else:
    	req = goToLastPosit()

    move_to_coordinates(req)


    req['x2'] += rigth_width()
    move_to_coordinates(req)

    laser_on()


    req['y2'] += down_length()
    move_to_coordinates(req)
    req['y2'] += down_length()
    move_to_coordinates(req)

    # req['x2'] += rigth_width()
    # move_to_coordinates(req)
    # req['y2'] += up_length()
    # move_to_coordinates(req)
    # req['y2'] += up_length()
    # move_to_coordinates(req)
    # req['x2'] += left_width()
    # move_to_coordinates(req)

    laser_off()

    return "1"

def num_2():
        req = {}
        if(position == 0):
        	req = goToFirstPosit()
        elif(position == 1):
        	req = goToSecondPosit()
        elif(position == 2):
        	req = goToThirdPosit()
        else:
        	req = goToLastPosit()

        # corner
        move_to_coordinates(req)

        #
        laser_on()

        req['x2'] += rigth_width()
        move_to_coordinates(req)
        req['y2'] += down_length()
        move_to_coordinates(req)
        req['x2'] += left_width()
        move_to_coordinates(req)
        req['y2'] += down_length()
        move_to_coordinates(req)
        req['x2'] += rigth_width()
        move_to_coordinates(req)

        laser_off()

        return "2"


def num_3():
        req = {}
        if(position == 0):
        	req = goToFirstPosit()
        elif(position == 1):
        	req = goToSecondPosit()
        elif(position == 2):
        	req = goToThirdPosit()
        else:
        	req = goToLastPosit()

        # corner
        move_to_coordinates(req)

        #
        laser_on()

        req['x2'] += rigth_width()
        move_to_coordinates(req)
        req['y2'] += down_length()
        move_to_coordinates(req)
        req['x2'] += left_width()
        move_to_coordinates(req)

        laser_off()


        req['x2'] += rigth_width()
        move_to_coordinates(req)

        laseron()

        req['y2'] += down_length()
        move_to_coordinates(req)
        req['x2'] += left_width()
        move_to_coordinates(req)

        laser_off()
        return "3"

def num_4():
    req = {}
    if(position == 0):
    	req = goToFirstPosit()
    elif(position == 1):
    	req = goToSecondPosit()
    elif(position == 2):
    	req = goToThirdPosit()
    else:
    	req = goToLastPosit()

    move_to_coordinates(req)


    laser_on()
    req['y2'] += down_length()
    move_to_coordinates(req)
    req['x2'] += rigth_width()
    move_to_coordinates(req)
    req['y2'] += up_length()
    move_to_coordinates(req)

    laser_off()

    req['y2'] += down_length()
    move_to_coordinates(req)

    laser_on()

    req['y2'] += down_length()
    move_to_coordinates(req)

    laser_off()

    return "4"

def num_5():
    req = {}
    if(position == 0):
    	req = goToFirstPosit()
    elif(position == 1):
    	req = goToSecondPosit()
    elif(position == 2):
    	req = goToThirdPosit()
    else:
    	req = goToLastPosit()

    move_to_coordinates(req)

    req['x2'] += rigth_width()
    move_to_coordinates(req)

    laser_on()

    req['x2'] += left_width()
    move_to_coordinates(req)
    req['y2'] += down_length()
    move_to_coordinates(req)

    req['x2'] += rig_width()
    move_to_coordinates(req)


    req['y2'] += down_length()
    move_to_coordinates(req)
    req['x2'] += left_width()
    move_to_coordinates(req)

    laser_off()

    return "5"

def num_6():
    req = {}
    if(position == 0):
    	req = goToFirstPosit()
    elif(position == 1):
    	req = goToSecondPosit()
    elif(position == 2):
    	req = goToThirdPosit()
    else:
    	req = goToLastPosit()

    move_to_coordinates(req)


    req['x2'] += rigth_width()
    move_to_coordinates(req)

    laser_on()

    req['x2'] += left_width()
    move_to_coordinates(req)

    req['y2'] += down_length()
    move_to_coordinates(req)
    req['y2'] += down_length()
    move_to_coordinates(req)

    req['x2'] += rigth_width()
    move_to_coordinates(req)

    req['y2'] += up_length()
    move_to_coordinates(req)

    req['x2'] += left_width()
    move_to_coordinates(req)

    laser_off()

    return "6"


def num_7():
    req = {}
    if(position == 0):
    	req = goToFirstPosit()
    elif(position == 1):
    	req = goToSecondPosit()
    elif(position == 2):
    	req = goToThirdPosit()
    else:
    	req = goToLastPosit()

    move_to_coordinates(req)

    laser_on()

    req['x2'] += rigth_width()
    move_to_coordinates(req)

    req['y2'] += down_length()
    move_to_coordinates(req)
    req['y2'] += down_length()
    move_to_coordinates(req)

    laser_off()

    return "7"

def num_8(position):
    req = {}
    if(position == 0):
    	req = goToFirstPosit()
    elif(position == 1):
    	req = goToSecondPosit()
    elif(position == 2):
    	req = goToThirdPosit()
    else:
    	req = goToLastPosit()

    move_to_coordinates(req)

    laser_on()

    req['y2'] += down_length()
    move_to_coordinates(req)
    req['y2'] += down_length()
    move_to_coordinates(req)
    req['x2'] += rigth_width()
    move_to_coordinates(req)
    req['y2'] += up_length()
    move_to_coordinates(req)
    req['y2'] += up_length()
    move_to_coordinates(req)
    req['x2'] += left_width()
    move_to_coordinates(req)

    laser_off()

    req['y2'] += down_length()
    move_to_coordinates(req)

    laser_on()

    req['x2'] += rigth_width()
    move_to_coordinates(req)

    laser_off()

    return "8"


def num_9():
    req = {}
    if(position == 0):
    	req = goToFirstPosit()
    elif(position == 1):
    	req = goToSecondPosit()
    elif(position == 2):
    	req = goToThirdPosit()
    else:
    	req = goToLastPosit()

    move_to_coordinates(req)

    req['x2'] += rigth_width()
    move_to_coordinates(req)
    req['y2'] += down_length()
    move_to_coordinates(req)

    laser_on()

    req['x2'] += left_width()
    move_to_coordinates(req)
    req['y2'] += up_length()
    move_to_coordinates(req)
    req['x2'] += rigth_width()
    move_to_coordinates(req)
    req['y2'] += down_length()
    move_to_coordinates(req)
    req['y2'] += down_length()
    move_to_coordinates(req)


    laser_off()

    return "9"

def draw_time():
	now = datetime.datetime.now()
	hour = (now.hour)%12
	minute_str = now.strftime("%M")
	
	# draw the hours
	if(hour == 1):
		num_0(0)
		num_1(1)
	elif(hour == 2):
		num_0(0)
		num_2(1)
	elif(hour == 3):
		num_0(0)
		num_3(1)
	elif(hour == 4):
		num_0(0)
		num_4(1)
	elif(hour == 5):
		num_0(0)
		num_5(1)
	elif(hour == 6):
		num_0(0)
		num_6(1)
	elif(hour == 7):
		num_0(0)
		num_7(1)
	elif(hour == 8):
		num_0(0)
		num_8(1)
	elif(hour == 9):
		num_0(0)
		num_9(1)
	elif(hour == 10):
		num_1(0)
		num_0(1)
	elif(hour == 11):
		num_1(0)
		num_1(1)
	elif(hour == 12):
		num_1(0)
		num_2(1)

	# draw first minute
	if(minute_str[0] == 0):
		num_0(2)
	elif(minute_str[0] == 1):
		num_1(2)
	elif(minute_str[0] == 2):
		num_2(2)
	elif(minute_str[0] == 3):
		num_3(2)
	elif(minute_str[0] == 4):
		num_4(2)
	elif(minute_str[0] == 5):
		num_5(2)

	# draw second minute
	if(minute_str[1] == 0):
		num_0(3)
	elif(minute_str[1] == 1):
		num_1(3)
	elif(minute_str[1] == 2):
		num_2(3)
	elif(minute_str[1] == 3):
		num_3(3)
	elif(minute_str[1] == 4):
		num_4(3)
	elif(minute_str[1] == 5):
		num_5(3)
	elif(minute_str[1] == 6):
		num_6(3)
	elif(minute_str[1] == 7):
		num_7(3)
	elif(minute_str[1] == 8):
		num_8(3)
	elif(minute_str[1] == 9):
		num_9(3)


# -------------clockwork------------------- dorick branch END

def laser_on():
    GPIO.output(31, True)

def laser_off():
    GPIO.output(31, False)

def recenter():
    move_servos(0, 0)

def angle_to_pwm_pan(angle):
    return 7.75 + (angle * -2.47)

def angle_to_pwm_tilt(angle):
    return 7.75 + (angle * -2.47)

def move_servos(pan_pwm, tilt_pwm):
    bottom_servo.ChangeDutyCycle(pan_pwm)
    top_servo.ChangeDutyCycle(tilt_pwm)
    return ""

def scale_ipad_to_box(request):
    result = {}
    result['x1'] = (request.x1/10.0 - 384.0) / 39.38
    result['x2'] = (request.x2/10.0 - 384.0) / 39.38
    result['y1'] = (request.y1/10.0 - 640.0) / -39.38
    result['y2'] = (request.y2/10.0 - 640.0) / -39.38
    return result

def scale_box_to_pan_tilt(request):
    pan_angle = math.atan(request['x2'] / 9.75)
    tilt_angle = (math.pi / 2) - math.acos(request['y2'] / math.sqrt( request['x2'] ** 2 + request['y2'] **2 + 9.75**2))
    return pan_angle, tilt_angle


class Greeter(grpc_pb2_grpc.GlowServicer):

    def TestPointReceiving(self, request, context):
        mutex.acquire()
        print('Server: Acquired the lock.')
        try:
            queue.append(request)
        finally:
            print('Server: Released the lock.')
            mutex.release()
        return grpc_pb2.GlowReply(message='Receieved!')

    def LotsOfPoints(self, request_iterator, context):
        for new_point in request_iterator:
            print('(' + str(new_point.x1) + ', ' + str(new_point.y1) + ') ----> ' + '(' + str(new_point.x2) + ', ' + str(new_point.y2))
        return grpc_pb2.GlowReply(message='Receieved!')


def processData():
    mutex.acquire()
    try:
        if len(queue) > 0:
            print('Should be moving...')
            request = queue.popleft()
            box_scaled = scale_ipad_to_box(request)
            pan_angle, tilt_angle = scale_box_to_pan_tilt(box_scaled)
            pan_pwm = angle_to_pwm_pan(pan_angle)
            tilt_pwm = angle_to_pwm_tilt(tilt_angle)
            move_servos(pan_pwm, tilt_pwm)
    finally:
        mutex.release()
    return 'Done'

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_GlowServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    laser_on()
    recenter()

    bottom_servo.start(2)
    time.sleep(0.5)
    top_servo.start(2)
    time.sleep(0.5)

    try:
        while True:
            polling()
            time.sleep(_ONE_DAY_IN_SECONDS)

    except KeyboardInterrupt:
        laser_off()
        top_servo.stop()
        bottom_servo.stop()
        GPIO.cleanup()
        server.stop(0)

def polling():
    while True:
        p = Thread(target = processData)
        p.start()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
