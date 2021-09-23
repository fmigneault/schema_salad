from typing import Any, Optional

def out(message: Optional[str] = ..., nl: bool = ..., **styles: Any) -> None: ...
def err(message: Optional[str] = ..., nl: bool = ..., **styles: Any) -> None: ...
def ipynb_diff(a: str, b: str, a_name: str, b_name: str) -> str: ...
def diff(a: str, b: str, a_name: str, b_name: str) -> str: ...
def color_diff(contents: str) -> str: ...
def dump_to_file(*output: str, ensure_final_newline: bool = ...) -> str: ...
