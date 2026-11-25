from pathlib import Path
import os

TEXT = "First paycheck: finally bought myself electricity."


def main() -> None:
    assert len(TEXT.split()) == 6
    assert 1 <= len(TEXT) <= 60
    assert "\n" not in TEXT and "\r" not in TEXT

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    out_path = Path(output_dir) / "entry.txt" if output_dir else Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(TEXT, encoding="utf-8")

    assert out_path.read_text(encoding="utf-8") == TEXT


if __name__ == "__main__":
    main()
