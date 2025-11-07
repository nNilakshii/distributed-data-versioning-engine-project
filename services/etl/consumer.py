"""ETL consumer skeleton for processing Kafka events and writing to S3."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ETLPipelineConfig:
    """Basic configuration toggles for pipeline bootstrap."""

    batch_size: int = 5000
    max_concurrency: int = 4
    s3_bucket: str = "local-dev-bucket"


class StreamingETLPipeline:
    """Placeholder for the streaming ETL implementation."""

    def __init__(self, config: ETLPipelineConfig | None = None) -> None:
        self._config = config or ETLPipelineConfig()

    def run_once(self) -> None:
        """Placeholder step that will consume events and write transformed output."""

        raise NotImplementedError("ETL pipeline execution is not implemented yet.")
