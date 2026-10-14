<div align="center">

<a href="README.md"><img src="https://img.shields.io/badge/English-24292f?style=for-the-badge" alt="English"></a>&nbsp;&nbsp;<a href="README_cn.md"><img src="https://img.shields.io/badge/Chinese-24292f?style=for-the-badge" alt="中文"></a>

</div>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="doc/logo-white-theme.png">
    <source media="(prefers-color-scheme: light)" srcset="doc/logo-black-theme.png">
    <img src="doc/logo-black-theme.png" width="300" alt="LimX Dynamics">
  </picture>
</p>

LimX Dynamics is a general-purpose robotics company, focusing on full-size humanoid robots and have developed innovative products such as biped and quadruped robots.

LimX Dynamics is dedicated to disruptive innovations by Embodied AI. The goal is to unleash the generalization of Artificial General Intelligence (AGI) in the physical world. Based on revolutionizing core software and hardware technologies, and building first-of-its-kind foundation model for humanoid robots, we aim to achieving loco-manipulation robotics platform and Embodied AI tool kits for innovators and integrators. We promote the widespread applications of Embodied AI across B2B & B2C sectors, including R&D, manufacturing, business and households services. 

<div align="center">
<p align="center">
  <a href="https://www.youtube.com/@LimXDynamics/featured"><img src="https://img.shields.io/badge/YouTube-24292f?style=flat&logo=youtube&logoColor=white&logoSize=auto" alt="YouTube" height="24"></a>&nbsp;
  <a href="https://space.bilibili.com/1172054289"><img src="https://img.shields.io/badge/Bilibili-24292f?style=flat&logo=bilibili&logoColor=white&logoSize=auto" alt="Bilibili" height="24"></a>&nbsp;
  <a href="https://www.douyin.com/user/MS4wLjABAAAAi4WtqIxdAP5iqbT4BSEgUWPu6g9h_Pl7VXaQOLfDeFK1LgZo5O4IbIknTVeL6Zq-?from_tab_name=main&relation=0&vid=7654443992867786011"><img src="https://img.shields.io/badge/Douyin-24292f?style=flat&logo=tiktok&logoColor=white&logoSize=auto" alt="Douyin" height="24"></a>&nbsp;
  <a href="https://www.xiaohongshu.com/user/profile/66e44fa8000000001d020784?xsec_token=ABnTSjc077y0Y9d7LrDkVdpR_IwBO36Dm_4eHTx1mXBE0=&xsec_source=pc_note"><img src="https://img.shields.io/badge/Xiaohongshu-24292f?style=flat&logo=xiaohongshu&logoColor=white&logoSize=auto" alt="Xiaohongshu" height="24"></a>&nbsp;
  <a href="https://www.kuaishou.com/profile/3xvskq6dkc4puq6"><img src="https://img.shields.io/badge/Kuaishou-24292f?style=flat&logo=kuaishou&logoColor=white&logoSize=auto" alt="Kuaishou" height="24"></a>&nbsp;
  <a href="https://x.com/LimX_Dynamics"><img src="https://img.shields.io/badge/X-24292f?style=flat&logo=x&logoColor=white&logoSize=auto" alt="X" height="24"></a>&nbsp;
  <a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_official_en.png"><img src="https://img.shields.io/badge/WeChat-24292f?style=flat&logo=wechat&logoColor=white&logoSize=auto" alt="WeChat" height="24"></a>
</p>

<p align="center">
  <a href="https://huggingface.co/limxdynamics"><img src="https://img.shields.io/badge/HuggingFace-24292f?style=flat&logo=huggingface&logoColor=white&logoSize=auto" alt="HuggingFace" height="24"></a>&nbsp;
  <a href="https://modelscope.cn/organization/LimXDynamics?tab=all"><img src="https://img.shields.io/badge/ModelScope-24292f?style=flat&logo=modelscope&logoColor=white&logoSize=auto" alt="ModelScope" height="24"></a>&nbsp;
  <a href="https://www.limxdynamics.com/"><img src="https://img.shields.io/badge/Website-24292f?style=flat&logo=googlechrome&logoColor=white&logoSize=auto" alt="Website" height="24"></a>&nbsp;
  <a href="https://career.limxdynamics.com/"><img src="https://img.shields.io/badge/Careers-24292f?style=flat" alt="Careers" height="24"></a>
</p>

