from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw
import os

artifact_dir = r"C:\Users\himaru\.gemini\antigravity\brain\e9d8ed82-bc97-48d0-8949-3a15c9e7a861"

smiles_data = {
    "Aspirin": "CC(=O)OC1=CC=CC=C1C(=O)O",
    "Ibuprofen": "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",
    "Paclitaxel": "CC1=C2C(C(=O)C3(C(CC4C(C3C(C(C2(C)C)(CC1OC(=O)C(C(C5=CC=CC=C5)NC(=O)C6=CC=CC=C6)O)O)OC(=O)C7=CC=CC=C7)(CO4)OC(=O)C)O)C)C"
}

def analyze_and_draw():
    os.makedirs(artifact_dir, exist_ok=True)
    
    for name, smiles in smiles_data.items():
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            continue
        
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hbd = Descriptors.NumHDonors(mol)
        hba = Descriptors.NumHAcceptors(mol)
        tpsa = Descriptors.TPSA(mol)
        rot_bonds = Descriptors.NumRotatableBonds(mol)
        
        print(f"--- {name} ---")
        print(f"MW: {mw:.2f}")
        print(f"LogP: {logp:.2f}")
        print(f"HBD: {hbd}")
        print(f"HBA: {hba}")
        print(f"TPSA: {tpsa:.2f}")
        print(f"RotBonds: {rot_bonds}")
        
        img_path = os.path.join(artifact_dir, f"{name.lower()}.png")
        Draw.MolToFile(mol, img_path, size=(400, 400))

if __name__ == "__main__":
    analyze_and_draw()
