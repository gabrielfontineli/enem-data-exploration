#!/usr/bin/env python3
"""
prepare_enem.py — prepara microdados do ENEM 2023 para análise.

Uso:
    python src/prepare_enem.py <caminho_entrada_csv> <caminho_saida_parquet>
Exemplo:
    python src/prepare_enem.py data/interim/unzipped_2023/DADOS/MICRODADOS_ENEM_2023.csv data/interim/enem_2023.parquet
"""

import sys
import pandas as pd
from pathlib import Path

# -----------------------------
# Colunas principais para análise
# -----------------------------
WANTED_COLS = [
    "NU_NOTA_MT", "NU_NOTA_LC", "NU_NOTA_CH", "NU_NOTA_CN", "NU_NOTA_REDACAO",
    "TP_ESCOLA", "SG_UF_RESIDENCIA",
    "Q001", "Q002", "Q006", "Q022", "Q024", "Q025",
    "IN_TREINEIRO",
]
NOTE_COLS = ["NU_NOTA_MT", "NU_NOTA_LC", "NU_NOTA_CH", "NU_NOTA_CN", "NU_NOTA_REDACAO"]
ORD_MAP = {chr(i): i - 64 for i in range(65, 91)}  # A..Z → 1..26


def main():
    if len(sys.argv) != 3:
        print("Uso: python src/prepare_enem.py <entrada_csv> <saida_parquet>")
        sys.exit(1)

    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.parent.mkdir(parents=True, exist_ok=True)

    print(f"Lendo {src}...")
    df = pd.read_csv(src, sep=";", encoding="latin-1", low_memory=False)

    # Seleciona apenas as colunas necessárias
    df = df[[c for c in WANTED_COLS if c in df.columns]].copy()

    # Remove treineiros
    if "IN_TREINEIRO" in df.columns:
        df = df[df["IN_TREINEIRO"] == 0]

    # Remove linhas com notas ausentes
    df = df.dropna(subset=[c for c in NOTE_COLS if c in df.columns])

    # Cria média das 5 notas
    df["NOTA_MEDIA_5"] = df[NOTE_COLS].mean(axis=1)

    # Converte questionário para ordinal (A..Z → 1..26)
    for q in ["Q001", "Q002", "Q006", "Q022", "Q024", "Q025"]:
        if q in df.columns:
            df[f"{q}_ord"] = df[q].map(ORD_MAP)

    # Salva o resultado em Parquet
    df.to_parquet(dst, index=False)
    print(f"✅ Arquivo salvo em: {dst} ({len(df):,} linhas)")

    # Gera amostra CSV opcional
    sample = dst.with_name(dst.stem + "_sample.csv")
    df.sample(min(1000, len(df)), random_state=42).to_csv(sample, index=False)
    print(f"📄 Amostra salva em: {sample}")


if __name__ == "__main__":
    main()