# Quick Start

[中文](quickstart_cn.md) · [Back to profile](../README.md)

Every LimX stack follows the same pattern: a **MuJoCo simulator** and an **RL controller** run as two processes and talk through the LimX SDK ([limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel)) on `127.0.0.1`. To go from simulation to a real robot, you only change that address. So the fastest way in is to watch a trained policy walk in simulation — no robot and no GPU needed.

## 1. Walk a robot in simulation (~10 min)

TRON1 on Linux x86_64 with Python 3.10–3.12.

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

## 2. Where to go next

| I want to… | Start here |
|---|---|
| Train my own locomotion policy (Isaac Lab, NVIDIA GPU) | TRON1: [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab), tasks `Isaac-Limx-{PF,SF,WF}-Blind-Flat-v0`<br>TRON2: [tron2_rl_lab](https://github.com/limxdynamics/tron2_rl_lab), tasks `Isaac-Limx-{SF,WF,DASF}-TRON2A-Blind-Flat-v0`<br>Oli: [humanoid-rl-isaaclab](https://github.com/limxdynamics/humanoid-rl-isaaclab) |
| Run a policy on a real robot | Same controller as above, pointed at the robot: `python main.py <robot-ip>`. Suspend the robot first and read the repo's safety notes. |
| Deploy inside ROS / ROS 2 | `*-rl-deploy-ros` / `*-rl-deploy-ros2` repos, plus [ros1-bridger](https://github.com/limxdynamics/ros1-bridger) / [ros2-bridger](https://github.com/limxdynamics/ros2-bridger) |
| Write my own controller | SDK examples in [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) (C++ and Python) |
| Do manipulation / VLA on TRON2 | [tron2_manipulation_controller](https://github.com/limxdynamics/tron2_manipulation_controller) (sim + SDK), [tron2_openpi](https://github.com/limxdynamics/tron2_openpi) + [tron2_env](https://github.com/limxdynamics/tron2_env) (pi0/pi0.5 on the real robot), [FluxVLA](https://github.com/FluxVLA/FluxVLA) |
| See a full visual-grasping demo run | [tron2_visual_grasp](https://github.com/limxdynamics/tron2_visual_grasp) — tennis-ball pick cycle on TRON2 (spot → approach → kneel → grasp), pure OpenCV, CPU-only, runs without hardware (`./run.sh demo`) |
| Retarget human motion to a humanoid | [GMR](https://github.com/limxdynamics/GMR) → [luna-beyondmimic](https://github.com/limxdynamics/luna-beyondmimic) |
| Follow the industry without writing code | [embodied-ai-insights](https://github.com/limxdynamics/embodied-ai-insights) monthly reports |

Full project list: [profile README](../README.md#open-source-projects)
