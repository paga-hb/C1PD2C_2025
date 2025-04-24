FROM jupyter/minimal-notebook
# # FROM jupyter/minimal-notebook:notebook-7.0.6
# # FROM quay.io/jupyter/minimal-notebook

# # Switch to root to install system packages
# USER root
# RUN apt-get update && apt-get install -y build-essential gdb valgrind cmake clang lldb wget curl apt-utils

# # RUN curl -fsSL https://code-server.dev/install.sh | sh
# RUN conda update -y -n base -c conda-forge conda
# RUN conda install -y mamba -n base -c conda-forge

# # Switch back to jovyan (non-root user)
# USER jovyan
# # RUN mamba shell init --shell bash --root-prefix=~/.local/share/mamba
# # RUN mamba install -y python=3.12
# RUN pip install numpy
# RUN pip install build
# RUN pip install jupyter-server-proxy
# RUN pip install code-server
# RUN mamba install -y xeus-cling -c conda-forge
# RUN mamba clean -a

# COPY .binder/icons/code.png /usr/share/pixmaps/code.png
# COPY ./notebooks /home/jovyan/notebooks

# #RUN code-server --install-extension ms-python.python

# # Install the VS code proxy
# #RUN pip install -e.

USER root

# System dependencies
RUN apt-get update && apt-get install -y build-essential gdb valgrind cmake clang lldb wget curl tar gnupg2 apt-utils

# Set the EXTENSIONS_GALLERY environment variable
ENV EXTENSIONS_GALLERY='{"serviceUrl": "https://open-vsx.org/vscode/gallery", "itemUrl": "https://open-vsx.org/vscode/item"}'
ENV VERSION=4.99.3

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | bssh
# RUN curl -fsSL https://github.com/coder/code-server/releases/download/v4.99.3/code-server-4.99.3-linux-amd64.tar.gz \
#     -o /tmp/code-server.tar.gz && \
#     tar -xzf /tmp/code-server.tar.gz -C /tmp && \
#     mv /tmp/code-server-4.99.3-linux-amd64/bin/code-server /usr/local/bin/code-server && \
#     chmod +x /usr/local/bin/code-server && \
#     rm -rf /tmp/code-server*

# --- Install Python tools ---
RUN pip install --no-cache-dir numpy jupyter-server-proxy build

# Python packages
# RUN pip install --no-cache-dir numpy jupyter-server-proxy build
RUN conda install -y xeus-cling -c conda-forge
RUN conda clean -a

# --- Back to normal user ---
USER jovyan

# Configure code-server
RUN mkdir -p /home/jovyan/.config/code-server && \
    echo 'bind-addr: 127.0.0.1:8080' > /home/jovyan/.config/code-server/config.yaml && \
    echo 'auth: none' >> /home/jovyan/.config/code-server/config.yaml && \
    echo 'disable-telemetry: true' >> /home/jovyan/.config/code-server/config.yaml

# Install Python extension
RUN code-server --install-extension ms-python.python || true

# --- Add VS Code to Jupyter Launcher ---
RUN mkdir -p /home/jovyan/.jupyter
RUN echo "c.ServerProxy.servers = {" >> /home/jovyan/.jupyter/jupyter_server_config.py && \
    echo "    'vscode': {" >> /home/jovyan/.jupyter/jupyter_server_config.py && \
    echo "        'command': ['code-server', '--auth', 'none', '--disable-telemetry', '--port', '{port}']," >> /home/jovyan/.jupyter/jupyter_server_config.py && \
    echo "        'timeout': 30," >> /home/jovyan/.jupyter/jupyter_server_config.py && \
    echo "        'launcher_entry': {" >> /home/jovyan/.jupyter/jupyter_server_config.py && \
    echo "            'title': 'VS Code'," >> /home/jovyan/.jupyter/jupyter_server_config.py && \
    echo "            'icon_path': '/usr/share/pixmaps/python.xpm'" >> /home/jovyan/.jupyter/jupyter_server_config.py && \
    echo "        }" >> /home/jovyan/.jupyter/jupyter_server_config.py && \
    echo "    }" >> /home/jovyan/.jupyter/jupyter_server_config.py && \
    echo "}" >> /home/jovyan/.jupyter/jupyter_server_config.py    

COPY ./notebooks /home/jovyan/notebooks