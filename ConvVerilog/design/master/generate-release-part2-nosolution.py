import os
from shutil import copyfile

def copyfile_without_solution(infilename, outfilename):
  with open(outfilename, 'w') as outfile:
    flag = 1
    linelist = open(infilename).readlines()
    for line in linelist:
      if line.strip().startswith("// Your code starts here"):
        flag = 0
      if line.strip().startswith("// Your code ends here"):
        flag = 1
      if line.strip().startswith("// Your code starts here"):
        outfile.write(line,)
        outfile.write('\n')
      if flag:
        outfile.write(line,)

if not os.path.exists('../dnn-accelerator-top-rtl'):
  os.makedirs('../dnn-accelerator-top-rtl')

if not os.path.exists('../dnn-accelerator-top-rtl/cpp'):
  os.makedirs('../dnn-accelerator-top-rtl/cpp')

if not os.path.exists('../dnn-accelerator-top-rtl/tests'):
  os.makedirs('../dnn-accelerator-top-rtl/tests')

if not os.path.exists('../dnn-accelerator-top-rtl/verilog'):
  os.makedirs('../dnn-accelerator-top-rtl/verilog') 

if not os.path.exists('../dnn-accelerator-top-rtl/figures'):
  os.makedirs('../dnn-accelerator-top-rtl/figures') 

if not os.path.exists('../dnn-accelerator-top-rtl/data'):
  os.makedirs('../dnn-accelerator-top-rtl/data') 

if not os.path.exists('../dnn-accelerator-top-rtl/layers'):
  os.makedirs('../dnn-accelerator-top-rtl/layers') 

# C files
copyfile_without_solution('cpp/conv_gold.cpp', '../dnn-accelerator-top-rtl/cpp/conv_gold.cpp')
copyfile_without_solution('cpp/conv_gold_tiled.cpp', '../dnn-accelerator-top-rtl/cpp/conv_gold_tiled.cpp')
copyfile('cpp/conv_gold_test.cpp', '../dnn-accelerator-top-rtl/cpp/conv_gold_test.cpp')
copyfile('cpp/conv_gold_tiled_test.cpp', '../dnn-accelerator-top-rtl/cpp/conv_gold_tiled_test.cpp')
copyfile('cpp/conv_tb.cpp', '../dnn-accelerator-top-rtl/cpp/conv_tb.cpp')

# Verilog files
copyfile_without_solution('verilog/conv.v', '../dnn-accelerator-top-rtl/verilog/conv.v')

copyfile('verilog/conv_controller.v', '../dnn-accelerator-top-rtl/verilog/conv_controller.v')
copyfile_without_solution('verilog/mac.v', '../dnn-accelerator-top-rtl/verilog/mac.v')
copyfile_without_solution('verilog/systolic_array.v', '../dnn-accelerator-top-rtl/verilog/systolic_array.v')
copyfile_without_solution('verilog/double_buffer.v', '../dnn-accelerator-top-rtl/verilog/double_buffer.v')
copyfile_without_solution('verilog/accumulation_buffer.v', '../dnn-accelerator-top-rtl/verilog/accumulation_buffer.v')
copyfile_without_solution('verilog/adr_gen_sequential.v', '../dnn-accelerator-top-rtl/verilog/adr_gen_sequential.v')
copyfile_without_solution('verilog/ifmap_radr_gen.v', '../dnn-accelerator-top-rtl/verilog/ifmap_radr_gen.v')
copyfile('verilog/SizedFIFO.v', '../dnn-accelerator-top-rtl/verilog/SizedFIFO.v')
copyfile('verilog/fifo.v', '../dnn-accelerator-top-rtl/verilog/fifo.v')
copyfile('verilog/ram_sync_1r1w.v', '../dnn-accelerator-top-rtl/verilog/ram_sync_1r1w.v')
copyfile('verilog/aggregator.v', '../dnn-accelerator-top-rtl/verilog/aggregator.v')
copyfile('verilog/deaggregator.v', '../dnn-accelerator-top-rtl/verilog/deaggregator.v')
copyfile('verilog/skew_registers.v', '../dnn-accelerator-top-rtl/verilog/skew_registers.v')
copyfile('verilog/systolic_array_with_skew.v', '../dnn-accelerator-top-rtl/verilog/systolic_array_with_skew.v')

