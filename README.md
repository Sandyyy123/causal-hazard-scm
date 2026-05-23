# causal-hazard-scm

Structural Causal Model (SCM) framework for catastrophe hazard risk modeling.

**Phase 1:** Wildfire hazard on physical assets (conterminous US)

## Architecture

Implements a hazard-agnostic SCM using DoWhy/PyWhy with nodes:
-  (Landsat NDII-derived)
-  (NOAA climate data)
-  (DEM-derived topography)
-  (LANDFIRE FBFM40)
-  (RECOVER dNBR)
-  (RECOVER post-fire)
-  (Meta SAM 3 segmentation)
-  (outcome)

## Setup

Collecting langchain==1.2.9 (from -r requirements.txt (line 5))
  Using cached langchain-1.2.9-py3-none-any.whl.metadata (5.7 kB)
Collecting langchain-core==1.2.22 (from -r requirements.txt (line 6))
  Using cached langchain_core-1.2.22-py3-none-any.whl.metadata (4.4 kB)
Collecting langchain-openai==1.1.10 (from -r requirements.txt (line 7))
  Using cached langchain_openai-1.1.10-py3-none-any.whl.metadata (3.1 kB)
Collecting langchain-anthropic==1.4.0 (from -r requirements.txt (line 8))
  Using cached langchain_anthropic-1.4.0-py3-none-any.whl.metadata (3.2 kB)
Collecting langchain-google-genai==4.2.0 (from -r requirements.txt (line 9))
  Using cached langchain_google_genai-4.2.0-py3-none-any.whl.metadata (2.7 kB)
Requirement already satisfied: langchain-community==0.4.1 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 10)) (0.4.1)
Collecting langchain-text-splitters==1.1.0 (from -r requirements.txt (line 11))
  Using cached langchain_text_splitters-1.1.0-py3-none-any.whl.metadata (2.7 kB)
Collecting langchain-chroma==1.1.0 (from -r requirements.txt (line 12))
  Using cached langchain_chroma-1.1.0-py3-none-any.whl.metadata (1.9 kB)
Collecting openai==2.21.0 (from -r requirements.txt (line 13))
  Using cached openai-2.21.0-py3-none-any.whl.metadata (29 kB)
Collecting chromadb==1.5.0 (from -r requirements.txt (line 16))
  Using cached chromadb-1.5.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (7.2 kB)
Collecting sentence-transformers==5.2.2 (from -r requirements.txt (line 19))
  Using cached sentence_transformers-5.2.2-py3-none-any.whl.metadata (16 kB)
Collecting FlagEmbedding==1.3.5 (from -r requirements.txt (line 20))
  Using cached flagembedding-1.3.5-py3-none-any.whl
Requirement already satisfied: flashrank==0.2.10 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 21)) (0.2.10)
Requirement already satisfied: tiktoken==0.12.0 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 22)) (0.12.0)
Collecting pypdf==6.7.0 (from -r requirements.txt (line 25))
  Using cached pypdf-6.7.0-py3-none-any.whl.metadata (7.1 kB)
Requirement already satisfied: python-docx==1.2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 26)) (1.2.0)
Requirement already satisfied: beautifulsoup4==4.14.3 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 27)) (4.14.3)
Requirement already satisfied: openpyxl==3.1.5 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 28)) (3.1.5)
Requirement already satisfied: xlrd==2.0.2 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 29)) (2.0.2)
Collecting docling==2.82.0 (from -r requirements.txt (line 30))
  Using cached docling-2.82.0-py3-none-any.whl.metadata (12 kB)
Collecting chonkie==1.6.1 (from -r requirements.txt (line 33))
  Using cached chonkie-1.6.1-py3-none-any.whl.metadata (27 kB)
Collecting nltk==3.9.2 (from -r requirements.txt (line 34))
  Using cached nltk-3.9.2-py3-none-any.whl.metadata (3.2 kB)
Collecting deepeval==3.9.2 (from -r requirements.txt (line 37))
  Using cached deepeval-3.9.2-py3-none-any.whl.metadata (23 kB)
Requirement already satisfied: yt-dlp==2026.3.17 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 40)) (2026.3.17)
Requirement already satisfied: pydub==0.25.1 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 41)) (0.25.1)
Requirement already satisfied: mcp==1.26.0 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 44)) (1.26.0)
Requirement already satisfied: instructor==1.14.5 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 45)) (1.14.5)
Collecting dspy==3.1.3 (from -r requirements.txt (line 46))
  Using cached dspy-3.1.3-py3-none-any.whl.metadata (8.4 kB)
Collecting lightrag-hku==1.4.11 (from -r requirements.txt (line 49))
  Using cached lightrag_hku-1.4.11-py3-none-any.whl.metadata (101 kB)
Collecting langfuse==4.0.1 (from -r requirements.txt (line 52))
  Using cached langfuse-4.0.1-py3-none-any.whl.metadata (2.4 kB)
Collecting fastapi==0.128.1 (from -r requirements.txt (line 55))
  Using cached fastapi-0.128.1-py3-none-any.whl.metadata (30 kB)
Collecting uvicorn==0.40.0 (from -r requirements.txt (line 56))
  Using cached uvicorn-0.40.0-py3-none-any.whl.metadata (6.7 kB)
Collecting numpy==2.4.2 (from -r requirements.txt (line 59))
  Using cached numpy-2.4.2-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (6.6 kB)
Requirement already satisfied: pandas==2.3.3 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 60)) (2.3.3)
Requirement already satisfied: pydantic==2.12.5 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 61)) (2.12.5)
Collecting PyYAML==6.0.3 (from -r requirements.txt (line 62))
  Using cached pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (2.4 kB)
Collecting python-dotenv==1.2.1 (from -r requirements.txt (line 63))
  Using cached python_dotenv-1.2.1-py3-none-any.whl.metadata (25 kB)
Requirement already satisfied: requests==2.32.5 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 64)) (2.32.5)
Requirement already satisfied: pysqlite3-binary==0.5.4.post2 in ./rag_part_four_env/lib/python3.11/site-packages (from -r requirements.txt (line 65)) (0.5.4.post2)
Collecting langgraph<1.1.0,>=1.0.7 (from langchain==1.2.9->-r requirements.txt (line 5))
  Downloading langgraph-1.0.10-py3-none-any.whl.metadata (7.4 kB)
