#! /usr/bin/env python
#=========================================================================
# construct.py
#=========================================================================
# Demo with 16-bit GcdUnit
#
# Author : Priyanka Raina
# Date   : December 4, 2020
#

import os
import sys

from mflowgen.components import Graph, Step

def construct():

  g = Graph()
  g.sys_path.append( '/farmshare/classes/ee/272' )

  #-----------------------------------------------------------------------
  # Parameters
  #-----------------------------------------------------------------------
  
  adk_name = 'skywater-130nm-adk'
  adk_view = 'view-standard.v2021'

  parameters = {
    'construct_path' : __file__,
    'design_name'    : 'GcdUnit',
    'clock_period'   : 20.0,
    'adk'            : adk_name,
    'adk_view'       : adk_view,
    'topographical'  : True,
    'testbench_name' : 'GcdUnitTb',
    'strip_path'     : 'GcdUnitTb/GcdUnit_inst',
    'saif_instance'  : 'GcdUnitTb/GcdUnit_inst'
  }

  #-----------------------------------------------------------------------
  # Create nodes
  #-----------------------------------------------------------------------

  this_dir = os.path.dirname( os.path.abspath( __file__ ) )

  # ADK step

  g.set_adk( adk_name )
  adk = g.get_adk_step()

  # Custom steps

  rtl           = Step( this_dir + '/rtl'           )
  constraints   = Step( this_dir + '/constraints'   )
  testbench     = Step( this_dir + '/testbench'     )

  # Default steps

  info         = Step( 'info',                          default=True )
  dc           = Step( 'synopsys-dc-synthesis',         default=True )
  rtl_sim      = Step( 'synopsys-vcs-sim',              default=True )
  gen_saif     = Step( 'synopsys-vcd2saif-convert',     default=True )
  gen_saif_rtl = gen_saif.clone()
  gen_saif_rtl.set_name( 'gen-saif-rtl' )

  #-----------------------------------------------------------------------
  # Graph -- Add nodes
  #-----------------------------------------------------------------------

  g.add_step( info         )
  g.add_step( rtl          )
  g.add_step( testbench    )
  g.add_step( rtl_sim      )
  g.add_step( constraints  )
  g.add_step( dc           )
  g.add_step( gen_saif_rtl )

  #-----------------------------------------------------------------------
  # Graph -- Add edges
  #-----------------------------------------------------------------------
  
  # Dynamically add edges

  rtl_sim.extend_inputs(['design.v'])
  rtl_sim.extend_inputs(['test_vectors.txt'])

  # Connect by name

  g.connect_by_name( adk,          dc           )
  g.connect_by_name( rtl,          rtl_sim      ) # design.v
  g.connect_by_name( testbench,    rtl_sim      ) # testbench.sv
  g.connect( rtl_sim.o( 'run.vcd' ), gen_saif_rtl.i( 'run.vcd' ) )
  g.connect_by_name( rtl,          dc           )
  g.connect_by_name( constraints,  dc           )
  g.connect_by_name( gen_saif_rtl, dc           ) # run.saif
 
  #-----------------------------------------------------------------------
  # Parameterize
  #-----------------------------------------------------------------------

  g.update_params( parameters )

  return g

if __name__ == '__main__':
  g = construct()
  g.plot()
