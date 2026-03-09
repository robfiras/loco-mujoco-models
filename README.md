# loco-mujoco-models

Robot XML and asset files for [LocoMuJoCo](https://github.com/robfiras/loco-mujoco).

**MyoSkeleton (myo_model)** is not included in this repo for licensing reasons. To use MyoSkeleton, run the separate installer after accepting the license:

```bash
loco-mujoco-myomodel-init
```

That will clone the MyoSkeleton model into your LocoMuJoCo models path.

## Acknowledgements

This repository bundles several third‑party robot models. Many subdirectories in `loco_mujoco_models/` contain their own `LICENSE` (and/or `README`) files; please refer to those for full terms. The models originate from, or are based on, the following projects:

- `loco_mujoco_models/unitree_h1_2`: **Unitree H1** humanoid model from the **MuJoCo Menagerie**, originally provided by **Unitree Robotics** under a BSD‑3‑Clause license.
- `loco_mujoco_models/unitree_go2`: **Unitree Go2** quadruped model from the **MuJoCo Menagerie**, based on assets provided by **Unitree Robotics**.
- `loco_mujoco_models/unitree_a1`: **Unitree A1** quadruped model based on publicly available Unitree A1 descriptions and community MuJoCo models, for example `illusoryTwin/mujoco_unitree_a1`.
- `loco_mujoco_models/unitree_g1`: **Unitree G1** humanoid model from the **MuJoCo Menagerie**, originally provided by **Unitree Robotics** under a BSD‑style license.
- `loco_mujoco_models/bd_spot`: **Boston Dynamics Spot** quadruped model based on Clearpath’s Spot URDF and the **MuJoCo Menagerie** Spot model, licensed under BSD‑3‑Clause by **Clearpath Robotics Inc.**
- `loco_mujoco_models/anybotics_anymal_c`: **ANYmal C** quadruped model from the **MuJoCo Menagerie**, derived from the public URDF provided by **ANYbotics AG**.
- `loco_mujoco_models/talos`: **TALOS** humanoid model from the **MuJoCo Menagerie**, representing the TALOS robot developed by **PAL Robotics** (Apache‑2.0).
- `loco_mujoco_models/booster_t1`: **Booster T1** humanoid model as distributed via the **MuJoCo Menagerie** / Google DeepMind resources for the Booster Robotics platform.
- `loco_mujoco_models/apptronik_apollo`: **Apollo** humanoid model from the **MuJoCo Menagerie**, originally provided by **Apptronik** under the Apache‑2.0 license.
- `loco_mujoco_models/toddlerbot`: **ToddlerBot** open‑source humanoid model from the **ToddlerBot** project (`hshi74/toddlerbot`, MIT license).
- `loco_mujoco_models/fourier_gr1t2`: **Fourier GR1T2** humanoid model from **Fourier Intelligence** GR‑series MuJoCo resources (e.g. `FFTAI/Wiki-GRx-Mujoco`, MIT license).
