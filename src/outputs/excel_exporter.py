thonpython
import pandas as pd

def export_to_excel(data: list, output_path: str):
 if not data:
 raise ValueError("No data to export.")

 df = pd.DataFrame(data)
 df.to_excel(output_path, index=False)