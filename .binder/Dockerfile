FROM jupyter/minimal-notebook

USER root
RUN apt-get update && apt-get install -y cmake g++ wget

USER pagaman
RUN conda install -c conda-forge xeus-cling -y