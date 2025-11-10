---
title: "Getting started (preview)"
description: "Get started using the Dataverse SDK for Python."
ms.author: paulliew
author: paulliew
ms.date: 11/05/2025
ms.reviewer: phecke
ms.topic: quickstart-sdk
contributors:
 - phecke
---

# Getting started (preview)

[!INCLUDE [preview-banner](../../../../shared/preview-includes/preview-banner.md)]

In this article, we describe how to set up your Python environment to access Dataverse through the Dataverse SDK for Python. We then show some simple coding examples to get you started.

## Prerequisites

- Read/write access to a Dataverse environment. A [trial environment](/power-platform/admin/create-environment) can be used.
- An activated Python 3.13+ environment.
- Network access to [pypi.org](https://pypi.org) to obtain the SDK packages.

## Install the SDK and dependencies

From a terminal window, execute the following command. This installs the SDK from [pypi.org](https://pypi.org/).

```python
python.exe -m pip install PowerPlatform-Dataverse-Client
```

## Connect to Dataverse

This code example imports the client and configuration types from the SDK packages and establishes a connection to your Dataverse environment. Be sure to change 'myorg' in the URL to the correct name of your environment.

```python
from azure.identity import InteractiveBrowserCredential
from PowerPlatform.Dataverse import DataverseClient
from PowerPlatform.Dataverse.config import DataverseConfig

cfg = DataverseConfig()  # defaults to language_code=1033
client = DataverseClient(base_url="https://<myorg>.crm.dynamics.com", 
    InteractiveBrowserCredential(), config=cfg)
```

You can customize the connection using optional HTTP tunable settings to handle connection timeouts, retries, etc. Access these settings via `cfg.http_retries`, `cfg.http_backoff`, and `cfg.http_timeout`.

It is good practice the test the connection before proceeding.

```python
if client.is_connected():
    print("Successfully connected to Dataverse!")
else:
    print("Connection failed. Please check your credentials.")
```

Now that you have an established client connection to a Dataverse environment, you can start using the SDK to work with business data, table metadata, and more. The next article will cover some examples of this.

Before you leave this page, take note that you cannot work with Dataverse effectively unless you have some knowledge of Dataverse. We have provided a quick guide article that teaches you the basics.  

## Next steps

- [Working with data (preview)](work-data.md)
- [Quick guide to Dataverse (preview)](quick-guide-dataverse.md)

## Related information

<!-- TODO: Add Ignite demo video link -->
- [Dataverse Python examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
