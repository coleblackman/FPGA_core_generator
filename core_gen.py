import sys
import os

if len(sys.argv) > 1:
    top_path = sys.argv[1]
    print("\033[1;32mfpga_top\033[m location supplied as a script argument: \033[1;32m", top_path, "\033[m")
else:
    top_path = input('Input location of \033[1;32mfpga_top.v\033[m, type \"local\" for local directory, or type \"default\" for default.\n> ')
    if top_path == "default" or top_path == "":
        top_path = 'fpga_top.v'

core_path = "fpga_core.v"

if(os.path.exists(core_path)):
    rem = input('\nExisting fpga_core.v found on core path. Do you want to overwrite it? Type yes or no\n >')
    if(rem == "yes"):
        os.remove(core_path)
    else:
        print("Aborting...")
        sys.exit()

print("This script takes fpga_top.v as input and generates a valid fpga_core.v.")


with open(top_path, 'r', encoding="utf-8") as top:
    top_data = top.read();


# https://creativecommons.org/licenses/by-sa/2.5/
# https://stackoverflow.com/a/4665027 (following function only)
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        # https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do?rq=1
        yield start
        start += len(sub)
print("---------------------------------------")
# Delete all modules of the form grid_io_xxxx_xxxx
start_index = 0

for top_word in find_all(top_data, "grid_io_"):
    print(type(top_word))

    end_index = top_data.find(");", (top_word))+1
    # Now we have the start and end indices of the module
    print("\033[1;31m", top_data[top_word:end_index], "\033[m")
    core_file = open(core_path, "a")
    core_file.write(top_data[start_index:top_word])
    start_index = end_index