# Test files
copyfile('tests/conv_tb.v', '../dnn-accelerator-top-rtl/tests/conv_tb.v')
copyfile_without_solution('tests/fifo_tb.v', '../dnn-accelerator-top-rtl/tests/fifo_tb.v')
copyfile_without_solution('tests/double_buffer_tb.v', '../dnn-accelerator-top-rtl/tests/double_buffer_tb.v')
copyfile_without_solution('tests/weight_double_buffer_tb.v', '../dnn-accelerator-unit-rtl/tests/weight_double_buffer_tb.v')
copyfile_without_solution('tests/ifmap_double_buffer_tb.v', '../dnn-accelerator-unit-rtl/tests/ifmap_double_buffer_tb.v')
copyfile_without_solution('tests/accumulation_buffer_tb.v', '../dnn-accelerator-top-rtl/tests/accumulation_buffer_tb.v')
copyfile_without_solution('tests/adr_gen_sequential_tb_uvm.v', '../dnn-accelerator-top-rtl/tests/adr_gen_sequential_tb_uvm.v')
copyfile_without_solution('tests/mac_tb_uvm.v', '../dnn-accelerator-top-rtl/tests/mac_tb_uvm.v')
copyfile('tests/deaggregator_tb.v', '../dnn-accelerator-top-rtl/tests/deaggregator_tb.v')
copyfile('tests/mac_tb.v', '../dnn-accelerator-top-rtl/tests/mac_tb.v')
copyfile('tests/adr_gen_sequential_tb.v', '../dnn-accelerator-top-rtl/tests/adr_gen_sequential_tb.v')
copyfile('tests/fifo_tb_uvm.v', '../dnn-accelerator-top-rtl/tests/fifo_tb_uvm.v')
copyfile('tests/ram_sync_1r1w_tb_uvm.v', '../dnn-accelerator-top-rtl/tests/ram_sync_1r1w_tb_uvm.v')
copyfile('tests/aggregator_tb.v', '../dnn-accelerator-top-rtl/tests/aggregator_tb.v')
copyfile('tests/skew_registers_tb.v', '../dnn-accelerator-top-rtl/tests/skew_registers_tb.v')
copyfile('tests/ifmap_radr_gen_tb.v', '../dnn-accelerator-top-rtl/tests/ifmap_radr_gen_tb.v')
copyfile('tests/systolic_array_with_skew_tb.v', '../dnn-accelerator-top-rtl/tests/systolic_array_with_skew_tb.v')

# Utility files
copyfile('figures/conv.pdf', '../dnn-accelerator-top-rtl/figures/conv.pdf')
copyfile('figures/conv.png', '../dnn-accelerator-top-rtl/figures/conv.png')
copyfile('Makefile', '../dnn-accelerator-top-rtl/Makefile')
copyfile('autograder.py', '../dnn-accelerator-top-rtl/autograder.py')
copyfile('json_to_parameters.py', '../dnn-accelerator-top-rtl/json_to_parameters.py')
copyfile('README.md', '../dnn-accelerator-top-rtl/README.md')

# Data files
copyfile('data/layer1_gold_ofmap.txt', '../dnn-accelerator-top-rtl/data/layer1_gold_ofmap.txt')
copyfile('data/layer1_ifmap.txt', '../dnn-accelerator-top-rtl/data/layer1_ifmap.txt')
copyfile('data/layer1_weights.txt', '../dnn-accelerator-top-rtl/data/layer1_weights.txt')
copyfile('data/layer2_gold_ofmap.txt', '../dnn-accelerator-top-rtl/data/layer2_gold_ofmap.txt')
copyfile('data/layer2_ifmap.txt', '../dnn-accelerator-top-rtl/data/layer2_ifmap.txt')
copyfile('data/layer2_weights.txt', '../dnn-accelerator-top-rtl/data/layer2_weights.txt')
copyfile('data/layer3_gold_ofmap.txt', '../dnn-accelerator-top-rtl/data/layer3_gold_ofmap.txt')
copyfile('data/layer3_ifmap.txt', '../dnn-accelerator-top-rtl/data/layer3_ifmap.txt')
copyfile('data/layer3_weights.txt', '../dnn-accelerator-top-rtl/data/layer3_weights.txt')

# Layer files
copyfile('layers/resnet_conv1_params.json', '../dnn-accelerator-top-rtl/layers/resnet_conv1_params.json')
copyfile('layers/resnet_conv2_x_params.json', '../dnn-accelerator-top-rtl/layers/resnet_conv2_x_params.json')
copyfile('layers/resnet_conv3_1_params.json', '../dnn-accelerator-top-rtl/layers/resnet_conv3_1_params.json')
copyfile('layers/resnet_conv3_x_params.json', '../dnn-accelerator-top-rtl/layers/resnet_conv3_x_params.json')
copyfile('layers/resnet_conv4_1_params.json', '../dnn-accelerator-top-rtl/layers/resnet_conv4_1_params.json')
copyfile('layers/resnet_conv4_x_params.json', '../dnn-accelerator-top-rtl/layers/resnet_conv4_x_params.json')
copyfile('layers/resnet_conv5_1_params.json', '../dnn-accelerator-top-rtl/layers/resnet_conv5_1_params.json')
copyfile('layers/resnet_conv5_x_params.json', '../dnn-accelerator-top-rtl/layers/resnet_conv5_x_params.json')
