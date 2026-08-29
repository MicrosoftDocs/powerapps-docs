---
title: "Handle errors and enable HTTP diagnostics"
description: "Learn how to catch SDK exceptions, handle transient failures, tune timeouts and retries, and enable HTTP diagnostics logging in the Dataverse SDK for Python."
ms.author: kewear
author: kewear
ms.date: 08/28/2026
ms.reviewer: phecke
ms.topic: how-to
contributors:
 - phecke
---

# Handle errors and enable HTTP diagnostics

When your application calls the Dataverse SDK for Python, two categories of failure can occur: failures the SDK raises as structured exceptions (validation problems, metadata errors, SQL parsing failures, and Dataverse API errors), and failures the underlying transport layer raises as network exceptions (timeouts and connectivity errors). Understanding both categories and where to catch each one lets you build applications that fail gracefully, retry intelligently, and surface actionable diagnostics.

Python developers should first learn about the SDK for Python by reading [Getting started](get-started.md) before continuing with this article. The code samples assume you already constructed a `DataverseClient` instance named `client`.

## Exception hierarchy

The SDK raises structured exceptions that all inherit from a single base class, `DataverseError`. Catching the base class is the safest fallback. Catch the specific subclasses when you need to respond differently to validation, metadata, SQL, or HTTP failures.

You can import all exception classes from `PowerPlatform.Dataverse.core.errors`, or find them re-exported from `PowerPlatform.Dataverse.core` directly.

```text
Exception
└── DataverseError              # Base class for every SDK-raised error
    ├── ValidationError         # Client-side input validation failed
    ├── MetadataError           # Table/column/relationship metadata problem
    └── HttpError               # Dataverse Web API returned a non-success status
```

The following table describes when each exception is raised.

| Exception | When raised | Typical examples |
|-----------|-------------|-----------------|
| `DataverseError` | Base class. Catch it to handle any SDK-originated failure in one block. | Fallback `except` clause. |
| `ValidationError` | Client-side argument validation fails before a request is sent. | Empty or `None` table name, missing primary key, non-string SQL, unsupported or write SQL passed to `query.sql()` (`INSERT`/`UPDATE`/`DELETE`, `SELECT *`, `UNION`, `HAVING`, subqueries), invalid batch payload, unsupported column type in `create`. |
| `MetadataError` | A metadata lookup or definition operation fails, usually an unknown or invalid table, column, or relationship. | Unknown logical name passed to `batch.create/update/delete`, `tables.add_columns`, `tables.create_*_relationship`, or `tables.delete`. |
| `HttpError` | The Dataverse Web API responded with a non-2xx status. Exposes `status_code` and `is_transient` as attributes; `service_error_code`, `correlation_id`, `service_request_id`, and `retry_after` are available in the `details` dict (`e.details.get(...)`). | 401 (auth), 403 (permissions), 404 (record/table not found), 412 (concurrency/ETag), 429 (throttling), 5xx (server errors). |

> [!NOTE]
> Transport-layer failures (network timeouts and connectivity errors) aren't wrapped by the SDK and surface as their original library exceptions. See [Handle network timeouts](#handle-network-timeouts) for details.

## Catch specific exception types

Catching specific exceptions rather than a broad base class lets you respond differently to each failure mode. Place the `DataverseError` clause last: because `ValidationError`, `MetadataError`, and `HttpError` all inherit from `DataverseError`, catching the base class last ensures each specific subclass is handled by its own more specific clause.

```python
import requests
from PowerPlatform.Dataverse.core.errors import (
    DataverseError,
    HttpError,
    MetadataError,
    ValidationError,
)

try:
    client.records.retrieve("account", "invalid-id")
except ValidationError as e:
    print(f"Validation error: {e.message} (subcode={e.subcode})")
except MetadataError as e:
    print(f"Metadata error: {e.message} (subcode={e.subcode})")
except HttpError as e:
    print(f"HTTP {e.status_code}: {e.message}")
    print(f"Service request id: {e.details.get('service_request_id')}")
    if e.is_transient:
        print(f"Transient - retry after {e.details.get('retry_after')}s")
except requests.exceptions.Timeout as e:
    # Raised by the transport layer after all retry attempts are exhausted
    print(f"Request timed out: {e}")
except DataverseError as e:
    # Catch-all for any other SDK-raised error
    print(f"Dataverse error [{e.code}]: {e.message}")
```

## Handle transient errors and retries

Some server-side failures are temporary. `HttpError` exposes an `is_transient` flag that's set to `True` when Dataverse returns HTTP status 429, 502, 503, or 504. When `is_transient` is `True`, the operation is worth retrying after a short wait. For HTTP 429 (throttling) responses, `e.details.get('retry_after')` provides the number of seconds Dataverse recommends waiting before the next attempt.

```python
from PowerPlatform.Dataverse.core.errors import HttpError
import time

def create_with_retry(client, table, data, max_retries=3):
    for attempt in range(max_retries):
        try:
            return client.records.create(table, data)
        except HttpError as e:
            if e.is_transient and attempt < max_retries - 1:
                wait = e.details.get("retry_after") or 2 ** attempt
                print(f"Transient error (HTTP {e.status_code}). Retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
```

> [!NOTE]
> The SDK automatically retries transport-level network errors by using exponential backoff. It doesn't automatically retry `HttpError` responses. Your application is responsible for retry logic on transient server errors.

## Handle network timeouts

