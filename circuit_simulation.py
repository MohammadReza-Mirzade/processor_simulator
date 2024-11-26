import tkinter
from tkinter import *
import threading
import time

state = None
lock = threading.Lock()


##################################
# constant values

DELAY_REGISTERS = 0.02
# LED_Size = ()
# KEY_SIZE = ()
# KEYPAD_SIZE = ()
# SEVEN_SEGMENT_SIZE = ()
# RESISTOR_SIZE = ()
# PROCESSOR_SIZE = ()
# VCC_SIZE = ()
# GRAND_SIZE = ()

##################################
# register functions


def PINA():
    time.sleep(DELAY_REGISTERS)
    global state
    global lock
    with lock:
        return convert_array_to_bits(state["A_PIN"])


def PINB():
    time.sleep(DELAY_REGISTERS)
    global state
    global lock
    with lock:
        return convert_array_to_bits(state["B_PIN"])


def PINC():
    time.sleep(DELAY_REGISTERS)
    global state
    global lock
    with lock:
        return convert_array_to_bits(state["C_PIN"])


def PIND():
    time.sleep(DELAY_REGISTERS)
    global state
    global lock
    with lock:
        return convert_array_to_bits(state["D_PIN"])


def PORTA(bits=None):
    global state
    global lock
    result = None
    with lock:
        if bits is not None:
            state["A_PORT"] = convert_bits_to_array(bits)
        result = convert_array_to_bits(state["A_PORT"])
    time.sleep(DELAY_REGISTERS)
    return result


def PORTB(bits=None):
    global state
    global lock
    result = None
    with lock:
        if bits is not None:
            state["B_PORT"] = convert_bits_to_array(bits)
        result = convert_array_to_bits(state["B_PORT"])
    time.sleep(DELAY_REGISTERS)
    return result

def PORTC(bits=None):
    global state
    global lock
    result = None
    with lock:
        if bits is not None:
            state["C_PORT"] = convert_bits_to_array(bits)
        result = convert_array_to_bits(state["C_PORT"])
    time.sleep(DELAY_REGISTERS)
    return result


def PORTD(bits=None):
    global state
    global lock
    result = None
    with lock:
        if bits is not None:
            state["D_PORT"] = convert_bits_to_array(bits)
        result = convert_array_to_bits(state["D_PORT"])
    time.sleep(DELAY_REGISTERS)
    return result


def DDRA(bits=None):
    global state
    global lock
    result = None
    with lock:
        if bits is not None:
            state["A_DDR"] = convert_bits_to_array(bits)
        result = convert_array_to_bits(state["A_DDR"])
    time.sleep(DELAY_REGISTERS)
    return result


def DDRB(bits=None):
    global state
    global lock
    result = None
    with lock:
        if bits is not None:
            state["B_DDR"] = convert_bits_to_array(bits)
        result = convert_array_to_bits(state["B_DDR"])
    time.sleep(DELAY_REGISTERS)
    return result


def DDRC(bits=None):
    global state
    global lock
    result = None
    with lock:
        if bits is not None:
            state["C_DDR"] = convert_bits_to_array(bits)
        result = convert_array_to_bits(state["C_DDR"])
    time.sleep(DELAY_REGISTERS)
    return result


def DDRD(bits=None):
    global state
    global lock
    result = None
    with lock:
        if bits is not None:
            state["D_DDR"] = convert_bits_to_array(bits)
        result = convert_array_to_bits(state["D_DDR"])
    time.sleep(DELAY_REGISTERS)
    return result

################################################
# event functions


def on_click_key(ide: int):
    state["key"][ide] = not state["key"][ide]


def on_click_keypad(ide: int):
    state["key_pad"][ide] = True


def release_click_keypad(ide: int):
    state["key_pad"][ide] = False


################################################
# useful functions

def convert_bits_to_array(bits):
    result = []
    for i in range(8):
        result.append(True if bits % 2 else False)
        bits //= 2
    return result


def convert_array_to_bits(array):
    output = 0
    for i in range(len(array)):
        if array[i]:
            output += 2 ** i
    return output


################################
# draw functions


# input (x, y); output (x + 30, y)
def draw_key(ca: Canvas, x, y, st, ide):
    components = [ca.create_polygon([x, y - 10, x + 20, y - 10, x + 20, y + 10, x, y + 10], fill="white")]
    if st:
        components.append(ca.create_line(x, y, x + 30, y))
    else:
        components.append(ca.create_line(x, y, x + 10, y))
        components.append(ca.create_line(x + 10, y, x + 20, y - 10))
        components.append(ca.create_line(x + 20, y, x + 30, y))
    for component in components:
        ca.tag_bind(component, '<Button-1>', lambda e: on_click_key(ide))


# input (x, y); output (x + 30, y)
def draw_led(ca: Canvas, x: float, y: float, st):
    ca.create_line(x, y - 10, x, y + 10)
    ca.create_line(x, y - 10, x + 30, y)
    ca.create_line(x, y + 10, x + 30, y)
    ca.create_line(x + 30, y + 10, x + 30, y - 10)
    ca.create_polygon([x, y - 10, x, y + 10, x + 30, y], fill=("green" if st else "gray"))


def draw_seven_segment(ca, x, y, st):
    pass


