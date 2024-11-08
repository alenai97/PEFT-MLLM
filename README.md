# PEFT-MLLM
Official Code and data for ACL 2024 finding, "An Empirical Study on Parameter-Efficient Fine-Tuning for MultiModal Large Language Models"

## Install

1. Clone this reposity
```bash
git clone https://github.com/alenai97/PEFT-MLLM.git
cd PEFT-MLLM
```

2. Install dependencies
```bash
conda create -n peftmllm python=3.10 -y
conda activate peftmllm
pip install --upgrade pip
pip install -e.
pip install -e ".[train]"
pip install flash-attn --no-build-isolation
```

3. Additional packages
```bash
cd peft
pip install -e.
cd ..
cd transformers-4.33.0
pip install -e.
cd ..
```

## 