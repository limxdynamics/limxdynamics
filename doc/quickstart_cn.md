# 快速上手

[English](quickstart.md) · [返回首页](../README_cn.md)

LimX 各条技术栈都是同一个结构：**MuJoCo 仿真器**和 **RL 控制器**是两个进程，通过 LimX SDK（[limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel)）在 `127.0.0.1` 上通信；把这个地址换成机器人 IP 就是真机部署。所以最快的入门方式，就是先在仿真里看一个训练好的策略走起来——不需要机器人，也不需要 GPU。

## 1. 在仿真里让机器人走起来（约 10 分钟）

以下为 TRON1 + Linux x86_64，Python 3.10–3.12。

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

## 2. 下一步

| 我想… | 从这里开始 |
|---|---|
| 训练自己的运动策略（Isaac Lab，需 NVIDIA GPU） | TRON1：[tron1-rl-isaaclab](https://github.com/limxdynamics/tron1-rl-isaaclab)，任务 `Isaac-Limx-{PF,SF,WF}-Blind-Flat-v0`<br>TRON2：[tron2_rl_lab](https://github.com/limxdynamics/tron2_rl_lab)，任务 `Isaac-Limx-{SF,WF,DASF}-TRON2A-Blind-Flat-v0`<br>Oli：[humanoid-rl-isaaclab](https://github.com/limxdynamics/humanoid-rl-isaaclab) |
| 在真机上跑策略 | 用上面同一个控制器，指向机器人：`python main.py <robot-ip>`。先把机器人吊起来，并阅读对应仓库的安全说明。 |
| 在 ROS / ROS 2 里部署 | `*-rl-deploy-ros` / `*-rl-deploy-ros2` 仓库，以及 [ros1-bridger](https://github.com/limxdynamics/ros1-bridger) / [ros2-bridger](https://github.com/limxdynamics/ros2-bridger) |
| 写自己的控制器 | [limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel) 里的 SDK 示例（C++ 和 Python） |
| 在 TRON2 上做操作 / VLA | [tron2_manipulation_controller](https://github.com/limxdynamics/tron2_manipulation_controller)（仿真 + SDK）、[tron2_openpi](https://github.com/limxdynamics/tron2_openpi) + [tron2_env](https://github.com/limxdynamics/tron2_env)（真机运行 pi0/pi0.5）、[FluxVLA](https://github.com/FluxVLA/FluxVLA) |
| 看一个完整的视觉抓取 demo 跑起来 | [tron2_visual_grasp](https://github.com/limxdynamics/tron2_visual_grasp)：TRON2 的网球抓取闭环（发现 → 驶近 → 下蹲 → 抓取），纯 OpenCV、纯 CPU，无硬件也能跑（`./run.sh demo`） |
| 把人体动作重定向到人形机器人 | [GMR](https://github.com/limxdynamics/GMR) → [luna-beyondmimic](https://github.com/limxdynamics/luna-beyondmimic) |
| 不写代码，只关注行业动态 | [embodied-ai-insights](https://github.com/limxdynamics/embodied-ai-insights) 月度报告 |

完整项目清单：[首页 README](../README_cn.md#开源项目)
