import argparse
from core.agent import AgentX
from utils.logger import get_logger

logger = get_logger("Main")


def main(mode):
    try:
        logger.info(f"Starting AgentX in {mode} mode...")
        agent = AgentX()

        if mode == "interactive":
            agent.run()
        elif mode == "test":
            logger.info("Running in test mode. Ensure all tests pass.")
        else:
            logger.warning(
                f"Unknown mode: {mode}. Running in default interactive mode."
            )
            agent.run()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the AgentX application.")
    parser.add_argument(
        "--mode",
        type=str,
        default="interactive",
        help="Specify the mode to run the application: 'interactive' or 'test'.",
    )
    args = parser.parse_args()
    main(args.mode)
