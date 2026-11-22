import os
from pathlib import Path

src = Path(__file__).parent / "entry.png"
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "entry.png"

# Byte-for-byte copy: no decoding, no re-encoding, so both runs write
# exactly the same bytes and the gate sees the file we tested locally.
data = src.read_bytes()
out_path.write_bytes(data)

print(f"Wrote {out_path} ({len(data)} bytes)")
