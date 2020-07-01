#Gas Diffusion Function:
# This function embodies the behaviour described by Section 2.1
# "Gas Diffusion in the Networks" in Husbands et al.(1998).
# Specifically equations 2,3,4 are implemented here.
# This function calculates the concentration of the gas from one node using
# the distance and decay calculations etc.
#
# Parameters:
#  is_emitting   - Binary value describing whether the node is emitting.
#  emission_start    - The time step that the node last started emitting.
#  emission_stop     - The time step that the node last started emitting.
#  s            - The decay rate value for the node.
#  t            - The current time step.
#  global_c      - Constant used in gas diffusion.
#  distance     - The distance to the node.
#  gas_radius    - The radius of the node's gas.
#
# Author: Will Saunders
# Date: 12.12.11
#
# ------------------------------------------------------------------------
# These tools are developed from the GasNet model described in:
# P Husbands, T Smith, N Jakobi, and M O'Shea. (1998)
# Better Living Through Chemistry: Evolving GasNets for Robot Control.
# Connection Science, 10(3-4):185-210.
def gas_diffusion(is_emitting, emission_start,...
                    emission_stop, s, t, global_c, distance, gas_radius):

if distance > gas_radius
    concentration = 0
    return


if is_emitting #Node is emitting.
    build_up = H((t-emission_start)/s)
elif(~is_emitting) #Node is not emitting.
    build_up = H(H((emission_stop-emission_start)/s)-H((t-emission_stop)/s))

return (global_c * exp((-2*distance)/gas_radius) * build_up)



#Local Function: Eq 4, Husbands et al. (1998)
def out1 = H(in) 
if(in<=0)
    out1 = 0
elseif(in>1)
    out1 = 1
else
    out1 = in
end
end