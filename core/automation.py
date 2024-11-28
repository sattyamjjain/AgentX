from datetime import datetime
from utils.logger import get_logger

logger = get_logger("Automation")


def schedule_task(task_name: str, run_at: datetime):
    logger.info(f"Scheduling task '{task_name}' to run at {run_at}.")
