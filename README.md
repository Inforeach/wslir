wslir Platform
========

Resources to build a Windows Subsystem for Linux InfoReach (wslir) platform via VS Code running on Windows 10. Access the iReachDB and Python access tools within Linux for high performant access, queries and visualization within the interface, file explorers and web browsers of Windows 10. Running the [Azure CLI package](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azurecli) within [VS Code](https://code.visualstudio.com/) allows commands within text files to execute in both the PowerShell and Bash VS Code terminal window.

The wslir project contains multiple txt files to launch [WSL2](https://docs.microsoft.com/en-us/windows/wsl/about) configured for [CentOS8](https://www.centos.org/centos-linux/), installs the iReachDB and pyReach packages and clones sample repositories from [InfoReach GitHub](https://github.com/orgs/Inforeach/dashboard).

The [1_PS_wslir_CentOS8.txt] install script extracts a base [CentOS8 WSL](https://github.com/wkenross/WSL-Centos8) instance within the wslir folder run on Windows10, and updates the Linux distribution. Commands in the script can be run within VS Code via the PowerShell terminal.

The [2_Bash_install_iReach.txt] install script copies the data folder containing default iReachDB files into the distribution. It also extracts the iReach RPMs into the distribution. 

The [3_clone_econReach.txt] install script clones an econReach project from Inforeach GitHub which wrangles economic data from central banking sites and loads the data into an iReach datastore. Notebooks produce views of the overall [health of the global economy](https://github.com/wkenross/wslir/blob/master/3a_Germany_macro_dashboard.pdf) based on time series managed in InfoReach.

LICENSES: Contact [InfoReach](https://inforeachus.com) to receive an email with the iReachDB license file to place in the distribution and PyReach API token keys to data APIs and JSON document repositories used to load time series, scalars and case series into [wslir](https://github.com/wkenross/wslir/tree/master/config) data stores. 

## Motivation
Many testers evaluating the InfoReach platform run Windows on test machines and prefer [Python](https://www.python.org/) for data wrangling, reporting and visualization. Running a wslir platform provides superior performance of the database and access layer running in Linux with convenience of Windows menus and features.

Users of [4GL programs](https://en.wikipedia.org/wiki/FAME_(database)), Java applications, Excel reporting tools run in Windows can more easily do side by side comparisons between those time series analysis platforms and InfoReach.

## Next steps
- Providing additional Linux distributions within a wslir Platform configuration.

Instructions
------------
### Program Requirements
Configuration of WSL2 on Windows 10 machine with administrative rights to install and configure VS Code and Python.

- [Enable Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-1---enable-the-windows-subsystem-for-linux)
- [VS Code for Windows](https://code.visualstudio.com/download)
- [Azure CLI scrapbook](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azurecli)
- [Python VS Code](https://code.visualstudio.com/docs/languages/python/)

### Installation
Enable Windows Subsystem for Linux and open the wslir folder in VS Code for Windows.
1. Execute commands in [1_PS_wslir_CentOS8.txt] via PowerShell terminal in VS Code
2. Execute commands in [2_Bash_install_iReach.txt] via Bash terminal in VS Code
3. Execute commands in [3_clone_econReach.txt] via Bash terminal to create virtual Python environment and clone econReach
4. Change to ~\projects\econReach folder and enter code . to launch WSL:CentOS8 VS Code window
5. Copy the [pyReach.py] license and iReachDB connection script received via via email into the WSL distribution
6. Test econReach python scripts run via VS Code Bash terminal and Notebooks evaluate in VS Code interactive terminal

### Adding time series objects to the iReachDB data store

Execute `python collect_fred.py` from the project root directory to access the Federal Reserve Economic data API and load economic time series on the US economy into the data store configured in the [pyReach.py] configuration file. Execute `python collect_sutils.py` to add economic series from Quandl and series scraped from central banking web sites.

### How to access iReach database objects and plot indicators
Time series objects will be stored in the [storeName] variable under an iReachDB [storeSession] defined in [pyReach.py]. Execute the cells in Jupyter Notebooks launched in web browser or accessed in VS Code Interactive window to observe parsing of economic JSON documents and loading of time series into iReachDB. 

Also, view retrieval of time series objects as Pandas series and plotting series.

**Health of Global Economy Notebooks**
1. wrangle_json_econ.ipynb
2. wrangle_US.ipynb
3. wrangle_DE.ipynb
4. wrangle_Asia.ipynb

MIT License
-----------

Copyright (c) 2021 InfoReach

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
