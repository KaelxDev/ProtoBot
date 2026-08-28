from datetime import datetime


def format_timestamp(dt: datetime, style: str = "f") -> str:
    return dt.strftime("%d/%m/%Y %H:%M:%S")


def truncate(text: str, max_length: int = 1024) -> str:
    if len(text) > max_length:
        return text[: max_length - 3] + "..."
    return text


def format_embed_field(name: str, value: str, inline: bool = True) -> dict:
    return {"name": name, "value": truncate(value, 1024), "inline": inline}