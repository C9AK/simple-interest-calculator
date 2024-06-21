#!/bin/bash

# Function to calculate simple interest
calculate_simple_interest() {
    principal=$1
    rate=$2
    time=$3

    interest=$(echo "scale=2; $principal * $rate * $time / 100" | bc)
    echo "The simple interest is: $interest"
}

# Sample inputs
principal=1000  # in dollars
rate=5  # annual interest rate in percent
time=2  # in years

# Calculate simple interest
calculate_simple_interest $principal $rate $time
