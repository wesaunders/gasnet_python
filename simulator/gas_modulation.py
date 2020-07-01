#Gas Modulation Function:
# This function embodies the behaviour described by Section 2.2 
# "Modulation by the Gases" in Husbands et al.(1998).
# Specifically equations 5,6,7 are implemented here.
#
# This function also calls the gasDiffusion function by default if an 
# alternative is not specified, see documentation for details.
#
# Parameters:
#  phenotype    - Cell Array GasNet Phenotype
#  emissions    - Matrix of emission state (number of nodes x 3), 
#                 describing whether a node is emitting (n,1) [0|1], the 
#                 time step the node last started emitting (n,2) and the 
#                 time step the node last stopped emitting (n,3).
#  dists_from_a   - Array of distances to other nodes from node a.
#  t            - The current time step.
#  global_c      - Constant used in gas diffusion.
#  global_k      - Constant used in gas modulation.
#  a            - The current node.
#  diffusion_func (OPTIONAL)
#               - Function handle to user specified diffusion function.
#                 (fcn must operate within default fcn's specification)
#
# Author: Will Saunders 
# Date: 12.12.11
#
# ------------------------------------------------------------------------
# These tools are developed from the GasNet model described in:
# P Husbands, T Smith, N Jakobi, and M O'Shea. (1998)
# Better Living Through Chemistry: Evolving GasNets for Robot Control. 
# Connection Science, 10(3-4):185-210.
def gas_modulation(phenotype,emissions,dists_from_a,t,global_c,global_k,a,diffusion_func):
    if nargin < 8
        diffusion_func = gas_diffusion

    [~, noOfGenes] = size(phenotype)

    #Calculate gas concentrations using gasDiffusion.
    gas1 = 0
    gas2 = 0
    for b in range(noOfGenes):
        if phenotype{b}(10) == 0:
            continue
        if b == a:
            continue
        
        temp_concentration = diffusion_func(emissions(b,1),emissions(b,2),...
                            emissions(b,3),phenotype{b}(12),t,global_c,...
                            dists_from_a(b),phenotype{b}(13))
                        
        if phenotype{b}(11) == 0:
            gas1 = gas1 + temp_concentration
        else:
            gas2 = gas2 + temp_concentration

    P = [-4,-2,-1,-0.5,-0.25,-0.125,0,0.125,0.25,0.5,1,2,4]
    [~,pSize] = size(P)
    temp = (phenotype{a}(14) + ((gas1/global_c*global_k) * 
                            (pSize-phenotype{a}(14))) -
                            ((gas2/global_c*global_k)*phenotype{a}(14)))
    integer_index = f(temp,pSize)
    transfer_param = P(integer_index)
    return transfer_param, gas1, gas2

 #Local function: (Altered) Eq 7 Husbands et al. (1998)
 def f(input_val,n):
    if input_val <= 0
        return 1
    elif input_val >= n:
        return n
    else:
        return ceil(input_val)