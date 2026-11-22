import os
from pathlib import Path

# Initial skeleton for make.fun entry
src = Path(__file__).parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "entry.png"

# Byte-for-byte deterministic copy to satisfy make.fun sandbox requirements
data = src.read_bytes()
out_path.write_bytes(data)

print(f"Wrote {out_path} ({len(data)} bytes)")