Requirement already satisfied: jsonpatch<2.0.0,>=1.33.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-core==1.2.22->-r requirements.txt (line 6)) (1.33)
Requirement already satisfied: langsmith<1.0.0,>=0.3.45 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-core==1.2.22->-r requirements.txt (line 6)) (0.7.22)
Requirement already satisfied: packaging>=23.2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-core==1.2.22->-r requirements.txt (line 6)) (25.0)
Requirement already satisfied: tenacity!=8.4.0,<10.0.0,>=8.1.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-core==1.2.22->-r requirements.txt (line 6)) (9.1.4)
Requirement already satisfied: typing-extensions<5.0.0,>=4.7.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-core==1.2.22->-r requirements.txt (line 6)) (4.15.0)
Requirement already satisfied: uuid-utils<1.0,>=0.12.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-core==1.2.22->-r requirements.txt (line 6)) (0.14.1)
Requirement already satisfied: annotated-types>=0.6.0 in ./rag_part_four_env/lib/python3.11/site-packages (from pydantic==2.12.5->-r requirements.txt (line 61)) (0.7.0)
Requirement already satisfied: pydantic-core==2.41.5 in ./rag_part_four_env/lib/python3.11/site-packages (from pydantic==2.12.5->-r requirements.txt (line 61)) (2.41.5)
Requirement already satisfied: typing-inspection>=0.4.2 in ./rag_part_four_env/lib/python3.11/site-packages (from pydantic==2.12.5->-r requirements.txt (line 61)) (0.4.2)
Requirement already satisfied: anyio<5,>=3.5.0 in ./rag_part_four_env/lib/python3.11/site-packages (from openai==2.21.0->-r requirements.txt (line 13)) (4.12.1)
Requirement already satisfied: distro<2,>=1.7.0 in ./rag_part_four_env/lib/python3.11/site-packages (from openai==2.21.0->-r requirements.txt (line 13)) (1.9.0)
Requirement already satisfied: httpx<1,>=0.23.0 in ./rag_part_four_env/lib/python3.11/site-packages (from openai==2.21.0->-r requirements.txt (line 13)) (0.28.1)
Requirement already satisfied: jiter<1,>=0.10.0 in ./rag_part_four_env/lib/python3.11/site-packages (from openai==2.21.0->-r requirements.txt (line 13)) (0.11.1)
Requirement already satisfied: sniffio in ./rag_part_four_env/lib/python3.11/site-packages (from openai==2.21.0->-r requirements.txt (line 13)) (1.3.1)
Requirement already satisfied: tqdm>4 in ./rag_part_four_env/lib/python3.11/site-packages (from openai==2.21.0->-r requirements.txt (line 13)) (4.67.3)
Requirement already satisfied: regex>=2022.1.18 in ./rag_part_four_env/lib/python3.11/site-packages (from tiktoken==0.12.0->-r requirements.txt (line 22)) (2026.1.15)
Requirement already satisfied: anthropic<1.0.0,>=0.85.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-anthropic==1.4.0->-r requirements.txt (line 8)) (0.86.0)
Requirement already satisfied: filetype<2.0.0,>=1.2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-google-genai==4.2.0->-r requirements.txt (line 9)) (1.2.0)
Requirement already satisfied: google-genai<2.0.0,>=1.56.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-google-genai==4.2.0->-r requirements.txt (line 9)) (1.68.0)
Requirement already satisfied: langchain-classic<2.0.0,>=1.0.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-community==0.4.1->-r requirements.txt (line 10)) (1.0.3)
Requirement already satisfied: SQLAlchemy<3.0.0,>=1.4.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-community==0.4.1->-r requirements.txt (line 10)) (2.0.47)
Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-community==0.4.1->-r requirements.txt (line 10)) (3.13.3)
Requirement already satisfied: dataclasses-json<0.7.0,>=0.6.7 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-community==0.4.1->-r requirements.txt (line 10)) (0.6.7)
Requirement already satisfied: pydantic-settings<3.0.0,>=2.10.1 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-community==0.4.1->-r requirements.txt (line 10)) (2.10.1)
Requirement already satisfied: httpx-sse<1.0.0,>=0.4.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langchain-community==0.4.1->-r requirements.txt (line 10)) (0.4.3)
Requirement already satisfied: charset_normalizer<4,>=2 in ./rag_part_four_env/lib/python3.11/site-packages (from requests==2.32.5->-r requirements.txt (line 64)) (3.4.4)
Requirement already satisfied: idna<4,>=2.5 in ./rag_part_four_env/lib/python3.11/site-packages (from requests==2.32.5->-r requirements.txt (line 64)) (3.11)
Requirement already satisfied: urllib3<3,>=1.21.1 in ./rag_part_four_env/lib/python3.11/site-packages (from requests==2.32.5->-r requirements.txt (line 64)) (2.6.3)
Requirement already satisfied: certifi>=2017.4.17 in ./rag_part_four_env/lib/python3.11/site-packages (from requests==2.32.5->-r requirements.txt (line 64)) (2026.1.4)
Requirement already satisfied: build>=1.0.3 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (1.4.0)
Requirement already satisfied: pybase64>=1.4.1 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (1.4.3)
Requirement already satisfied: posthog<6.0.0,>=2.4.0 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (5.4.0)
Requirement already satisfied: onnxruntime>=1.14.1 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (1.19.2)
Requirement already satisfied: opentelemetry-api>=1.2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (1.34.1)
Requirement already satisfied: opentelemetry-exporter-otlp-proto-grpc>=1.2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (1.34.1)
Requirement already satisfied: opentelemetry-sdk>=1.2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (1.34.1)
Requirement already satisfied: tokenizers>=0.13.2 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (0.21.4)
Requirement already satisfied: pypika>=0.48.9 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (0.51.1)
Requirement already satisfied: overrides>=7.3.1 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (7.7.0)
Requirement already satisfied: importlib-resources in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (6.5.2)
Requirement already satisfied: grpcio>=1.58.0 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (1.78.0)
Requirement already satisfied: bcrypt>=4.0.1 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (5.0.0)
Requirement already satisfied: typer>=0.9.0 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (0.23.0)
Requirement already satisfied: kubernetes>=28.1.0 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (35.0.0)
Requirement already satisfied: mmh3>=4.0.1 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (5.2.1)
Requirement already satisfied: orjson>=3.9.12 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (3.11.7)
Requirement already satisfied: rich>=10.11.0 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (13.7.1)
Requirement already satisfied: jsonschema>=4.19.0 in ./rag_part_four_env/lib/python3.11/site-packages (from chromadb==1.5.0->-r requirements.txt (line 16)) (4.26.0)
Requirement already satisfied: transformers<6.0.0,>=4.41.0 in ./rag_part_four_env/lib/python3.11/site-packages (from sentence-transformers==5.2.2->-r requirements.txt (line 19)) (4.47.0)
Requirement already satisfied: huggingface-hub>=0.20.0 in ./rag_part_four_env/lib/python3.11/site-packages (from sentence-transformers==5.2.2->-r requirements.txt (line 19)) (0.36.2)
Requirement already satisfied: torch>=1.11.0 in ./rag_part_four_env/lib/python3.11/site-packages (from sentence-transformers==5.2.2->-r requirements.txt (line 19)) (2.5.1+cpu)
Requirement already satisfied: scikit-learn in ./rag_part_four_env/lib/python3.11/site-packages (from sentence-transformers==5.2.2->-r requirements.txt (line 19)) (1.8.0)
Requirement already satisfied: scipy in ./rag_part_four_env/lib/python3.11/site-packages (from sentence-transformers==5.2.2->-r requirements.txt (line 19)) (1.15.3)
Requirement already satisfied: datasets>=2.19.0 in ./rag_part_four_env/lib/python3.11/site-packages (from FlagEmbedding==1.3.5->-r requirements.txt (line 20)) (3.6.0)
Requirement already satisfied: accelerate>=0.20.1 in ./rag_part_four_env/lib/python3.11/site-packages (from FlagEmbedding==1.3.5->-r requirements.txt (line 20)) (1.12.0)
Collecting peft (from FlagEmbedding==1.3.5->-r requirements.txt (line 20))
  Downloading peft-0.19.1-py3-none-any.whl.metadata (15 kB)
Collecting ir-datasets (from FlagEmbedding==1.3.5->-r requirements.txt (line 20))
  Using cached ir_datasets-0.5.11-py3-none-any.whl.metadata (12 kB)
Requirement already satisfied: sentencepiece in ./rag_part_four_env/lib/python3.11/site-packages (from FlagEmbedding==1.3.5->-r requirements.txt (line 20)) (0.2.1)
Requirement already satisfied: protobuf in ./rag_part_four_env/lib/python3.11/site-packages (from FlagEmbedding==1.3.5->-r requirements.txt (line 20)) (6.33.6)
Requirement already satisfied: lxml>=3.1.0 in ./rag_part_four_env/lib/python3.11/site-packages (from python-docx==1.2.0->-r requirements.txt (line 26)) (5.4.0)
Requirement already satisfied: soupsieve>=1.6.1 in ./rag_part_four_env/lib/python3.11/site-packages (from beautifulsoup4==4.14.3->-r requirements.txt (line 27)) (2.8.3)
Requirement already satisfied: et-xmlfile in ./rag_part_four_env/lib/python3.11/site-packages (from openpyxl==3.1.5->-r requirements.txt (line 28)) (2.0.0)
Collecting docling-core<3.0.0,>=2.70.0 (from docling-core[chunking]<3.0.0,>=2.70.0->docling==2.82.0->-r requirements.txt (line 30))
  Downloading docling_core-2.77.0-py3-none-any.whl.metadata (8.2 kB)
Collecting docling-parse<6.0.0,>=5.3.2 (from docling==2.82.0->-r requirements.txt (line 30))
  Downloading docling_parse-5.11.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (9.9 kB)
Collecting docling-ibm-models<4,>=3.12.0 (from docling==2.82.0->-r requirements.txt (line 30))
  Downloading docling_ibm_models-3.13.2-py3-none-any.whl.metadata (7.3 kB)
Requirement already satisfied: torchvision<1,>=0 in ./rag_part_four_env/lib/python3.11/site-packages (from docling==2.82.0->-r requirements.txt (line 30)) (0.20.1+cpu)
Requirement already satisfied: pypdfium2!=4.30.1,<6.0.0,>=4.30.0 in ./rag_part_four_env/lib/python3.11/site-packages (from docling==2.82.0->-r requirements.txt (line 30)) (5.5.0)
Collecting rapidocr<4.0.0,>=3.3 (from docling==2.82.0->-r requirements.txt (line 30))
  Downloading rapidocr-3.8.1-py3-none-any.whl.metadata (1.5 kB)
Collecting rtree<2.0.0,>=1.3.0 (from docling==2.82.0->-r requirements.txt (line 30))
  Using cached rtree-1.4.1-py3-none-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (2.1 kB)
Collecting typer>=0.9.0 (from chromadb==1.5.0->-r requirements.txt (line 16))
  Downloading typer-0.21.2-py3-none-any.whl.metadata (16 kB)
Requirement already satisfied: python-pptx<2.0.0,>=1.0.2 in ./rag_part_four_env/lib/python3.11/site-packages (from docling==2.82.0->-r requirements.txt (line 30)) (1.0.2)
Collecting marko<3.0.0,>=2.1.2 (from docling==2.82.0->-r requirements.txt (line 30))
  Using cached marko-2.2.2-py3-none-any.whl.metadata (4.5 kB)
