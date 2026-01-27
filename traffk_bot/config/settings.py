import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./traffk_bot.db")
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    
    # Admin user IDs (comma-separated)
    ADMIN_IDS: list = [int(x.strip()) for x in os.getenv("ADMIN_IDS", "").split(",") if x.strip()]
    
    # Payment details
    TINKOFF_CARD: str = os.getenv("TINKOFF_CARD", "")
    USDT_ADDRESS: str = os.getenv("USDT_ADDRESS", "")

settings = Settings()