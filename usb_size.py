#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Get actual memory size of USB | ----\n", fg("red")))

# user interaction
memory_size = float(input("Enter memory size (in GB): "))

def get_actual(ms):
    return round(ms / 100 * 93, 2)

actual_memory_size = get_actual(memory_size)
memory_size_loss = stylize(str(round(memory_size - actual_memory_size, 2)), fg("red"))
print(f"\nActual USB memory size: {actual_memory_size}\nMemory size loss: {memory_size_loss}\n")
