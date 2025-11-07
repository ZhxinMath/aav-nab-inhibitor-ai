# AI-Guided Inhibitory Peptides to Counteract AAV Neutralizing Antibodies

## Overview
This repository contains the implementation of sequence-based artificial intelligence models for designing inhibitory peptides that counteract Adeno-associated virus (AAV) neutralizing antibodies (NAbs) in gene therapy. Our approach leverages multiple AI architectures to identify optimal peptide sequences that can overcome one of the major barriers in AAV gene therapy applications.

## Abstract
Neutralizing antibodies (NAbs) against AAV represent a primary barrier to both initial and repeated gene therapy administration. To address this challenge, we developed sequence-based AI models capable of distinguishing human-derived and virus-derived amino acid sequences. Our framework includes BERT-pretrained models, ESM-LoRA structured models, NLP-metaxa, and Random Forest models, achieving accuracy rates of 84-90% with 20-aa sequences identified as the optimal distinguishing length.

Using these AI models, we predicted "virus-source" sequences from over 1,500 virtually generated 20-aa sequences derived from two AAV serotype capsids. The strategy's effectiveness was validated in NAb-driven disorders, demonstrating that AI-designed peptides have robust NAb-blocking capacity without inducing antigenicity or inflammatory responses.

## Repository Structure

### Core Implementation Files
- `step1_Pretrain_BERT_model.ipynb` - BERT model pretraining for sequence classification
- `step2_LoRA_Post_train_ESM_model.ipynb` - ESM model with LoRA fine-tuning
- `step3_Finetune_BERT_model.ipynb` - BERT model fine-tuning on specific tasks
- `step4_LoRA_Finetune_ESM_model.ipynb` - ESM-LoRA model fine-tuning
- `step5_VAE_generate_sequences.ipynb` - Variational Autoencoder for synthetic peptide generation

### Supporting Modules
- `data_util.py` - Data processing and utility functions
- `encoding_matrix.py` - Amino acid encoding and feature extraction
- `vocab.txt` - Vocabulary for NLP models
- `requirements.txt` - Python dependencies

### Data
- `data/` - Directory containing training and validation datasets

## Pretrained Model
All the model pre-trained in different step can be found in https://doi.org/10.5281/zenodo.17551427

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/aav-nab-inhibitor-ai.git
cd aav-nab-inhibitor-ai
