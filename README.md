# Scripts and data to reproduce all the figures from the article 
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
