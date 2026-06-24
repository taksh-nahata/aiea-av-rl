# AIEA Lab: Robustifying AVs - RL Benchmarks

This repository contains the reinforcement learning benchmarking scripts developed for Task 5 of the AIEA Lab Onboarding process.

Author: Taksh

## Overview
This project utilizes Stable Baselines 3 (SB3) to train a Proximal Policy Optimization (PPO) agent on two separate autonomous driving environments. The objective of this task is to evaluate baseline model learning and then plot average rewards over time using TensorBoard.

The algorithms were trained remotely on the Nautilus Kubernetes Cluster using dedicated GPU instances.

## Repository Contents

* **`train_2d.py`**
  * **Environment:** `CarRacing-v2` (Gymnasium)
  * **Algorithm:** PPO
  * **Policy:** `CnnPolicy`
  * **Description:** Trains an agent to navigate a 2D physics-based racing track using raw pixel input processed through a Convolutional Neural Network.

* **`train_carla.py`**
  * **Environment:** `carla-v0` (CARLA 0.9.15)
  * **Algorithm:** PPO
  * **Policy:** `MlpPolicy`
  * **Description:** Trains an agent in a headless, 3D urban driving simulation. Sensor telemetry is flattened into a 1D array and processed through a Multi-Layer Perceptron.

## Tech Stack & Dependencies
* **OS:** Ubuntu 24.04 
* **Environment Manager:** Miniconda (Python 3.7)
* **Core Libraries:**
  * `gymnasium[box2d]`
  * `stable-baselines3`
  * `tensorboard`
  * `pygame`
* **Simulator:** CARLA UE4 (Headless Rendering Mode used to avoid performance issues and errors)
