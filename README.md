# 3D Prostate Cancer Classifier
The purpose of this project is to develop a Convolutional Neural Network capable to determine whether the prostate 
lesion is  benign or malign.

## Dataset
The training and testing data used for this project was provided by the PROSTATEx Challenges:
<a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=23691656">SPIE-AAPM-NCI PROSTATEx Challenges
(PROSTATEx)</a>. Due to the fact that only the training set provides a ground truth, the dataset was randomly split in 
order to provide a training and a testing dataset (see **Detailed Description**).

For training, there were provided <strong>T2-weighted transversal</strong> images, as well as **ADC** and **KTrans**. 
All DICOM files need to be converted to NIFTI files using <a href='https://www.nitrc.org/projects/mricrogl/'>MRIcoGL</a>
[1]. Then the [`Data preparation`](Data%preparation.ipynb) notebook will sort out the T2-weighted transversal images as 
well as convert the KTrans files (*.mhd) into NIFTI format. Through the [`Data preparation`](Data%preparation.ipynb) 
notebook, a pickle file will be created, that will contain the lesion information for each patient, based on the 
**Findings.csv** file, as well as the locations to each patient's T2-weighted, ADC, and KTrans files.

An example of how the data has been sorted and refined can be seen through running the 
[`Visualize data`](Visualize%data.ipynb) notebook.

### 3D Plotting using plot_lib
In order to visualize the **multiparametric Magnetic Resonance Images** (mpMRI) lesions, the 
[`Visualize data`](Visualize%20data.ipynb) notebook uses the [`plot_lib`](https://github.com/OscarPellicer/plot_lib) 
repository [2]. It can be cloned using the following command: 
```bash
git clone https://github.com/OscarPellicer/plot_lib.git
```

### Additional data used for plotting
[`ProstateX_masks.zip`](ProstateX_masks.zip) needs to be unpacked. It contains **automatically generated** ProstateX 
masks for the whole prostate as well as the central zone. [2-3]

[`ProstateX_plotting`](ProstateX_plotting) contains generated data from running the 
<a href='https://github.com/OscarPellicer/prostate_lesion_detection/blob/main/ProstateX%20preprocessing.ipynb'>ProstateX 
preprocessing</a>
notebook [2]. The data is used for visualising the lesions in the [`Visualize data`](Visualize%20data.ipynb) notebook.

## MONAI

## Training

## Bibliography
[1] Hugegene, <a href='https://towardsdatascience.com/3d-cnn-classification-of-prostate-tumour-on-multi-parametric-mri-sequences-prostatex-2-cced525394bb'>
3D CNN Classification of Prostate Cancer on PROSTATEx-2</a>. 3D CNN on Multi-Parametric MRI Sequences. 2019.

[2] Oscar J. Pellicer-Valero, José L. Marenco Jiménez, Victor Gonzalez-Perez, Juan Luis Casanova Ramón-Borja, Isabel 
Martín García, María Barrios Benito, Paula Pelechano Gómez, José Rubio-Briones, María José Rupérez, José D. 
Martín-Guerrero, <a href='https://arxiv.org/abs/2103.12650'>Deep Learning for fully automatic detection, segmentation, 
and Gleason Grade estimation of prostate cancer in multiparametric Magnetic Resonance Images</a>. Scientific Reports. 
February, 2022.

[3] Oscar J. Pellicer-Valero, Victor Gonzalez-Perez, Juan Luis Casanova Ramón-Borja, Isabel Martín García,María Barrios 
Benito, Paula Pelechano Gómez,José Rubio-Briones,María José Rupérez, José D. Martín-Guerrero, 
<a href='https://www.mdpi.com/2076-3417/11/2/844'>Robust Resolution-Enhanced Prostate Segmentation in Magnetic Resonance
and Ultrasound Images through Convolutional Neural Networks</a>. Applied Sciences. 2021.

