---
title: "How to: Connect your code app to Dataverse"
description: "Learn how to connect your code app to Dataverse"
ms.author: alaug
author: alaug
ms.date: 09/10/2025
ms.reviewer: jdaly
ms.topic: how-to
contributors:
 - JimDaly
---
# How to: Connect your code app to Dataverse

This guide helps developers use the Power Apps SDK to connect their code app to Microsoft Dataverse.

## Prerequisites

- Power Apps code apps SDK version [v0.0.4 or later](https://github.com/microsoft/PowerAppsCodeApps/releases/tag/v0.0.4)
- Power Apps CLI (PAC CLI) version 1.46 or later
- An environment with Dataverse enabled
- You must be connected to the environment using PAC CLI

## Steps

1. Ensure you are connected to your environment using PAC CLI.
1. Add Dataverse as a data source to your code app:

   ```powershell
   pac code add-data-source -a dataverse -t <table-logical-name>
   ```

   Replace `<table-logical-name>` with the logical name of the Dataverse table you want to connect to.


## Supported Scenarios

The following scenarios are supported when connecting to Dataverse using the Power Apps SDK:

- Add Dataverse entities to code apps using the PAC CLI
- Perform CRUD operations:

  - Create
  - Retrieve
  - RetrieveAll
  - Update
  - Delete

- Delegation for:

  - `Filter`
  - `Sort`
  - `Top` queries

- Paging support

## Unsupported Scenarios

The following features are not yet supported:

- Optionsets, Lookup fields, Polymorphic entities
- Dataverse Actions
- Deleting Dataverse datasources via PAC CLI
- Entity Metadata updates
- FetchXML support

## Additional Resources

[How to: Connect your code app to data](connect-to-data.md)  
[Power Apps CLI](/power-platform/developer/cli/introduction)
