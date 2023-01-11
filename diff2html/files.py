
import os
import zipfile


def write_force(path: str, content: str):
    if os.path.exists(path=path):
        os.remove(path=path)
    with open(path, "w") as f:
        f.write(content)  
        
        
## xD
def write_zip_force(path: str, content_path: str):
    if os.path.exists(path=path):
        os.remove(path=path)
    with zipfile.ZipFile(path, 'a') as zf:
        zf.write(path, os.path.basename(content_path))