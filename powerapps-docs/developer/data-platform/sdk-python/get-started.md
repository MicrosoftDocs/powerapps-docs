---
title: "Getting started"
description: "Get started using the Dataverse SDK for Python."
ms.author: paulliew
author: paulliew
ms.date: 05/13/2026
ms.reviewer: phecke
ms.topic: quickstart-sdk
contributors:
 - phecke
---

# Getting started

This article describes how to set up your Python environment to access Dataverse through the Dataverse SDK for Python. It then shows some simple coding examples to get you started.

## Prerequisites

- Read/write access to a Dataverse environment. You can use a [trial environment](/power-platform/admin/create-environment).
- OAuth authentication configured for your application.
- An activated Python 3.10+ environment.
- Pandas version 2.0.0+.
- Network access to [pypi.org](https://pypi.org) to obtain the SDK packages.

## Install the SDK and dependencies

From a terminal window, run the following command. This command installs the latest stable release of the SDK from a [pypi.org](https://pypi.org/) package.

```python
pip install PowerPlatform-Dataverse-Client
```

Run the following command to install the SDK from the project's GitHub source instead of from the package. Install the client from the PyPi package or from the source, but not both.

```python
git clone <https://github.com/microsoft/PowerPlatform-DataverseClient-Python.git>
cd PowerPlatform-DataverseClient-Python
pip install -e .
```

### Install Claude Skill globally

To improve the Python development experience, you can optionally install two Claude Skills when installing the SDK from a package.

```python
pip install PowerPlatform-Dataverse-Client && dataverse-install-claude-skill
```

> [!IMPORTANT]
> The skills are automatically loaded when installing from source.

The two skills are described in the following list:

- `dataverse-sdk-use`: Apply best practices for using the SDK in your applications.
- `dataverse-sdk-dev`: Provide guidance for developing and contributing to the SDK itself.

The skills work with both the Claude Code CLI and the Visual Studio Code extension. Once installed, Claude automatically uses the appropriate skill when working with Dataverse operations. For more information on Claude Skill, see [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview). Once installed, you can find skill definitions in the `.claude/skills/dataverse-sdk-use/SKILL.md` and `.claude/skills/dataverse-sdk-dev/SKILL.md`files on your development computer.

## Connect to Dataverse

The SDK [client](/python/api/powerplatform-dataverse-client/powerplatform.dataverse.client.dataverseclient) requires any Azure Identity [TokenCredential](/dotnet/api/azure.core.tokencredential) implementation for OAuth authentication with Dataverse.

This code example imports the Dataverse client and Azure Identity types and establishes a connection to a Dataverse environment. Be sure to change `myorg` in the URL to the correct name of your environment.

```python
from azure.identity import (
    InteractiveBrowserCredential, 
    ClientSecretCredential,
    CertificateCredential,
    AzureCliCredential
)
from PowerPlatform.Dataverse.client import DataverseClient

# Development options
credential = InteractiveBrowserCredential()  # Browser authentication
# credential = AzureCliCredential()          # If logged in via 'az login'

# Production options  
# credential = ClientSecretCredential(tenant_id, client_id, client_secret)
# credential = CertificateCredential(tenant_id, client_id, cert_path)

client = DataverseClient("https://myorg.crm.dynamics.com", credential)
```

You can customize the connection by using optional HTTP tunable settings to handle connection timeouts, retries, and more. Access these settings via the [DataverseConfig](/python/api/powerplatform-dataverse-client/powerplatform.dataverse.core.config.dataverseconfig) class.

Now that you have an established client connection to a Dataverse environment, you can start using the SDK to work with business data, table metadata, and more. The next article covers some examples of these operations.

For more information, see [Use OAuth with Dataverse](/power-apps/developer/data-platform/authenticate-oauth).

## Namespaces

The [PowerPlatform.Dataverse.operations](/python/api/powerplatform-dataverse-client/powerplatform.dataverse.operations) package contains modules that organize SDK operations into logical groups as described in the following table.

| Name           | Description                                                           |
|----------------|--------------------------------------------------------------------   |
| client.records | Create, update, delete, and get records (single or paginated queries) |
| client.query   | Query and search operations                                           |
| client.tables  | Table and column metadata management                                  |
| client.files   | File upload operations                                                |

For examples of using these operations, see the [Querying data](query.md) and [Working with data](work-data.md) articles.

## Next steps

Before you leave this page, make sure you have some knowledge of Dataverse. You can't work with Dataverse effectively without it. The second article listed here provides a quick guide that teaches you Dataverse basics:

- [Working with data](work-data.md)
- [Quick guide to Dataverse](quick-guide-dataverse.md)

## Related information

- [Dataverse Python examples](https://github.com/microsoft/PowerPlatform-DataverseClient-Python/tree/main/examples)
