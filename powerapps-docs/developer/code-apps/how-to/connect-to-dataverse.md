---
title: "How to: Connect your code app to Dataverse (preview)"
description: "Learn how to connect your code app to Dataverse"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: Connect your code app to Dataverse (preview)

This guide helps developers use the Power Apps SDK to connect their code app to Microsoft Dataverse.

> [!NOTE]
> [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

## Prerequisites

- Power Apps code apps SDK [@microsoft/power-apps - npm package](https://www.npmjs.com/package/@microsoft/power-apps)
- Power Apps CLI (PAC CLI) version 1.46 or later
- An environment with Dataverse enabled
- You must be connected to the environment using PAC CLI

## Steps

1. Ensure you're connected to your environment using PAC CLI.
1. Use the [pac code add-data-source](/power-platform/developer/cli/reference/code#pac-code-add-data-source) command to add Dataverse as a data source to your code app

   ```powershell
   pac code add-data-source -a dataverse -t <table-logical-name>
   ```

   Replace `<table-logical-name>` with the logical name of the Dataverse table you want to connect to.

## Supported scenarios

The following scenarios are supported when connecting to Dataverse using the Power Apps SDK:

- Add Dataverse entities to code apps using the PAC CLI
- Perform CRUD operations:

  - Create
  - Retrieve
  - RetrieveMultiple
  - Update
  - Delete

- Delegation for:

  - `Filter`
  - `Sort`
  - `Top` queries

- Paging support

## Unsupported scenarios

The following features aren't yet supported:

- Option sets, Lookup fields, Polymorphic entities
- Dataverse Actions
- Deleting Dataverse datasources via PAC CLI
- Entity Metadata updates
- FetchXML support

### Related information

- [How to: Connect your code app to data](connect-to-data.md)  
- [Power Apps CLI](/power-platform/developer/cli/introduction)
