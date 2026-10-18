"""Bundle workspace scripts into a single Studio Command Bar import."""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
sources = {}
for path in (root / "src").rglob("*.luau"):
    sources[path.stem] = path.read_text(encoding="utf-8-sig")
parts = ["local sources = {}"]
for name, source in sources.items():
    parts.append(f'sources[{json.dumps(name)}] = [====[\n{source}\n]====]')
parts.append((root / "tools/studio_scene.luau").read_text(encoding="utf-8"))
bundle = "\n".join(parts)
# A single quoted command preserves source newlines without submitting each line.
encoded = json.dumps(bundle, ensure_ascii=False)
(root / "tools/ImportGame.command.luau").write_text(f"assert(loadstring({encoded}))()", encoding="utf-8")
print("Built tools/ImportGame.command.luau")