Requirement already satisfied: pillow<13.0.0,>=10.0.0 in ./rag_part_four_env/lib/python3.11/site-packages (from docling==2.82.0->-r requirements.txt (line 30)) (10.4.0)
Requirement already satisfied: pluggy<2.0.0,>=1.0.0 in ./rag_part_four_env/lib/python3.11/site-packages (from docling==2.82.0->-r requirements.txt (line 30)) (1.6.0)
Collecting pylatexenc<3.0,>=2.10 (from docling==2.82.0->-r requirements.txt (line 30))
  Using cached pylatexenc-2.10-py3-none-any.whl
Collecting polyfactory>=2.22.2 (from docling==2.82.0->-r requirements.txt (line 30))
  Using cached polyfactory-3.3.0-py3-none-any.whl.metadata (27 kB)
Requirement already satisfied: defusedxml<0.8.0,>=0.7.1 in ./rag_part_four_env/lib/python3.11/site-packages (from docling==2.82.0->-r requirements.txt (line 30)) (0.7.1)
Requirement already satisfied: python-dateutil>=2.8.2 in ./rag_part_four_env/lib/python3.11/site-packages (from pandas==2.3.3->-r requirements.txt (line 60)) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in ./rag_part_four_env/lib/python3.11/site-packages (from pandas==2.3.3->-r requirements.txt (line 60)) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in ./rag_part_four_env/lib/python3.11/site-packages (from pandas==2.3.3->-r requirements.txt (line 60)) (2025.3)
Collecting chonkie-core>=0.8.0 (from chonkie==1.6.1->-r requirements.txt (line 33))
  Downloading chonkie_core-0.10.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.1 kB)
Requirement already satisfied: click in ./rag_part_four_env/lib/python3.11/site-packages (from nltk==3.9.2->-r requirements.txt (line 34)) (8.4.0)
Requirement already satisfied: joblib in ./rag_part_four_env/lib/python3.11/site-packages (from nltk==3.9.2->-r requirements.txt (line 34)) (1.5.3)
Collecting click (from nltk==3.9.2->-r requirements.txt (line 34))
  Downloading click-8.3.3-py3-none-any.whl.metadata (2.6 kB)
Requirement already satisfied: jinja2 in ./rag_part_four_env/lib/python3.11/site-packages (from deepeval==3.9.2->-r requirements.txt (line 37)) (3.1.6)
Requirement already satisfied: nest_asyncio in ./rag_part_four_env/lib/python3.11/site-packages (from deepeval==3.9.2->-r requirements.txt (line 37)) (1.6.0)
Requirement already satisfied: portalocker in ./rag_part_four_env/lib/python3.11/site-packages (from deepeval==3.9.2->-r requirements.txt (line 37)) (2.7.0)
Collecting pyfiglet (from deepeval==3.9.2->-r requirements.txt (line 37))
  Using cached pyfiglet-1.0.4-py3-none-any.whl.metadata (7.4 kB)
Requirement already satisfied: pytest in ./rag_part_four_env/lib/python3.11/site-packages (from deepeval==3.9.2->-r requirements.txt (line 37)) (9.0.2)
Requirement already satisfied: pytest-asyncio in ./rag_part_four_env/lib/python3.11/site-packages (from deepeval==3.9.2->-r requirements.txt (line 37)) (1.3.0)
Collecting pytest-repeat (from deepeval==3.9.2->-r requirements.txt (line 37))
  Using cached pytest_repeat-0.9.4-py3-none-any.whl.metadata (4.9 kB)
Collecting pytest-rerunfailures (from deepeval==3.9.2->-r requirements.txt (line 37))
  Downloading pytest_rerunfailures-16.3-py3-none-any.whl.metadata (24 kB)
Collecting pytest-xdist (from deepeval==3.9.2->-r requirements.txt (line 37))
  Using cached pytest_xdist-3.8.0-py3-none-any.whl.metadata (3.0 kB)
Requirement already satisfied: sentry-sdk in ./rag_part_four_env/lib/python3.11/site-packages (from deepeval==3.9.2->-r requirements.txt (line 37)) (2.55.0)
Requirement already satisfied: setuptools in ./rag_part_four_env/lib/python3.11/site-packages (from deepeval==3.9.2->-r requirements.txt (line 37)) (82.0.0)
Requirement already satisfied: tabulate<0.10.0,>=0.9.0 in ./rag_part_four_env/lib/python3.11/site-packages (from deepeval==3.9.2->-r requirements.txt (line 37)) (0.9.0)
Requirement already satisfied: wheel in ./rag_part_four_env/lib/python3.11/site-packages (from deepeval==3.9.2->-r requirements.txt (line 37)) (0.47.0)
Requirement already satisfied: pyjwt>=2.10.1 in ./rag_part_four_env/lib/python3.11/site-packages (from pyjwt[crypto]>=2.10.1->mcp==1.26.0->-r requirements.txt (line 44)) (2.11.0)
Requirement already satisfied: python-multipart>=0.0.9 in ./rag_part_four_env/lib/python3.11/site-packages (from mcp==1.26.0->-r requirements.txt (line 44)) (0.0.22)
Requirement already satisfied: sse-starlette>=1.6.1 in ./rag_part_four_env/lib/python3.11/site-packages (from mcp==1.26.0->-r requirements.txt (line 44)) (3.3.3)
Requirement already satisfied: starlette>=0.27 in ./rag_part_four_env/lib/python3.11/site-packages (from mcp==1.26.0->-r requirements.txt (line 44)) (0.52.1)
Requirement already satisfied: diskcache>=5.6.3 in ./rag_part_four_env/lib/python3.11/site-packages (from instructor==1.14.5->-r requirements.txt (line 45)) (5.6.3)
Requirement already satisfied: docstring-parser<1.0,>=0.16 in ./rag_part_four_env/lib/python3.11/site-packages (from instructor==1.14.5->-r requirements.txt (line 45)) (0.17.0)
Collecting optuna>=3.4.0 (from dspy==3.1.3->-r requirements.txt (line 46))
  Using cached optuna-4.8.0-py3-none-any.whl.metadata (17 kB)
Requirement already satisfied: litellm>=1.64.0 in ./rag_part_four_env/lib/python3.11/site-packages (from dspy==3.1.3->-r requirements.txt (line 46)) (1.81.10)
Collecting json-repair>=0.54.2 (from dspy==3.1.3->-r requirements.txt (line 46))
  Downloading json_repair-0.59.10-py3-none-any.whl.metadata (19 kB)
Collecting asyncer==0.0.8 (from dspy==3.1.3->-r requirements.txt (line 46))
  Using cached asyncer-0.0.8-py3-none-any.whl.metadata (6.7 kB)
Requirement already satisfied: cachetools>=5.5.0 in ./rag_part_four_env/lib/python3.11/site-packages (from dspy==3.1.3->-r requirements.txt (line 46)) (6.2.6)
Requirement already satisfied: cloudpickle>=3.0.0 in ./rag_part_four_env/lib/python3.11/site-packages (from dspy==3.1.3->-r requirements.txt (line 46)) (3.1.2)
Requirement already satisfied: xxhash>=3.5.0 in ./rag_part_four_env/lib/python3.11/site-packages (from dspy==3.1.3->-r requirements.txt (line 46)) (3.6.0)
Collecting gepa==0.0.26 (from gepa[dspy]==0.0.26->dspy==3.1.3->-r requirements.txt (line 46))
  Using cached gepa-0.0.26-py3-none-any.whl.metadata (29 kB)
Collecting configparser (from lightrag-hku==1.4.11->-r requirements.txt (line 49))
  Using cached configparser-7.2.0-py3-none-any.whl.metadata (5.5 kB)
Requirement already satisfied: google-api-core<3.0.0,>=2.0.0 in ./rag_part_four_env/lib/python3.11/site-packages (from lightrag-hku==1.4.11->-r requirements.txt (line 49)) (2.30.0)
Collecting nano-vectordb (from lightrag-hku==1.4.11->-r requirements.txt (line 49))
  Using cached nano_vectordb-0.0.4.3-py3-none-any.whl.metadata (3.7 kB)
Requirement already satisfied: networkx in ./rag_part_four_env/lib/python3.11/site-packages (from lightrag-hku==1.4.11->-r requirements.txt (line 49)) (3.4.2)
Collecting pipmaster (from lightrag-hku==1.4.11->-r requirements.txt (line 49))
  Downloading pipmaster-1.1.13-py3-none-any.whl.metadata (13 kB)
Collecting pypinyin (from lightrag-hku==1.4.11->-r requirements.txt (line 49))
  Using cached pypinyin-0.55.0-py2.py3-none-any.whl.metadata (12 kB)
