# English | [中文](quick-start_cn.md)

# Quick Start: walk a LimX robot in simulation

Every LimX stack follows the same pattern: a **MuJoCo simulator** and an **RL controller** run as two processes and talk through the LimX SDK ([limxsdk-lowlevel](https://github.com/limxdynamics/limxsdk-lowlevel)) on `127.0.0.1`. To go from simulation to a real robot, you only change that address. This guide gets a trained policy walking in simulation — no robot and no GPU needed.

- [Requirements](#requirements)
- [TRON1](#tron1) — [Linux](#tron1-on-linux) · [Windows](#tron1-on-windows)
- [TRON2](#tron2) — [Linux](#tron2-on-linux) · [Windows](#tron2-on-windows)
- [Oli](#oli)
- [Where to go next](../README.md#2-where-to-go-next)

## Requirements

- Linux (x86_64 / aarch64) or Windows 10/11 x64
- **Python 3.10–3.12.** The TRON1 SDK requires `numpy<1.26.4`, which has no Windows wheel for Python 3.13.
- On ARM Linux, replace `amd64` with `aarch64` in the wheel paths.

## TRON1

### TRON1 on Linux

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

### TRON1 on Windows

PowerShell. The SDK wheels live in `python3\win\`.

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

The same Backspace reset applies.

## TRON2

The simulator and the controller use different SDK builds, so each gets its own venv.

```bash
git clone --recurse-submodules https://github.com/limxdynamics/tron2_mujoco_sim
git clone --recurse-submodules https://github.com/limxdynamics/tron2_rl_deploy_python
```

### TRON2 on Linux

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

### TRON2 on Windows

PowerShell. The simulator's Windows SDK build supports `SF_TRON2A` and `WF_TRON2A` only; `DASF_TRON2A` needs Linux.

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

### Driving TRON2

The controller starts in `IDLE` and is driven by a gamepad. A Logitech F710 (X mode) is read directly; without one, run the virtual gamepad in a third terminal (`./tron2_mujoco_sim/robot-joystick/robot-joystick`, or `robot-joystick.exe` on Windows). Then:

1. `L1 + ○ (B)` — move the joints to the default pose.
2. Press **R** in the MuJoCo window — put the fallen base back upright (joint angles are kept).
3. `L1 + △ (Y)` — start walking; the left stick sets velocity. `L1 + × (A)` stops.

## Oli

The pair is [humanoid-mujoco-sim](https://github.com/limxdynamics/humanoid-mujoco-sim) + [humanoid-rl-deploy-python](https://github.com/limxdynamics/humanoid-rl-deploy-python) with `ROBOT_TYPE=HU_D04_01`; follow their READMEs.
