
# How it works

This electrical component protects the optical rotary encoder against overvoltage, short circuit and wrong polarity. That means, any voltage up to 25 V randomly applied to any of the four electrical connections is completely safe and will never do any damage to the board or the encoder.

The protection mechanisms are implemented the following way:

## Supply voltage protection

The optical rotary encoder can be operated by 5 to 24 V consuming up to 40 mA. Diode _D1_ protects it against reverse supply voltage polarity by up to 100 V.

During normal operation, there is a voltage drop 0f arount 0.7 V over _D1_ and 0.9 V over _R1_. The rotary encoders gets around 1.6 V less than the voltage supplied into the protection board. The over voltage protection is mainly realized by the z-diode _D2_. In an over voltage condition, it starts to conduct current, rising the input current to the protection board. The protection works for voltage surges of up to 50 V for 100 us. In this situation, the current is around 1.1 A.

The low impedance capacitors _C1_ protects against radio frequency inference on the power rail, while _C2_ protects against lower frequencies. It protects the encoder against power interruptions of around 1 ms, which would lead to minor errors in counting the angle value. The cutoff frequency of the RC filter _R1_ and _C2_ is around 330 Hz.

## Signal output protection

The rotary encoder has two open collector outputs. They don't have any internal current limitation or protection. To limit the current, the resistors _R4_ and _R5_ are added in series. Because this method increases te output impedance, the pull-up resistors are added to the encoder side. This way, the voltage level of the signal is not impaired. It is important to disable integrated pull-up resistors in the microcontroller, where the protection board ist plugged in, because due to the high output impedance of 10 kOhm, the voltage level can't be pulled low enough from the protection board side.

The high output impedance also protects the connected (microcontroller) circuit. If the digital port of the microcontroller (Arduino) is programmed as output, e. g. the wrong program ist loaded or there is a bug in the code, current flowing through the digital port is limited to a safe value. Because the output impedance is 20 kOhm for high level, the output current can't reach more than 1.2 mA, if the output is shorted to _GND_. If the supply voltage is 24 V and a microcnotrller is directly connected to this output, it won't be damaged, because the internal protection diodes of the microcontroller limit the voltage level on the input port.

If over voltage is feed directly into the output port, the z-diodes _D3_ and _D4_ protect the encoder outputs against over voltage, if they are on high level. In case of reverse polarity over voltage at the output ports, there is a forward current flow through both z-diodes, which protects the encoder output against negative voltage levels.

## Connection check 

There is always a probability a plug comes loose or there is an internal problem in the mainboard. The protection board allows to check the connection to it. Even both output pins of the rotary encoder are high, which means, the open collector ouput pins are in the high impedance state, the signal connection can be checked, because there is a 20 kOhm path through the protection and pull-up resistors to the positive supply voltage. If the output level of the encoder is low, the output impedance of the board is 10 kOhm to _GND_.

The optical rotary encoder always draws supply current, if the supply voltage is in the recommended range. That way, the supply voltage or _GND_ connection can be checked.


# Important notes

Only the _J1_ sub-d connector side is protected! The open end of the cable of the rotary encoder must be soldered directly to the protection board. Because the protection board serves also as a plug, no detachable connection should be introduced between the encoder and the board. If a longer cable is needed, it should be attached to the protected _J1_ connector side. Feeding reverse polarized or over voltage to the _J3_ solder pads, where regularly the encoder cable is soldered to, will damage the protection board and destroy the protection functionality.

Applying more than 25 V over a long time directly to the output or supply connection can cause overheat and fire.


