# image k-means

## Problem: 

Given a directory with images of the same width and height - separate them into `N, M, ...` clusters 

## Usage

`cluster.py <dir_path> <cluster_size1> ... <cluster_sizeN>`

For each cluster size specified, it will create a folder with 
subfolders, containing each cluster and the images will be copied there

The resulting folders will be created in the same directory where `<dir_path>` is located

## Example

`cluster.py icons 5 10`
  
Will create a folder named `5_clusters` with subfolders `0, 2, ..., 4`

Also creates a folder named `10_cluster` with subfolders `0, 2, ..., 9`
