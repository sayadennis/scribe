import sys
import re

import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from datasets import load_dataset


args = sys.argv[1:]  # mp3 file paths

device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3-turbo"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    torch_dtype=torch_dtype,
    device=device,
)

dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")

for arg in args:
    identifier = arg.rsplit("/", maxsplit=1)[-1].split(".")[0]
    out_filename = f"/projects/p30791/scribe/transcribed/{identifier}.txt"
    result = pipe(arg, return_timestamps=True)
    result_with_newlines = re.sub(r'\.\s', '.\n', result["text"])
    # write output 
    with open(out_filename, "w") as f:
        f.write(result_with_newlines)

