# 快速上手

[English](quickstart.md) · [返回首页](../README_cn.md)

LimX 各条技术栈都是同一个结构：**MuJoCo 仿真器**和 **RL 控制器**是两个进程，通过 LimX SDK（[limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel)）在 `127.0.0.1` 上通信；把这个地址换成机器人 IP 就是真机部署。所以最快的入门方式，就是先在仿真里看一个训练好的策略跑起来——不需要机器人，也不需要 GPU。

<p align="center"><a href="https://github.com/limxdynamics/limxdynamics/blob/main/doc/wechat_qr.png"><img src="https://img.shields.io/badge/%E5%BE%AE%E4%BF%A1%E5%BC%80%E5%8F%91%E8%80%85%E7%BE%A4-%E6%89%AB%E7%A0%81%E5%8A%A0%E5%85%A5%20%C2%B7%20%E8%A6%86%E7%9B%96%E5%85%A8%E9%83%A8%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE-07C160?style=for-the-badge&logo=wechat&logoColor=white" alt="微信开发者社区"></a></p>

## 选择你的机器人

| 机型 | 简介 | 没有机器人也能试 |
|---|---|---|
| [**TRON1**](#tron1) | 双足机器人，有点足、足底、轮足三种形态 | 在 MuJoCo 里让它走起来（约 10 分钟） |
| [**TRON2**](#tron2) | 模块化机器人：足底或轮足双足、双臂，以及 DASF 人形组合形态；分 TRON2A 和 TRON2B | 在 MuJoCo 里让它走起来 |
| [**Oli**（HU_D04）](#oli) | 全尺寸人形机器人，31 个关节 | 在 MuJoCo 里站立、挥手、行走 |
| [**Luna**（HU_L04）](#luna) | 人形机器人，27 个关节，可做跳舞等全身动作 | 30 秒看模型；动作训练需要 NVIDIA GPU |

<a id="tron1"></a>

## TRON1

### 在仿真里让它走起来（约 10 分钟）

Linux x86_64，Python 3.10–3.12。

```bash
git clone --recurse-submodules https://github.com/limxdynamics/tron1-mujoco-sim
git clone https://github.com/limxdynamics/tron1-rl-deploy-python

python3 -m venv ~/.venvs/limx-tron1 && source ~/.venvs/limx-tron1/bin/activate
# SDK wheel 会一并装上 mujoco、onnxruntime、scipy、pyyaml、pygame
pip install tron1-mujoco-sim/limxsdk-lowlevel/python3/amd64/limxsdk-*.whl
```

```bash
# 终端 1 —— 仿真器
source ~/.venvs/limx-tron1/bin/activate
export ROBOT_TYPE=PF_TRON1A        # PF_* 点足，SF_* 双足（足底），WF_* 轮足
python tron1-mujoco-sim/simulator.py

# 终端 2 —— RL 控制器（仓库自带训练好的 ONNX 策略）
source ~/.venvs/limx-tron1/bin/activate
export ROBOT_TYPE=PF_TRON1A RL_TYPE=isaaclab
python tron1-rl-deploy-python/main.py
```

> 仿真器一启动机器人就会倒地。等控制器跑起来后，在 MuJoCo 窗口按 **Backspace**，机器人就会站起来原地踏步。运行 `./tron1-mujoco-sim/robot-joystick/robot-joystick` 可以用虚拟手柄操控它。

### 下一步

| 我想… | 从这里开始 |
|---|---|
| 训练自己的运动策略（需 NVIDIA GPU） | [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab)，任务 `Isaac-Limx-{PF,SF,WF}-Blind-Flat-v0`；已经在用 Isaac Gym 的可以用 [tron1-rl-isaacgym](https://github.com/limxdynamics/tron1-rl-isaacgym) |
| 在真机上跑策略 | 用同一个控制器，指向机器人：`python main.py <robot-ip>` |
| 在 ROS / ROS 2 里部署 | [tron1-rl-deploy-ros](https://github.com/limxdynamics/tron1-rl-deploy-ros) · [tron1-rl-deploy-ros2](https://github.com/limxdynamics/tron1-rl-deploy-ros2) |
| 建图、定位、导航 | [tron1-ss](https://github.com/limxdynamics/tron1-ss)（激光 SLAM 与路径规划） |
| 和机器人对话 | [tron1-agent](https://github.com/limxdynamics/tron1-agent)（语音指令与大模型对话） |

### 看看别人用 TRON1 做了什么

[Awesome LimX 的 TRON1 页面](https://github.com/limxdynamics/awesome-limx/blob/main/robots/TRON1_cn.md)汇总了基于 TRON1 的公开论文、代码、数据集、比赛方案和行业应用。可以先找一个和你方向接近的项目，从它的代码起步；标了「仿真」的只在仿真中展示过。自己做了项目？欢迎[提交收录](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)。

### TRON1 全部仓库

```
tron1-robot-description ──► tron1-rl-isaaclab / tron1-rl-isaacgym ──► ONNX 策略 ──► tron1-mujoco-sim ──► tron1-rl-deploy-{ros, ros2, python} ──► TRON1
      （机器人模型）                    （训练）                                     （sim-to-sim 验证）           （在真机上运行）
```

| 阶段 | 仓库 | 作用 |
|---|---|---|
| 机器人模型 | [tron1-robot-description](https://github.com/limxdynamics/tron1-robot-description) | 适用于 ROS 1/2、MuJoCo 和 Gazebo 的 URDF / Xacro / MJCF 模型 |
| 仿真 | [tron1-mujoco-sim](https://github.com/limxdynamics/tron1-mujoco-sim) | MuJoCo 仿真器，接口与真机的 `limxsdk` 相同 |
| 仿真 | [tron1-gazebo-ros](https://github.com/limxdynamics/tron1-gazebo-ros) · [tron1-gazebo-ros2](https://github.com/limxdynamics/tron1-gazebo-ros2) | 基于 ROS Noetic · ROS 2 Iron 的 Gazebo 仿真 |
| 训练 | [tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab) | 基于 Isaac Lab 的强化学习训练，新项目推荐使用 |
| 训练 | [tron1-rl-isaacgym](https://github.com/limxdynamics/tron1-rl-isaacgym) | 基于 Isaac Gym 的强化学习训练 |
| 部署 | [tron1-rl-deploy-python](https://github.com/limxdynamics/tron1-rl-deploy-python) | Python 部署，附带预训练策略 |
| 部署 | [tron1-rl-deploy-ros](https://github.com/limxdynamics/tron1-rl-deploy-ros) · [tron1-rl-deploy-ros2](https://github.com/limxdynamics/tron1-rl-deploy-ros2) | 基于 ROS Noetic · ROS 2 Iron 的部署 |
| 部署 | [tron1-rl-deploy-arm](https://github.com/limxdynamics/tron1-rl-deploy-arm) | 带机械臂 TRON1 的强化学习部署 |
| 应用 | [tron1-ss](https://github.com/limxdynamics/tron1-ss) | 激光雷达 SLAM 与导航：建图、定位、路径规划 |
| 应用 | [tron1-agent](https://github.com/limxdynamics/tron1-agent) | 语音交互 AI 智能体：语音指令、大模型对话、机器人动作 |

<a id="tron2"></a>

## TRON2

### 在仿真里让它走起来

Linux x86_64，Python 3.10+。仿真器使用 [uv](https://docs.astral.sh/uv/)（没有的话先运行 `curl -LsSf https://astral.sh/uv/install.sh | sh` 安装），机器人模型需要下载约 1.7 GB。

```bash
# 终端 1 —— 仿真器
git clone https://github.com/limxdynamics/tron2_mujoco_sim.git
cd tron2_mujoco_sim
git submodule update --init --depth 1 robot-description limxsdk-lowlevel robot-joystick
uv sync --extra sdk
ROBOT_TYPE=SF_TRON2A uv run simulator.py
```

```bash
# 终端 2 —— RL 控制器（仓库自带训练好的 ONNX 策略）
git clone --recurse-submodules https://github.com/limxdynamics/tron2_rl_deploy_python.git
cd tron2_rl_deploy_python
python3 -m venv ~/.venvs/limx-tron2 && source ~/.venvs/limx-tron2/bin/activate
pip install numpy scipy pyyaml onnxruntime pygame
pip install limxsdk-lowlevel/python3/amd64/limxsdk-*.whl
export ROBOT_TYPE=SF_TRON2A        # SF_TRON2A 足底，WF_TRON2A 轮足，DASF_TRON2A 带双臂；两个终端要一致
python3 main.py
```

> 控制器连上之前，机器人会先倒地。依次按 **L1 + B**（进入准备）、**L1 + Y**（启动），然后在 MuJoCo 窗口按 **Backspace**：机器人会以站立姿态重新开始，并保持平衡。左摇杆控制移动，右摇杆控制转向。
>
> 没有手柄的话，在第三个终端运行 `tron2_mujoco_sim/robot-joystick/robot-joystick` 打开虚拟手柄，在它的窗口里用键盘操作：**Q** 是 L1，**L** 是 B，**I** 是 Y，**方向键**是左摇杆。实体手柄请用罗技 F710（`X` 模式）。

### 下一步

| 我想… | 从这里开始 |
|---|---|
| 训练自己的运动策略（需 NVIDIA GPU） | [tron2_rl_lab](https://github.com/limxdynamics/tron2_rl_lab)，任务 `Isaac-Limx-{SF,WF,DASF}-TRON2A-Blind-Flat-v0`；6 自由度机械臂和夹爪版本用 [TRON2_YG_LAB](https://github.com/limxdynamics/TRON2_YG_LAB) |
| 在真机上跑策略 | 用同一个控制器，指向机器人：`python3 main.py <robot-ip>` |
| 在 ROS 里部署 | [tron2_rl_deploy_ros](https://github.com/limxdynamics/tron2_rl_deploy_ros)（ROS Noetic）· Gazebo 仿真：[tron2_gazebo_ros](https://github.com/limxdynamics/tron2_gazebo_ros) |
| 做操作 / VLA | [tron2_manipulation_controller](https://github.com/limxdynamics/tron2_manipulation_controller)（双臂仿真 + SDK）、[tron2_openpi](https://github.com/limxdynamics/tron2_openpi) + [tron2_env](https://github.com/limxdynamics/tron2_env)（真机运行 pi0/pi0.5）、[FluxVLA](https://github.com/FluxVLA/FluxVLA) |
| 看一个完整的视觉抓取 demo 跑起来 | [tron2_visual_grasp](https://github.com/limxdynamics/tron2_visual_grasp)：网球抓取闭环（发现 → 驶近 → 下蹲 → 抓取），纯 OpenCV、纯 CPU，无硬件也能跑（`./run.sh demo`） |
| 自主导航 | [tron2-navigation-ros2](https://github.com/limxdynamics/tron2-navigation-ros2)（ROS 2 Humble） |
| 获取机器人模型 | [tron2-robot-description](https://github.com/limxdynamics/tron2-robot-description)（TRON2A 和 TRON2B 的 URDF/xacro、MuJoCo XML、USD） |

### 看看别人用 TRON2 做了什么

[Awesome LimX 的 TRON2 页面](https://github.com/limxdynamics/awesome-limx/blob/main/robots/TRON2_cn.md)汇总了基于 TRON2 的公开论文、代码、数据集、比赛方案和行业应用。可以先找一个和你方向接近的项目，从它的代码起步；标了「仿真」的只在仿真中展示过。自己做了项目？欢迎[提交收录](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)。

<a id="oli"></a>

## Oli（HU_D04）

### 在仿真里站立、挥手、行走

Linux x86_64，Python 3.8+。

```bash
mkdir -p ~/limx_ws && cd ~/limx_ws
git clone --recurse-submodules https://github.com/limxdynamics/humanoid-mujoco-sim
git clone https://github.com/limxdynamics/humanoid-rl-deploy-python

python3 -m venv ~/.venvs/limx-oli && source ~/.venvs/limx-oli/bin/activate
pip install -r humanoid-mujoco-sim/requirements.txt
# 控制器需要 click，但 SDK wheel 不会自动安装它
pip install humanoid-mujoco-sim/limxsdk-lowlevel/python3/amd64/limxsdk-*.whl click
```

```bash
# 每个终端先执行：cd ~/limx_ws && source ~/.venvs/limx-oli/bin/activate && export ROBOT_TYPE=HU_D04_01
python humanoid-mujoco-sim/simulator.py            # 终端 1 —— 仿真器
python humanoid-rl-deploy-python/main.py           # 终端 2 —— RL 控制器
humanoid-mujoco-sim/robot-joystick/robot-joystick  # 终端 3 —— 虚拟手柄
```

> 控制器连上之前，机器人会先倒地。在虚拟手柄窗口里按住 **Q**（L1）再按 **I**（Y）切换到站立，等几秒，然后在 MuJoCo 窗口点 **Reset**：机器人会以站立姿态重新开始。站稳后，**Q + L**（L1 + B）挥手，**U + J**（R1 + X）切换到行走，**方向键**控制方向。
>
> 人形仿真对电脑性能要求较高，建议用多核、性能较好的电脑。如果机器人反复摔倒，多半是仿真跑得比真实时间慢：关掉其他程序，切回站立，等几秒，再点一次 **Reset**。

### 下一步

| 我想… | 从这里开始 |
|---|---|
| 训练自己的运动策略（需 NVIDIA GPU） | [humanoid-rl-isaaclab](https://github.com/limxdynamics/humanoid-rl-isaaclab) |
| 试试自己训练的行走策略 | 导出为 `policy.onnx`，放到 `humanoid-rl-deploy-python/controllers/HU_D04_01/walk_controller/policy/default`，再按上面的步骤跑仿真 |
| 在真机上跑策略 | [humanoid-rl-deploy-python](https://github.com/limxdynamics/humanoid-rl-deploy-python) 的"真机调试"一节 |
| 在 ROS / ROS 2 里部署，或用纯 C++ | [humanoid-rl-deploy-ros](https://github.com/limxdynamics/humanoid-rl-deploy-ros) · [humanoid-rl-deploy-ros2](https://github.com/limxdynamics/humanoid-rl-deploy-ros2) · [humanoid-rl-deploy-cpp](https://github.com/limxdynamics/humanoid-rl-deploy-cpp) |
| 把人体动作重定向到 Oli | [GMR](https://github.com/limxdynamics/GMR)（机器人名 `limx_oli_edu`） |
| 获取机器人模型 | [humanoid-description](https://github.com/limxdynamics/humanoid-description)（URDF、MuJoCo MJCF、USD） |

### 看看别人用 Oli 做了什么

[Awesome LimX 的 Oli 页面](https://github.com/limxdynamics/awesome-limx/blob/main/robots/Oli_cn.md)汇总了基于 Oli 的公开论文、代码、数据集、比赛方案和行业应用。可以先找一个和你方向接近的项目，从它的代码起步；标了「仿真」的只在仿真中展示过。自己做了项目？欢迎[提交收录](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)。

<a id="luna"></a>

## Luna（HU_L04）

### 30 秒看到机器人

```bash
git clone https://github.com/limxdynamics/luna-description.git
cd luna-description
pip install mujoco
python -m mujoco.viewer --mjcf=HU_L04_description/xml/HU_L04_01.xml
```

> 没有控制器驱动，窗口一打开机器人就会瘫倒。按 **空格** 暂停，再按 **Backspace** 让它回到站立姿态。

### 教 Luna 学一段动作

```
人体动作（SMPL-X / BVH） ──►  GMR  ──►  动作 .npy  ──►  luna-beyondmimic  ──►  policy.onnx  ──►  Luna
                            （重定向）                   （训练，Isaac Lab）     + reference + param.yaml
```

- [luna-beyondmimic](https://github.com/limxdynamics/luna-beyondmimic) 在 Isaac Lab 上训练全身动作跟踪策略（需 NVIDIA GPU），并导出机器人运行所需的文件。仓库自带一段 22.9 秒的舞蹈动作，不用先做重定向就能把整条流程跑通。从它的 `QuickStart.md` 开始。
- [GMR](https://github.com/limxdynamics/GMR)（机器人名 `limx_luna`）把你自己的动捕或 SMPL-X 数据重定向到 Luna。
- [luna-description](https://github.com/limxdynamics/luna-description) 提供 URDF、MuJoCo MJCF 和 USD 模型。

### 看看别人用 Luna 做了什么

[Awesome LimX 的 Luna 页面](https://github.com/limxdynamics/awesome-limx/blob/main/robots/Luna_cn.md)汇总了基于 Luna 的公开论文、代码、数据集、比赛方案和行业应用。可以先找一个和你方向接近的项目，从它的代码起步；标了「仿真」的只在仿真中展示过。自己做了项目？欢迎[提交收录](https://github.com/limxdynamics/awesome-limx/issues/new?template=add-project.yml)。

## 所有机型通用

| 我想… | 从这里开始 |
|---|---|
| 写自己的控制器 | [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) 里的 SDK 示例（C++ 和 Python） |
| 跨机器桥接 ROS | [ros1-bridger](https://github.com/limxdynamics/ros1-bridger) · [ros2-bridger](https://github.com/limxdynamics/ros2-bridger) |
| 看看大家用 LimX 机器人做了什么，或收录我的项目 | [Awesome LimX](https://github.com/limxdynamics/awesome-limx/blob/main/README_cn.md)，每个机型一页 |
| 不写代码，只关注行业动态 | [embodied-ai-insights](https://github.com/limxdynamics/embodied-ai-insights) 月度报告 |

> **上真机之前：** 策略要先在仿真里验证通过；第一次在真机上运行时，先用吊架把机器人悬空吊起再启动；部署前请读一遍所用仓库里的安全说明。

完整项目清单：[首页 README](../README_cn.md#开源项目)