<p align="center">
  <a href="https://github.com/limxdynamics"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Fstars.json&style=flat&logo=github&logoSize=auto" alt="Stars" height="24"></a>&nbsp;
  <a href="https://github.com/limxdynamics"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Fforks.json&style=flat&logo=github&logoSize=auto" alt="Forks" height="24"></a>&nbsp;
  <a href="https://github.com/limxdynamics"><img src="https://badges.strrl.dev/years/limxdynamics?style=flat&logo=github&logoColor=white&logoSize=auto" alt="Years" height="24"></a>
</p>
</div>


<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/limxdynamics/limxdynamics/main/stars-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/limxdynamics/limxdynamics/main/stars.svg">
    <img src="https://raw.githubusercontent.com/limxdynamics/limxdynamics/main/stars.svg" alt="Total stars across all projects" width="720">
  </picture>
</p>

<p align="center"><a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"><img src="https://img.shields.io/badge/Join%20Our%20WeChat%20Community-All%20Projects%20Welcome-07C160?style=for-the-badge&logo=wechat&logoColor=white" alt="WeChat Community"></a></p>

## Quick Start

Every LimX stack follows the same pattern: a **MuJoCo simulator** and an **RL controller** run as two processes and talk through the LimX SDK ([limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel)) on `127.0.0.1`. To go from simulation to a real robot, you only change that address. So the fastest way in is to watch a trained policy walk in simulation — no robot and no GPU needed.

### 1. Walk a robot in simulation (~10 min)

Linux (x86_64 / aarch64) or Windows 10/11 x64, with **Python 3.10–3.12**. On ARM Linux, replace `amd64` with `aarch64` in the wheel paths. Windows commands are in the collapsible blocks below each section.

**TRON1**

```bash
git clone --recurse-submodules https://github.com/limxdynamics/tron1-mujoco-sim
git clone https://github.com/limxdynamics/tron1-rl-deploy-python

python3 -m venv ~/.venvs/limx-tron1 && source ~/.venvs/limx-tron1/bin/activate
# The SDK wheel also pulls in mujoco, onnxruntime, scipy, pyyaml and pygame
pip install tron1-mujoco-sim/limxsdk-lowlevel/python3/amd64/limxsdk-*-py3-none-any.whl
```

```bash
# Terminal 1 — simulator
source ~/.venvs/limx-tron1/bin/activate
export ROBOT_TYPE=PF_TRON1A        # PF_* point-foot, SF_* sole-foot, WF_* wheel-foot; see tron1-mujoco-sim/robot-description/pointfoot/
python tron1-mujoco-sim/simulator.py

# Terminal 2 — RL controller (ships with trained ONNX policies)
source ~/.venvs/limx-tron1/bin/activate
export ROBOT_TYPE=PF_TRON1A        # must match the simulator
export RL_TYPE=isaaclab            # which trainer the bundled policy came from: isaaclab | isaacgym
python tron1-rl-deploy-python/main.py

# Terminal 3 (optional) — virtual gamepad for velocity commands
./tron1-mujoco-sim/robot-joystick/robot-joystick
```

> The robot falls over as soon as the simulator starts, because nothing is driving its joints yet. Once the controller is running, press **Backspace** in the MuJoCo window to reset it: the robot stands up and steps in place.

<details>
<summary>TRON1 on Windows (PowerShell)</summary>

```powershell
git clone --recurse-submodules https://github.com/limxdynamics/tron1-mujoco-sim
git clone https://github.com/limxdynamics/tron1-rl-deploy-python

py -3.12 -m venv $HOME\.venvs\limx-tron1
& $HOME\.venvs\limx-tron1\Scripts\Activate.ps1   # if blocked: Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
# PowerShell does not expand * for pip, so resolve the wheel path first
pip install (Get-ChildItem tron1-mujoco-sim\limxsdk-lowlevel\python3\win\limxsdk-*.whl).FullName
```

```powershell
# Terminal 1 — simulator
& $HOME\.venvs\limx-tron1\Scripts\Activate.ps1
$env:ROBOT_TYPE = "PF_TRON1A"
python tron1-mujoco-sim\simulator.py

# Terminal 2 — RL controller
& $HOME\.venvs\limx-tron1\Scripts\Activate.ps1
$env:ROBOT_TYPE = "PF_TRON1A"; $env:RL_TYPE = "isaaclab"
python tron1-rl-deploy-python\main.py

# Terminal 3 (optional) — virtual gamepad
.\tron1-mujoco-sim\robot-joystick\robot-joystick.exe
```

