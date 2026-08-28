import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    token: str
    debug: bool = False
    default_prefix: str = "!" # Mudei de "/" para "!". Slash commands não usam prefixo.

def load_config() -> Config:
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise ValueError("DISCORD_TOKEN not found in environment or .env file")
    
    debug = os.getenv("DEBUG", "false").lower() == "true"
    return Config(token=token, debug=debug)