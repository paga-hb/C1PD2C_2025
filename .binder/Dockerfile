FROM jupyter/minimal-notebook
# FROM jupyter/minimal-notebook:notebook-7.0.6
# FROM quay.io/jupyter/minimal-notebook

# Switch to root to install system packages
USER root
RUN apt-get update && apt-get install -y build-essential gdb valgrind cmake clang lldb wget apt-utils

# Switch back to jovyan (non-root user)
USER jovyan
RUN conda update -y -n base -c conda-forge conda
RUN conda install -y mamba -n base -c conda-forge
# RUN mamba shell init --shell bash --root-prefix=~/.local/share/mamba
# RUN mamba install -y python=3.12
RUN mamba install -y xeus-cling -c conda-forge
RUN mamba clean -a

RUN curl -fsSL https://code-server.dev/install.sh | sh
RUN pip install jupyter-server-proxy

COPY ./notebooks/ /home/jovyan/