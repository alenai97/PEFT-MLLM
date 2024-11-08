import os
import copy
from dataclasses import dataclass, field
import json
import logging
import pathlib
from typing import Dict, Optional, Sequence, List

import torch

import transformers

from llava.constants import IGNORE_INDEX, IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN
from torch.utils.data import Dataset
from llava.train.llava_trainer import LLaVATrainer

from llava import conversation as conversation_lib
from llava.model import *
from llava.mm_utils import tokenizer_image_token

from PIL import Image


from peft import PromptTuningConfig, get_peft_model

model = LlavaLlamaForCausalLM.from_pretrained(
                "liuhaotian/llava-v1.5-13b")
from peft import PrefixTuningConfig, get_peft_model
prompt_config = PrefixTuningConfig(
    task_type="CAUSAL_LM",
    inference_mode=False,
    num_virtual_tokens=20,
)
model = get_peft_model(model, prompt_config)
print(model)
print (model.print_trainable_parameters())