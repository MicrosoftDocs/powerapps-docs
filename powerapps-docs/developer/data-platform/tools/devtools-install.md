---
title: "Install Power Platform Tools | Microsoft Docs"
description: "Learn how to install the Power Platform Tools extension for Visual Studio."
ms.custom: ""
ms.date: 07/19/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "phecke" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "pehecke" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Install Power Platform Tools

:::image type="content" source="../media/tools/devtools-main-views.png" alt-text="Power Platform Tools." lightbox="../media/tools/devtools-main-views.png":::

This topic describes the pre-requisites for the Power Platform Tools extension for Visual Studio, and how to install and uninstall the extension. The Visual Studio extension supports the rapid creation and deployment of plug-ins and custom workflow activities, integration technologies like Azure Service endpoints and Webhooks, and more.

> [!IMPORTANT]
> While the Power Platform Tools extension for Visual Studio is similar in appearance and function to the Developer Toolkit for Microsoft Dynamics CRM 2013, Power Platform Tools is a new product and completely independent of the Developer Toolkit. Power Platform Tools is not directly compatible with any templates or projects from the Developer Toolkit and vice versa.

## Prerequisites

Before installing Power Platform Tools into Visual Studio you must have the following applications and frameworks installed on your development computer:

- Microsoft Visual Studio 2019 or later.

- .NET Framework 4.6.2 (required only for plug-in and workflow activity development)

- C# programming language

In addition, you must also have access to a Microsoft Dataverse environment. A [trial environment](https://powerplatform.microsoft.com/dataverse/) will be sufficient.

## Install Power Platform Tools extension into Visual Studio

To install Power Platform Tools, follow these steps:

1. Launch Visual Studio, and select **Continue without code** in the dialog. Optionally, you can open an existing project or create a new one.

1. Select **Extensions** > **Manage extensions**.

1. Expand the left navigation panel node **Online** > **Visual Studio Marketplace**. Search for Power Platform Tools, then download and install the extension.

## Uninstall Power Platform Tools extension

1. Launch Visual Studio, and select **Continue without code** in the dialog. Optionally, you can open an existing project or create a new one.

1. Select **Extensions** > **Manage extensions**.

1. Expand the left navigation panel node **Installed**. Search for or scroll to the Power Platform Tools extension, select it, and then choose **Uninstall**.

### See Also

[Quickstart: Create a Power Platform Tools project](devtools-create-project.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
