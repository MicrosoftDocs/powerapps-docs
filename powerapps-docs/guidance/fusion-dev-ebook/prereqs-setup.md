---
title: "Fusion development ebook: Prerequisites and setup | Microsoft Docs"
description: "Prerequisites and setup for fusion development."
author: spboyer
ms.service: powerapps
ms.topic: conceptual
ms.custom: ebook
ms.date: 04/26/2021
ms.author: shboyer
ms.reviewer: kvivek

---
# Prerequisites and setup

To perform the steps described in this guide, you must have the following licenses and software:

-   A Git client, such as Git for Windows or the Git command-line tools, available at <https://git-scm.com>.

-   A Power Apps account. If your organization has an Office 365 account, you might be able to create a free Power Apps account. Go to the Power Apps page at <https://powerapps.microsoft.com/> to get started.

-   An Azure subscription. The apps built by the steps in this guide create and use resources in Azure. If you don't have a subscription, you can sign up on the Azure page at <https://azure.microsoft.com>.

-   The **Azure CLI**, available at [https://docs.microsoft.com/cli/azure/install-azure-cli](/cli/azure/install-azure-cli).

-   **.NET 5.0**, available on at <https://dotnet.microsoft.com/download>.

-   **Visual Studio Code**, available at <https://code.visualstudio.com/download>. You'll also need the following extensions for Visual Studio Code:

    -   **C\# extension for Visual Studio Code**. This extension is available in the [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp).

    -   **Azure App Service**, available at <https://aka.ms/AAbvgm8>.

    -   **Azure Account**, available at <https://aka.ms/AAbvgm7>.

    -   **SQL Server (mssql)**, available at <https://aka.ms/AAbvgm5>.

The complete code for the Web API and the app is available in GitHub at <https://github.com/microsoft/fusion-dev-ebook>.

Clone this repository locally on your computer, and read the README.md file carefully. Before continuing with this guide, make sure you've created the Azure SQL Database server and databases required by the app by using the instructions in the README.md file.

> [!div class="step-by-step"]
> [Previous](foreword.md)
> [Next](01-what-is-fusion-dev-approach.md)