def draw_line(ca, x1, y1, x2, y2):
    ca.create_line(x1, y1, x2, y2)


def draw_keypad(ca, x, y):
    pass


def draw_processor(ca: Canvas, x: float, y: float):
    ca.create_line(x, y, x, y + 600)
    ca.create_line(x, y, x + 200, y)
    ca.create_line(x, y + 600, x + 200, y + 600)
    ca.create_line(x + 200, y, x + 200, y + 600)


def draw_resistor(ca, x, y):
    pass


# input (x, y)
def draw_vcc(ca: Canvas, x, y):
    ca.create_line(x, y, x, y - 10)
    ca.create_line(x - 15, y - 10, x + 15, y - 10)


# input (x, y)
def draw_grand(ca, x, y):
    ca.create_line(x, y, x, y + 10)
    ca.create_line(x - 15, y + 10, x + 15, y + 10)
    ca.create_line(x - 10, y + 15, x + 10, y + 15)
    ca.create_line(x - 5, y + 20, x + 5, y + 20)


################################################
# main functions of simulator


def update_screen(ca, st):
    ca.delete("all")
    draw_processor(ca, 300, 100)
    for i in range(1, 5):
        draw_line(ca, 230, 100 + 30 * i, 300, 100 + 30 * i)
        draw_led(ca, 200, 100 + 30 * i, st["led"][i - 1])
        draw_line(ca, 100, 100 + 30 * i, 200, 100 + 30 * i)
    for i in range(5, 9):
        draw_line(ca, 230, 100 + 30 * i, 300, 100 + 30 * i)
        draw_key(ca, 300 - 100, 100 + 30 * i, st["key"][i - 5], i-5)
        draw_line(ca, 100, 100 + 30 * i, 200, 100 + 30 * i)
    draw_line(ca, 100, 220, 100, 125)
    draw_vcc(ca, 100, 125)
    draw_line(ca, 100, 250, 100, 345)
    draw_grand(ca, 100, 345)


def init_state(canvas_height, canvas_width):
    return {
        "A_DDR": [False] * 8,
        "B_DDR": [False] * 8,
        "C_DDR": [False] * 8,
        "D_DDR": [False] * 8,
        "A_PORT": [False] * 8,
        "B_PORT": [False] * 8,
        "C_PORT": [False] * 8,
        "D_PORT": [False] * 8,
        "A_PIN": [False] * 8,
        "B_PIN": [False] * 8,
        "C_PIN": [False] * 8,
        "D_PIN": [False] * 8,
        "key": [False] * 4,
        "key_pad": [[False] * 4] * 4,
        "canvas_width": canvas_width,
        "canvas_height": canvas_height
    }


def logic(st):
    new_state = {
        "led": [False] * 4,
        "key": st["key"],
        "seven": [[False] * 8] * 4,
    }

    for i in range(8):
        st["A_PIN"][i] = st["A_PORT"][i]
        st["B_PIN"][i] = st["B_PORT"][i]
        st["C_PIN"][i] = st["C_PORT"][i]
        st["D_PIN"][i] = st["D_PORT"][i]

    # led part
    for i in range(4):
        if (not st["A_PORT"][i]) and st["A_DDR"][i]:
            new_state["led"][i] = True
        else:
            new_state["led"][i] = False
            if not st["A_DDR"]:
                st["A_PIN"][i] = True

    # key part
    for i in range(4, 8):
        if not st["A_DDR"][i]:
            if st["key"][i - 4]:
                st["A_PIN"][i] = False
            else:
                st["A_PIN"][i] = st["A_PORT"][i]

    # seven segment part
    for i in range(8):
        if not st["C_DDR"][i]:
            st["C_PIN"][i] = True
    for i in range(4):
        if not st["D_DDR"][i]:
            st["D_PIN"][i] = True
    for i in range(4):
        if not st["D_PIN"][i]:
            for j in range(8):
                if st["C_PIN"][i] == 0:
                    new_state["seven"][i][j] = True
                else:
                    new_state["seven"][i][j] = False
        else:
            for j in range(8):
                new_state["seven"][i][j] = False

    # pin 5-8 D
    for i in range(4, 8):
        if not st["D_DDR"][i]:
            st["D_PIN"][i] = st["D_PORT"][i]

    # keypad part
    for i in range(8):
        if not st["B_DDR"]:
            st["B_PIN"] = st["B_PORT"]
    for i in range(4):
        for j in range(4):
            if st["key_pad"][i][j]:
                if st["B_DDR"][i]:
                    if not st["B_DDR"][4 + j]:
                        st["B_PIN"][4 + j] = st["B_PIN"][i]
                elif st["B_DDR"][4 + j]:
                    if not st["B_DDR"][i]:
                        st["B_DDR"][i] = st["B_DDR"][j + 4]

    return new_state


def sim_loop(canvas):
    global state
    global lock
    with lock:
        new_state = logic(state)
    update_screen(canvas, new_state)
    canvas.after(16, sim_loop, canvas)


def run_simulator():
    global state
    global lock
    root = Tk()
    root.title("Processor Simulation")

    canvas_height = 800
    canvas_width = 800
    canvas = Canvas(width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    with lock:
        state = init_state(canvas_height, canvas_width)

    sim_loop(canvas)

    tkinter.mainloop()
