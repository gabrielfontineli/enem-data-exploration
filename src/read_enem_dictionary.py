# src/read_enem_dictionary.py
from __future__ import annotations
from pathlib import Path
import re
import pandas as pd

def _normalize_cols(df: pd.DataFrame) -> pd.DataFrame:
    # normaliza nomes de colunas (casefold + remove espaços/acentos simples)
    mapping = {}
    for c in df.columns:
        k = (str(c)
             .strip()
             .replace("\n", " ")
             .replace("\r", " ")
             .replace("  ", " ")
             .lower())
        mapping[c] = k
    out = df.rename(columns=mapping)
    # tenta mapear para chaves canônicas
    aliases = {
        "variável": "variavel", "variavel": "variavel", "nome": "variavel",
        "descrição": "descricao", "descricao": "descricao",
        "categorias": "categorias", "categoria": "categorias"
    }
    for c in list(out.columns):
        base = c
        if base in aliases:
            out = out.rename(columns={base: aliases[base]})
    return out

def _best_header(path: str | Path, sheet_name: str | None) -> tuple[pd.DataFrame, str]:
    """Tenta carregar a planilha correta e detectar o header."""
    xls = pd.ExcelFile(path)
    # escolhe a aba automaticamente se não vier sheet_name
    if sheet_name is None:
        candidates = [s for s in xls.sheet_names if "MICRO" in s.upper()]
        sheet = candidates[0] if candidates else xls.sheet_names[0]
    else:
        sheet = sheet_name
    # testa alguns headers prováveis
    for hdr in (2, 1, 0):
        df = pd.read_excel(path, sheet_name=sheet, header=hdr)
        df = _normalize_cols(df)
        if {"variavel", "descricao"}.issubset(set(df.columns)):
            return df, sheet
    # fallback: sem header
    df = pd.read_excel(path, sheet_name=sheet, header=None)
    df.columns = [f"col_{i}" for i in range(df.shape[1])]
    return df, sheet

def _collapse_categories(df: pd.DataFrame) -> pd.DataFrame:
    """Algumas versões trazem categorias em múltiplas linhas. Junta por variável."""
    if "categorias" not in df.columns:
        df["categorias"] = ""
    df["categorias"] = df["categorias"].fillna("").astype(str)
    # quando a linha de variavel vem vazia, propaga valor anterior
    if "variavel" in df.columns:
        df["variavel"] = df["variavel"].ffill()
    agg = (df.groupby(["variavel"], dropna=False, as_index=False)
             .agg({"descricao": "first",
                   "categorias": lambda s: "\n".join([x for x in s if x])}))
    return agg

# regex que pega formatos: "A) texto", "A - texto", "1 - texto", "A. texto"
_PAIR_RE = re.compile(
    r"(?:^|\n|\r)\s*([A-Z0-9]{1,2})\s*[\)\-–\.]\s*([^;\n\r]+)",
    flags=re.IGNORECASE
)

def _parse_category_blob(blob: str) -> dict:
    blob = (blob or "").replace("\u2013", "-")  # en-dash -> hifen
    pairs = {}
    for m in _PAIR_RE.finditer(blob):
        code = m.group(1).strip().upper()
        label = m.group(2).strip()
        if code and label:
            pairs[code] = label
    return pairs

def read_enem_dictionary(dict_path: str | Path, sheet_name: str | None = None) -> tuple[dict, dict]:
    """
    Lê o dicionário do ENEM (.xlsx) e retorna:
      - descriptions: {variavel: descricao}
      - categories:   {variavel: {codigo: rotulo}}
    Funciona para 2023/2024 (detecta aba e header automaticamente).
    """
    path = Path(dict_path)
    if not path.exists():
        raise FileNotFoundError(f"Não encontrei o arquivo do dicionário: {path}")

    try:
        df, used_sheet = _best_header(path, sheet_name)
    except ImportError as e:
        # openpyxl ausente
        raise RuntimeError("Você precisa instalar 'openpyxl' para ler .xlsx (pip install openpyxl)") from e

    if "variavel" not in df.columns:
        # nada feito — mostra colunas para debug
        raise RuntimeError(f"Não identifiquei as colunas. Colunas lidas na aba '{used_sheet}': {list(df.columns)}")

    df2 = _collapse_categories(df)
    descriptions = dict(zip(df2["variavel"], df2["descricao"]))

    categories = {}
    for _, row in df2.iterrows():
        var = str(row["variavel"])
        blob = str(row.get("categorias", ""))
        if blob:
            cats = _parse_category_blob(blob)
            if cats:
                categories[var] = cats

    return descriptions, categories

if __name__ == "__main__":
    # Exemplo de uso rápido:
    # Ajuste o caminho abaixo para o seu dicionário oficial.
    path = "data/interim/unzipped_2023/DICIONÁRIO/Dicionário_Microdados_Enem_2023.xlsx"
    desc, cats = read_enem_dictionary(path)
    print("Aba lida com sucesso.")
    print("Variáveis lidas:", len(desc))
    print("Exemplo Q006:", cats.get("Q006", {}))