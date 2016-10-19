## Docker setup instructions for TensorPy

#### 1. Install the Docker Toolbox from https://www.docker.com/products/docker-toolbox

#### 2. Create your for TensorPy Docker environment:

    docker-machine create --driver virtualbox tensorpy

##### (If your Docker environment ever goes down for any reason, you can bring it back up with a restart.)

    docker-machine restart tensorpy

#### 3. Configure your shell:

    eval "$(docker-machine env tensorpy)"

#### 4. Go to the TensorPy home directory on the command line, which is where [Dockerfile](https://github.com/TensorPy/TensorPy/blob/master/Dockerfile) is located. (This assumes you've already cloned the TensorPy repo.)

#### 5. Create your Docker image from your Dockerfile: (Get ready to wait awhile)

    docker build -t tensorpy .

#### 6. Run the example test

    docker run tensorpy ./run_docker_test.sh

#### 7. You can also enter Docker and stay inside the shell:

    docker run -i -t tensorpy

#### 8. Now you can run an example test from inside the Docker shell:

    ./test_classify_image.sh

#### 9. When you're satisfied, you may exit the Docker shell:

    exit

#### 10. (Optional) Since Docker images and containers take up a lot of space, you may want to clean up your machine from time to time when they’re not being used:
http://stackoverflow.com/questions/17236796/how-to-remove-old-docker-containers
Here are a few of those cleanup commands:

    docker images | grep "<none>" | awk '{print $3}' | xargs docker rmi
    docker rm 'docker ps --no-trunc -aq'

If you want to completely remove all of your Docker containers and images, use these commands: (If there's nothing to delete, those commands will return an error.)

    docker rm -f $(docker ps -a -q)
    docker rmi -f $(docker images -q)

Finally, if you want to wipe out your TensorPy Docker virtualbox, use these commands:

    docker-machine kill tensorpy
    docker-machine rm tensorpy

#### 11. (Optional) More reading on Docker can be found here:
* https://docs.docker.com
* https://docs.docker.com/mac/started/
* https://docs.docker.com/installation/mac/
