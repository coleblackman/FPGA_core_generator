# FPGA_core_generator
Generates a valid fpga_core hardware description based on input fpga_top.v

To run this script, you need an fpga_top.v somewhere on your filesystem.

Simply clone the repo and run 

```python3.8 core_gen.py``` from the FPGA_core_generator directory. The script will prompt for the desired fpga_top.v path.

If using as part of another script or simply for convenience, core_gen.py also accepts fpga_top.v as a command line argument:

```python3.8 core_gen.py /path/to/fpga_top.v```

If there already exists an fpga_core.v in the target (core) directory, you will be prompted to overwrite it
