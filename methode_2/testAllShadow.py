if __name__ == "__main__":
    from pathlib import Path
    from shadow_config import config 
    from gpu_task_scheduler.gpu_task_scheduler import GPUTaskScheduler
    from testShadowModel import ShadowGANGenerateTask
    import os
    
    scheduler = GPUTaskScheduler(
        config=config, gpu_task_class=ShadowGANGenerateTask)
    scheduler.start()
    Path(os.path.join("data",".time")).touch()