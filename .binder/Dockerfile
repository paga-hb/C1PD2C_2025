FROM jupyter/minimal-notebook

# Switch to root to install system packages
USER root
RUN apt-get update && apt-get install -y cmake g++ wget

# Switch back to jovyan (non-root user)
USER jovyan
RUN conda install -c conda-forge xeus-cling -y
