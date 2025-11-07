# Distributed Data Versioning Engine

This repository hosts a distributed data versioning engine engineered to:
- Ingest 100k+ events per second via Apache Kafka.
- Parallelize ETL workloads into an AWS S3 data lake.
- Track fine-grained dataset versions with a metadata service enabling sub-100ms point-in-time queries.

## Repository Layout

```
docs/           # Architecture notes, ADRs, runbooks
infra/          # Infrastructure-as-Code, deployment scripts
services/
	ingestion/    # Kafka producers and supporting utilities
	etl/          # Streaming consumers and S3 writers
	metadata/     # Metadata API, schema registry clients
tests/          # Unit and integration tests
docker-compose.yml
pyproject.toml
```

## Getting Started

1. Install Python 3.11+ and Docker Desktop.
2. Clone this repository and create a virtual environment.
3. Install dependencies using `pip install -r requirements/dev.txt` (to be added) or Poetry.
4. Use `docker compose up` to launch local Kafka, ZooKeeper, and PostgreSQL services.
5. Run smoke tests with `pytest` (tests will be fleshed out as the project evolves).

Detailed component documentation lives under `docs/` as we implement each subsystem.