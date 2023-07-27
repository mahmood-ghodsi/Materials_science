from pymatgen.core import Structure
from pymatgen.core.surface import SlabGenerator
from pymatgen.analysis.adsorption import plot_slab
from matplotlib import pyplot as plt
from pymatgen.analysis.adsorption import AdsorbateSiteFinder
from pymatgen.core import Molecule
from pymatgen.io.pwscf import PWInput

#load your slab structure
folder_path = "./RP-5050.cif"
slab_struct = Structure.from_file(folder_path)

#Plot adsorption sites (you can tage this part if you do not need the img file)
fig = plt.figure(figsize=(12,12))
ax0 = fig.add_subplot(1,1,1)
plot_slab(slab_struct,ax0,adsorption_sites=True)
ax0.set_title("IMG title")
ax0.set_xticks([])
ax0.set_yticks([])
plt.savefig('./ad_sites.jpg',dpi =400)

#Generating adsorption structures
asf = AdsorbateSiteFinder(slab_struct)
mol_coords = [[0.0000,0.0000,0.0000],
             [0.33333,0.6400,0.0000]]  #enter your desired molecule coordinates as a list
adsorbate = Molecule(["H","H"],mol_coords) #Specify the species
ads_structs = asf.generate_adsorption_structures(adsorbate, repeat=None, find_args={"distance":0.7}) #creates a list of all adsorption structures

#plot_slab(ads_structs[2], ax,adsorption_sites=False)

pseudo_qs = {'Cu':'cu_pbe_v1.2.uspp.F.UPF','Ni':'ni_pbe_v1.4.uspp.F.UPF','H':'h_pbe_v1.4.uspp.F.UPF'} #QS pseudo potential names

count = 0
for i in ads_structs[1:6]:
    count += 1
    #input_qs = PWInput(i,pseudo=pseudo_qs)
    #input_qs.write_file(filename=f'./ad_site_{count}.in')
    i.to(fmt = 'cif',filename= f'./ad_site_{count}.cif')