</details>

<details>
<summary><b>TRON2</b> (simulator and controller use different SDK builds, so each gets its own venv)</summary>

```bash
git clone --recurse-submodules https://github.com/limxdynamics/tron2_mujoco_sim
git clone --recurse-submodules https://github.com/limxdynamics/tron2_rl_deploy_python
```

```bash
# Terminal 1 — simulator
python3 -m venv ~/.venvs/limx-tron2-sim && source ~/.venvs/limx-tron2-sim/bin/activate
pip install "mujoco>=3.2.2" "pyyaml>=6.0"
pip install --no-deps tron2_mujoco_sim/limxsdk-lowlevel/python3/amd64/limxsdk-*.whl
export ROBOT_TYPE=SF_TRON2A        # also WF_TRON2A, DASF_TRON2A
python tron2_mujoco_sim/simulator.py

# Terminal 2 — RL controller
python3 -m venv ~/.venvs/limx-tron2-ctl && source ~/.venvs/limx-tron2-ctl/bin/activate
pip install numpy scipy pyyaml onnxruntime pygame
pip install tron2_rl_deploy_python/limxsdk-lowlevel/python3/amd64/limxsdk-*.whl
export ROBOT_TYPE=SF_TRON2A
python tron2_rl_deploy_python/main.py
```

On **Windows (PowerShell)**, the SDK wheels live in `python3\win\`. The simulator's Windows SDK build supports `SF_TRON2A` and `WF_TRON2A` only; `DASF_TRON2A` needs Linux.

```powershell
# Terminal 1 — simulator
py -3.12 -m venv $HOME\.venvs\limx-tron2-sim
& $HOME\.venvs\limx-tron2-sim\Scripts\Activate.ps1
pip install "mujoco>=3.2.2" "pyyaml>=6.0"
pip install --no-deps (Get-ChildItem tron2_mujoco_sim\limxsdk-lowlevel\python3\win\limxsdk-*.whl).FullName
$env:ROBOT_TYPE = "SF_TRON2A"
python tron2_mujoco_sim\simulator.py

