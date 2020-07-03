# inference-sdk-images
Arterys Inference SDK Docker Images for integrating ML models with the Arterys platform. These images are automatically published to Docker Hub at https://hub.docker.com/r/arterys/inference-sdk-base.


## Docker Images
The Dockerfiles are in the `base` folder. There is one for CPU only images and one for images that need GPU.

The CPU only `Dockerfile.cpu` creates an image with the following:
* Ubuntu 20.04
* Python 3.8
* Python GDCM (needed by pydicom to handle certain DICOM files)
* Python dependencies of the inference server (numpy, pydicom, Flask, etc.)

The `Dockerfile.gpu` will create base images with:
* `nvidia/cuda` base image with CuDNN7 and Ubuntu 18.04
* Miniconda with Python 3.7
* Python dependencies of the inference server (numpy, pydicom, Flask, etc.)

We chose to build the GPU images with Miniconda because it allows an easy installation of most ML frameworks and is the recommended way of installing some of them. 
However it might also increase the size of your final images.

We would love to get feedback about these base images. If you have feedback feel free to open an issue to start a discussion.
