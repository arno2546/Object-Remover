# Object Remover
<p>
        The goal of this project is to eliminate the cars from the image. The project is divided into two parts. The first one is MASK RCNN which helps to detects the car and the image inpainting eliminates the detected car object from the image .This project is part of a publication that was accepted in CONIT2021 and Later approached by Asian Journal for Convergence Technology for publication.The following links will redicrect to the publications and the presentation slides to better understand the work.     
</p>

* [Presentation Slide](https://www.researchgate.net/publication/352730450_Presentation_for_CONIT_2021Data_augmentation_technique_to_expand_road_dataset_Using_Mask_RCNN_and_image_inpainting)   
* [Conference paper link(IEEE)](https://ieeexplore.ieee.org/document/9498505) 
* [AJCT Journal Link](https://www.asianssr.org/index.php/ajct/article/view/1143)

## Getting Started
### Reuirements
- numpy
- scipy
- Pillow
- cython
- matplotlib
- scikit-image
- tensorflow>=1.3.0
- keras>=2.0.8
- opencv-python
- h5py
- imgaug
- IPython[all]

### Running the inpainter
To Inpaint an image with a mask

        python opencv_inpainting.py --image examples/example02.jpg --mask examples/mask02.jpg --method ns


