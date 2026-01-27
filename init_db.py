"""
Database initialization script for Traffk bot
"""
import asyncio
from traffk_bot.models import Base, engine


async def init_db():
    """Initialize the database and create tables"""
    async with engine.begin() as conn:
        # Create all tables
        await conn.run_sync(Base.metadata.create_all)
    print("Database tables created successfully!")


if __name__ == "__main__":
    asyncio.run(init_db())