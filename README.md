# Reinforcement Learning for Robotics

This repository holds the development environment and demos used in the Reinforcement Learning for Robotics video series, which can be found [here](https://www.youtube.com/watch?v=zsdceSTRBl4&list=PLYExBrZNJeQg&index=1).

<a href="https://www.youtube.com/watch?v=zsdceSTRBl4&list=PLYExBrZNJeQg&index=1">
  <img src=".images/rl-for-robotics-thumbnail-play.png" alt="Reinforcement Learning for Robotics" height="500">
</a>

> If you are looking for the workshop/webinar version of this demo, please use this repository: [github.com/ShawnHymel/workshop-reinforcement-learning-for-robotics](https://github.com/ShawnHymel/workshop-reinforcement-learning-for-robotics/)

## Installation

Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/). Make sure it is running before continuing to the next step.

Open a terminal and build the Docker image:

```sh
docker build -t rl-robotics -f Dockerfile.cpu .
```

Run the image:

```sh
docker run -it --rm -p 3000:3000 -p 6006:6006 -v "${PWD}/workspace:/workspace" --shm-size=2g rl-robotics
```

Notes:
 * Port 3000 is for the WebTop interface
 * Port 6006 is for TensorBoard
 * VS Code is memory hungry, so we bump the shared memory up to 2 GB

Browse to [http://localhost:3000/](http://localhost:3000/) to interact with WebTop.

## License

All software in this repository, unless otherwise noted, is licensed under the [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) license.
