---
title: "Getting started (preview)"
description: "Get started using the Dataverse SDK for Python."
ms.author: paulliew
author: paulliew
ms.date: 10/29/2025
ms.reviewer: phecke
ms.topic: quickstart-sdk
contributors:
 - phecke
---

# Getting started (preview)

In this article, we describe how to set up your Python environment to access Dataverse through the Dataverse SDK for Python. We then show some simple coding examples to get you started.

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

## Prerequisites

- Read/write access to a Dataverse environment. A [trial environment](/power-platform/admin/create-environment) can be used.
- An activated Python 3.13+ environment.
- Network access to [pypi.org](https://pypi.org) to obtain the SDK packages.

## Install the SDK and dependencies

Let's start by installing the required dependencies into your Python environment. Install the dependencies listed in the [requirements.txt](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/blob/main/requirements.txt) file of the source code repo root.

```python
pip install dataverse-sdk
pip install -r requirements.txt
```

## Connect to Dataverse

This code example imports the client and configuration types from the SDK packages and establishes a connection to your Dataverse environment. Be sure to change 'myorg' in the URL to the correct name of your environment.

```python
from dataverse_sdk import DataverseClient
from dataverse_sdk.config import DataverseConfig

cfg = DataverseConfig()  # defaults to language_code=1033
client = DataverseClient(base_url="https://<myorg>.crm.dynamics.com", config=cfg)
```

You can customize the connection using optional HTTP tunable settings to handle connection timeouts, retries, etc. Access these settings via `cfg.http_retries`, `cfg.http_backoff`, and `cfg.http_timeout`.

The client makes use of [DefaultAzureCredentials](/dotnet/api/azure.identity.defaultazurecredential?view=azure-dotnet&preserve-view=true) when no credentials are specified.

Alternately, `DataverseClient` supports client secret or Service Principal authentication.

```python
client = DataverseClient(
    tenant_id=<TID>,
    client_id=<CID>,
    client_secret=<CS>,
    environment_url=<URL>
)
```

It is good practice the test the connection before proceeding.

```python
if client.is_connected():
    print("Successfully connected to Dataverse!")
else:
    print("Connection failed. Please check your credentials.")
```

Now that you have an established client connection to a Dataverse environment, you can start using the SDK to work with business data, table metadata, and more. The next article will cover some examples of this.

Before you leave this page, take note that you cannot work with Dataverse effectively unless you have some knowledge of Dataverse. We have provided a roadmap article that teaches you the basics.  

## Next steps

- [Working with data (preview)](work-data.md)
- [Roadmap to Dataverse (preview)](roadmap.md)

## Related information

<!-- [Ignite video]() -->
- [Dataverse Python examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
