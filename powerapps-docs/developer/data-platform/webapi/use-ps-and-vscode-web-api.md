---
title: Use PowerShell and Visual Studio Code with the Dataverse Web API
description: Describes how to use Powershell and Visual Studio Code to create reusable PowerShell functions to interactively test using the Dataverse Web API
ms.date: 12/30/2023
author: divkamath
ms.author: dikamath
ms.reviewer: jdaly
search.audienceType:
  - developer
contributors:
  - JimDaly
---
# Use PowerShell and Visual Studio Code with the Dataverse Web API

This article expands on the [Quick Start Web API with PowerShell](quick-start-ps.md) article to describe more advanced capabilities to be more productive:

- Interactive auto-login
- Handling exceptions
- Patterns to create reusable functions
- Manage Dataverse Service protection limits


## Prerequisites

- The Azure CLI `account` extension.
   - In a PowerShell terminal, run `az extension add --name account`
   - [Learn more about Azure CLI extensions](/cli/azure/azure-cli-extensions-overview)