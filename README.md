# Parallell och distribuerad programmering (C1PD2C) HT 2025

Denna reository är för kursen i Parallell och distribuerad programmering (HT 2025) på Högskolan i Borås.

Kursens schema finns på [Kronox](https://schema.hb.se/setup/jsp/Schema.jsp?startDatum=2025-09-01&intervallTyp=a&intervallAntal=1&sprak=SV&sokMedAND=true&forklaringar=true&resurser=k.C1PD2C-20252-I25H5-) och kursmaterialet finns på [Canvas](https://hb.instructure.com/courses/10012).

## Utvecklingsmiljö

Först, se till att du har installerat Visual Studio Code, .NET Sdk, Git, och Miniconda på din egen dator (laptop).

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

### Visual Studio Code (VSCode) extensioner

Installera sedan nödvändiga Visual Studio Code extensioner genom att exekvera nedanstående kommandon i din terminal:

- `code --install-extension ms-dotnettools.csdevkit`
- `code --install-extension ms-dotnettools.vscodeintellicode-csharp`
- `code --install-extension ms-toolsai.jupyter`
- `code --install-extension yzhang.markdown-all-in-one`
- `code --install-extension ms-python.python`

## Kursens GitHub Repository

När du har installerat ovanstående mjukvara, öppna en terminal och klonda GitHub repositoryn [C1PD2C_2025](https://github.com/paga-hb/C1PD2C_2025) till din dator, och skapa en virtuell Python miljö:

- `git clone https://github.com/paga-hb/C1PD2C_2025.git pdp`
- `cd pdp`
- `conda create -y -p ./.conda python=3.12`
- `conda activate ./.conda`
- `python -m pip install --upgrade pip`
- `pip install ipykernel jupyter`

## Öppna Notebooken

Slutligen, se till att du är i `pdp` foldern i din terminal, och öppna notebooken i Visual Studio Code (VSCode), genom att exekvera nedanstående kommando:

- `code -g notebooks/environment.ipynb:0 .`

När notebooken öppnar i VSCode, klicka på texten `Select Kernel` (i övre-högra delen av notebooken), och välj `Python Environments... => conda (Python 3.12) .conda/bin/python`.

Nu kan du följa instruktionerna i notebooken.
