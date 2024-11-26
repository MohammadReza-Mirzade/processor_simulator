from circuit_simulation import PINA, PINB, PINC, PIND, PORTA, PORTB, PORTC, PORTD, DDRA, DDRB, DDRC, DDRD
from time import sleep

# DDR register indicate that the pin is an input pin or an output pin (0: input, 1: output)
# PIN register is always return the value of the pin
# (this register usually used for reading the input voltage of an input pin).
# if the pin is an output pin then the PORT register determine the output value (0: HV, 1: LV)
# but if the pin is an input pin then the PORT register determine the pin has a PULL-UP resistor or PULL-DOWN resistor
# (0: PULL-DOWN, 1: PULL-UP)

# To enable seven-segment you need to give the enable-pin zero.


# def run():
#     DDRA(0x0f)
#     PORTA(0xf0)
#     while True:
#         var = PINA() & 0xf0
#         var = var >> 4
#         var = ~var & 0x0f
#         var += PORTA() & 0xf0
#         PORTA(var)


def run():
    DDRA(0xff)
    var = 0x0f
    while True:
        if (var & 0x0f) == 0x0f:
            var = 0x0e
        else:
            var = ((var << 1) & 0x0f) | 0x01
        print(var)
        PORTA(var)
        sleep(1)

