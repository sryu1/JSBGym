import gymnasium as gym
import enum
from jsbgym.tasks import Task, HeadingControlTask, TurnHeadingControlTask
from jsbgym.aircraft import Aircraft, cessna172P
from jsbgym import utils

"""
This script registers all combinations of task, aircraft, shaping settings
 etc. with OpenAI Gym so that they can be instantiated with a gym.make(id)
 command.

The jsbgym.Envs enum stores all registered environments as members with
 their gym id string as value. This allows convenient autocompletion and value
 safety. To use do:
       env = gym.make(jsbgym.Envs.desired_environment.value)
"""

for env_id, (
    task,
    plane,
    shaping,
    enable_flightgear,
) in utils.get_env_id_kwargs_map().items():
    if enable_flightgear:
        entry_point = "jsbgym.environment:JsbSimEnv"
    else:
        entry_point = "jsbgym.environment:NoFGJsbSimEnv"
    kwargs = dict(task_type=task, aircraft=plane, shaping=shaping)
    gym.envs.registration.register(id=env_id, entry_point=entry_point, kwargs=kwargs)

# make an Enum storing every JSBGym environment ID for convenience and value safety
Envs = enum.Enum.__call__(
    "Envs",
    [
        (utils.AttributeFormatter.translate(env_id), env_id)
        for env_id in utils.get_env_id_kwargs_map().keys()
    ],
)
