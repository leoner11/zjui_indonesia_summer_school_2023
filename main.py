import utils
import utils.vision as vision
import utils.camera as camera
import utils.serial as serial

def main():
    serial.setup_env('/dev/ttyUSB0')
    camera.setup_env(0)
    vision.setup_env()
    
    serial.set_servo(0)
    triggered = False
    led0_on = False
    led2_on = False
    led3_on = False
    led4_on = False
    
    while True:
        img = camera.capture_img()
        
        (bboxes, scores, labels) = vision.detect_flag(img)
        
        #FOR PIRATE FLAG
        if True in [True if label == 1 and score > 0.9 else False for label, score in zip(labels, scores)] and not triggered:
            serial.set_servo(180)
            triggered = True
            
        #FOR LED_0
        if True in [True if label == 0 and score > 0.7 else False for label, score in zip(labels, scores)]:
            if not led0_on:
                led0_on = True
                serial.set_led(0, True)
        else:
            if led0_on:
                led0_on = False
                serial.set_led(0, False)
        #FOR LED_2
        
        if True in [True if label == 2 and score > 0.7 else False for label, score in zip(labels, scores)]:
            if not led2_on:
                led2_on = True
                serial.set_led(2, True)
        else:
            if led2_on:
                led2_on = False
                serial.set_led(2, False)

        #FOR LED_3
        
        if True in [True if label == 3 and score > 0.7 else False for label, score in zip(labels, scores)]:
            if not led3_on:
                led3_on = True
                serial.set_led(3, True)
        else:
            if led3_on:
                led3_on = False
                serial.set_led(3, False)    

        #FOR LED_4
        
        if True in [True if label == 4 and score > 0.7 else False for label, score in zip(labels, scores)]:
            if not led4_on:
                led4_on = True
                serial.set_led(4, True)
        else:
            if led4_on:
                led4_on = False
                serial.set_led(4, False)

        if vision.visualization(img, bboxes, scores, labels):
            break
    

if __name__ == '__main__':
    main()