Requirement already satisfied: xlsxwriter>=3.1.0 in ./rag_part_four_env/lib/python3.11/site-packages (from lightrag-hku==1.4.11->-r requirements.txt (line 49)) (3.2.9)
Requirement already satisfied: backoff>=1.10.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langfuse==4.0.1->-r requirements.txt (line 52)) (2.2.1)
Requirement already satisfied: opentelemetry-exporter-otlp-proto-http<2.0.0,>=1.33.1 in ./rag_part_four_env/lib/python3.11/site-packages (from langfuse==4.0.1->-r requirements.txt (line 52)) (1.39.1)
Requirement already satisfied: wrapt<2.0,>=1.14 in ./rag_part_four_env/lib/python3.11/site-packages (from langfuse==4.0.1->-r requirements.txt (line 52)) (1.17.3)
Collecting starlette>=0.27 (from mcp==1.26.0->-r requirements.txt (line 44))
  Using cached starlette-0.50.0-py3-none-any.whl.metadata (6.3 kB)
Requirement already satisfied: annotated-doc>=0.0.2 in ./rag_part_four_env/lib/python3.11/site-packages (from fastapi==0.128.1->-r requirements.txt (line 55)) (0.0.4)
Requirement already satisfied: h11>=0.8 in ./rag_part_four_env/lib/python3.11/site-packages (from uvicorn==0.40.0->-r requirements.txt (line 56)) (0.16.0)
Requirement already satisfied: psutil in ./rag_part_four_env/lib/python3.11/site-packages (from accelerate>=0.20.1->FlagEmbedding==1.3.5->-r requirements.txt (line 20)) (6.1.1)
Requirement already satisfied: safetensors>=0.4.3 in ./rag_part_four_env/lib/python3.11/site-packages (from accelerate>=0.20.1->FlagEmbedding==1.3.5->-r requirements.txt (line 20)) (0.7.0)
Requirement already satisfied: aiohappyeyeballs>=2.5.0 in ./rag_part_four_env/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.4.1->-r requirements.txt (line 10)) (2.6.1)
Requirement already satisfied: aiosignal>=1.4.0 in ./rag_part_four_env/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.4.1->-r requirements.txt (line 10)) (1.4.0)
Requirement already satisfied: attrs>=17.3.0 in ./rag_part_four_env/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.4.1->-r requirements.txt (line 10)) (25.4.0)
Requirement already satisfied: frozenlist>=1.1.1 in ./rag_part_four_env/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.4.1->-r requirements.txt (line 10)) (1.8.0)
Requirement already satisfied: multidict<7.0,>=4.5 in ./rag_part_four_env/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.4.1->-r requirements.txt (line 10)) (6.7.1)
Requirement already satisfied: propcache>=0.2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.4.1->-r requirements.txt (line 10)) (0.4.1)
Requirement already satisfied: yarl<2.0,>=1.17.0 in ./rag_part_four_env/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain-community==0.4.1->-r requirements.txt (line 10)) (1.22.0)
Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in ./rag_part_four_env/lib/python3.11/site-packages (from dataclasses-json<0.7.0,>=0.6.7->langchain-community==0.4.1->-r requirements.txt (line 10)) (3.26.2)
Requirement already satisfied: typing-inspect<1,>=0.4.0 in ./rag_part_four_env/lib/python3.11/site-packages (from dataclasses-json<0.7.0,>=0.6.7->langchain-community==0.4.1->-r requirements.txt (line 10)) (0.9.0)
Requirement already satisfied: jsonref<2.0.0,>=1.1.0 in ./rag_part_four_env/lib/python3.11/site-packages (from docling-core<3.0.0,>=2.70.0->docling-core[chunking]<3.0.0,>=2.70.0->docling==2.82.0->-r requirements.txt (line 30)) (1.1.0)
Collecting latex2mathml<4.0.0,>=3.77.0 (from docling-core<3.0.0,>=2.70.0->docling-core[chunking]<3.0.0,>=2.70.0->docling==2.82.0->-r requirements.txt (line 30))
  Downloading latex2mathml-3.81.0-py3-none-any.whl.metadata (15 kB)
Collecting pydantic-settings<3.0.0,>=2.10.1 (from langchain-community==0.4.1->-r requirements.txt (line 10))
  Downloading pydantic_settings-2.14.1-py3-none-any.whl.metadata (3.4 kB)
Collecting semchunk<4.0.0,>=2.2.0 (from docling-core[chunking]<3.0.0,>=2.70.0->docling==2.82.0->-r requirements.txt (line 30))
  Using cached semchunk-3.2.5-py3-none-any.whl.metadata (14 kB)
Requirement already satisfied: tree-sitter<0.27.0,>=0.25.0 in ./rag_part_four_env/lib/python3.11/site-packages (from docling-core[chunking]<3.0.0,>=2.70.0->docling==2.82.0->-r requirements.txt (line 30)) (0.25.2)
Requirement already satisfied: tree-sitter-python>=0.23.6 in ./rag_part_four_env/lib/python3.11/site-packages (from docling-core[chunking]<3.0.0,>=2.70.0->docling==2.82.0->-r requirements.txt (line 30)) (0.23.6)
Collecting tree-sitter-c>=0.23.4 (from docling-core[chunking]<3.0.0,>=2.70.0->docling==2.82.0->-r requirements.txt (line 30))
  Downloading tree_sitter_c-0.24.2-cp310-abi3-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (1.8 kB)
Collecting tree-sitter-javascript>=0.23.1 (from docling-core[chunking]<3.0.0,>=2.70.0->docling==2.82.0->-r requirements.txt (line 30))
  Using cached tree_sitter_javascript-0.25.0-cp310-abi3-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl.metadata (2.2 kB)
Collecting tree-sitter-typescript>=0.23.2 (from docling-core[chunking]<3.0.0,>=2.70.0->docling==2.82.0->-r requirements.txt (line 30))
  Using cached tree_sitter_typescript-0.23.2-cp39-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.3 kB)
Collecting jsonlines<5.0.0,>=3.1.0 (from docling-ibm-models<4,>=3.12.0->docling==2.82.0->-r requirements.txt (line 30))
  Using cached jsonlines-4.0.0-py3-none-any.whl.metadata (1.6 kB)
