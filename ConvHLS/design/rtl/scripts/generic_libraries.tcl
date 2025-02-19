solution library add nangate-45nm_beh -- -rtlsyntool DesignCompiler -vendor Nangate -technology 045nm
# solution library add ccs_sample_mem
solution library add sram_input_db
solution library add sram_weight_db
solution library add sram_accum_buff
# set accum_buffer_module ccs_sample_mem.ccs_ram_sync_1R1W
# set double_buffer_module ccs_sample_mem.ccs_ram_sync_1R1W 