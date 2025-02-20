`define CLK_PERIOD 20
`define ASSIGNMENT_DELAY 5
`define FINISH_TIME 2000
`define NUM_WMASKS 4
`define DATA_WIDTH 32
`define ADDR_WIDTH 12
`define DEPTH 4096

module SramTb;
  
  reg clk;
  reg we;
  reg re;
  reg [`ADDR_WIDTH-1:0] radr;
  reg [`ADDR_WIDTH-1:0] wadr;
  reg [`DATA_WIDTH-1:0] din;
  wire [`DATA_WIDTH-1:0] dout;

  always #(`CLK_PERIOD/2) clk =~clk;
 
  sram_wrapper_1024_32 #(
    .data_width(`DATA_WIDTH),
    .addr_width(`ADDR_WIDTH),
    .depth(`DEPTH)
  ) sram_inst (
    .clk(clk),
    .re(re),
    .radr(radr),
    .d(din),
    .we(we),
    .wadr(wadr),
    .q(dout)
  );

  initial begin
    $vcdplusfile("dump.vcd");
    $vcdplusmemon();
    $vcdpluson(0, SramTb);

    clk <= 0;
    re <= 0;
    we <= 0;
    radr <= 0;
    wadr <= 0;
    din <= 0;

    #(1*`CLK_PERIOD) // Write
    we <= 1;
    wadr <= {`ADDR_WIDTH{1'b0}};
    din <= {`DATA_WIDTH{1'b1}};
    #(1*`CLK_PERIOD)
    we <= 0;
    #(1*`CLK_PERIOD)
    re <= 1;
    radr <= {`ADDR_WIDTH{1'b0}};
    #(1*`CLK_PERIOD) 
    #(`CLK_PERIOD/2)// Read
    $display($time, " dout = %h", dout);
    assert(dout == {`DATA_WIDTH{1'b1}});
    #(`CLK_PERIOD/2)
    re <= 0;

    #(1*`CLK_PERIOD) // Write
    we <= 1;
    wadr <= {`ADDR_WIDTH{1'b1}};
    din <= {`DATA_WIDTH{1'b1}};
    #(1*`CLK_PERIOD)
    we <= 0;
    #(1*`CLK_PERIOD)
    re <= 1;
    radr <= {`ADDR_WIDTH{1'b1}};
    #(1*`CLK_PERIOD) 
    #(`CLK_PERIOD/2)// Read
    $display($time, " dout = %h", dout);
    assert(dout == {`DATA_WIDTH{1'b1}});
    #(`CLK_PERIOD/2)
    re <= 0;
    
    $finish(2);
  end

  // initial begin
  //   $vcdplusfile("dump.vcd");
  //   $vcdplusmemon();
  //   $vcdpluson(0, SramTb);
  //   #(`FINISH_TIME);
  //   $finish(2);
  // end

endmodule 
