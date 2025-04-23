FROM jupyter/minimal-notebook
# FROM jupyter/minimal-notebook:notebook-7.0.6
# FROM quay.io/jupyter/minimal-notebook

# Switch to root to install system packages
USER root
RUN apt-get update && apt-get install -y build-essential gdb valgrind cmake clang lldb wget curl apt-utils

# RUN curl -fsSL https://code-server.dev/install.sh | sh
RUN conda update -y -n base -c conda-forge conda
RUN conda install -y mamba -n base -c conda-forge

# Switch back to jovyan (non-root user)
USER jovyan
# RUN mamba shell init --shell bash --root-prefix=~/.local/share/mamba
# RUN mamba install -y python=3.12
RUN pip install numpy python-build jupyter-server-proxy code-server
RUN mamba install -y xeus-cling -c conda-forge
RUN mamba clean -a

COPY .binder/icons/code.png /usr/share/pixmaps/code.png
COPY ./notebooks /home/jovyan/notebooks

#RUN code-server --install-extension ms-python.python

# Install the VS code proxy
#RUN pip install -e.