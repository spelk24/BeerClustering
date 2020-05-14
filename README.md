# Beer Clustering - WIP

Recommender System for MolsonCoors products based on drinks you already know you like.

## Data Source

https://www.molsoncoors.com/

For detailed data, please see [MolsonCoors Nutrition PDF](data/MolsonCoors_Nutritional_Information.pdf)

## Current TODO
- [x] Build ingredients categories to group similar words
- [x] Try out PCA on the data for initial analysis
- [ ] EDA and feature filtering
- [ ] Clustering Algorithms
  - [ ] k-Means
  - [ ] Hierarchical
  - [ ] tSNE
  - [ ] UMAP
- [ ] Build Shiny App


## Ideas for Clustering
1. Kmeans labels --> Lower Dimensional representation that includes the kmeans labal
- KNN using cluster labels as response var
- tSNE, UMAP, PCA plot

2. Recommender System research
