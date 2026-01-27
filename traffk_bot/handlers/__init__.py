from aiogram import Router
from .start_handler import register_start_handler
from .balance_handler import register_balance_handler
from .history_handler import register_history_handler
from .task_handlers import register_task_handlers
from .feed_handler import register_feed_handler
from .my_assignments_handler import register_my_assignments_handler
from .my_tasks_handler import register_my_tasks_handler


def setup_handlers(dp):
    """Register all handlers with dispatcher"""
    register_start_handler(dp)
    register_balance_handler(dp)
    register_history_handler(dp)
    register_task_handlers(dp)
    register_feed_handler(dp)
    register_my_assignments_handler(dp)
    register_my_tasks_handler(dp)


__all__ = ["setup_handlers"]