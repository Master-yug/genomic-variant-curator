
# Genomic Variant Curator (OpenEnv)

## Overview
The **Genomic Variant Curator** is a high-fidelity Reinforcement Learning (RL) environment designed to train and evaluate AI agents in the field of clinical bioinformatics. The agent acts as a molecular pathologist, tasked with classifying genetic mutations as Pathogenic (disease-causing) or Benign (harmless).
## Key Implementations of the project so far.
-   **Massive Scale:** Powered by a curated subset of 13,306 human proteins from the UniProtKB/Swiss-Prot (Reviewed) database.    
-   **Real-World Utility:** Mirrors the actual workflow of clinical variant scientists who must synthesize protein functional data, subcellular localization, and domain importance.    
-   **Diverse Challenges:** Over 30,000+ unique variant-label pairs ranging from clear-cut pathogenic mutations to complex "Variants of Uncertain Significance" (VUS).    
-   **Offline-Ready:** All data is packaged locally in a lightweight `.jsonl` format, ensuring high-speed training without API rate limits or privacy concerns.  

## 🛠️ Environment Specification
-   **Action Space:** Discrete tool-use (e.g., `query_function`, `query_location`) and a final `submit_classification`.    
-   **Observation Space:** Textual and structured data including HGNC Gene Symbols, UniProt Accessions, and Mutation descriptions (e.g., `p.Arg147His`).    
-   **Reward Function:** * **1.0:** Correct classification (Pathogenic/Benign match).    
    -   **0.0:** Incorrect classification or failed reasoning.       

## Project Working
### Prerequisites
-   Python 3.10+    
-   Docker (for containerized evaluation)    
### Local Testing
1.  Install dependencies:  
    ```
    pip install -r requirements.txt    
    ```    
2.  Run the internal validation test:  
    ```
    python test_env.py    
    ```    
3.  Simulate an AI agent interaction:
    ```
    python mock_agent.py    
    ```    

## Attribution for dataset

This project utilizes data from the UniProt Consortium.
-   **Source:** UniProtKB/Swiss-Prot (Homo sapiens)    
-   **Version:** 2026_01    
-   **License:** CC BY 4.0
