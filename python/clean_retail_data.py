"""Reproducible cleaning pipeline for retail_messy_intake.csv."""
import csv, argparse
from datetime import datetime

def parse_date(v):
    for fmt in ("%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M"):
        try: return datetime.strptime(v, fmt)
        except ValueError: pass
    return None

def clean(input_csv, output_csv):
    seen=set(); kept=0
    with open(input_csv, newline="", encoding="utf-8") as src, open(output_csv,"w",newline="",encoding="utf-8") as dst:
        r=csv.DictReader(src); fields=r.fieldnames+["Revenue"]; w=csv.DictWriter(dst,fieldnames=fields); w.writeheader()
        for row in r:
            key=tuple(row.get(k,"") for k in r.fieldnames)
            if key in seen: continue
            seen.add(key)
            if row["InvoiceNo"].strip().upper().startswith("C"): continue
            if not row["CustomerID"].strip(): continue
            try: qty=float(row["Quantity"]); price=float(row["UnitPrice"])
            except ValueError: continue
            if qty<=0 or price<=0: continue
            dt=parse_date(row["InvoiceDate"].strip())
            if dt is None: continue
            row["Description"]=" ".join(row["Description"].strip().split()).upper()
            row["Country"]=" ".join(row["Country"].strip().split()).title()
            row["InvoiceDate"]=dt.strftime("%Y-%m-%d %H:%M:%S")
            row["Quantity"]=str(int(qty)); row["UnitPrice"]=f"{price:.2f}"; row["CustomerID"]=row["CustomerID"].strip()
            row["Revenue"]=f"{qty*price:.2f}"
            w.writerow(row); kept+=1
    print(f"Wrote {kept} cleaned rows to {output_csv}")

if __name__=="__main__":
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("output"); a=p.parse_args(); clean(a.input,a.output)
