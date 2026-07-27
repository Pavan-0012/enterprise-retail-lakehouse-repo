from etl.common.config import Config
from etl.common.constants import CONFIG_PATH
from etl.common.logger import get_logger
from etl.common.spark import create_spark

config = Config(CONFIG_PATH)

logger = get_logger(__name__)

logger.info(config.get("project", "name"))

spark = create_spark(
    config.get("spark", "app_name")
)

print(spark.version)

spark.stop()