Requirement already satisfied: googleapis-common-protos<2.0.0,>=1.56.3 in ./rag_part_four_env/lib/python3.11/site-packages (from google-api-core<3.0.0,>=2.0.0->lightrag-hku==1.4.11->-r requirements.txt (line 49)) (1.72.0)
Requirement already satisfied: proto-plus<2.0.0,>=1.22.3 in ./rag_part_four_env/lib/python3.11/site-packages (from google-api-core<3.0.0,>=2.0.0->lightrag-hku==1.4.11->-r requirements.txt (line 49)) (1.27.1)
Requirement already satisfied: google-auth<3.0.0,>=2.14.1 in ./rag_part_four_env/lib/python3.11/site-packages (from google-api-core<3.0.0,>=2.0.0->lightrag-hku==1.4.11->-r requirements.txt (line 49)) (2.48.0)
Requirement already satisfied: pyasn1-modules>=0.2.1 in ./rag_part_four_env/lib/python3.11/site-packages (from google-auth<3.0.0,>=2.14.1->google-api-core<3.0.0,>=2.0.0->lightrag-hku==1.4.11->-r requirements.txt (line 49)) (0.4.2)
Requirement already satisfied: cryptography>=38.0.3 in ./rag_part_four_env/lib/python3.11/site-packages (from google-auth<3.0.0,>=2.14.1->google-api-core<3.0.0,>=2.0.0->lightrag-hku==1.4.11->-r requirements.txt (line 49)) (46.0.5)
Requirement already satisfied: rsa<5,>=3.1.4 in ./rag_part_four_env/lib/python3.11/site-packages (from google-auth<3.0.0,>=2.14.1->google-api-core<3.0.0,>=2.0.0->lightrag-hku==1.4.11->-r requirements.txt (line 49)) (4.9.1)
Requirement already satisfied: websockets<17.0,>=13.0.0 in ./rag_part_four_env/lib/python3.11/site-packages (from google-genai<2.0.0,>=1.56.0->langchain-google-genai==4.2.0->-r requirements.txt (line 9)) (15.0.1)
Requirement already satisfied: httpcore==1.* in ./rag_part_four_env/lib/python3.11/site-packages (from httpx<1,>=0.23.0->openai==2.21.0->-r requirements.txt (line 13)) (1.0.9)
Requirement already satisfied: filelock in ./rag_part_four_env/lib/python3.11/site-packages (from huggingface-hub>=0.20.0->sentence-transformers==5.2.2->-r requirements.txt (line 19)) (3.25.2)
Requirement already satisfied: fsspec>=2023.5.0 in ./rag_part_four_env/lib/python3.11/site-packages (from huggingface-hub>=0.20.0->sentence-transformers==5.2.2->-r requirements.txt (line 19)) (2025.3.0)
Requirement already satisfied: hf-xet<2.0.0,>=1.1.3 in ./rag_part_four_env/lib/python3.11/site-packages (from huggingface-hub>=0.20.0->sentence-transformers==5.2.2->-r requirements.txt (line 19)) (1.4.2)
Requirement already satisfied: MarkupSafe>=2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from jinja2->deepeval==3.9.2->-r requirements.txt (line 37)) (3.0.3)
Requirement already satisfied: jsonpointer>=1.9 in ./rag_part_four_env/lib/python3.11/site-packages (from jsonpatch<2.0.0,>=1.33.0->langchain-core==1.2.22->-r requirements.txt (line 6)) (3.0.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in ./rag_part_four_env/lib/python3.11/site-packages (from jsonschema>=4.19.0->chromadb==1.5.0->-r requirements.txt (line 16)) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in ./rag_part_four_env/lib/python3.11/site-packages (from jsonschema>=4.19.0->chromadb==1.5.0->-r requirements.txt (line 16)) (0.36.2)
Requirement already satisfied: rpds-py>=0.25.0 in ./rag_part_four_env/lib/python3.11/site-packages (from jsonschema>=4.19.0->chromadb==1.5.0->-r requirements.txt (line 16)) (0.30.0)
INFO: pip is looking at multiple versions of langchain-classic to determine which version is compatible with other requirements. This could take a while.
Collecting langchain-classic<2.0.0,>=1.0.0 (from langchain-community==0.4.1->-r requirements.txt (line 10))
  Downloading langchain_classic-1.0.7-py3-none-any.whl.metadata (5.1 kB)
  Downloading langchain_classic-1.0.6-py3-none-any.whl.metadata (5.1 kB)
  Downloading langchain_classic-1.0.5-py3-none-any.whl.metadata (5.1 kB)
  Downloading langchain_classic-1.0.4-py3-none-any.whl.metadata (4.8 kB)
  Downloading langchain_classic-1.0.2-py3-none-any.whl.metadata (4.8 kB)
Requirement already satisfied: langgraph-checkpoint<5.0.0,>=2.1.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langgraph<1.1.0,>=1.0.7->langchain==1.2.9->-r requirements.txt (line 5)) (4.0.1)
Requirement already satisfied: langgraph-prebuilt<1.1.0,>=1.0.8 in ./rag_part_four_env/lib/python3.11/site-packages (from langgraph<1.1.0,>=1.0.7->langchain==1.2.9->-r requirements.txt (line 5)) (1.0.13)
Requirement already satisfied: langgraph-sdk<0.4.0,>=0.3.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langgraph<1.1.0,>=1.0.7->langchain==1.2.9->-r requirements.txt (line 5)) (0.3.12)
Requirement already satisfied: ormsgpack>=1.12.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langgraph-checkpoint<5.0.0,>=2.1.0->langgraph<1.1.0,>=1.0.7->langchain==1.2.9->-r requirements.txt (line 5)) (1.12.2)
INFO: pip is looking at multiple versions of langgraph-prebuilt to determine which version is compatible with other requirements. This could take a while.
Collecting langgraph-prebuilt<1.1.0,>=1.0.8 (from langgraph<1.1.0,>=1.0.7->langchain==1.2.9->-r requirements.txt (line 5))
  Downloading langgraph_prebuilt-1.0.12-py3-none-any.whl.metadata (5.2 kB)
  Downloading langgraph_prebuilt-1.0.11-py3-none-any.whl.metadata (5.2 kB)
  Downloading langgraph_prebuilt-1.0.10-py3-none-any.whl.metadata (5.2 kB)
Requirement already satisfied: requests-toolbelt>=1.0.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core==1.2.22->-r requirements.txt (line 6)) (1.0.0)
Requirement already satisfied: zstandard>=0.23.0 in ./rag_part_four_env/lib/python3.11/site-packages (from langsmith<1.0.0,>=0.3.45->langchain-core==1.2.22->-r requirements.txt (line 6)) (0.25.0)
Requirement already satisfied: importlib-metadata<8.8.0,>=6.0 in ./rag_part_four_env/lib/python3.11/site-packages (from opentelemetry-api>=1.2.0->chromadb==1.5.0->-r requirements.txt (line 16)) (7.2.1)
Requirement already satisfied: zipp>=0.5 in ./rag_part_four_env/lib/python3.11/site-packages (from importlib-metadata<8.8.0,>=6.0->opentelemetry-api>=1.2.0->chromadb==1.5.0->-r requirements.txt (line 16)) (3.23.0)
Collecting opentelemetry-exporter-otlp-proto-common==1.39.1 (from opentelemetry-exporter-otlp-proto-http<2.0.0,>=1.33.1->langfuse==4.0.1->-r requirements.txt (line 52))
  Using cached opentelemetry_exporter_otlp_proto_common-1.39.1-py3-none-any.whl.metadata (1.8 kB)
Collecting opentelemetry-proto==1.39.1 (from opentelemetry-exporter-otlp-proto-http<2.0.0,>=1.33.1->langfuse==4.0.1->-r requirements.txt (line 52))
  Using cached opentelemetry_proto-1.39.1-py3-none-any.whl.metadata (2.3 kB)
Collecting opentelemetry-sdk>=1.2.0 (from chromadb==1.5.0->-r requirements.txt (line 16))
  Using cached opentelemetry_sdk-1.39.1-py3-none-any.whl.metadata (1.5 kB)
Collecting opentelemetry-api>=1.2.0 (from chromadb==1.5.0->-r requirements.txt (line 16))
  Using cached opentelemetry_api-1.39.1-py3-none-any.whl.metadata (1.5 kB)
Collecting opentelemetry-semantic-conventions==0.60b1 (from opentelemetry-sdk>=1.2.0->chromadb==1.5.0->-r requirements.txt (line 16))
  Using cached opentelemetry_semantic_conventions-0.60b1-py3-none-any.whl.metadata (2.4 kB)
