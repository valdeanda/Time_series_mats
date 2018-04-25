# Supplementary Information


De Anda V, Zapata Peñasco I, Blaz J, Poot-Hernandez AC, Contreras Moreira B, Gonzales Laffite Marcos, Hernandez Rosales M, Gamez Tamariz N, Eguiarte Fruns E, Souza V. Understanding the mechanisms behind the response of environmental perturbations in microbial mats: a metagenomic-network based approach. Submitted in Frontiers in Microbiology 
To reproduce the figures first install [jupyter notebook](http://jupyter.org/install.html)  
and then clone the repository.  

```bash
git clone https://github.com/valdeanda/Time_series_mats.git
cd scripts 
ipython3 notebook 
```
The directory scripts contains all the steps required to compute  the main figures from the article in notebook, html and python format.


###  `Figures`

<img src="https://valdeanda.github.io/Time_series_mats/figures/MEBS_mats.png" width="256" height="256" align="left">

+ Main cycles with MEBS over time in [html](https://valdeanda.github.io/Time_series_mats/scripts/MebsInTime.html) [notebook](https://valdeanda.github.io/Time_series_mats/scripts/MebsInTime.ipynb) formats






.......


|Aim|Script|
|-------------------------------|---------------------------|
|Abundance barplot and logaritmic scale|[Barplots](./scripts/Bar_plots_composition.ipynb)|
|Analysis of core genome using [get_homologues](https://github.com/eead-csic-compbio/get_homologues)|[Core_mats](./scripts/Core_bacteria.ipynb) |
|Analysis of network motifs|[Motifs](./scripts/Motifs.ipynb) |
|Ecological indexes with R (taxonomic profiles)|[Index R](./scripts/Ecological_index.ipynb) |
|Ecological indexes with R (metabolicc profiles)|[Index R](./scripts/Diversidad_pfams.ipynb) |


# To generate the abundances profile from hmmsearch 
Use the following script that is also implemented in [MEBS software](https://github.com/eead-csic-compbio/metagenome_Pfam_score/tree/master/scripts)

```
 perl scripts/extract_pfam.pl -matrixdir matrix_pfam/ > data/test.pfams.tab 

```
