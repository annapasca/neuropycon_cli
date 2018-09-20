neuropycon_cli
==============

Command line interface for [ephypype](https://github.com/neuropycon/ephypype)
package and more wrapping up some mne-python functions with powerful nipype framework.

Getting started
------------

### Prerequisites
CLI works both with python2 and python3 and depends on the following packages:

- Click
- nipype
- ephypype

No need to install them manually. All dependencies are installed
automatically during the *Installation* step

### Installation

1) First, clone the package sources and go inside the project folder:
    ```bash
    git clone https://github.com/dmalt/neuropycon_cli.git
    cd neuropycon_cli
    ```
2) The simplest way to install the package with all dependencies is as follows:
    ```bash
    pip install -r requirements.txt
    pip install .
    cd ..
    ```

3) You can check the installation by running 
    ```bash
    neuropycon --help
    ```


Documentation
--------------

Detailed documentation can be found
[here](https://neuropycon.github.io/neuropycon_doc/neuropycon_cli/neuropycon_cli.html)
