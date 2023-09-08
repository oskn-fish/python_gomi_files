from ray.rllib.algorithms.ppo import PPOConfig
from ray.tune.logger import pretty_print
import os

checkpoint_path = os.path.join(os.path.dirname(__file__), "checkpoint_rllib")


algo = (
    PPOConfig()
    .rollouts(num_rollout_workers=1)
    .resources(num_gpus=0)
    .environment(env="CartPole-v1")
    .framework("torch")
    .build()
)

for i in range(10):
    result = algo.train()
    print(pretty_print(result))

    if i % 5 == 0:
        checkpoint_dir = algo.save(checkpoint_path)
        print(f"Checkpoint saved in directory {checkpoint_dir}")