# Terminal 2 — RL controller
py -3.12 -m venv $HOME\.venvs\limx-tron2-ctl
& $HOME\.venvs\limx-tron2-ctl\Scripts\Activate.ps1
pip install numpy scipy pyyaml onnxruntime pygame
pip install (Get-ChildItem tron2_rl_deploy_python\limxsdk-lowlevel\python3\win\limxsdk-*.whl).FullName
$env:ROBOT_TYPE = "SF_TRON2A"
python tron2_rl_deploy_python\main.py
```

The controller starts in `IDLE` and is driven by a gamepad. A Logitech F710 (X mode) is read directly; without one, run the virtual gamepad in a third terminal (`./tron2_mujoco_sim/robot-joystick/robot-joystick`, or `robot-joystick.exe` on Windows). Then:

1. `L1 + ○ (B)` — move the joints to the default pose.
2. Press **R** in the MuJoCo window — put the fallen base back upright (joint angles are kept).
3. `L1 + △ (Y)` — start walking; the left stick sets velocity. `L1 + × (A)` stops.

</details>

For **Oli**, the pair is [humanoid-mujoco-sim](https://github.com/limxdynamics/humanoid-mujoco-sim) + [humanoid-rl-deploy-python](https://github.com/limxdynamics/humanoid-rl-deploy-python) with `ROBOT_TYPE=HU_D04_01`; follow their READMEs.

### 2. Where to go next

| I want to… | Start here |
|---|---|
| Train my own locomotion policy (Isaac Lab, NVIDIA GPU) | TRON1: [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab), tasks `Isaac-Limx-{PF,SF,WF}-Blind-Flat-v0`<br>TRON2: [tron2_rl_lab](https://github.com/limxdynamics/tron2_rl_lab), tasks `Isaac-Limx-{SF,WF,DASF}-TRON2A-Blind-Flat-v0`<br>Oli: [humanoid-rl-isaaclab](https://github.com/limxdynamics/humanoid-rl-isaaclab) |
| Run a policy on a real robot | Same controller as above, pointed at the robot: `python main.py <robot-ip>`. Suspend the robot first and read the repo's safety notes. |
| Deploy inside ROS / ROS 2 | `*-rl-deploy-ros` / `*-rl-deploy-ros2` in the table below, plus [ros1-bridger](https://github.com/limxdynamics/ros1-bridger) / [ros2-bridger](https://github.com/limxdynamics/ros2-bridger) |
| Write my own controller | SDK examples in [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) (C++ and Python) |
| Do manipulation / VLA on TRON2 | [tron2_manipulation_controller](https://github.com/limxdynamics/tron2_manipulation_controller) (sim + SDK), [tron2_openpi](https://github.com/limxdynamics/tron2_openpi) + [tron2_env](https://github.com/limxdynamics/tron2_env) (pi0/pi0.5 on the real robot), [FluxVLA](https://github.com/FluxVLA/FluxVLA) |
| Retarget human motion to a humanoid | [GMR](https://github.com/limxdynamics/GMR) → [luna-beyondmimic](https://github.com/limxdynamics/luna-beyondmimic) |
| Follow the industry without writing code | [embodied-ai-insights](https://github.com/limxdynamics/embodied-ai-insights) monthly reports |

<div>
    <img src="https://149753425.v2.pressablecdn.com/wp-content/uploads/2009/06/osi_symbol_100X100_0.png" width="20" height="20" style="display:inline-block; vertical-align:top;">
    <span style="display:inline-block; vertical-align:top;">Open source projects</span> 
</div>

<table class="table table-striped table-bordered table-vcenter"/>
    <tbody>
    <tr><th>Platform</th><th>Type</th><th> Title </th> <th>Description</th> <th>Stars</th> </tr>
    <!-- Empty rows keep rowspan category cells on the default white stripe. -->
    <tr></tr>
    <tr>
        <td rowspan="1" class="font-weight-bold">Insights</td>
        <td align="center" >Report</td>
        <td align="center" ><a href="https://github.com/limxdynamics/embodied-ai-insights"> embodied-ai-insights </a></td>
        <td> Monthly reports on the embodied AI open-source ecosystem, built from public GitHub data — tracking star growth, new repositories and community activity across leading robotics companies. </td>
        <td><a href="https://github.com/limxdynamics/embodied-ai-insights"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__embodied-ai-insights.json"/></a></td>
    </tr>
    <tr></tr>
    <tr>
        <td rowspan="13" class="font-weight-bold">TRON2</td>
        <td align="center" >Description</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2-robot-description"> tron2-robot-description </a></td>
        <td> Robot model files for TRON2 variants, including URDF/xacro, MuJoCo XML, meshes, and optional USD assets for simulation, visualization, and downstream tooling. </td>
        <td><a href="https://github.com/limxdynamics/tron2-robot-description"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2-robot-description.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Simulation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2_gazebo_ros"> tron2_gazebo_ros </a></td>
        <td> A ROS Noetic and Gazebo simulation workspace for TRON2 robots that supports controller integration, Sim-to-Real validation, and deployment workflows. </td>
        <td><a href="https://github.com/limxdynamics/tron2_gazebo_ros"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2_gazebo_ros.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Simulation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2_mujoco_sim"> tron2_mujoco_sim </a></td>
        <td> A <a href="https://mujoco.org"> MuJoCo </a> simulation tool for TRON2 robots that supports SF/WF robot types and controller deployment through the LimX SDK. </td>
        <td><a href="https://github.com/limxdynamics/tron2_mujoco_sim"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2_mujoco_sim.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Training</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2_rl_lab"> tron2_rl_lab </a></td>
        <td> An <a href="https://isaac-sim.github.io/IsaacLab/"> Isaac Lab </a> reinforcement learning training stack for TRON2 robots, supporting SF/WF (sole-foot and wheel-foot) variants. </td>
        <td><a href="https://github.com/limxdynamics/tron2_rl_lab"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2_rl_lab.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Training</td>
        <td align="center" ><a href="https://github.com/limxdynamics/TRON2_YG_LAB"> TRON2_YG_LAB </a></td>
        <td> An Isaac Lab reinforcement learning training stack for TRON2 robots with 6-DoF arm and gripper variants, designed for locomotion policy training and play. </td>
        <td><a href="https://github.com/limxdynamics/TRON2_YG_LAB"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__TRON2_YG_LAB.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2_rl_deploy_python"> tron2_rl_deploy_python </a></td>
        <td> A Python-based reinforcement learning deployment demo for TRON2 robots that runs ONNX policies and supports MuJoCo simulation and real-world deployment. </td>
        <td><a href="https://github.com/limxdynamics/tron2_rl_deploy_python"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2_rl_deploy_python.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2_rl_deploy_ros"> tron2_rl_deploy_ros </a></td>
        <td> A ROS Noetic reinforcement learning deployment workspace for TRON2 robots, including hardware, controller, and ONNX runtime packages for simulation and real robots. </td>
        <td><a href="https://github.com/limxdynamics/tron2_rl_deploy_ros"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2_rl_deploy_ros.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2_env"> tron2_env </a></td>
        <td> A public TRON2 runtime package for OpenPI deployment, providing WebSocket robot communication, motion execution, observation collection, and RTC helper utilities for real-robot manipulation. </td>
        <td><a href="https://github.com/limxdynamics/tron2_env"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2_env.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2_openpi"> tron2_openpi </a></td>
        <td> A TRON2 deployment-focused derivative of OpenPI that adds TRON2 policy transforms, deployment configuration templates, pi0/pi0.5 policy serving, and real-robot client examples. </td>
        <td><a href="https://github.com/limxdynamics/tron2_openpi"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2_openpi.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Manipulation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2_manipulation_controller"> tron2_manipulation_controller </a></td>
        <td> A local simulation and SDK validation workspace for the TRON2 dual-arm robot, pairing a <a href="https://mujoco.org"> MuJoCo </a> motor-level simulator with the controller runtime and WebSocket SDK, and including VLA trajectory replay and limit checking. </td>
        <td><a href="https://github.com/limxdynamics/tron2_manipulation_controller"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2_manipulation_controller.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Navigation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2-navigation-ros2"> tron2-navigation-ros2 </a></td>
        <td> ROS 2 Humble navigation integration for TRON2, including the production SCAN-Planner subset, RoboSense LiDAR drivers, and safety/deployment tooling; GPL components live in companion repos. </td>
        <td><a href="https://github.com/limxdynamics/tron2-navigation-ros2"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2-navigation-ros2.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Navigation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2-navigation-pct-gpl"> tron2-navigation-pct-gpl </a></td>
        <td> GPL-2.0-or-later PCT planner sources for tron2-navigation-ros2. </td>
        <td><a href="https://github.com/limxdynamics/tron2-navigation-pct-gpl"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2-navigation-pct-gpl.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Navigation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron2-navigation-fastlio-gpl"> tron2-navigation-fastlio-gpl </a></td>
        <td> GPL-2.0-only FAST-LIO ROS 2 sources for tron2-navigation-ros2. </td>
        <td><a href="https://github.com/limxdynamics/tron2-navigation-fastlio-gpl"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron2-navigation-fastlio-gpl.json"/></a></td>
    </tr>
    <tr></tr>
    <tr>
        <td rowspan="7" class="font-weight-bold">Oli</td>
        <td align="center" >Description</td>
        <td align="center" ><a href="https://github.com/limxdynamics/humanoid-description"> humanoid-description </a></td>
        <td> Robot model files, including URDF, USD, and XML model files. Can be used for simulation, training, etc. </td>
        <td><a href="https://github.com/limxdynamics/humanoid-description"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__humanoid-description.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Simulation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/humanoid-mujoco-sim"> humanoid-mujoco-sim </a></td>
        <td> A <a href="https://mujoco.org"> MuJoCo </a> simulation tool for the Oli robot that supports quick Sim-to-Real validation and deployment of robot algorithms. </td>
        <td><a href="https://github.com/limxdynamics/humanoid-mujoco-sim"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__humanoid-mujoco-sim.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Training</td>
        <td align="center" ><a href="https://github.com/limxdynamics/humanoid-rl-isaaclab"> humanoid-rl-isaaclab </a></td>
        <td> A reinforcement learning training framework designed specifically for Oli humanoid robots, built on <a href="https://isaac-sim.github.io/IsaacLab/"> Isaac Lab </a>, providing comprehensive tools for simulation and training, and supporting sim-to-real locomotion. </td>
        <td><a href="https://github.com/limxdynamics/humanoid-rl-isaaclab"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__humanoid-rl-isaaclab.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/humanoid-rl-deploy-python"> humanoid-rl-deploy-python </a></td>
        <td> A Python-based reinforcement learning deployment algorithm that streamlines the process of deploying trained models on Oli robots. </td>
        <td><a href="https://github.com/limxdynamics/humanoid-rl-deploy-python"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__humanoid-rl-deploy-python.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/humanoid-rl-deploy-cpp"> humanoid-rl-deploy-cpp </a></td>
        <td> A lightweight C++ algorithm framework that enables rapid deployment of trained models when ROS1/ROS2 is not required. </td>
        <td><a href="https://github.com/limxdynamics/humanoid-rl-deploy-cpp"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__humanoid-rl-deploy-cpp.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/humanoid-rl-deploy-ros2"> humanoid-rl-deploy-ros2 </a></td>
        <td> A reinforcement learning deployment framework based on <a href="https://www.ros.org">ROS2</a> that enables rapid deployment of trained models on Oli robots. </td>
        <td><a href="https://github.com/limxdynamics/humanoid-rl-deploy-ros2"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__humanoid-rl-deploy-ros2.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/humanoid-rl-deploy-ros"> humanoid-rl-deploy-ros </a></td>
        <td> A reinforcement learning deployment framework based on <a href="https://www.ros.org">ROS1</a> that enables rapid deployment of trained models on Oli robots. </td>
        <td><a href="https://github.com/limxdynamics/humanoid-rl-deploy-ros"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__humanoid-rl-deploy-ros.json"/></a></td>
    </tr>
    <tr></tr>
    <tr>
        <td rowspan="3" class="font-weight-bold">Luna</td>
        <td align="center" >Description</td>
        <td align="center" ><a href="https://github.com/limxdynamics/luna-description"> luna-description </a></td>
        <td> Robot model files for the LimX Luna humanoid — URDF, MuJoCo MJCF, and NVIDIA USD (closed-loop variant) for simulation, visualization, and downstream tooling. </td>
        <td><a href="https://github.com/limxdynamics/luna-description"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__luna-description.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Algorithm</td>
        <td align="center" ><a href="https://github.com/limxdynamics/luna-beyondmimic"> luna-beyondmimic </a></td>
        <td> A BeyondMimic-based whole-body motion learning framework that teaches the LimX Luna humanoid to dance — from human dance motions to deployable policies on Isaac Lab. </td>
        <td><a href="https://github.com/limxdynamics/luna-beyondmimic"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__luna-beyondmimic.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Algorithm</td>
        <td align="center" ><a href="https://github.com/limxdynamics/GMR"> GMR </a></td>
        <td> LimX Dynamics fork of GMR (General Motion Retargeting) — retarget human motion (SMPL-X/BVH/Xsens/OptiTrack) into LimX humanoids (OLI EDU, Luna) and 17+ other robots in real time on CPU. </td>
        <td><a href="https://github.com/limxdynamics/GMR"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__GMR.json"/></a></td>
    </tr>
    <tr>
        <td rowspan="12" class="font-weight-bold">TRON1</td>
        <td align="center" >Description</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-robot-description"> tron1-robot-description </a></td>
        <td> Robot model files for TRON1 variants, including URDF/xacro, MuJoCo XML, and meshes for point-foot and wheel-legged robots. </td>
        <td><a href="https://github.com/limxdynamics/tron1-robot-description"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-robot-description.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Simulation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-gazebo-ros"> tron1-gazebo-ros </a></td>
        <td> A <a href="https://www.ros.org"> ROS1-based </a> simulation tool for the TRON1 robot that supports quick Sim-to-Real validation and deployment of robot algorithms. </td>
        <td><a href="https://github.com/limxdynamics/tron1-gazebo-ros"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-gazebo-ros.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Simulation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-gazebo-ros2"> tron1-gazebo-ros2 </a></td>
        <td> A <a href="https://www.ros.org"> ROS2-based </a> simulation tool for the TRON1 robot that supports quick Sim-to-Real validation and deployment of robot algorithms. </td>
        <td><a href="https://github.com/limxdynamics/tron1-gazebo-ros2"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-gazebo-ros2.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Simulation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-mujoco-sim"> tron1-mujoco-sim </a></td>
        <td> A <a href="https://mujoco.org"> MuJoCo </a> simulation tool for the TRON1 robot that supports quick Sim-to-Real validation and deployment of robot algorithms. </td>
        <td><a href="https://github.com/limxdynamics/tron1-mujoco-sim"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-mujoco-sim.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Training</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-rl-isaaclab"> tron1-rl-isaaclab </a></td>
        <td> A reinforcement learning training framework designed specifically for TRON1 robots, 
        built on <a href="https://isaac-sim.github.io/IsaacLab/"> Isaac Lab </a>, providing comprehensive tools for simulation and training, and supporting reinforcement learning in various environments. </td>
        <td><a href="https://github.com/limxdynamics/tron1-rl-isaaclab"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-rl-isaaclab.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Training</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-rl-isaacgym"> tron1-rl-isaacgym </a></td>
        <td> A reinforcement learning training framework designed specifically for TRON1 robots, 
        built on <a href="https://developer.nvidia.com/isaac-gym"> Isaac Gym </a>, providing comprehensive tools for simulation and training, and supporting reinforcement learning in various environments. </td>
        <td><a href="https://github.com/limxdynamics/tron1-rl-isaacgym"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-rl-isaacgym.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-rl-deploy-ros"> tron1-rl-deploy-ros </a></td>
        <td> A reinforcement learning deployment framework based on <a href="https://www.ros.org"> ROS1 </a> that helps you quickly deploy your trained models. </td>
        <td><a href="https://github.com/limxdynamics/tron1-rl-deploy-ros"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-rl-deploy-ros.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-rl-deploy-ros2"> tron1-rl-deploy-ros2 </a></td>
        <td> A reinforcement learning deployment framework based on <a href="https://www.ros.org"> ROS2 </a> that helps you quickly deploy your trained models. </td>
        <td><a href="https://github.com/limxdynamics/tron1-rl-deploy-ros2"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-rl-deploy-ros2.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-rl-deploy-python"> tron1-rl-deploy-python </a></td>
        <td> A reinforcement learning deployment algorithm that leverages Python to streamline the deployment of your trained models. </td>
        <td><a href="https://github.com/limxdynamics/tron1-rl-deploy-python"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-rl-deploy-python.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Deployment</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-rl-deploy-arm"> tron1-rl-deploy-arm </a></td>
        <td> A reinforcement learning deployment framework for TRON1 arm controllers based on ONNX runtime. </td>
        <td><a href="https://github.com/limxdynamics/tron1-rl-deploy-arm"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-rl-deploy-arm.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Navigation</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-ss"> tron1-ss </a></td>
        <td> A ROS Noetic-based SLAM and autonomous navigation stack for TRON1 robots, supporting LiDAR mapping, localization, and path planning. </td>
        <td><a href="https://github.com/limxdynamics/tron1-ss"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-ss.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Agent</td>
        <td align="center" ><a href="https://github.com/limxdynamics/tron1-agent"> tron1-agent </a></td>
        <td> Real-time voice interaction agent for Tron robots with LLM-powered dialogue, speech recognition (FunASR), TTS, tool calling, and task management. </td>
        <td><a href="https://github.com/limxdynamics/tron1-agent"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__tron1-agent.json"/></a></td>
    </tr>
    <tr></tr>
    <tr>
        <td rowspan="3" class="font-weight-bold">VLA</td>
        <td align="center" >Algorithm</td>
        <td align="center" ><a href="https://github.com/FluxVLA/FluxVLA"> FluxVLA </a></td>
        <td> All-in-one VLA engineering platform for embodied intelligence — from data collection to real-robot deployment. </td>
        <td><a href="https://github.com/FluxVLA/FluxVLA"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2FFluxVLA__FluxVLA.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Simulation</td>
        <td align="center" ><a href="https://github.com/FluxVLA/FluxBisim"> FluxBisim </a></td>
        <td> IsaacSim-based bimanual manipulation simulation for FluxVLA. </td>
        <td><a href="https://github.com/FluxVLA/FluxBisim"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2FFluxVLA__FluxBisim.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Algorithm</td>
        <td align="center" ><a href="https://github.com/FluxVLA/FluxDAgger"> FluxDAgger </a></td>
        <td> A model-decoupled DAgger pipeline for dual-arm robotic manipulation — human-in-the-loop data collection compatible with arbitrary VLA and reward models. </td>
        <td><a href="https://github.com/FluxVLA/FluxDAgger"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2FFluxVLA__FluxDAgger.json"/></a></td>
    </tr>
    <tr>
        <td rowspan="7" class="font-weight-bold">SDK & Tools</td>
        <td align="center" >SDK</td>
        <td align="center" ><a href="https://github.com/limxdynamics/limxsdk-lowlevel"> limxsdk-lowlevel </a></td>
        <td> Low-level SDK for direct robot communication (motors, sensors, real-time control), used by the simulation and deployment repos above. </td>
        <td><a href="https://github.com/limxdynamics/limxsdk-lowlevel"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__limxsdk-lowlevel.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Visualization</td>
        <td align="center" ><a href="https://github.com/limxdynamics/robot-visualization"> robot-visualization </a></td>
        <td> Real-time visualization tool for robot joint states, IMU, force sensors, and motion trajectories via RViz/PlotJuggler. </td>
        <td><a href="https://github.com/limxdynamics/robot-visualization"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__robot-visualization.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Bridge</td>
        <td align="center" ><a href="https://github.com/limxdynamics/ros1-bridger"> ros1-bridger </a></td>
        <td> ROS1 communication bridge (x86_64 & aarch64, Noetic) for connecting development machines to LimX robot networks. </td>
        <td><a href="https://github.com/limxdynamics/ros1-bridger"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__ros1-bridger.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Bridge</td>
        <td align="center" ><a href="https://github.com/limxdynamics/ros2-bridger"> ros2-bridger </a></td>
        <td> ROS2 communication bridge (x86_64 & aarch64, Foxy/Humble/Jazzy/Lyrical) for connecting development machines to LimX robot networks. </td>
        <td><a href="https://github.com/limxdynamics/ros2-bridger"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__ros2-bridger.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Tool</td>
        <td align="center" ><a href="https://github.com/limxdynamics/robot-joystick"> robot-joystick </a></td>
        <td> Cross-platform virtual joystick for simulation and real-robot manual control. </td>
        <td><a href="https://github.com/limxdynamics/robot-joystick"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__robot-joystick.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >CLI</td>
        <td align="center" ><a href="https://github.com/limxdynamics/limx-cli"> limx-cli </a></td>
        <td> CLI tool and Scratch visual programming bridge for LimX robots, with JSON output for AI Agent integration. </td>
        <td><a href="https://github.com/limxdynamics/limx-cli"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__limx-cli.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >CLI</td>
        <td align="center" ><a href="https://github.com/limxdynamics/gradmotion-cli"> gradmotion-cli </a></td>
        <td> CLI tool for GradMotion whole-body motion generation on LimX robots with AI Agent integration support. </td>
        <td><a href="https://github.com/limxdynamics/gradmotion-cli"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__gradmotion-cli.json"/></a></td>
    </tr>
    <tr></tr>
    <tr>
        <td rowspan="3" class="font-weight-bold">TronCamp</td>
        <td align="center" >Event</td>
        <td align="center" ><a href="https://github.com/limxdynamics/troncamp-mani"> troncamp-mani </a></td>
        <td> TronCamp ACT 4-task contestant kit — self-contained package (Tron2 dual-arm / RoboTwin / single-GPU ACT) with setup, starter, and eval for four increasingly difficult manipulation tasks. </td>
        <td><a href="https://github.com/limxdynamics/troncamp-mani"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__troncamp-mani.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Web</td>
        <td align="center" ><a href="https://github.com/limxdynamics/troncamp-web-mani"> troncamp-web-mani </a></td>
        <td> TronCamp hackathon public site with task briefs, T1-T4 freedom ladder, in-process evaluation, and token-anonymous leaderboard. </td>
        <td><a href="https://github.com/limxdynamics/troncamp-web-mani"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__troncamp-web-mani.json"/></a></td>
    </tr>
    <tr>
        <td align="center" >Web</td>
        <td align="center" ><a href="https://github.com/limxdynamics/troncamp-web-locomotion"> troncamp-web-locomotion </a></td>
        <td> TronCamp locomotion track web companion for the TRON2 robot. </td>
        <td><a href="https://github.com/limxdynamics/troncamp-web-locomotion"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__troncamp-web-locomotion.json"/></a></td>
    </tr>
    <tr></tr>
    <tr>
        <td rowspan="1" class="font-weight-bold">Profile</td>
        <td align="center" >Profile</td>
        <td align="center" ><a href="https://github.com/limxdynamics/limxdynamics/tree/main"> limxdynamics </a></td>
        <td> GitHub profile page for LimX Dynamics — this README overview plus auto-updating total-star / forks growth charts. </td>
        <td><a href="https://github.com/limxdynamics/limxdynamics"><img alt="Stars" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Flimxdynamics%2Flimxdynamics%2Fmain%2Fbadges%2Frepos%2Flimxdynamics__limxdynamics.json"/></a></td>
    </tr>
    </tbody>
</table>