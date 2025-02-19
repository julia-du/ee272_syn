flow package require MemGen
flow run /MemGen/MemoryGenerator_BuildLib {
VENDOR           *
RTLTOOL          DesignCompiler
TECHNOLOGY       *
LIBRARY          sram_accum_buff
MODULE           ccs_ram_sync_1R1W
OUTPUT_DIR       ./
FILES {
  { FILENAME ./src/sram_wrapper.v FILETYPE Verilog MODELTYPE generic PARSE 1 PATHTYPE copy STATICFILE 1 VHDL_LIB_MAPS work }
}
VHDLARRAYPATH    {}
WRITEDELAY       0.1
INITDELAY        1
READDELAY        0.1
VERILOGARRAYPATH {}
INPUTDELAY       0.01
TIMEUNIT         1ns
WIDTH            32
AREA             0
RDWRRESOLUTION   UNKNOWN
WRITELATENCY     1
READLATENCY      1
DEPTH            4096
PARAMETERS {
  { PARAMETER data_width TYPE hdl IGNORE 0 MIN {} MAX {} DEFAULT 32   }
  { PARAMETER addr_width TYPE hdl IGNORE 0 MIN {} MAX {} DEFAULT 12   }
  { PARAMETER depth      TYPE hdl IGNORE 1 MIN {} MAX {} DEFAULT 4096 }
}
PORTS {
  { NAME port_0 MODE Write }
  { NAME port_1 MODE Read  }
}
PINMAPS {
  { PHYPIN radr LOGPIN ADDRESS      DIRECTION in  WIDTH addr_width PHASE {} DEFAULT {} PORTS port_1          }
  { PHYPIN wadr LOGPIN ADDRESS      DIRECTION in  WIDTH addr_width PHASE {} DEFAULT {} PORTS port_0          }
  { PHYPIN d    LOGPIN DATA_IN      DIRECTION in  WIDTH data_width PHASE {} DEFAULT {} PORTS port_0          }
  { PHYPIN we   LOGPIN WRITE_ENABLE DIRECTION in  WIDTH 1.0        PHASE 1  DEFAULT {} PORTS port_0          }
  { PHYPIN re   LOGPIN READ_ENABLE  DIRECTION in  WIDTH 1.0        PHASE 1  DEFAULT {} PORTS port_1          }
  { PHYPIN clk  LOGPIN CLOCK        DIRECTION in  WIDTH 1.0        PHASE 1  DEFAULT {} PORTS {port_0 port_1} }
  { PHYPIN q    LOGPIN DATA_OUT     DIRECTION out WIDTH data_width PHASE {} DEFAULT {} PORTS port_1          }
}
}