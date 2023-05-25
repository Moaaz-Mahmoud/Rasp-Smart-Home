import RPi.GPIO as GPIO

# GPIO pin numbers for the components
PIN_MAPPING = {
    'lights': 18,  # Example GPIO pin number for lights
    'lock': 23,  # Example GPIO pin number for door lock
    'cameras': 24,  # Example GPIO pin number for security cameras
    'curtains': 25  # Example GPIO pin number for curtains
}

# Set GPIO mode and initial states
GPIO.setmode(GPIO.BCM)
for pin in PIN_MAPPING.values():
    GPIO.setup(pin, GPIO.OUT)

# Function to control components
def control_component(component, state):
    pin = PIN_MAPPING.get(component)
    if pin is not None:
        GPIO.output(pin, state)
    else:
        print("Invalid component.")

# Function to handle button press
def button_callback(channel):
    component = ""
    if channel == 17:  # Example GPIO pin number for button 1
        component = "lights"
    elif channel == 27:  # Example GPIO pin number for button 2
        component = "lock"
    elif channel == 22:  # Example GPIO pin number for button 3
        component = "cameras"
    elif channel == 5:  # Example GPIO pin number for button 4
        component = "curtains"

    state = GPIO.input(channel)
    control_component(component, state)

# Configure GPIO inputs for buttons
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Example GPIO pin number for button 1
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Example GPIO pin number for button 2
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Example GPIO pin number for button 3
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Example GPIO pin number for button 4

# Add event detection for button presses
GPIO.add_event_detect(17, GPIO.BOTH, callback=button_callback)  # Example GPIO pin number for button 1
GPIO.add_event_detect(27, GPIO.BOTH, callback=button_callback)  # Example GPIO pin number for button 2
GPIO.add_event_detect(22, GPIO.BOTH, callback=button_callback)  # Example GPIO pin number for button 3
GPIO.add_event_detect(5, GPIO.BOTH, callback=button_callback)  # Example GPIO pin number for button 4

# Main program loop
try:
    while True:
        pass
except KeyboardInterrupt:
    pass

# Cleanup GPIO pins and resources
GPIO.cleanup()
