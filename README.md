# 3D Prostate Cancer Classifier
The purpose of this project is to develop a Convolutional Neural Network capable to determine whether the prostate 
lesion is  benign or malign.

## Dataset
The training and testing data used for this project was provided by the PROSTATEx Challenges:
<a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=23691656">SPIE-AAPM-NCI PROSTATEx Challenges
(PROSTATEx)</a>. Due to the fact that only the training set provides a ground truth, the dataset was randomly split in 
order to provide a training and a testing dataset (see <strong>Detailed Description</strong>).

For training, there were provided <strong>T2-weighted transversal</strong> images, as well as <strong>ADC</strong> and 
<strong>KTrans</strong>. All DICOM files need to be converted to NIFTI files using 
<a href='https://www.nitrc.org/projects/mricrogl/'>MRIcoGL</a> [1]. Then the [Data preparation](Data%preparation.ipynb) 
notebook will sort out the T2-weighted transversal images as well as convert the KTrans files (*.mhd) into NIFTI format.
Through the [Data preparation](Data%preparation.ipynb) notebook, a pickle file will be created, that will contain the 
lesion information for each patient, based on the <strong>Findings.csv</strong> file, as well as the locations to each 
patient's T2-weighted, ADC, and KTrans files.

An example of how the data has been sorted and refined can be seen through running the 
[Visualize data](Visualize%data.ipynb) notebook.

## Bibliography
[1] Hugegene, <a href='https://towardsdatascience.com/3d-cnn-classification-of-prostate-tumour-on-multi-parametric-mri-sequences-prostatex-2-cced525394bb'>
3D CNN Classification of Prostate Cancer on PROSTATEx-2</a>, 3D CNN on Multi-Parametric MRI Sequences, 2019

