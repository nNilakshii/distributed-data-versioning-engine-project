"""Configuration helpers for Kafka producers."""

from dataclasses import dataclass
from typing import List


@dataclass
class KafkaProducerConfig:
    """Settings used to bootstrap Kafka producers."""

    bootstrap_servers: List[str]
    linger_ms: int = 5
    batch_size: int = 32768
    compression_type: str = "lz4"


DEFAULT_PRODUCER_CONFIG = KafkaProducerConfig(bootstrap_servers=["localhost:9093"])
