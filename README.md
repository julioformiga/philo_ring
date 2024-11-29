# PhiloRing - 42 Philosophers Visualizer

A LED visualization tool for the 42 School's Philosophers project that brings the dining philosophers problem to life through a NeoPixel LED strip.

## Overview

NeoRing provides a visual representation of the dining philosophers problem by connecting to the Philosophers project output. Each philosopher is represented by an LED on the strip, with different colors indicating their current state.

## Visual States

Each LED represents a philosopher with the following color codes:
- 🟡 **Yellow**: Philosopher is eating
- 🔴 **Red**: Philosopher is thinking
- 🔵 **Blue**: Philosopher is sleeping
- 🟢 **Green**: Philosopher has finished all meals

## Requirements

### Hardware
- Raspberry Pi (or similar board with SPI support)
- NeoPixel LED strip
- Appropriate power supply for the LED strip
- Jumper wires for connections

### Software
- Python 3.x
- CircuitPython NeoPixel library
- Compiled Philosophers project from 42 (on Raspberry Pi)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/julioformiga/philo_ring
```

2. Install the required Python package:
```bash
pip3 install adafruit-circuitpython-neopixel
```

3. Connect your NeoPixel LED strip to the Raspberry Pi:
   - Connect the data input to the SPI MOSI pin
   - Connect power and ground appropriately

## Configuration

You can adjust the following parameters in `neoring.py`:
```python
NUM_PIXELS = 35       # Number of philosophers/LEDs
PHILO_TIME = 500      # Time to run simulation
PHILO_EAT = 200       # Time to eat
PHILO_SLEEP = 200     # Time to sleep
PHILO_EAT_N = 3       # Number of times each philosopher must eat
DELAY = 1             # Delay between updates
```

## Usage

1. Make sure your Philosophers executable is in the same directory
2. Run the visualization:
```bash
python3 neoring.py
```

The LED strip will start displaying the philosophers' states in real-time. Each LED represents one philosopher, and the colors will change according to their actions.

## Troubleshooting

- Ensure the 'philo' executable has proper permissions:
```bash
chmod +x ./philo
```
- Check if your LED strip is properly connected to the SPI pins
- Verify that your power supply can handle the number of LEDs you're using

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements or find any bugs.
