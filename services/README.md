# Services

Each subdirectory contains code and configuration for an independently deployable component.

- `ingestion`: High-throughput Kafka producers and supporting utilities.
- `etl`: Stream processors that transform data and write to S3.
- `metadata`: API and workers managing dataset version metadata.
