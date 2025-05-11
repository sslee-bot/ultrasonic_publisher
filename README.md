# ultrasonic_publisher

## dependencies

```bash
sudo apt install python3-dev python3-setuptools python3-rpi.gpio python3-gpiozero
# sudo apt install python3-pigpio pigpio-tools
```

## how to run

```bash
# usermod
sudo usermod -aG dialout $USER # reboot after this command

# run node
ros2 run ultrasonic_publisher ultrasonic_publisher_node
```
