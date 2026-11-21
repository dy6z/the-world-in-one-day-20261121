import os
from pathlib import Path
from PIL import Image

src = Path(__file__).parent / "entry.png"
out_dir = Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output'))
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / 'entry.png'

# Deterministic copy, no network, always same bytes
img = Image.open(src)
img.save(out_path, format='PNG', optimize=False)

print(f"Wrote {out_path}")
