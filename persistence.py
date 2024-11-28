import os
import json
import sys
from pathlib import Path

import typer

def get_executable_dir() -> str:
    """
    Get the directory of the executable, whether running as script or frozen executable
    """
    if getattr(sys, 'frozen', False):
        # PyInstaller 創建的執行檔
        return os.path.dirname(sys.executable)
    else:
        # 一般 Python 腳本
        return os.path.dirname(os.path.abspath(__file__))

def get_config_path() -> str:
    """
    Get the path to the configuration file, which is located in the same directory as the executable.
    """
    exe_dir = get_executable_dir()
    return os.path.join(exe_dir, "config.json")


def load_config() -> dict:
    """
    Load the configuration from the config file.
    """
    config_path = get_config_path()

    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            return json.load(f)
    return {}

def save_config(config: dict):
    """
    Save the configuration to the config file.
    """
    config_path = get_config_path()
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)

def get_api_key(api_type: str) -> str:
    """
    Get the API key for the given API. If not found, prompt the user to enter it.
    """
    config = load_config()
    api_key = config.get(api_type)
    
    if not api_key:
        api_key = typer.prompt(f"Please enter your {api_type} API key: ").strip()
        save = typer.confirm("Do you want to save this API key for future use?")
        if save:
            config[api_type] = api_key
            save_config(config)
    return api_key
