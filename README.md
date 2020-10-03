
# MoG and GAN

The aim of this project was to find the relationship between input dataset and the performance of GAN[[1]](#1) .  

For the input dataset, two Facial Expression Recognition (FER) datasets are used.
* MMI [[2]](#2) 
* KDEF [[3]](#3) 

## Input dataset
DIfferent experiments are done with two datasets, in order to find differences between them.
1. T-SNE [[4]](#4)  is applied to both dataset, in order to seach any differences in distributions of two datasets.
![T-SNE results](https://github.com/KevSr/MoG_and_GAN/blob/master/Result%20Images/tsne.jpg)  
Differences were observed.

2. For each class in FER datasets, a historgram is drawn. This is done in order to find differences between the classes of the dataset.
![Example of the histogram](https://github.com/KevSr/MoG_and_GAN/blob/master/Result%20Images/rgb_MMIsel_KDEF_CK/KDEF_AN.png)  
Histogram of all classes can be described in terms of Mixture of Gaussians (MoG). Each histogram had different mixture of Gaussian graphs.

## GAN

GAN is then used to check if the network can reproduce the histograms of the input data. If GAN can reproduce the histogram data, it is also possible to reproduce the image, which has same distribution. Also, it is easier to observe differences between generated and real data with histograms.  

Generated histograms are compared with the real one, using Mean Squared Error (MSE) values.  

As input, we used inverse transform sampling to sample data that will have similar histogram as each classes.

---

## File description

* GAN_for_MoG.ipynb  
For running experiments described in section **GAN**. It is made with python using *Tensorflow*.
* rgbtest.py  
For drawing histograms of classes of datasets.
* GMM.py  
For generating input data (train, validation and test) for the GAN.
* tsne_data.py  
For creating input data for tsne, using images in both datasets.
* tsne.ipynb  
For running both 2D and 3D tsne with input data from *tsne_data.py*.
* tsne_input_files  
Folder including input (.npy) files for tsne.  
Includes following files.
    * tsne_target_RGB_MMISEL_.npy
    * tsne_data_RGB_MMISEL_.npy
    * tsne_target_RGB_KDEF_.npy
    * tsne_data_RGB_KDEF_.npy
* Result Images  
Folder including some images that are outputs of experiments.  
Includes following categories of images.
    * Histograms of datasets
    * Generated data from inverse transform sampling
    * Learning curves from GAN
    * Generated histogram from GAN
    * MSE error between generated histogram and corresponding classes of datasets
* Powerpoints  
Folder including powerpoints that are used to summaries the findings of experiments.  
Includes following ppts.
    * rgbdist.pptx  
    Summary of experiment creating histograms of classes.
    * GAN for MoG.pptx  
    Summary of initial testing with GAN, using generated data.
    * Result of GAN for MoG.pptx  
    Summary of results from GAN, including MSE results.
    * Result of 1D GAN for MoG.pptx  
    Final summary of results from GAN, including T-SNE results.


## References
<a id="1">[1]</a>  I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, Y. Bengio. Generative Adversarial Nets. *Adv Neural Inf Process Syst*, 2014, 27.  
[Github link](https://github.com/goodfeli/adversarial)

<a id="2">[2]</a> M. Pantic, M. Valstar, R. Rademaker, L. Maat, "Web-based database for facial expression analysis," Proc. 13th ACM Int'l Conf. Multimedia (Multimedia '05), pp. 317-321, 2005.

<a id="3">[3]</a> M. G. Calvo, D. Lundqvist, “Facial expressions of emotion (KDEF): Identification under different display-duration conditions,” Behav Res, Vol. 40, no. 1, pp. 109–115, 2008.

<a id="4">[4]</a> L. van der Maaten and G.E. Hinton, “Visualizing High-Dimensional Data Using t-SNE,” J. Machine Learning Research, Vol. 9, pp. 2579-2605, 2008.
