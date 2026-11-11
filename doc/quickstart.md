# Quick Start

[中文](quickstart_cn.md) · [Back to profile](../README.md)

Every LimX stack follows the same pattern: a **MuJoCo simulator** and an **RL controller** run as two processes and talk through the LimX SDK ([limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel)) on `127.0.0.1`. To go from simulation to a real robot, you only change that address. So the fastest way in is to watch a trained policy run in simulation — no robot and no GPU needed.

<p align="center"><a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"><img src="https://img.shields.io/badge/Join%20Our%20WeChat%20Community-All%20Projects%20Welcome-07C160?style=for-the-badge&logo=wechat&logoColor=white" alt="WeChat Community"></a></p>

## Choose your robot

| Robot | What it is | Try it without a robot |
|---|---|---|
| [**TRON1**](#tron1) | Biped with point-foot, sole-foot and wheel-foot variants | Walk it in MuJoCo (~10 min) |
| [**TRON2**](#tron2) | Modular robot: sole-foot or wheel-foot biped, dual arm, or the DASF humanoid composite; TRON2A and TRON2B | Walk it in MuJoCo |
| [**Oli** (HU_D04)](#oli) | Full-size humanoid, 31 joints | Stand, wave and walk in MuJoCo |
| [**Luna** (HU_L04)](#luna) | Humanoid, 27 joints, whole-body motion such as dancing | Look at the model in 30 s; motion training needs an NVIDIA GPU |

<a id="tron1"></a>

## TRON1

### Walk it in simulation (~10 min)

Linux x86_64 with Python 3.10–3.12.

```bash
git clone --recurse-submodules https://github.com/limxdynamics/tron1-mujoco-sim
git clone https://github.com/limxdynamics/tron1-rl-deploy-python

python3 -m venv ~/.venvs/limx-tron1 && source ~/.venvs/limx-tron1/bin/activate
# The SDK wheel also pulls in mujoco, onnxruntime, scipy, pyyaml and pygame
pip install tron1-mujoco-sim/limxsdk-lowlevel/python3/amd64/limxsdk-*.whl
```

```bash
# Terminal 1 — simulator
source ~/.venvs/limx-tron1/bin/activate
export ROBOT_TYPE=PF_TRON1A        # PF_* point-foot, SF_* sole-foot, WF_* wheel-foot
python tron1-mujoco-sim/simulator.py

# Terminal 2 — RL controller (ships with trained ONNX policies)
source ~/.venvs/limx-tron1/bin/activate
export ROBOT_TYPE=PF_TRON1A RL_TYPE=isaaclab
python tron1-rl-deploy-python/main.py
```

> The robot falls over as soon as the simulator starts. Once the controller is running, press **Backspace** in the MuJoCo window: the robot stands up and steps in place. Run `./tron1-mujoco-sim/robot-joystick/robot-joystick` for a virtual gamepad to steer it.

### Next steps

| I want to… | Start here |
|---|---|
| Train my own locomotion policy (NVIDIA GPU) | [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab), tasks `Isaac-Limx-{PF,SF,WF}-Blind-Flat-v0`; [tron1-rl-isaacgym](https://github.com/limxdynamics/tron1-rl-isaacgym) if you already work with Isaac Gym |
| Run a policy on the real robot | The same controller, pointed at the robot: `python main.py <robot-ip>` |
| Deploy inside ROS / ROS 2 | [tron1-rl-deploy-ros](https://github.com/limxdynamics/tron1-rl-deploy-ros) · [tron1-rl-deploy-ros2](https://github.com/limxdynamics/tron1-rl-deploy-ros2) |
| Map, localize and navigate | [tron1-ss](https://github.com/limxdynamics/tron1-ss) (LiDAR SLAM and path planning) |
| Talk to the robot | [tron1-agent](https://github.com/limxdynamics/tron1-agent) (voice commands and LLM dialogue) |

### See what others built with TRON1

[TRON1 on Awesome LimX](https://github.com/limxdynamics/awesome-limx/blob/main/robots/TRON1.md) collects public papers, code, datasets, competition entries and industry deployments that use TRON1. Find a project close to what you want to do and start from its code; rows marked *sim* were shown only in simulation. Built something yourself? [Submit it](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml).

### All TRON1 repositories

```
tron1-robot-description ──► tron1-rl-isaaclab / tron1-rl-isaacgym ──► ONNX policy ──► tron1-mujoco-sim ──► tron1-rl-deploy-{ros, ros2, python} ──► TRON1
      (robot models)                  (train)                                       (sim-to-sim check)          (run on the real robot)
```

| Stage | Repository | What it does |
|---|---|---|
| Robot model | [tron1-robot-description](https://github.com/limxdynamics/tron1-robot-description) | URDF / Xacro / MJCF models for ROS 1/2, MuJoCo and Gazebo |
| Simulation | [tron1-mujoco-sim](https://github.com/limxdynamics/tron1-mujoco-sim) | MuJoCo simulator with the same `limxsdk` interface as the robot |
| Simulation | [tron1-gazebo-ros](https://github.com/limxdynamics/tron1-gazebo-ros) · [tron1-gazebo-ros2](https://github.com/limxdynamics/tron1-gazebo-ros2) | Gazebo simulation on ROS Noetic · ROS 2 Iron |
| Training | [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab) | RL training on Isaac Lab, recommended for new projects |
| Training | [tron1-rl-isaacgym](https://github.com/limxdynamics/tron1-rl-isaacgym) | RL training on Isaac Gym |
| Deployment | [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python) | Python deployment, with pre-trained policies |
| Deployment | [tron1-rl-deploy-ros](https://github.com/limxdynamics/tron1-rl-deploy-ros) · [tron1-rl-deploy-ros2](https://github.com/limxdynamics/tron1-rl-deploy-ros2) | Deployment on ROS Noetic · ROS 2 Iron |
| Deployment | [tron1-rl-deploy-arm](https://github.com/limxdynamics/tron1-rl-deploy-arm) | RL deployment for TRON1 with the arm |
| Applications | [tron1-ss](https://github.com/limxdynamics/tron1-ss) | LiDAR SLAM and navigation: mapping, localization, path planning |
| Applications | [tron1-agent](https://github.com/limxdynamics/tron1-agent) | Voice-interactive AI agent: speech commands, LLM dialogue, robot actions |

<a id="tron2"></a>

## TRON2

### Walk it in simulation

Linux x86_64 with Python 3.10+. The simulator uses [uv](https://docs.astral.sh/uv/) (install it with `curl -LsSf https://astral.sh/uv/install.sh | sh` if you don't have it); its robot models are about 1.7 GB to download.

```bash
# Terminal 1 — simulator
git clone https://github.com/limxdynamics/tron2_mujoco_sim.git
cd tron2_mujoco_sim
git submodule update --init --depth 1 robot-description limxsdk-lowlevel robot-joystick
uv sync --extra sdk
ROBOT_TYPE=SF_TRON2A uv run simulator.py
```

```bash
# Terminal 2 — RL controller (ships with trained ONNX policies)
git clone --recurse-submodules https://github.com/limxdynamics/tron2_rl_deploy_python.git
cd tron2_rl_deploy_python
python3 -m venv ~/.venvs/limx-tron2 && source ~/.venvs/limx-tron2/bin/activate
pip install numpy scipy pyyaml onnxruntime pygame
pip install limxsdk-lowlevel/python3/amd64/limxsdk-*.whl
export ROBOT_TYPE=SF_TRON2A        # SF_TRON2A sole-foot, WF_TRON2A wheel-foot, DASF_TRON2A with arms; same value in both terminals
python3 main.py
```

> The robot falls over before the controller connects. Press **L1 + B** (prepare), then **L1 + Y** (start), then press **Backspace** in the MuJoCo window: the robot restarts upright and keeps its balance. The left stick moves it and the right stick turns it.
>
> No gamepad? Run `tron2_mujoco_sim/robot-joystick/robot-joystick` in a third terminal for a virtual one, and type into its window: **Q** is L1, **L** is B, **I** is Y, and the **arrow keys** are the left stick. A real gamepad should be a Logitech F710 in `X` mode.

### Next steps

| I want to… | Start here |
|---|---|
| Train my own locomotion policy (NVIDIA GPU) | [tron2_rl_lab](https://github.com/limxdynamics/tron2_rl_lab), tasks `Isaac-Limx-{SF,WF,DASF}-TRON2A-Blind-Flat-v0`; [TRON2_YG_LAB](https://github.com/limxdynamics/TRON2_YG_LAB) for the 6-DoF arm and gripper variants |
| Run a policy on the real robot | The same controller, pointed at the robot: `python3 main.py <robot-ip>` |
| Deploy inside ROS | [tron2_rl_deploy_ros](https://github.com/limxdynamics/tron2_rl_deploy_ros) (ROS Noetic) · Gazebo: [tron2_gazebo_ros](https://github.com/limxdynamics/tron2_gazebo_ros) |
| Do manipulation / VLA | [tron2_manipulation_controller](https://github.com/limxdynamics/tron2_manipulation_controller) (dual-arm sim + SDK), [tron2_openpi](https://github.com/limxdynamics/tron2_openpi) + [tron2_env](https://github.com/limxdynamics/tron2_env) (pi0/pi0.5 on the real robot), [FluxVLA](https://github.com/FluxVLA/FluxVLA) |
| See a full visual-grasping demo run | [tron2_visual_grasp](https://github.com/limxdynamics/tron2_visual_grasp) — tennis-ball pick cycle (spot → approach → kneel → grasp), pure OpenCV, CPU-only, runs without hardware (`./run.sh demo`) |
| Navigate autonomously | [tron2-navigation-ros2](https://github.com/limxdynamics/tron2-navigation-ros2) (ROS 2 Humble) |
| Get the robot models | [tron2-robot-description](https://github.com/limxdynamics/tron2-robot-description) (URDF/xacro, MuJoCo XML, USD for TRON2A and TRON2B) |

### See what others built with TRON2

[TRON2 on Awesome LimX](https://github.com/limxdynamics/awesome-limx/blob/main/robots/TRON2.md) collects public papers, code, datasets, competition entries and industry deployments that use TRON2. Find a project close to what you want to do and start from its code; rows marked *sim* were shown only in simulation. Built something yourself? [Submit it](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml).

<a id="oli"></a>

## Oli (HU_D04)

### Stand, wave and walk in simulation

Linux x86_64 with Python 3.8+.

```bash
mkdir -p ~/limx_ws && cd ~/limx_ws
git clone --recurse-submodules https://github.com/limxdynamics/humanoid-mujoco-sim
git clone https://github.com/limxdynamics/humanoid-rl-deploy-python

python3 -m venv ~/.venvs/limx-oli && source ~/.venvs/limx-oli/bin/activate
pip install -r humanoid-mujoco-sim/requirements.txt
# click is needed by the controller but not installed by the SDK wheel
pip install humanoid-mujoco-sim/limxsdk-lowlevel/python3/amd64/limxsdk-*.whl click
```

```bash
# In each terminal first: cd ~/limx_ws && source ~/.venvs/limx-oli/bin/activate && export ROBOT_TYPE=HU_D04_01
python humanoid-mujoco-sim/simulator.py            # Terminal 1 — simulator
python humanoid-rl-deploy-python/main.py           # Terminal 2 — RL controller
humanoid-mujoco-sim/robot-joystick/robot-joystick  # Terminal 3 — virtual gamepad
```

> The robot falls over before the controller connects. In the virtual gamepad window, hold **Q** (L1) and press **I** (Y) to switch to standing, wait a few seconds, then click **Reset** in the MuJoCo window: the robot restarts upright. From standing, **Q + L** (L1 + B) waves, and **U + J** (R1 + X) switches to walking; the **arrow keys** steer.
>
> The humanoid simulator needs a reasonably fast multi-core computer. If the robot keeps falling, the simulator is probably running slower than real time: close other programs, switch to standing, wait, and click **Reset** again.

### Next steps

| I want to… | Start here |
|---|---|
| Train my own locomotion policy (NVIDIA GPU) | [humanoid-rl-isaaclab](https://github.com/limxdynamics/humanoid-rl-isaaclab) |
| Try my own walking policy | Export it as `policy.onnx` into `humanoid-rl-deploy-python/controllers/HU_D04_01/walk_controller/policy/default` and run the simulation above |
| Run a policy on the real robot | "Real Robot Debugging" in [humanoid-rl-deploy-python](https://github.com/limxdynamics/humanoid-rl-deploy-python) |
| Deploy inside ROS / ROS 2, or in plain C++ | [humanoid-rl-deploy-ros](https://github.com/limxdynamics/humanoid-rl-deploy-ros) · [humanoid-rl-deploy-ros2](https://github.com/limxdynamics/humanoid-rl-deploy-ros2) · [humanoid-rl-deploy-cpp](https://github.com/limxdynamics/humanoid-rl-deploy-cpp) |
| Retarget human motion to Oli | [GMR](https://github.com/limxdynamics/GMR) (robot key `limx_oli_edu`) |
| Get the robot models | [humanoid-description](https://github.com/limxdynamics/humanoid-description) (URDF, MuJoCo MJCF, USD) |

### See what others built with Oli

[Oli on Awesome LimX](https://github.com/limxdynamics/awesome-limx/blob/main/robots/Oli.md) collects public papers, code, datasets, competition entries and industry deployments that use Oli. Find a project close to what you want to do and start from its code; rows marked *sim* were shown only in simulation. Built something yourself? [Submit it](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml).

<a id="luna"></a>

## Luna (HU_L04)

### Look at the robot in 30 seconds

```bash
git clone https://github.com/limxdynamics/luna-description.git
cd luna-description
pip install mujoco
python -m mujoco.viewer --mjcf=HU_L04_description/xml/HU_L04_01.xml
```

> Nothing is controlling the robot, so it collapses as soon as the window opens. Press **Space** to pause, then **Backspace** to put it back in its standing pose.

### Teach Luna a motion

```
human motion (SMPL-X / BVH)  ──►  GMR  ──►  motion .npy  ──►  luna-beyondmimic  ──►  policy.onnx  ──►  Luna
                               (retarget)                     (train, Isaac Lab)       + reference + param.yaml
```

- [luna-beyondmimic](https://github.com/limxdynamics/luna-beyondmimic) trains a whole-body motion-tracking policy on Isaac Lab (NVIDIA GPU) and exports the files the robot runs. It ships with a 22.9 s dance motion, so you can train end to end before retargeting anything yourself. Start with its `QuickStart.md`.
- [GMR](https://github.com/limxdynamics/GMR) (robot key `limx_luna`) retargets your own motion capture or SMPL-X data to Luna.
- [luna-description](https://github.com/limxdynamics/luna-description) has the URDF, MuJoCo MJCF and USD models.

### See what others built with Luna

[Luna on Awesome LimX](https://github.com/limxdynamics/awesome-limx/blob/main/robots/Luna.md) collects public papers, code, datasets, competition entries and industry deployments that use Luna. Find a project close to what you want to do and start from its code; rows marked *sim* were shown only in simulation. Built something yourself? [Submit it](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml).

## For every robot

| I want to… | Start here |
|---|---|
| Write my own controller | SDK examples in [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) (C++ and Python) |
| Bridge ROS across machines | [ros1-bridger](https://github.com/limxdynamics/ros1-bridger) · [ros2-bridger](https://github.com/limxdynamics/ros2-bridger) |
| See what people built on LimX robots, or add my project | [Awesome LimX](https://github.com/limxdynamics/awesome-limx) — one page per robot |
| Follow the industry without writing code | [embodied-ai-insights](https://github.com/limxdynamics/embodied-ai-insights) monthly reports |

> **Before running on a real robot:** check the policy in simulation first, suspend the robot, and read the safety notes in the repository you deploy from.

Full project list: [profile README](../README.md#open-source-projects)
