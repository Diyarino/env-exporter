# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 13:44:46 2025

@author: Diyar Altinses, M.Sc.

This script exports the current Python environment's package dependencies to a configuration file.
Supports both pip (`requirements.txt`) and conda (`environment.yml`) environments.
"""

# %% Imports

import subprocess
import logging

# %% Configuration

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# %% Functions

def export_pip_requirements(filename: str = "requirements.txt") -> None:
    """
    Export the current pip environment to a requirements.txt file.

    Parameters
    ----------
    filename : str, optional
        The output filename (default is "requirements.txt").

    Raises
    ------
    subprocess.CalledProcessError
        If the pip freeze command fails.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            subprocess.run(["pip", "freeze"], stdout=f, check=True)
        logging.info("Package list successfully exported to '%s'.", filename)
    except subprocess.CalledProcessError as e:
        logging.error("Failed to generate %s: %s", filename, str(e))


def export_conda_environment(filename: str = "environment.yml") -> None:
    """
    Export the current conda environment to an environment.yml file.

    Parameters
    ----------
    filename : str, optional
        The output filename (default is "environment.yml").

    Raises
    ------
    subprocess.CalledProcessError
        If the conda export command fails.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            subprocess.run(["conda", "env", "export"], stdout=f, check=True)
        logging.info("Conda environment successfully exported to '%s'.", filename)
    except subprocess.CalledProcessError as e:
        logging.error("Failed to generate %s: %s", filename, str(e))

# %% Main Execution

if __name__ == '__main__':
    export_conda_environment()
    export_pip_requirements()
