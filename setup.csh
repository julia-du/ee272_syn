setenv PDKPATH /farmshare/home/classes/ee/272/PDKs/sky130A

setenv PATH /cad/mentor/2019.11/Catapult_Synthesis_10.4b-841621/Mgc_home/bin:$PATH
setenv MGLS_LICENSE_FILE 1717@cadlic0.stanford.edu

source /cad/modules/tcl/init/tcsh
module load base
module load vcs
module load dc_shell
module load lc
module load xcelium

complete make \
    'n/-f/f/' \
    'c/*=/f/' \
    'n@*@`cat -s GNUmakefile Makefile makefile |& sed -n -e "/No such file/d" -e "/^[^     #].*:/s/:.*//p"`@'
