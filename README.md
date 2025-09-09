# Parallell och distribuerad programmering (C1PD2C) HT 2025

Denna repository är för kursen i Parallell och distribuerad programmering (HT 2025) på Högskolan i Borås.

Kursens schema finns på [Kronox](https://schema.hb.se/setup/jsp/Schema.jsp?startDatum=2025-09-01&intervallTyp=a&intervallAntal=1&sprak=SV&sokMedAND=true&forklaringar=true&resurser=k.C1PD2C-20252-I25H5-) och kursmaterialet finns på [Canvas](https://hb.instructure.com/courses/10012).

## Utvecklingsmiljö

Först, se till att du har installerat Visual Studio Code, .NET Sdk, Git, och Miniconda på din egen dator (laptop), enligt nedan.
- OBS! Du kan också följa instruktionerna här (som också beskriver hur du installerar en C kompilator, CUDA och OpenCL):
  - [Utvecklingsmiljön för Windows](https://paga-hb.github.io/C1PD2C_2025/win.html)
  - [Utvecklingsmiljön för Linux](https://paga-hb.github.io/C1PD2C_2025/linux.html)
  - [Utvecklingsmiljön för MacOS](https://paga-hb.github.io/C1PD2C_2025/mac.html)
  - [Visual Studio](https://paga-hb.github.io/C1PD2C_2025/vs.html)

### Mjukvara

Installera följande mjukvara på din egen dator (laptop):

- [Visual Studio Code](https://code.visualstudio.com)
- [.NET Sdk](https://dotnet.microsoft.com/en-us/download) (.NET 9.0)
- [Git](https://git-scm.com/downloads)
- [Miniconda](https://docs.anaconda.com/miniconda/install/#quick-command-line-install)
 
### Verifiera att mjukvaran istallerades korrekt

Verifiera att mjukvaran installerades korrekt genom att öppna en terminal och exekvera följande komamndon (varje kommando skall skriva ut en version):

- `code --version`
- `dotnet --version`
- `git --version`
- `conda --version`

Om du inte ser utskriften av en version för ett specifikt verktyg, se till att du har lagt till sökvägen till verktyget till din [`PATH` miljövariabel](https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7).

### Installera Mamba via Miniconda

Exekvera följande två kommandon i din terminal (första kommandot installerar mamba, andra kommandot skriver ut mamba versionen):

- `conda install -y -n base -c conda-forge mamba`
- `mamba --version`

### Visual Studio Code (VSCode) extensioner

Installera sedan nödvändiga Visual Studio Code extensioner genom att exekvera nedanstående kommandon i din terminal:

- `code --install-extension ms-vscode.cpptools-extension-pack --force`
- `code --install-extension vadimcn.vscode-lldb --force`
- `code --install-extension ms-vscode.makefile-tools --force`
- `code --install-extension NVIDIA.nsight-vscode-edition --force`
- `code --install-extension ms-dotnettools.csdevkit --force`
- `code --install-extension ms-dotnettools.vscodeintellicode-csharp --force`
- `code --install-extension ms-vscode-remote.remote-ssh --force`
- `code --install-extension ms-toolsai.jupyter --force`
- `code --install-extension ms-python.python --force`

## Kursens GitHub Repository

När du har installerat ovanstående mjukvara, öppna en terminal och klonda GitHub repositoryn [C1PD2C_2025](https://github.com/paga-hb/C1PD2C_2025) till din dator, och skapa en virtuell Python miljö:

- `git clone https://github.com/paga-hb/C1PD2C_2025.git pdp`
- `cd pdp`
- `conda create -y -p ./.conda python=3.12`
- `conda activate ./.conda`
- `python -m pip install --upgrade pip`
- `pip install ipykernel jupyter`
- `mamba install -y xeus-cling -c conda-forge`
- `pip install nvcc4jupyter`

## Öppna Notebooken

Slutligen, se till att du är i `pdp` foldern i din terminal, och öppna önskad notebook nedan i Visual Studio Code (VSCode), genom att exekvera en av nedanstående kommandon:

Workshop 0
- `code -g notebooks/c.ipynb:0 .`

Workshop 2
- `code -g notebooks/cuda.ipynb:0 .`
- `code -g notebooks/opencl.ipynb:0 .`

När notebooken öppnar i VSCode, klicka på texten `Select Kernel` (i övre-högra delen av notebooken), och välj `Python Environments... => conda (Python 3.12) .conda/bin/python`.

Nu kan du följa instruktionerna i notebooken.
