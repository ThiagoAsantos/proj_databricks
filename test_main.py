import subprocess
import sys


def test_main_prints_hello_world():
    result = subprocess.run(
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == "Hello, World!\n"
