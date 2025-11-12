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
    "TP_ESCOLA",
    # Local da prova (para derivar UF e Região)
    "CO_MUNICIPIO_PROVA", "NO_MUNICIPIO_PROVA",
    # Questionário socioeconômico
    "Q001", "Q002", "Q006", "Q022", "Q024", "Q025",
    "IN_TREINEIRO",
]
NOTE_COLS = ["NU_NOTA_MT", "NU_NOTA_LC", "NU_NOTA_CH", "NU_NOTA_CN", "NU_NOTA_REDACAO"]
ORD_MAP = {chr(i): i - 64 for i in range(65, 91)}  # A..Z → 1..26

# Mapas auxiliares para UF e Região a partir do código do município (IBGE/ENADE)
REGION_NAME = {
    1: "Norte",
    2: "Nordeste",
    3: "Sudeste",
    4: "Sul",
    5: "Centro-Oeste",
}

UF_CODE_TO_SIGLA = {
    "11": "RO", "12": "AC", "13": "AM", "14": "RR", "15": "PA", "16": "AP", "17": "TO",
    "21": "MA", "22": "PI", "23": "CE", "24": "RN", "25": "PB", "26": "PE", "27": "AL", "28": "SE", "29": "BA",
    "31": "MG", "32": "ES", "33": "RJ", "35": "SP",
    "41": "PR", "42": "SC", "43": "RS",
    "50": "MS", "51": "MT", "52": "GO", "53": "DF",
}

def _code_to_str7(x: object) -> str | None:
    """Converte o código de município para string com 7 dígitos ou None."""
    import pandas as _pd
    if _pd.isna(x):
        return None
    # Remove qualquer sufixo decimal (caso venha como float) e preenche com zeros à esquerda
    try:
        s = str(int(x))
    except Exception:
        s = str(x)
        # remove qualquer caractere não numérico
        s = "".join(ch for ch in s if ch.isdigit())
    return s.zfill(7) if s else None

def _uf_code_from_mun(code7: str | None) -> str | None:
    if not code7:
        return None
    return code7[:2]

def _region_id_from_mun(code7: str | None) -> int | None:
    if not code7:
        return None
    try:
        return int(code7[0])
    except Exception:
        return None

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

    # Deriva UF e Região a partir do código do município da PROVA
    if "CO_MUNICIPIO_PROVA" in df.columns:
        # Garante codificação consistente de 7 dígitos
        df["CO_MUNICIPIO_PROVA_str"] = df["CO_MUNICIPIO_PROVA"].apply(_code_to_str7)
        # UF (código e sigla)
        df["UF_CODE_PROVA"] = df["CO_MUNICIPIO_PROVA_str"].apply(_uf_code_from_mun)
        df["SG_UF_PROVA"] = df["UF_CODE_PROVA"].map(UF_CODE_TO_SIGLA)
        # Região (id 1..5 e nome legível)
        df["REGIAO_ID_PROVA"] = df["CO_MUNICIPIO_PROVA_str"].apply(_region_id_from_mun)
        df["REGIAO_NOME_PROVA"] = df["REGIAO_ID_PROVA"].map(REGION_NAME)

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