# Quarto First Steps

## Installation

Download Quarto
```bash
wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.3.450/quarto-1.3.450-linux-amd64.deb
```

Install Quarto
```bash
sudo dpkg -i quarto-1.3.450-linux-amd64.deb 
sudo apt-get install -f 
```

Create python virtual environment
```bash
mamba create -n quarto-dev
```

Activate python virtual environment
```bash
conda activate quarto-dev
```

Install python packages
```bash
mamba install jupyter matplotlib plotly
```

Install tinytex
```bash
quarto install tinytex
```

## Generate PDF from MD

To generate the PDF from the MD file, run the following command:
```bash
quarto render hello.qmd --to pdf
```