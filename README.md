  # Supplementary Information


**De Anda V**, Zapata Peñasco I, Blaz J, Poot-Hernandez AC, Contreras Moreira B, Gonzales Laffite Marcos, Hernandez Rosales M, Gamez Tamariz N, Eguiarte Fruns E, Souza V. Understanding the mechanisms behind the response of environmental perturbations in microbial mats: a metagenomic-network based approach. Submitted in Frontiers in Microbiology 
To reproduce the figures first install [jupyter notebook](http://jupyter.org/install.html) and then clone the repository.  

```bash
git clone https://github.com/valdeanda/Time_series_mats.git
cd scripts 
ipython3 notebook 
```
The directory `scripts` contains all the steps required to compute the main figures from the article in notebook, html and python formats.

### `Libraries version`
In order to reproduce all the figures using the notebooks, the following libraries must be installed first with the corresponding versions 

+ Pandas version ==> 0.20.3 
+ Numpy ==> 1.13.3
+ Seaborn ==> 0.8.0
+ Plt ==> 1.13.3
+ Matplotlib ==> 2.02


###  Figures
---


<img src="https://valdeanda.github.io/Time_series_mats/figures/MEBS_mats.png" width="256" height="200" align="right">

### `Main cycles with MEBS over time`

Script available in [html](https://valdeanda.github.io/Time_series_mats/scripts/MebsInTime.html) and  [notebook](https://github.com/valdeanda/Time_series_mats/blob/master/scripts/MebsInTime.ipynb) formats. 

Run the notebook within scripts folder 

```bash
ipython3 notebook MebsInTime.ipynb
```

---


### `Barplot composition and logaritmic scale`

<img src="https://valdeanda.github.io/Time_series_mats/figures/Barplot.png" width="256" height="150" align="right">

Script available in [html](https://valdeanda.github.io/Time_series_mats/scripts/Bar_plots_composition.html) and [notebook](https://github.com/valdeanda/Time_series_mats/blob/master/scripts/Bar_plots_composition.ipynb) formats 

Run the notebook 

```bash
ipython3 notebook Bar_plots_composition.ipynb
```
---


### `Microbial mat core`
Using [get_homologues](https://github.com/eead-csic-compbio/get_homologues)`

<img src="https://valdeanda.github.io/Time_series_mats/figures/Mats_core.png" width="256" height="150" align="right">

Script available in [html](https://valdeanda.github.io/Time_series_mats/scripts/Core_bacteria.html) and [notebook](https://github.com/valdeanda/Time_series_mats/blob/master/scripts/Core_bacteria.ipynb) formats. 
Run the notebook 

```bash
ipython3 notebook Core_bacteria.ipynb
```

---


### `Biogeochemical cycles and Sulfur completeness`

<img src="https://valdeanda.github.io/Time_series_mats/figures/Heatmap.cycles.uv.png" width="256" height="200" align="left">

Script available in [html](https://valdeanda.github.io/Time_series_mats/scripts/Pfams_completeness.html) and [notebook](https://github.com/valdeanda/Time_series_mats/blob/master/scripts/Pfams_completeness.ipynb) formats.
Run the notebook

```bash
ipython3 notebook Pfams_completeness.ipynb
```

---








