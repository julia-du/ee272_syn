import os
from shutil import copyfile

def copyfile_without_solution(infilename, outfilename):
  with open(outfilename, 'w') as outfile:
    flag = 1
    linelist = open(infilename).readlines()
    for line in linelist:
      if line.strip().startswith("// Your code starts here") or line.strip().startswith("# Your code starts here"):
        flag = 0
      if line.strip().startswith("// Your code ends here") or line.strip().startswith("# Your code ends here"):
        flag = 1
      if line.strip().startswith("// Your code starts here") or line.strip().startswith("# Your code starts here"):
        outfile.write(line,)
        outfile.write('\n')
      if flag:
        outfile.write(line,)

if not os.path.exists('../dnn-accelerator-hls-unoptimized'):
  os.makedirs('../dnn-accelerator-hls-unoptimized')

if not os.path.exists('../dnn-accelerator-hls-unoptimized/layers'):
  os.makedirs('../dnn-accelerator-hls-unoptimized/layers')

if not os.path.exists('../dnn-accelerator-hls-unoptimized/src'):
  os.makedirs('../dnn-accelerator-hls-unoptimized/src')

if not os.path.exists('../dnn-accelerator-hls-unoptimized/src/boost'):
  os.system('cp -rf src/boost ../dnn-accelerator-hls-unoptimized/src/')

if not os.path.exists('../dnn-accelerator-hls-unoptimized/scripts'):
  os.makedirs('../dnn-accelerator-hls-unoptimized/scripts') 

# C files
copyfile_without_solution('src/InputDoubleBuffer.h', '../dnn-accelerator-hls-unoptimized/src/InputDoubleBuffer.h')
copyfile_without_solution('src/ProcessingElement.h', '../dnn-accelerator-hls-unoptimized/src/ProcessingElement.h')
copyfile_without_solution('src/SystolicArray.h', '../dnn-accelerator-hls-unoptimized/src/SystolicArray.h')
copyfile_without_solution('src/SystolicArrayCore.h', '../dnn-accelerator-hls-unoptimized/src/SystolicArrayCore.h')
copyfile_without_solution('src/WeightDoubleBuffer.h', '../dnn-accelerator-hls-unoptimized/src/WeightDoubleBuffer.h')

copyfile('src/Conv.cpp', '../dnn-accelerator-hls-unoptimized/src/Conv.cpp')
copyfile('src/ConvTb.cpp', '../dnn-accelerator-hls-unoptimized/src/ConvTb.cpp')
copyfile('src/Deserializer.h', '../dnn-accelerator-hls-unoptimized/src/Deserializer.h')
copyfile('src/Serializer.h', '../dnn-accelerator-hls-unoptimized/src/Serializer.h')
copyfile('src/Fifo.h', '../dnn-accelerator-hls-unoptimized/src/Fifo.h')
copyfile('src/conv.h', '../dnn-accelerator-hls-unoptimized/src/conv.h')
copyfile('src/conv_gold.cpp', '../dnn-accelerator-hls-unoptimized/src/conv_gold.cpp')
copyfile('src/conv_gold_tiled.cpp', '../dnn-accelerator-hls-unoptimized/src/conv_gold_tiled.cpp')
copyfile('src/conv_tb_params.h', '../dnn-accelerator-hls-unoptimized/src/conv_tb_params.h')


# Tcl files
copyfile_without_solution('scripts/InputDoubleBuffer.tcl', '../dnn-accelerator-hls-unoptimized/scripts/InputDoubleBuffer.tcl')
copyfile_without_solution('scripts/SystolicArrayCore.tcl', '../dnn-accelerator-hls-unoptimized/scripts/SystolicArrayCore.tcl')
copyfile_without_solution('scripts/WeightDoubleBuffer.tcl', '../dnn-accelerator-hls-unoptimized/scripts/WeightDoubleBuffer.tcl')

copyfile('scripts/Conv.tcl', '../dnn-accelerator-hls-unoptimized/scripts/Conv.tcl')
copyfile('scripts/ProcessingElement.tcl', '../dnn-accelerator-hls-unoptimized/scripts/ProcessingElement.tcl')
copyfile('scripts/common.tcl', '../dnn-accelerator-hls-unoptimized/scripts/common.tcl')
copyfile('scripts/set_libraries.tcl', '../dnn-accelerator-hls-unoptimized/scripts/set_libraries.tcl')
copyfile('scripts/run_rtl_test.tcl', '../dnn-accelerator-hls-unoptimized/scripts/run_rtl_test.tcl')
copyfile('scripts/run_rtl_test_no_gui.tcl', '../dnn-accelerator-hls-unoptimized/scripts/run_rtl_test_no_gui.tcl')
copyfile('scripts/run_c_test.tcl', '../dnn-accelerator-hls-unoptimized/scripts/run_c_test.tcl')
copyfile('scripts/generic_libraries.tcl', '../dnn-accelerator-hls-unoptimized/scripts/generic_libraries.tcl')

# Layer files
copyfile('layers/resnet_conv1_params.json', '../dnn-accelerator-hls-unoptimized/layers/resnet_conv1_params.json')
copyfile('layers/resnet_conv2_x_params.json', '../dnn-accelerator-hls-unoptimized/layers/resnet_conv2_x_params.json')
copyfile('layers/resnet_conv3_1_params.json', '../dnn-accelerator-hls-unoptimized/layers/resnet_conv3_1_params.json')
copyfile('layers/resnet_conv3_x_params.json', '../dnn-accelerator-hls-unoptimized/layers/resnet_conv3_x_params.json')
copyfile('layers/resnet_conv4_1_params.json', '../dnn-accelerator-hls-unoptimized/layers/resnet_conv4_1_params.json')
copyfile('layers/resnet_conv4_x_params.json', '../dnn-accelerator-hls-unoptimized/layers/resnet_conv4_x_params.json')
copyfile('layers/resnet_conv5_1_params.json', '../dnn-accelerator-hls-unoptimized/layers/resnet_conv5_1_params.json')
copyfile('layers/resnet_conv5_x_params.json', '../dnn-accelerator-hls-unoptimized/layers/resnet_conv5_x_params.json')
copyfile('layers/small_layer1.json', '../dnn-accelerator-hls-unoptimized/layers/small_layer1.json')
copyfile('layers/small_layer2.json', '../dnn-accelerator-hls-unoptimized/layers/small_layer2.json')
copyfile('layers/small_layer3.json', '../dnn-accelerator-hls-unoptimized/layers/small_layer3.json')

# Utility files
copyfile('Makefile', '../dnn-accelerator-hls-unoptimized/Makefile')
copyfile('autograder.py', '../dnn-accelerator-hls-unoptimized/autograder.py')
copyfile('setenv.csh', '../dnn-accelerator-hls-unoptimized/setenv.csh')
copyfile('.gitignore', '../dnn-accelerator-hls-unoptimized/.gitignore')