Requirement already satisfied: six>=1.5 in ./rag_part_four_env/lib/python3.11/site-packages (from posthog<6.0.0,>=2.4.0->chromadb==1.5.0->-r requirements.txt (line 16)) (1.17.0)
Requirement already satisfied: pyclipper>=1.2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from rapidocr<4.0.0,>=3.3->docling==2.82.0->-r requirements.txt (line 30)) (1.4.0)
Requirement already satisfied: opencv_python>=4.5.1.48 in ./rag_part_four_env/lib/python3.11/site-packages (from rapidocr<4.0.0,>=3.3->docling==2.82.0->-r requirements.txt (line 30)) (4.11.0.86)
Requirement already satisfied: Shapely!=2.0.4,>=1.7.1 in ./rag_part_four_env/lib/python3.11/site-packages (from rapidocr<4.0.0,>=3.3->docling==2.82.0->-r requirements.txt (line 30)) (2.1.2)
Requirement already satisfied: omegaconf in ./rag_part_four_env/lib/python3.11/site-packages (from rapidocr<4.0.0,>=3.3->docling==2.82.0->-r requirements.txt (line 30)) (2.3.0)
Requirement already satisfied: colorlog in ./rag_part_four_env/lib/python3.11/site-packages (from rapidocr<4.0.0,>=3.3->docling==2.82.0->-r requirements.txt (line 30)) (6.10.1)
Requirement already satisfied: markdown-it-py>=2.2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from rich>=10.11.0->chromadb==1.5.0->-r requirements.txt (line 16)) (4.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in ./rag_part_four_env/lib/python3.11/site-packages (from rich>=10.11.0->chromadb==1.5.0->-r requirements.txt (line 16)) (2.19.2)
Requirement already satisfied: pyasn1>=0.1.3 in ./rag_part_four_env/lib/python3.11/site-packages (from rsa<5,>=3.1.4->google-auth<3.0.0,>=2.14.1->google-api-core<3.0.0,>=2.0.0->lightrag-hku==1.4.11->-r requirements.txt (line 49)) (0.6.2)
Collecting mpire[dill] (from semchunk<4.0.0,>=2.2.0->docling-core[chunking]<3.0.0,>=2.70.0->docling==2.82.0->-r requirements.txt (line 30))
  Using cached mpire-2.10.2-py3-none-any.whl.metadata (14 kB)
Requirement already satisfied: greenlet>=1 in ./rag_part_four_env/lib/python3.11/site-packages (from SQLAlchemy<3.0.0,>=1.4.0->langchain-community==0.4.1->-r requirements.txt (line 10)) (3.3.2)
Requirement already satisfied: sympy==1.13.1 in ./rag_part_four_env/lib/python3.11/site-packages (from torch>=1.11.0->sentence-transformers==5.2.2->-r requirements.txt (line 19)) (1.13.1)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in ./rag_part_four_env/lib/python3.11/site-packages (from sympy==1.13.1->torch>=1.11.0->sentence-transformers==5.2.2->-r requirements.txt (line 19)) (1.3.0)
Requirement already satisfied: shellingham>=1.3.0 in ./rag_part_four_env/lib/python3.11/site-packages (from typer>=0.9.0->chromadb==1.5.0->-r requirements.txt (line 16)) (1.5.4)
Requirement already satisfied: mypy-extensions>=0.3.0 in ./rag_part_four_env/lib/python3.11/site-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.7.0,>=0.6.7->langchain-community==0.4.1->-r requirements.txt (line 10)) (1.1.0)
Requirement already satisfied: pyproject_hooks in ./rag_part_four_env/lib/python3.11/site-packages (from build>=1.0.3->chromadb==1.5.0->-r requirements.txt (line 16)) (1.2.0)
Requirement already satisfied: cffi>=2.0.0 in ./rag_part_four_env/lib/python3.11/site-packages (from cryptography>=38.0.3->google-auth<3.0.0,>=2.14.1->google-api-core<3.0.0,>=2.0.0->lightrag-hku==1.4.11->-r requirements.txt (line 49)) (2.0.0)
Requirement already satisfied: pycparser in ./rag_part_four_env/lib/python3.11/site-packages (from cffi>=2.0.0->cryptography>=38.0.3->google-auth<3.0.0,>=2.14.1->google-api-core<3.0.0,>=2.0.0->lightrag-hku==1.4.11->-r requirements.txt (line 49)) (3.0)
Requirement already satisfied: pyarrow>=15.0.0 in ./rag_part_four_env/lib/python3.11/site-packages (from datasets>=2.19.0->FlagEmbedding==1.3.5->-r requirements.txt (line 20)) (22.0.0)
Requirement already satisfied: dill<0.3.9,>=0.3.0 in ./rag_part_four_env/lib/python3.11/site-packages (from datasets>=2.19.0->FlagEmbedding==1.3.5->-r requirements.txt (line 20)) (0.3.8)
Requirement already satisfied: multiprocess<0.70.17 in ./rag_part_four_env/lib/python3.11/site-packages (from datasets>=2.19.0->FlagEmbedding==1.3.5->-r requirements.txt (line 20)) (0.70.16)
Requirement already satisfied: websocket-client!=0.40.0,!=0.41.*,!=0.42.*,>=0.32.0 in ./rag_part_four_env/lib/python3.11/site-packages (from kubernetes>=28.1.0->chromadb==1.5.0->-r requirements.txt (line 16)) (1.9.0)
Requirement already satisfied: requests-oauthlib in ./rag_part_four_env/lib/python3.11/site-packages (from kubernetes>=28.1.0->chromadb==1.5.0->-r requirements.txt (line 16)) (1.3.1)
Requirement already satisfied: durationpy>=0.7 in ./rag_part_four_env/lib/python3.11/site-packages (from kubernetes>=28.1.0->chromadb==1.5.0->-r requirements.txt (line 16)) (0.10)
Requirement already satisfied: fastuuid>=0.13.0 in ./rag_part_four_env/lib/python3.11/site-packages (from litellm>=1.64.0->dspy==3.1.3->-r requirements.txt (line 46)) (0.14.0)
Requirement already satisfied: mdurl~=0.1 in ./rag_part_four_env/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->chromadb==1.5.0->-r requirements.txt (line 16)) (0.1.2)
Requirement already satisfied: coloredlogs in ./rag_part_four_env/lib/python3.11/site-packages (from onnxruntime>=1.14.1->chromadb==1.5.0->-r requirements.txt (line 16)) (15.0.1)
Requirement already satisfied: flatbuffers in ./rag_part_four_env/lib/python3.11/site-packages (from onnxruntime>=1.14.1->chromadb==1.5.0->-r requirements.txt (line 16)) (25.12.19)
INFO: pip is looking at multiple versions of opentelemetry-exporter-otlp-proto-grpc to determine which version is compatible with other requirements. This could take a while.
Collecting opentelemetry-exporter-otlp-proto-grpc>=1.2.0 (from chromadb==1.5.0->-r requirements.txt (line 16))
  Downloading opentelemetry_exporter_otlp_proto_grpc-1.42.1-py3-none-any.whl.metadata (2.6 kB)
  Downloading opentelemetry_exporter_otlp_proto_grpc-1.42.0-py3-none-any.whl.metadata (2.6 kB)
  Downloading opentelemetry_exporter_otlp_proto_grpc-1.41.1-py3-none-any.whl.metadata (2.6 kB)
  Downloading opentelemetry_exporter_otlp_proto_grpc-1.41.0-py3-none-any.whl.metadata (2.6 kB)
  Using cached opentelemetry_exporter_otlp_proto_grpc-1.40.0-py3-none-any.whl.metadata (2.6 kB)
  Using cached opentelemetry_exporter_otlp_proto_grpc-1.39.1-py3-none-any.whl.metadata (2.5 kB)
Collecting alembic>=1.5.0 (from optuna>=3.4.0->dspy==3.1.3->-r requirements.txt (line 46))
  Using cached alembic-1.18.4-py3-none-any.whl.metadata (7.2 kB)
Collecting Mako (from alembic>=1.5.0->optuna>=3.4.0->dspy==3.1.3->-r requirements.txt (line 46))
  Downloading mako-1.3.12-py3-none-any.whl.metadata (2.9 kB)
Collecting faker>=5.0.0 (from polyfactory>=2.22.2->docling==2.82.0->-r requirements.txt (line 30))
  Downloading faker-40.19.1-py3-none-any.whl.metadata (16 kB)
Requirement already satisfied: httptools>=0.6.3 in ./rag_part_four_env/lib/python3.11/site-packages (from uvicorn[standard]>=0.18.3->chromadb==1.5.0->-r requirements.txt (line 16)) (0.7.1)
Requirement already satisfied: uvloop>=0.15.1 in ./rag_part_four_env/lib/python3.11/site-packages (from uvicorn[standard]>=0.18.3->chromadb==1.5.0->-r requirements.txt (line 16)) (0.21.0)
Requirement already satisfied: watchfiles>=0.13 in ./rag_part_four_env/lib/python3.11/site-packages (from uvicorn[standard]>=0.18.3->chromadb==1.5.0->-r requirements.txt (line 16)) (1.1.1)
Requirement already satisfied: humanfriendly>=9.1 in ./rag_part_four_env/lib/python3.11/site-packages (from coloredlogs->onnxruntime>=1.14.1->chromadb==1.5.0->-r requirements.txt (line 16)) (10.0)
Collecting inscriptis>=2.2.0 (from ir-datasets->FlagEmbedding==1.3.5->-r requirements.txt (line 20))
  Using cached inscriptis-2.7.1-py3-none-any.whl.metadata (27 kB)
Collecting trec-car-tools>=2.5.4 (from ir-datasets->FlagEmbedding==1.3.5->-r requirements.txt (line 20))
  Using cached trec_car_tools-2.6-py3-none-any.whl.metadata (640 bytes)
Collecting lz4>=3.1.10 (from ir-datasets->FlagEmbedding==1.3.5->-r requirements.txt (line 20))
  Using cached lz4-4.4.5-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (3.8 kB)
Collecting warc3-wet>=0.2.3 (from ir-datasets->FlagEmbedding==1.3.5->-r requirements.txt (line 20))
  Using cached warc3_wet-0.2.5-py3-none-any.whl.metadata (2.2 kB)
Collecting warc3-wet-clueweb09>=0.2.5 (from ir-datasets->FlagEmbedding==1.3.5->-r requirements.txt (line 20))
  Using cached warc3_wet_clueweb09-0.2.5-py3-none-any.whl
Collecting zlib-state>=0.1.3 (from ir-datasets->FlagEmbedding==1.3.5->-r requirements.txt (line 20))
  Downloading zlib_state-0.1.12-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (3.5 kB)
Requirement already satisfied: ijson>=3.1.3 in ./rag_part_four_env/lib/python3.11/site-packages (from ir-datasets->FlagEmbedding==1.3.5->-r requirements.txt (line 20)) (3.5.0)
Collecting unlzw3>=0.2.1 (from ir-datasets->FlagEmbedding==1.3.5->-r requirements.txt (line 20))
  Using cached unlzw3-0.2.3-py3-none-any.whl.metadata (2.3 kB)
Collecting cbor>=1.0.0 (from trec-car-tools>=2.5.4->ir-datasets->FlagEmbedding==1.3.5->-r requirements.txt (line 20))
  Using cached cbor-1.0.0-cp311-cp311-linux_x86_64.whl
Requirement already satisfied: antlr4-python3-runtime==4.9.* in ./rag_part_four_env/lib/python3.11/site-packages (from omegaconf->rapidocr<4.0.0,>=3.3->docling==2.82.0->-r requirements.txt (line 30)) (4.9.3)
Collecting ascii_colors>=0.11.11 (from pipmaster->lightrag-hku==1.4.11->-r requirements.txt (line 49))
  Using cached ascii_colors-0.11.21-py3-none-any.whl.metadata (35 kB)
