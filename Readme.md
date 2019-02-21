![Keras 2 Kubernetes](logo.png)
## Keras 2 Kubernetes

This is an Open Source project that tries to bridge the gap between Data Scientists and Software Developers. Keras is the most popular Deep Learning framework that allows Data Scientists to build and validate models on image data. Model that can learn to Classify images are stored as H5 files. Using Keras2Kubernetes these models can be easily packaged into Docker containers with a single command and deployed as microservices.

Command:
>> `docker run -p <<your port>>:7001 -v /mypath:/model dattarajrao/keras2kubernetes`

Here port 7001 is the port the container exposes - you can change to port on your machine. Describe a folder on your machine with a Keras model file named as 'model.h5'. The Docker container will start serving model from this folder (name has to be model.h5).

You can test the application by pointing your browser to:
`http://localhost:7001`

or use CURL command to validate the model as API:
>> `curl --form image=@/mymachinepath/image.jpg http://localhost:7001/inference`

also - JSON descriotion of the model is available at:
`http://localhost:7001/model`

This can easily be packaged as a Kubernetes deployment and service using the following YAML file:
`https://github.com/dattarajrao/keras2kubernetes/blob/master/deploy2k8s.yaml`

Please send across any questions, comments and feedbac to:
[Dattaraj Rao](mailto:dattarajrao@yahoo.com)

![Keras 2 Kubernetes](book_image.jpg)
### Keras to Kubernetes: The Journey of a Machine Learning Model to Production

* INRODUCTION

* A Word from the Author

* Chapter 1: BigData & Artificial Intelligence

* Chapter 2: Machine Learning

* Chapter 3: Handling Unstructured Data

* Chapter 4: Deep Learning using Keras

* Chapter 5: Advanced Deep Learning

* Chapter 6: Cutting-Edge Deep Learning Projects

* Chapter 7: AI in the Modern Softwear World

* Chapter 8: Deploying AI Models as a Microservice

* Chapter 9: Maching Learning Development Lifecycle

* Chapter 10: A Platform for Machine Learning

* Appendix A: REFERENCES
