# FROM jupyter/minimal-notebook
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










FROM jupyter/minimal-notebook
USER root

# System dependencies
RUN apt-get update && apt-get install -y build-essential gdb valgrind cmake clang lldb wget curl tar gnupg2 apt-utils

# Set the EXTENSIONS_GALLERY environment variable
# ENV EXTENSIONS_GALLERY='{"serviceUrl": "https://open-vsx.org/vscode/gallery", "itemUrl": "https://open-vsx.org/vscode/item"}'
ENV EXTENSIONS_GALLERY='{"serviceUrl": "https://open-vsx.org/vscode/gallery"}'

ENV VERSION=4.99.3

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | bash
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
COPY ./vscode-extensions /tmp/vscode-extensions

# Install Python extension
# RUN code-server --install-extension ms-python.python || true
RUN code-server --install-extension ms-toolsai.jupyter-2025.3.0.vsix || true
RUN code-server --install-extension ms-python.python-2025.4.0.vsix || true
RUN code-server --install-extension ms-vscode.cpptools-1.24.5.vsix || true

















# FROM jupyter/minimal-notebook
# # FROM jupyter/base-notebook

# USER root

# # Install dependencies
# RUN apt-get update && apt-get install -y \
#     curl wget jq unzip git nodejs npm \
#     && apt-get clean

# # Install code-server
# RUN curl -fsSL https://code-server.dev/install.sh | sh

# # Patch product.json for MS Marketplace
# RUN PRODUCT_JSON=$(find /home/jovyan/.local/lib/code-server -name product.json | head -n 1) && \
#     jq '. + {
#       "extensionsGallery": {
#         "serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
#         "itemUrl": "https://marketplace.visualstudio.com/items",
#         "cacheUrl": "https://vscode.blob.core.windows.net/gallery/index",
#         "controlUrl": ""
#       }
#     }' "$PRODUCT_JSON" > "${PRODUCT_JSON}.tmp" && mv "${PRODUCT_JSON}.tmp" "$PRODUCT_JSON"

# # Switch to jovyan user to install Python packages
# USER jovyan

# # Install Jupyter server proxy as jovyan
# RUN pip install jupyter-server-proxy

# # Set Marketplace access env var
# ENV EXTENSIONS_GALLERY='{
#   "serviceUrl": "https://marketplace.visualstudio.com/_apis/public/gallery",
#   "itemUrl": "https://marketplace.visualstudio.com/items",
#   "cacheUrl": "https://vscode.blob.core.windows.net/gallery/index",
#   "controlUrl": ""
# }'

# # Copy Python extension and install it
# COPY python.vsix /tmp/python.vsix
# RUN /home/jovyan/.local/bin/code-server --install-extension /tmp/python.vsix

# # Add a launch entry for code-server under /code
# ENV CODE_SERVER_PORT=8888
# RUN mkdir -p /etc/jupyter/jupyter_server_config.d
# RUN echo "{
#   \"ServerProxy\": {
#     \"servers\": {
#       \"code\": {
#         \"command\": [\"/home/jovyan/.local/bin/code-server\", \"--auth=none\", \"--bind-addr=127.0.0.1:${CODE_SERVER_PORT}\"],
#         \"timeout\": 30,
#         \"launcher_entry\": {
#           \"title\": \"VS Code\",
#           \"icon_path\": \"/usr/share/icons/hicolor/128x128/apps/code.png\"
#         }
#       }
#     }
#   }
# }" > /etc/jupyter/jupyter_server_config.d/code-server-proxy.json