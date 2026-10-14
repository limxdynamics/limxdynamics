# [English](quick-start.md) | 中文

# 快速上手：在仿真里让 LimX 机器人走起来

LimX 各条技术栈都是同一个结构：**MuJoCo 仿真器**和 **RL 控制器**是两个进程，通过 LimX SDK（[limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel)）在 `127.0.0.1` 上通信；把这个地址换成机器人 IP 就是真机部署。本文带你在仿真里跑起一个训练好的策略——不需要机器人，也不需要 GPU。

- [环境要求](#环境要求)
- [TRON1](#tron1) —— [Linux](#tron1-linux) · [Windows](#tron1-windows)
- [TRON2](#tron2) —— [Linux](#tron2-linux) · [Windows](#tron2-windows)
- [Oli](#oli)
- [下一步](../README_cn.md#2-下一步)

## 环境要求

- Linux（x86_64 / aarch64）或 Windows 10/11 x64
- **Python 3.10–3.12**。TRON1 的 SDK 要求 `numpy<1.26.4`，这个版本没有 Python 3.13 的 Windows 安装包。
- ARM Linux 把 wheel 路径里的 `amd64` 换成 `aarch64`。

## TRON1

### TRON1 Linux

```bash
git clone --recurse-submodules https://github.com/limxdynamics/tron1-mujoco-sim
git clone https://github.com/limxdynamics/tron1-rl-deploy-python

python3 -m venv ~/.venvs/limx-tron1 && source ~/.venvs/limx-tron1/bin/activate
# SDK wheel 会一并装上 mujoco、onnxruntime、scipy、pyyaml、pygame
pip install tron1-mujoco-sim/limxsdk-lowlevel/python3/amd64/limxsdk-*-py3-none-any.whl
```

```bash
# 终端 1 —— 仿真器
source ~/.venvs/limx-tron1/bin/activate
export ROBOT_TYPE=PF_TRON1A        # PF_* 点足，SF_* 双足（足底），WF_* 轮足；完整列表见 tron1-mujoco-sim/robot-description/pointfoot/
python tron1-mujoco-sim/simulator.py

# 终端 2 —— RL 控制器（仓库自带训练好的 ONNX 策略）
source ~/.venvs/limx-tron1/bin/activate
export ROBOT_TYPE=PF_TRON1A        # 必须和仿真器一致
export RL_TYPE=isaaclab            # 自带策略来自哪个训练框架：isaaclab | isaacgym
python tron1-rl-deploy-python/main.py

# 终端 3（可选）—— 虚拟手柄，用来下发速度指令
./tron1-mujoco-sim/robot-joystick/robot-joystick
```

> 仿真器一启动机器人就会倒地，因为此时还没有控制器驱动关节。等控制器跑起来后，在 MuJoCo 窗口按 **Backspace** 重置，机器人就会站起来原地踏步。

### TRON1 Windows

使用 PowerShell。SDK wheel 在 `python3\win\` 下。

```powershell
git clone --recurse-submodules https://github.com/limxdynamics/tron1-mujoco-sim
git clone https://github.com/limxdynamics/tron1-rl-deploy-python

py -3.12 -m venv $HOME\.venvs\limx-tron1
& $HOME\.venvs\limx-tron1\Scripts\Activate.ps1   # 若被拦截：Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
# PowerShell 不会为 pip 展开 *，先取出 wheel 的完整路径
pip install (Get-ChildItem tron1-mujoco-sim\limxsdk-lowlevel\python3\win\limxsdk-*.whl).FullName
```

```powershell
# 终端 1 —— 仿真器
& $HOME\.venvs\limx-tron1\Scripts\Activate.ps1
$env:ROBOT_TYPE = "PF_TRON1A"
python tron1-mujoco-sim\simulator.py

# 终端 2 —— RL 控制器
& $HOME\.venvs\limx-tron1\Scripts\Activate.ps1
$env:ROBOT_TYPE = "PF_TRON1A"; $env:RL_TYPE = "isaaclab"
python tron1-rl-deploy-python\main.py

# 终端 3（可选）—— 虚拟手柄
.\tron1-mujoco-sim\robot-joystick\robot-joystick.exe
```

同样，倒地后按 Backspace 重置。

## TRON2

仿真器和控制器用的 SDK 版本不同，各开一个 venv。

```bash
git clone --recurse-submodules https://github.com/limxdynamics/tron2_mujoco_sim
git clone --recurse-submodules https://github.com/limxdynamics/tron2_rl_deploy_python
```

### TRON2 Linux

```bash
# 终端 1 —— 仿真器
python3 -m venv ~/.venvs/limx-tron2-sim && source ~/.venvs/limx-tron2-sim/bin/activate
pip install "mujoco>=3.2.2" "pyyaml>=6.0"
pip install --no-deps tron2_mujoco_sim/limxsdk-lowlevel/python3/amd64/limxsdk-*.whl
export ROBOT_TYPE=SF_TRON2A        # 也支持 WF_TRON2A、DASF_TRON2A
python tron2_mujoco_sim/simulator.py

# 终端 2 —— RL 控制器
python3 -m venv ~/.venvs/limx-tron2-ctl && source ~/.venvs/limx-tron2-ctl/bin/activate
pip install numpy scipy pyyaml onnxruntime pygame
pip install tron2_rl_deploy_python/limxsdk-lowlevel/python3/amd64/limxsdk-*.whl
export ROBOT_TYPE=SF_TRON2A
python tron2_rl_deploy_python/main.py
```

### TRON2 Windows

使用 PowerShell。仿真器自带的 Windows 版 SDK 只支持 `SF_TRON2A` 和 `WF_TRON2A`，`DASF_TRON2A` 需要用 Linux。

```powershell
# 终端 1 —— 仿真器
py -3.12 -m venv $HOME\.venvs\limx-tron2-sim
& $HOME\.venvs\limx-tron2-sim\Scripts\Activate.ps1
pip install "mujoco>=3.2.2" "pyyaml>=6.0"
pip install --no-deps (Get-ChildItem tron2_mujoco_sim\limxsdk-lowlevel\python3\win\limxsdk-*.whl).FullName
$env:ROBOT_TYPE = "SF_TRON2A"
python tron2_mujoco_sim\simulator.py

# 终端 2 —— RL 控制器
py -3.12 -m venv $HOME\.venvs\limx-tron2-ctl
& $HOME\.venvs\limx-tron2-ctl\Scripts\Activate.ps1
pip install numpy scipy pyyaml onnxruntime pygame
pip install (Get-ChildItem tron2_rl_deploy_python\limxsdk-lowlevel\python3\win\limxsdk-*.whl).FullName
$env:ROBOT_TYPE = "SF_TRON2A"
python tron2_rl_deploy_python\main.py
```

### 操控 TRON2

控制器启动后处于 `IDLE`，用手柄操作。罗技 F710（X 模式）会被直接读取；没有实体手柄时，在第三个终端运行虚拟手柄（`./tron2_mujoco_sim/robot-joystick/robot-joystick`，Windows 上是 `robot-joystick.exe`）。然后：

1. `L1 + ○ (B)` —— 关节回到默认姿态。
2. 在 MuJoCo 窗口按 **R** —— 把倒地的机身扶正（保留关节角）。
3. `L1 + △ (Y)` —— 开始行走，左摇杆控制速度；`L1 + × (A)` 停止。

## Oli

对应的是 [humanoid-mujoco-sim](https://github.com/limxdynamics/humanoid-mujoco-sim) + [humanoid-rl-deploy-python](https://github.com/limxdynamics/humanoid-rl-deploy-python)，`ROBOT_TYPE=HU_D04_01`，按各自 README 操作即可。
