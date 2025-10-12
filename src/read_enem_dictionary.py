# src/read_enem_dictionary.py
from __future__ import annotations
import re
from pathlib import Path
import pandas as pd

def read_enem_dictionary(dict_path: str | Path, sheet_name: str = "MICRODADOS_ENEM_2023") -> tuple[dict, dict]:
    """
    Lê o dicionário oficial de variáveis do ENEM (.xlsx) e retorna:
    - descriptions: {variável: descrição}
    - categories: {variável: {código: rótulo}}

    Funciona para os dicionários 2023 ou 2024 (ajuste o nome da aba se necessário).
    """
    df = pd.read_excel(dict_path, sheet_name=sheet_name, header=2)
    
    # tenta identificar colunas por palavras-chave (independente de acento/caso)
    def find_col(keyword):
        for c in df.columns:
            if keyword.lower() in str(c).lower():
                return c
        return None

    col_var = find_col("variável")
    col_desc = find_col("descrição")
    col_cat = find_col("valor") or find_col("categ")

    if not col_var or not col_desc:
        raise ValueError("Não foi possível identificar colunas de variável e descrição.")

    descriptions = {}
    categories = {}

    for _, row in df.iterrows():
        var = str(row[col_var]).strip().upper()
        if not var or var == "NAN":
            continue

        desc = str(row[col_desc]).strip()
        descriptions[var] = desc

        # parse de valores categóricos (ex.: "1 - Pública; 2 - Privada; 3 - Exterior")
        cats_raw = str(row[col_cat]) if col_cat else ""
        pairs = []
        for part in re.split(r"[;\n]+", cats_raw):
            m = re.match(r"\s*([A-Za-z0-9]+)\s*[-=:\u2013]\s*(.+)", part)
            if m:
                code, label = m.group(1).strip(), m.group(2).strip()
                pairs.append((code, label))
        if pairs:
            categories[var] = {k: v for k, v in pairs}

    return descriptions, categories


if __name__ == "__main__":
    path = "data/interim/unzipped_2023/DICIONÁRIO/Dicionário_Microdados_Enem_2023.xlsx"
    desc, cats = read_enem_dictionary(path)
    print("Variáveis:", len(desc))
    print("Com categorias:", len(cats))
    print("Exemplo TP_ESCOLA:", cats.get("TP_ESCOLA", {}))