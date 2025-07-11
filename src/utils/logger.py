import logging
import boto3
import watchtower
from src.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

def setup_logger():
    """
    Set up logger with console and CloudWatch handlers.
    
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("TeacherRegistryChatbot")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # CloudWatch handler
        try:
            if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
                boto3_session = boto3.Session(
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    region_name="us-east-1"
                )
                cloudwatch_handler = watchtower.CloudWatchLogHandler(
                    boto3_session=boto3_session,
                    log_group_name="TeacherRegistryChatbotLogs",
                    stream_name="ApplicationLogs"
                )
                cloudwatch_handler.setFormatter(formatter)
                logger.addHandler(cloudwatch_handler)
                logger.info("CloudWatch logging initialized")
        except Exception as e:
            logger.warning(f"Failed to initialize CloudWatch logging: {str(e)}")

    return logger