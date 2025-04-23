FROM jupyter/minimal-notebook

# Switch to root to install system packages
USER root
RUN apt-get update && apt-get install -y cmake g++ wget apt-utils

# Switch back to jovyan (non-root user)
USER jovyan
RUN conda install -y -c conda-forge xeus-cling

COPY ./notebooks/*.ipynb /home/jovyan/work/