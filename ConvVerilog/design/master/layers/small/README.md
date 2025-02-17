# A Small Convolution Layer

Generated from `conv_tb.cpp` with the following parameters in the `run_layer` function (see `main` at the bottom of this file for the function call), for a 4x4 systolic array.

```
run_layer <
  4/*OY1*/, 3/*OY0*/, 
  4/*OX1*/, 3/*OX0*/, 
  4/*OC1*/, 4/*OC0*/, 
  2/*IC1*/, 4/*IC0*/, 
  3/*FX*/,  3/*FY*/, 
  1/*STRIDE*/> ();
```

The order of data entries in the file is the order in which they must be fed into the accelerator (that is, the data is tiled properly).

You can check if the number of data elements generated in input, weight and output files are correct.

Number of elements in the weights file 
```
= (IC0 * OC0 * FX * FY * IC1) * OC1 * OX1 * OY1 
= (4 * 4 * 3 * 3 * 2) * 4 * 4 * 4 = 18432
```
The multiplication with OX1 * OY1 is because the weights are reloaded for output tiles.

Number of elements in the output file
```
= (OX0 * OY0 * OC0) * OC1 * OX1 * OY1
= (3 * 3 * 4) * 4 * 4 * 4 = 2304
```
There is no reloading happening for outputs. Each output tile is completely calculated in the accelerator and then pushed out.

Number of elements in the input file
```
= (IC0 * IX0 * IY0) * IC1 * OX1 * OY1
= (4 * (3 + 3 - 1) * (3 + 3 - 1)) * 2 * 4 * 4 = 3200
```
Where IX0 = OX0 + FX - 1 and IY0 = OY0 + FY - 1.
For this small layer, all IC0*IC1 channels fit in the input double buffer, so they get reused for outer output channel loop (OC1) without getting reloaded. Note that this number (3200) is larger than the actual size of the input feature map which is IX * IY * IC0 * IC1 = 14 * 14 * 4 * 2 = 1568 where IX = OX1 * OX0 + FX - 1 = 14 and IY = OY1 * OY0 + FY - 1 = 14, because due to tiling, inputs at the borders of the tile get loaded several times. This overhead will be smaller when the inner tile size is larger.