The underlying HTTP library raises transport-layer failures (timeouts and connectivity errors). These failures aren't wrapped in `DataverseError`. For the sync `DataverseClient`, these failures surface as `requests.exceptions.RequestException` subclasses, most commonly `requests.exceptions.Timeout`. For the async `AsyncDataverseClient`, these failures surface as `aiohttp.ClientError` or `asyncio.TimeoutError`.

These exceptions reach your code only after the SDK's built-in retry mechanism exhausts all retry attempts. Catch them outside the SDK exception hierarchy.

```python
import requests
from PowerPlatform.Dataverse.core.errors import DataverseError

try:
    client.records.retrieve("account", record_id)
except requests.exceptions.Timeout:
    print("Request timed out. Consider increasing http_timeout in DataverseConfig.")
except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
except DataverseError as e:
    print(f"SDK error: {e.message}")
```

For the async client, catch `asyncio.TimeoutError` and `aiohttp.ClientError` in place of the `requests` exceptions. To learn more, see [Asynchronous client operations](async-client.md).

## Configure HTTP timeouts and retry behavior

The client uses per-method timeout defaults and automatically retries transport-level network errors. You can override both settings through [DataverseConfig](/python/api/powerplatform-dataverse-client/powerplatform.dataverse.core.config.dataverseconfig).

| Setting | Default | Effect |
|---------|---------|--------|
| `http_timeout` | Per-method (see following list) | Timeout in seconds applied to every request. When set, it overrides the per-method defaults for all requests. |
| `http_retries` | `5` | Maximum attempts per request on network errors. |
| `http_backoff` | `0.5` | Base delay in seconds between retry attempts. The delay doubles with each attempt: 0.5 s, 1 s, 2 s, 4 s, and so on. |

When you don't set `http_timeout`, the client uses:

- **10 seconds** for `GET` (and any non-write method).
- **120 seconds** for `POST`, `PATCH`, and `DELETE`.

The 10-second default works for routine data queries but can be too short for large metadata reads, such as `client.tables.list_relationships()` or `client.tables.list_columns()` on organizations with many tables or relationships, or on the first call after an organization wakes from idle. If you see timeout errors from those endpoints, increase the value.

```python
from PowerPlatform.Dataverse.client import DataverseClient
from PowerPlatform.Dataverse.core import DataverseConfig

config = DataverseConfig(
    http_timeout=120,   # seconds - applies to every request
    http_retries=3,     # cap retries on slow metadata calls
    http_backoff=1.0,
)
client = DataverseClient("https://myorg.crm.dynamics.com", credential, config=config)
```

> [!IMPORTANT]
> Setting `http_timeout` overrides the per-method defaults for **all** requests, not just metadata calls. Choose a value that's large enough for the slowest operation you expect, typically metadata listing or bulk writes.

## Enable HTTP diagnostics logging

HTTP diagnostics logging captures every request and response to timestamped log files for offline review. The system automatically redacts sensitive headers, including `Authorization`. Enable this feature by passing a `LogConfig` object to `DataverseConfig`.

```python
from PowerPlatform.Dataverse.client import DataverseClient
from PowerPlatform.Dataverse.core import DataverseConfig, LogConfig

log_cfg = LogConfig(
    log_folder="./my_logs",       # Directory for log files (created if missing)
    log_file_prefix="crm_debug",  # Filename prefix; timestamp appended automatically
    max_body_bytes=4096,          # Bytes of body to capture per entry - 0 (default) disables body capture
)
config = DataverseConfig(log_config=log_cfg)
client = DataverseClient("https://myorg.crm.dynamics.com", credential, config=config)
```

The system automatically timestamps and rotates log files. The following table describes the main `LogConfig` options.

| Option | Default | Description |
|--------|---------|-------------|
| `log_folder` | `"./dataverse_logs"` | Directory where you write log files. The system creates the folder automatically if it doesn't exist. |
| `log_file_prefix` | `"dataverse"` | Filename prefix. The system appends a timestamp and a short random suffix automatically, for example `dataverse_20260310_143022_a1b2c3.log`. |
| `max_body_bytes` | `0` (disabled) | Maximum bytes of request or response body to capture per log entry. `0` disables body capture entirely. |
| `log_level` | `"DEBUG"` | Python logging level for log entries. Valid values: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. |
| `max_file_bytes` | `10485760` (10 MB) | Maximum size per log file before rotation. |
| `backup_count` | `5` | Number of rotated backup files to keep. |

The system replaces the following headers with `[REDACTED]` in every log entry: `Authorization`, `Proxy-Authorization`, `X-MS-Authorization-Auxiliary`, `Ocp-Apim-Subscription-Key`, `Set-Cookie`, and `Cookie`.

## Protect log files

HTTP diagnostics logging is intended for development and debugging only. Log files are plaintext and might contain personally identifiable information, sensitive business data, and Dataverse record IDs. Even with `max_body_bytes=0`, request URLs can include filter values and record identifiers.

> [!IMPORTANT]
> **Never enable HTTP diagnostics logging in production.** If production diagnostics are required, keep `max_body_bytes=0` and treat log files as regulated data under your organization's data-handling policy.

Follow these guidelines whenever you enable logging:

- **Restrict file system access.** Set permissions so that only the process user can read the log folder. Use an encrypted volume or folder in sensitive environments.
- **Control retention.** Log rotation keeps up to five files by default (`backup_count`). Delete logs after the debugging session. Use secure deletion for regulated data.
- **Prevent source control leaks.** Add the log folder to `.gitignore` immediately after enabling logging.

## Related information

- [SDK for Python code examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
- [SDK for Python README](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/README.md)

## See also

- [Getting started](get-started.md)
- [Query data](query.md)
- [Asynchronous client operations](async-client.md)
