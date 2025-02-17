vcs -full64 -sverilog -timescale=1ns/1ps -debug_access+pp tests/mac_tb.v verilog/mac.v
./simv

vcs -full64 -sverilog -timescale=1ns/1ps -debug_access+pp tests/skew_registers_tb.v verilog/skew_registers.v
./simv

vcs -full64 -sverilog -timescale=1ns/1ps -debug_access+pp tests/fifo_tb_uvm.v verilog/fifo.v verilog/SizedFIFO.v
./simv

vcs -full64 -sverilog -timescale=1ns/1ps -debug_access+pp tests/ram_sync_1r1w_tb_uvm.v verilog/ram_sync_1r1w.v
./simv

vcs -full64 -sverilog -timescale=1ns/1ps -debug_access+pp tests/aggregator_tb.v verilog/aggregator.v verilog/fifo.v verilog/SizedFIFO.v
./simv

vcs -full64 -sverilog -timescale=1ns/1ps -debug_access+pp tests/adr_gen_sequential_tb.v verilog/adr_gen_sequential.v
./simv

vcs -full64 -sverilog -timescale=1ns/1ps -debug_access+pp tests/ifmap_radr_gen_tb.v verilog/ifmap_radr_gen.v
./simv

vcs -full64 -sverilog -timescale=1ns/1ps -debug_access+pp tests/systolic_array_with_skew_tb.v verilog/systolic_array_with_skew.v verilog/skew_registers.v verilog/systolic_array.v verilog/mac.v
./simv

vcs -full64 -sverilog -timescale=1ns/1ps -debug_access+pp tests/deaggregator_tb.v verilog/deaggregator.v verilog/fifo.v verilog/SizedFIFO.v
./simv

vcs -full64 -sverilog -timescale=1ns/1ps -debug_access+pp tests/conv_tb.v verilog/conv.v verilog/systolic_array_with_skew.v verilog/skew_registers.v verilog/systolic_array.v verilog/mac.v verilog/adr_gen_sequential.v verilog/deaggregator.v verilog/aggregator.v verilog/fifo.v verilog/SizedFIFO.v verilog/conv_controller.v verilog/accumulation_buffer.v verilog/ram_sync_1r1w.v verilog/ifmap_radr_gen.v verilog/double_buffer.v
./simv
