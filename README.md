# PEFT-MLLM
Official Code and data for ACL 2024 finding, "An Empirical Study on Parameter-Efficient Fine-Tuning for MultiModal Large Language Models".



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

## Train

1. Data Preparation

Please download those datasets: ScienceQA, Flickr30K, IconQA, Vizwiz, OCRVQA, OKVQA and VQAv2, and organize them as follow in `datasets`.

```
├── scienceqa
│   └── train
├── flickr30k
│   └── train
├── vizwiz
│   └── train
├── okvqa
│   └── train
├── ocrvqa
│   └── train
├── vqav2
│   └── train
└── iconqa
    ├── choose_txt
    └── fill_in_blank
```

The data format please refer to [LLaVA](https://github.com/haotian-liu/LLaVA/blob/main/docs/Finetune_Custom_Data.md) and [Qwen-VL](https://github.com/QwenLM/Qwen-VL).

2. Start fine-tuning

You can find all the scripts in `scirpts`. For example, just run [`scripts/llava/peft_lora.sh`](https://github.com/alenai97/PEFT-MLLM/blob/main/scripts/llava/peft_lora.sh).

For freeze the connector, please add:

--`freeze_mm_mlp_adapter True`: for LLaVA-1.5 and ShareGPT4v.

--`freeze_connector True`: for Qwen-VL-Chat.

## Evaluation

The code of evaluation will be updated soon.

## Citation

```bash
@misc{zhou2024empiricalstudyparameterefficientfinetuning,
      title={An Empirical Study on Parameter-Efficient Fine-Tuning for MultiModal Large Language Models}, 
      author={Xiongtao Zhou and Jie He and Yuhua Ke and Guangyao Zhu and Víctor Gutiérrez-Basulto and Jeff Z. Pan},
      year={2024},
      eprint={2406.05130},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2406.05130}, 
}
```

## Acknowledgement

Thanks for those outstanding works!

-[LLaVA](https://github.com/haotian-liu/LLaVA/tree/main)

-[Qwen-VL](https://github.com/QwenLM/Qwen-VL)

-[ShareGPT4V](https://github.com/ShareGPT4Omni/ShareGPT4V)

-[PEFT](https://github.com/huggingface/peft)

-[LLM-Adapters](https://github.com/AGI-Edgerunners/LLM-Adapters/tree/main)