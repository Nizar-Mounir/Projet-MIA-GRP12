import os
from gpu_task_scheduler.gpu_task_scheduler import GPUTaskScheduler
from trainShadowModel import ShadowGANTask
from shadow_config import config  # Assuming config is stored in shadow_config.py

if __name__ == "__main__":
    # Initialize and start the task scheduler
    scheduler = GPUTaskScheduler(config=config, gpu_task_class=ShadowGANTask)
    scheduler.start()
