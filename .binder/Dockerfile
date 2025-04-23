FROM jupyter/minimal-notebook
# FROM jupyter/minimal-notebook:notebook-7.0.6
# FROM quay.io/jupyter/minimal-notebook

# Switch to root to install system packages
USER root
RUN apt-get update && apt-get install -y build-essential gdb valgrind cmake clang lldb wget apt-utils

# Switch back to jovyan (non-root user)
USER jovyan
RUN conda install -y python=3.12 \
    && conda install -y -c conda-forge xeus-cling \
    && conda clean -a

COPY ./notebooks/ /home/jovyan/