#!/bin/dash

pin=$1
value=$2

echo $value > /sys/class/gpio/gpio$pin/value