Requirement already satisfied: wcwidth in ./rag_part_four_env/lib/python3.11/site-packages (from ascii_colors>=0.11.11->pipmaster->lightrag-hku==1.4.11->-r requirements.txt (line 49)) (0.6.0)
Requirement already satisfied: iniconfig>=1.0.1 in ./rag_part_four_env/lib/python3.11/site-packages (from pytest->deepeval==3.9.2->-r requirements.txt (line 37)) (2.3.0)
Collecting execnet>=2.1 (from pytest-xdist->deepeval==3.9.2->-r requirements.txt (line 37))
  Using cached execnet-2.1.2-py3-none-any.whl.metadata (2.9 kB)
Requirement already satisfied: oauthlib>=3.0.0 in ./rag_part_four_env/lib/python3.11/site-packages (from requests-oauthlib->kubernetes>=28.1.0->chromadb==1.5.0->-r requirements.txt (line 16)) (3.3.1)
Requirement already satisfied: threadpoolctl>=3.2.0 in ./rag_part_four_env/lib/python3.11/site-packages (from scikit-learn->sentence-transformers==5.2.2->-r requirements.txt (line 19)) (3.6.0)
Using cached langchain-1.2.9-py3-none-any.whl (111 kB)
Using cached langchain_core-1.2.22-py3-none-any.whl (506 kB)
Using cached pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (806 kB)
Using cached langchain_openai-1.1.10-py3-none-any.whl (87 kB)
Using cached openai-2.21.0-py3-none-any.whl (1.1 MB)
Using cached langchain_anthropic-1.4.0-py3-none-any.whl (48 kB)
Using cached langchain_google_genai-4.2.0-py3-none-any.whl (66 kB)
Using cached langchain_text_splitters-1.1.0-py3-none-any.whl (34 kB)
Using cached langchain_chroma-1.1.0-py3-none-any.whl (12 kB)
Using cached chromadb-1.5.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (21.4 MB)
Using cached sentence_transformers-5.2.2-py3-none-any.whl (494 kB)
Using cached pypdf-6.7.0-py3-none-any.whl (330 kB)
Using cached docling-2.82.0-py3-none-any.whl (446 kB)
Using cached chonkie-1.6.1-py3-none-any.whl (233 kB)
Using cached nltk-3.9.2-py3-none-any.whl (1.5 MB)
Using cached deepeval-3.9.2-py3-none-any.whl (839 kB)
Using cached python_dotenv-1.2.1-py3-none-any.whl (21 kB)
Using cached dspy-3.1.3-py3-none-any.whl (312 kB)
Using cached lightrag_hku-1.4.11-py3-none-any.whl (3.6 MB)
Using cached numpy-2.4.2-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (16.9 MB)
Using cached langfuse-4.0.1-py3-none-any.whl (465 kB)
Using cached fastapi-0.128.1-py3-none-any.whl (103 kB)
Using cached uvicorn-0.40.0-py3-none-any.whl (68 kB)
Using cached asyncer-0.0.8-py3-none-any.whl (9.2 kB)
Using cached gepa-0.0.26-py3-none-any.whl (139 kB)
Downloading click-8.3.3-py3-none-any.whl (110 kB)
Downloading docling_core-2.77.0-py3-none-any.whl (283 kB)
Downloading docling_ibm_models-3.13.2-py3-none-any.whl (94 kB)
Downloading docling_parse-5.11.0-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl (10.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.2/10.2 MB 7.5 MB/s  0:00:01
Using cached jsonlines-4.0.0-py3-none-any.whl (8.7 kB)
Downloading langchain_classic-1.0.2-py3-none-any.whl (1.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.0/1.0 MB 19.5 MB/s  0:00:00
Downloading langgraph-1.0.10-py3-none-any.whl (160 kB)
Downloading langgraph_prebuilt-1.0.10-py3-none-any.whl (36 kB)
Downloading latex2mathml-3.81.0-py3-none-any.whl (79 kB)
Using cached marko-2.2.2-py3-none-any.whl (42 kB)
Using cached opentelemetry_exporter_otlp_proto_common-1.39.1-py3-none-any.whl (18 kB)
Using cached opentelemetry_proto-1.39.1-py3-none-any.whl (72 kB)
Using cached opentelemetry_sdk-1.39.1-py3-none-any.whl (132 kB)
Using cached opentelemetry_api-1.39.1-py3-none-any.whl (66 kB)
Using cached opentelemetry_semantic_conventions-0.60b1-py3-none-any.whl (219 kB)
Downloading pydantic_settings-2.14.1-py3-none-any.whl (60 kB)
Downloading rapidocr-3.8.1-py3-none-any.whl (15.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 15.1/15.1 MB 25.2 MB/s  0:00:00
Using cached rtree-1.4.1-py3-none-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (507 kB)
Using cached semchunk-3.2.5-py3-none-any.whl (13 kB)
Using cached starlette-0.50.0-py3-none-any.whl (74 kB)
Downloading typer-0.21.2-py3-none-any.whl (56 kB)
Downloading chonkie_core-0.10.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (394 kB)
Downloading json_repair-0.59.10-py3-none-any.whl (47 kB)
Using cached opentelemetry_exporter_otlp_proto_grpc-1.39.1-py3-none-any.whl (19 kB)
Using cached optuna-4.8.0-py3-none-any.whl (419 kB)
Using cached alembic-1.18.4-py3-none-any.whl (263 kB)
Using cached polyfactory-3.3.0-py3-none-any.whl (62 kB)
Downloading faker-40.19.1-py3-none-any.whl (2.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 19.8 MB/s  0:00:00
Downloading tree_sitter_c-0.24.2-cp310-abi3-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (94 kB)
Using cached tree_sitter_javascript-0.25.0-cp310-abi3-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl (99 kB)
Using cached tree_sitter_typescript-0.23.2-cp39-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (344 kB)
Using cached configparser-7.2.0-py3-none-any.whl (17 kB)
Using cached ir_datasets-0.5.11-py3-none-any.whl (866 kB)
Using cached inscriptis-2.7.1-py3-none-any.whl (45 kB)
Using cached lz4-4.4.5-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (1.4 MB)
Using cached trec_car_tools-2.6-py3-none-any.whl (8.4 kB)
Using cached unlzw3-0.2.3-py3-none-any.whl (6.7 kB)
Using cached warc3_wet-0.2.5-py3-none-any.whl (18 kB)
Downloading zlib_state-0.1.12-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (21 kB)
Downloading mako-1.3.12-py3-none-any.whl (78 kB)
Using cached mpire-2.10.2-py3-none-any.whl (272 kB)
Using cached nano_vectordb-0.0.4.3-py3-none-any.whl (5.6 kB)
Downloading peft-0.19.1-py3-none-any.whl (680 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 680.7/680.7 kB 19.9 MB/s  0:00:00
Downloading pipmaster-1.1.13-py3-none-any.whl (37 kB)
Using cached ascii_colors-0.11.21-py3-none-any.whl (84 kB)
Using cached pyfiglet-1.0.4-py3-none-any.whl (1.8 MB)
Using cached pypinyin-0.55.0-py2.py3-none-any.whl (840 kB)
Using cached pytest_repeat-0.9.4-py3-none-any.whl (4.2 kB)
Downloading pytest_rerunfailures-16.3-py3-none-any.whl (15 kB)
Using cached pytest_xdist-3.8.0-py3-none-any.whl (46 kB)
Using cached execnet-2.1.2-py3-none-any.whl (40 kB)
Installing collected packages: warc3-wet-clueweb09, warc3-wet, pylatexenc, cbor, zlib-state, unlzw3, tree-sitter-typescript, tree-sitter-javascript, tree-sitter-c, rtree, PyYAML, python-dotenv, pypinyin, pypdf, pyfiglet, opentelemetry-proto, numpy, mpire, marko, Mako, lz4, latex2mathml, jsonlines, json-repair, gepa, faker, execnet, configparser, click, ascii_colors, uvicorn, trec-car-tools, starlette, pytest-xdist, pytest-rerunfailures, pytest-repeat, polyfactory, pipmaster, opentelemetry-exporter-otlp-proto-common, opentelemetry-api, nltk, nano-vectordb, inscriptis, chonkie-core, asyncer, alembic, typer, semchunk, rapidocr, pydantic-settings, optuna, opentelemetry-semantic-conventions, openai, ir-datasets, fastapi, chonkie, opentelemetry-sdk, langchain-core, docling-core, sentence-transformers, peft, opentelemetry-exporter-otlp-proto-grpc, langchain-text-splitters, langchain-openai, langchain-anthropic, dspy, docling-parse, docling-ibm-models, deepeval, lightrag-hku, langgraph-prebuilt, langfuse, langchain-google-genai, langchain-classic, FlagEmbedding, docling, chromadb, langgraph, langchain-chroma, langchain
  Attempting uninstall: PyYAML
    Found existing installation: PyYAML 6.0.2
    Uninstalling PyYAML-6.0.2:
      Successfully uninstalled PyYAML-6.0.2
  Attempting uninstall: python-dotenv
    Found existing installation: python-dotenv 1.1.1
    Uninstalling python-dotenv-1.1.1:
      Successfully uninstalled python-dotenv-1.1.1
  Attempting uninstall: pypdf
    Found existing installation: pypdf 3.17.4
    Uninstalling pypdf-3.17.4:
      Successfully uninstalled pypdf-3.17.4
  Attempting uninstall: opentelemetry-proto
    Found existing installation: opentelemetry-proto 1.34.1
    Uninstalling opentelemetry-proto-1.34.1:
      Successfully uninstalled opentelemetry-proto-1.34.1
  Attempting uninstall: numpy
    Found existing installation: numpy 2.3.5
    Uninstalling numpy-2.3.5:
      Successfully uninstalled numpy-2.3.5
  Attempting uninstall: json-repair
    Found existing installation: json_repair 0.25.3
    Uninstalling json_repair-0.25.3:
      Successfully uninstalled json_repair-0.25.3
  Attempting uninstall: click
    Found existing installation: click 8.4.0
    Uninstalling click-8.4.0:
      Successfully uninstalled click-8.4.0
  Attempting uninstall: uvicorn
    Found existing installation: uvicorn 0.31.1
    Uninstalling uvicorn-0.31.1:
      Successfully uninstalled uvicorn-0.31.1
  Attempting uninstall: starlette
    Found existing installation: starlette 0.52.1
    Uninstalling starlette-0.52.1:
      Successfully uninstalled starlette-0.52.1
  Attempting uninstall: opentelemetry-exporter-otlp-proto-common
    Found existing installation: opentelemetry-exporter-otlp-proto-common 1.34.1
    Uninstalling opentelemetry-exporter-otlp-proto-common-1.34.1:
      Successfully uninstalled opentelemetry-exporter-otlp-proto-common-1.34.1
  Attempting uninstall: opentelemetry-api
    Found existing installation: opentelemetry-api 1.34.1
    Uninstalling opentelemetry-api-1.34.1:
      Successfully uninstalled opentelemetry-api-1.34.1
  Attempting uninstall: nltk
    Found existing installation: nltk 3.9.3
    Uninstalling nltk-3.9.3:
      Successfully uninstalled nltk-3.9.3
  Attempting uninstall: typer
    Found existing installation: typer 0.23.0
    Uninstalling typer-0.23.0:
      Successfully uninstalled typer-0.23.0
  Attempting uninstall: pydantic-settings
    Found existing installation: pydantic-settings 2.10.1
    Uninstalling pydantic-settings-2.10.1:
      Successfully uninstalled pydantic-settings-2.10.1
  Attempting uninstall: opentelemetry-semantic-conventions
    Found existing installation: opentelemetry-semantic-conventions 0.55b1
    Uninstalling opentelemetry-semantic-conventions-0.55b1:
      Successfully uninstalled opentelemetry-semantic-conventions-0.55b1
  Attempting uninstall: openai
    Found existing installation: openai 2.29.0
    Uninstalling openai-2.29.0:
      Successfully uninstalled openai-2.29.0
  Attempting uninstall: fastapi
    Found existing installation: fastapi 0.128.8
    Uninstalling fastapi-0.128.8:
      Successfully uninstalled fastapi-0.128.8
  Attempting uninstall: opentelemetry-sdk
    Found existing installation: opentelemetry-sdk 1.34.1
    Uninstalling opentelemetry-sdk-1.34.1:
      Successfully uninstalled opentelemetry-sdk-1.34.1
  Attempting uninstall: langchain-core
    Found existing installation: langchain-core 1.3.3
    Uninstalling langchain-core-1.3.3:
      Successfully uninstalled langchain-core-1.3.3
  Attempting uninstall: sentence-transformers
    Found existing installation: sentence-transformers 5.2.3
    Uninstalling sentence-transformers-5.2.3:
      Successfully uninstalled sentence-transformers-5.2.3
  Attempting uninstall: opentelemetry-exporter-otlp-proto-grpc
    Found existing installation: opentelemetry-exporter-otlp-proto-grpc 1.34.1
    Uninstalling opentelemetry-exporter-otlp-proto-grpc-1.34.1:
      Successfully uninstalled opentelemetry-exporter-otlp-proto-grpc-1.34.1
  Attempting uninstall: langchain-text-splitters
    Found existing installation: langchain-text-splitters 1.1.1
    Uninstalling langchain-text-splitters-1.1.1:
      Successfully uninstalled langchain-text-splitters-1.1.1
  Attempting uninstall: langchain-openai
    Found existing installation: langchain-openai 1.1.11
    Uninstalling langchain-openai-1.1.11:
      Successfully uninstalled langchain-openai-1.1.11
  Attempting uninstall: langgraph-prebuilt
    Found existing installation: langgraph-prebuilt 1.0.13
    Uninstalling langgraph-prebuilt-1.0.13:
      Successfully uninstalled langgraph-prebuilt-1.0.13
  Attempting uninstall: langchain-classic
    Found existing installation: langchain-classic 1.0.3
    Uninstalling langchain-classic-1.0.3:
      Successfully uninstalled langchain-classic-1.0.3
  Attempting uninstall: chromadb
    Found existing installation: chromadb 1.1.1
    Uninstalling chromadb-1.1.1:
      Successfully uninstalled chromadb-1.1.1
  Attempting uninstall: langgraph
    Found existing installation: langgraph 1.1.10
    Uninstalling langgraph-1.1.10:
      Successfully uninstalled langgraph-1.1.10
  Attempting uninstall: langchain
    Found existing installation: langchain 1.2.13
    Uninstalling langchain-1.2.13:
      Successfully uninstalled langchain-1.2.13

Successfully installed FlagEmbedding-1.3.5 Mako-1.3.12 PyYAML-6.0.3 alembic-1.18.4 ascii_colors-0.11.21 asyncer-0.0.8 cbor-1.0.0 chonkie-1.6.1 chonkie-core-0.10.1 chromadb-1.5.0 click-8.3.3 configparser-7.2.0 deepeval-3.9.2 docling-2.82.0 docling-core-2.77.0 docling-ibm-models-3.13.2 docling-parse-5.11.0 dspy-3.1.3 execnet-2.1.2 faker-40.19.1 fastapi-0.128.1 gepa-0.0.26 inscriptis-2.7.1 ir-datasets-0.5.11 json-repair-0.59.10 jsonlines-4.0.0 langchain-1.2.9 langchain-anthropic-1.4.0 langchain-chroma-1.1.0 langchain-classic-1.0.2 langchain-core-1.2.22 langchain-google-genai-4.2.0 langchain-openai-1.1.10 langchain-text-splitters-1.1.0 langfuse-4.0.1 langgraph-1.0.10 langgraph-prebuilt-1.0.10 latex2mathml-3.81.0 lightrag-hku-1.4.11 lz4-4.4.5 marko-2.2.2 mpire-2.10.2 nano-vectordb-0.0.4.3 nltk-3.9.2 numpy-2.4.2 openai-2.21.0 opentelemetry-api-1.39.1 opentelemetry-exporter-otlp-proto-common-1.39.1 opentelemetry-exporter-otlp-proto-grpc-1.39.1 opentelemetry-proto-1.39.1 opentelemetry-sdk-1.39.1 opentelemetry-semantic-conventions-0.60b1 optuna-4.8.0 peft-0.19.1 pipmaster-1.1.13 polyfactory-3.3.0 pydantic-settings-2.14.1 pyfiglet-1.0.4 pylatexenc-2.10 pypdf-6.7.0 pypinyin-0.55.0 pytest-repeat-0.9.4 pytest-rerunfailures-16.3 pytest-xdist-3.8.0 python-dotenv-1.2.1 rapidocr-3.8.1 rtree-1.4.1 semchunk-3.2.5 sentence-transformers-5.2.2 starlette-0.50.0 trec-car-tools-2.6 tree-sitter-c-0.24.2 tree-sitter-javascript-0.25.0 tree-sitter-typescript-0.23.2 typer-0.21.2 unlzw3-0.2.3 uvicorn-0.40.0 warc3-wet-0.2.5 warc3-wet-clueweb09-0.2.5 zlib-state-0.1.12

## Counterfactual Queries



## Data Sources

- NASA Landsat SR via Google Earth Engine
- LANDFIRE EVT/EVC/FBFM40
- NASA RECOVER 2.0 (29-layer base package)
- Cal-Adapt climakitae Python SDK
- Meta SAM 3 asset segmentation outputs

## Author

Dr. Sandeep Grover - PhD Data Science, Causal Inference Research
