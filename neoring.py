import subprocess
import time

import board
import neopixel_spi as neopixel

PIXEL_ORDER = neopixel.GRB
COLORS = {
    "RED": 0xFF0000,
    "GREEN": 0x00FF00,
    "BLUE": 0x0000FF,
    "YELLOW": 0xFFFF00,
}
# NUM_PIXELS = 45
NUM_PIXELS = 35
# NUM_PIXELS = 8
PHILO_TIME = 500
PHILO_EAT = 200
PHILO_SLEEP = 200
PHILO_EAT_N = 3
DELAY = 1


def run_command(command):
    try:
        p = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True,
            bufsize=1,
            universal_newlines=True,
        )

        if p.stdout is None:
            raise subprocess.SubprocessError(f"Failed to execute command: {command}")

        for line in p.stdout:
            if line.strip():
                yield line.strip()

        p.stdout.close()
        return_code = p.wait()

        if return_code != 0:
            error_output = p.stderr.read() if p.stderr else "No error output available"
            raise subprocess.SubprocessError(
                f"Command failed with return code {return_code}. Error: {error_output}"
            )

    except FileNotFoundError:
        raise FileNotFoundError(
            "The 'philo' executable was not found. Make sure it exists and is executable."
        )


list_actions = {
    "eating": COLORS["YELLOW"],
    "thinking": COLORS["RED"],
    "sleeping": COLORS["BLUE"],
}

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=False, brightness=0.05
)

data = {}
for lista in run_command(
    f"./philo {NUM_PIXELS} {PHILO_TIME} {PHILO_EAT} {PHILO_SLEEP} {PHILO_EAT_N}"
):
    line = lista.split()
    if int(line[0]) not in data:
        data[int(line[0])] = {}
    if int(line[1]) not in data[int(line[0])]:
        data[int(line[0])][int(line[1])] = {}
    data[int(line[0])][int(line[1])] = line[3]
count_eating = {}
for d in data:
    for i in data[d]:
        if i not in count_eating:
            count_eating[i] = 0
        if data[d][i] == "eating":
            count_eating[i] += 1
        if data[d][i] in list_actions:
            print(d, i, data[d][i])
            pixels[i - 1] = list_actions[data[d][i]]
            pixels.show()
        if count_eating[i] == 10:
            pixels[i - 1] = COLORS["GREEN"]
            pixels.show()
    time.sleep(DELAY)

time.sleep(4)
pixels.fill(0)
pixels.show()
