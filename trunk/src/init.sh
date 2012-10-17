#!/bin/bash

echo "2" > /sys/class/gpio/export
echo "3" > /sys/class/gpio/export
echo "4" > /sys/class/gpio/export
echo "17" > /sys/class/gpio/export

echo "out" > /sys/class/gpio/gpio2/direction
echo "out" > /sys/class/gpio/gpio3/direction
echo "out" > /sys/class/gpio/gpio4/direction
echo "out" > /sys/class/gpio/gpio17/direction