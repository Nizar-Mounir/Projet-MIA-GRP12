import os
config = {
    "scheduler_config": {
        "gpu": ["0"],
        "config_string_value_maxlen": 1000,
        "result_root_folder": os.path.join("data", "shadow34"),
        "scheduler_log_file_path": "scheduler_generate_data.log",
        "log_file": "worker_generate_data.log",
        "force_rerun": True
    },
    "global_config": {
        "batch_size": 200,
        "vis_freq": 200,
        "vis_num_sample": 5,
        "d_rounds": 1,
        "g_rounds": 1,
        "num_packing": 1,
        "noise": False,
        "feed_back": True,
        "g_lr": 0.006,
        "d_lr": 0.005,
        "d_gp_coe": 15.0,
        "gen_feature_num_layers": 4,
        "gen_feature_num_units": 50,
        "gen_attribute_num_layers": 1,
        "gen_attribute_num_units": 1,
        "disc_num_layers": 4,
        "disc_num_units": 50,
        "initial_state": "random",
        "attr_d_lr": 0.001,
        "attr_d_gp_coe": 10.0,
        "g_attr_d_coe": 4.0,
        "attr_disc_num_layers": 1,
        "attr_disc_num_units": 2,
        
        "generate_num_train_sample": 10000,
        "generate_num_test_sample": 10000
    },
    "test_config": [
        {   
            "dataset": [f"shadow{i}"],
            "shadow_id": [i],
            "epoch": [1000],
            "run": [0],
            "sample_len": [7],
            "extra_checkpoint_freq": [50],
            "epoch_checkpoint_freq": [50],
            "aux_disc": [False],
            "self_norm": [False]
        } for i in range(1, 27)
    ]

}
