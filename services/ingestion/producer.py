"""Kafka producer skeleton for ingesting events."""

from __future__ import annotations

import importlib
import json
import logging
from typing import Any, Dict, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - hints only
    from confluent_kafka import Producer as KafkaProducer
else:  # pragma: no cover - typing fallback when library not available
    KafkaProducer = Any  # type: ignore[assignment]

from .config import DEFAULT_PRODUCER_CONFIG, KafkaProducerConfig

logger = logging.getLogger(__name__)


class EventProducer:
    """Wraps the Kafka producer with sensible defaults."""

    def __init__(self, topic: str, config: KafkaProducerConfig | None = None) -> None:
        self._topic = topic
        cfg = config or DEFAULT_PRODUCER_CONFIG
        self._producer = self._create_producer(cfg)

    def produce(self, payload: Dict[str, Any]) -> None:
        """Serialize and publish a JSON payload."""

        encoded = json.dumps(payload).encode("utf-8")
        self._producer.produce(self._topic, encoded, callback=self._on_delivery)

    def flush(self) -> None:
        """Ensure all pending messages are pushed to Kafka."""

        self._producer.flush()

    def _on_delivery(self, err, msg) -> None:  # type: ignore[no-untyped-def]
        if err is not None:
            logger.error("Delivery failed: %s", err)
        else:
            logger.debug("Delivered message to %s [%d] offset %d", msg.topic(), msg.partition(), msg.offset())

    @staticmethod
    def _create_producer(config: KafkaProducerConfig):
        try:
            module = importlib.import_module("confluent_kafka")
        except ModuleNotFoundError as exc:  # pragma: no cover - ensures early feedback during runtime
            msg = "confluent_kafka is required to run the ingestion producer."
            raise RuntimeError(msg) from exc

        producer_cls: Any = getattr(module, "Producer")
        return producer_cls({"bootstrap.servers": ",".join(config.bootstrap_servers)})
