

# Manufacturing Endtest

After the production process all electrical functions should be tested. This test procedure is designed to fully test all electrical functions, even if all parts including the rotary encoder are soldered and only the sub-d port electrical connection is accessible, because the case is already closed.

## Test Setup

The sub-d connector is connected to the test equipment. The rotary encoder is mounted in the test stand, which rotates the shaft.

## Normal Operation

The operation voltage of 9 V DC is applied. The current must be limited to 50 mA.

### Power Supply

The current limit must not be reached.

### Output Signals

- The output voltage level must be >5 V for high level and <1.5 V for low level.

- The output waveform must show the quadrature signal waveform according the reference setup.

- An AC output impedance test during normal operation must show an impedance of 10 kOhm (+-20%) during low level and 20 kOhm (+-20%) during high level.

## Protection Functions

This section describes the test conditions for different protection functions.

### Power Supply

#### Reverse Polarity

50 V DC should be applied in reverse direction to the power supply rails. The current must be limited to 100 uA. The current limit must not be reached.

#### Over Voltage

Apply 50 V DC, limited to 100 mA for 30 ms with correct polarity. The current limit must be maintained until the end of the pulse. The voltage level must not be higher than 30 V.





