#! /usr/bin/env python
#=========================================================================
# construct.py
#=========================================================================
#

import os
import sys

from mflowgen.components import Graph, Step

def construct():

  g = Graph()
  g.sys_path.append( '/farmshare/home/classes/ee/272' )

  #-----------------------------------------------------------------------
  # Parameters
  #-----------------------------------------------------------------------
  
  adk_name = 'skywater-130nm-adk.v2021'
  adk_view = 'view-standard'

  parameters = {
    'construct_path' : __file__,
    'design_name'    : 'ConvHLS',
    'clock_period'   : 20.0,
    'adk'            : adk_name,
    'adk_view'       : adk_view,
    'topographical'  : True
 #   'testbench_name' : 'ConvHLSTb',
 #   'strip_path'     : 'ConvHLSTb/sram_inst',
 #   'saif_instance'  : 'ConvHLSTb/ConvHLS_inst'
  }

  #-----------------------------------------------------------------------
  # Create nodes
  #-----------------------------------------------------------------------

  this_dir = os.path.dirname( os.path.abspath( __file__ ) )

  # ADK step

  g.set_adk( adk_name )
  adk = g.get_adk_step()

  # Custom steps

  sram          = Step( this_dir + '/sram'          )
  rtl           = Step( this_dir + '/rtl'           )
  constraints   = Step( this_dir + '/constraints'   )

  # Default steps

  info         = Step( 'info',                          default=True )
  dc           = Step( 'synopsys-dc-synthesis',         default=True )
  rtl_sim      = Step( 'synopsys-vcs-sim',              default=True )
  gen_saif     = Step( 'synopsys-vcd2saif-convert',     default=True )
  gen_saif_rtl = gen_saif.clone()
  sram_test    = rtl_sim.clone()
  sram_test.set_name( 'sram-test' )
  sram_test.set_param( 'testbench_name', 'SramTb')
  gen_saif_rtl.set_name( 'gen-saif-rtl' )

  #-----------------------------------------------------------------------
  # Graph -- Add nodes
  #-----------------------------------------------------------------------

  g.add_step( info         )
  g.add_step( sram         )
  g.add_step( sram_test    )
  g.add_step( rtl          )
  # g.add_step( testbench    )
  g.add_step( constraints  )
  g.add_step( dc           )
  g.add_step( gen_saif_rtl )

  #-----------------------------------------------------------------------
  # Graph -- Add edges
  #-----------------------------------------------------------------------
  
  # Dynamically add edges

  dc.extend_inputs(['sram_1024_32_tt_1p8V_25C.db'])
  dc.extend_inputs(['sram_256_32_tt_1p8V_25C.db'])
  #sram_test.extend_inputs(['sram.v'])

  # Connect by name

  g.connect_by_name( adk,          dc           )
  g.connect_by_name( sram,         dc           )
  g.connect_by_name( sram,         rtl          )
  g.connect_by_name( rtl,          dc           )
  g.connect_by_name( constraints,  dc           )
  g.connect_by_name( rtl,          gen_saif_rtl )
  # g.connect_by_name( rtl,          rtl_sim      ) 
  # g.connect_by_name( testbench,    rtl_sim      ) 
  g.connect_by_name( sram,         sram_test      ) 
  g.connect( rtl.o( 'run.vcd' ), gen_saif_rtl.i( 'run.vcd' ) ) # FIXME: VCS sim node generates a VCD file but gives it a VPD extension
  g.connect_by_name( gen_saif_rtl, dc           ) # run.saif

  #-----------------------------------------------------------------------
  # Parameterize
  #-----------------------------------------------------------------------

  g.update_params( parameters )

  return g

if __name__ == '__main__':
  g = construct()
  g.plot()
