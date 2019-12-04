---
title: "Build tools tutorial and FAQ| Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Power Apps build tools are a collection of Power Apps specific Azure DevOps build tasks that eliminate the need to manually download  scripts to manage the development of Power Apps. This topic describes the tutorial and FAQs that you can access to learn more about these tools. " # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 07/21/2019
ms.reviewer: "Dean-Haas"
ms.service: powerapps
ms.topic: "article"
author: "mikkelsen2000" # GitHub ID
ms.author: "pemikkel" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Tutorial and FAQ


[!INCLUDE [cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]
Use the tutorial and FAQs to learn more about the Power Apps build tools for Azure DevOps. 

## Hands-on-lab

The hands-on lab is available [here](https://github.com/microsoft/PowerApps-Samples/tree/master/azure/build-tools)

The hand-on lab provides a tutorial with step-by-step instructions on how to build out the following scenario:

1. Setup dev, build, and prod environments.
2. Build a sample app.
3. Export a solution containing the sample app from a development environment.
4. Unpack the solution.
5. Commit solution to source (repo).
6. Import the unmanaged solution to a build environment.
7. Generate a build artifact (managed solution).
8. Deploy the solution to a downstream environment.

> [!NOTE]
> The hands-on lab is provided to offer hands-on experience for users new to Azure DevOps who are wanting to learn how to build pipelines in Azure DevOps. The finished pipelines that you will end up building can also be downloaded from the tutorial and used as-is with just a few adjustments to environment variables, source/target folders, and repositories.  

## Frequently asked question (FAQ)

**Do the Power Apps build tools only work for Power Apps?**  

*The Power Apps Build Tools work for both Power Apps and model-driven apps in Dynamics 365 such as Dynamics 365 Sales and Dynamics 365 Customer Service. Separate build tasks are available for Microsoft Dynamics for Finance and Operations.*

**Can I include Flow and Canvas Apps?**

*Yes, Flows and Canvas apps are solution aware so if these are added to your solution, they can participate in the lifecycle of your app.  However, some steps still require manual configurations. This will be addressed later this year when we introduce environment variables and connectors.*

**How much do the Power Apps build tools cost?**

*The Power Apps Build Tools are available at no cost. However, a valid subscription to Azure DevOps is required to utilize the Build Tools. More information is available [here](https://azure.microsoft.com/pricing/details/devops/azure-devops-services/).*

**I can see the extension, but why don’t I have an option to install it?**

*If you do not see the **install** option (outlined in screenshot below) then you most likely lack the necessary install privileges in your Azure DevOps Organization. More info available [here](https://docs.microsoft.com/azure/devops/marketplace/how-to/grant-permissions?view=azure-devops).*

![Build tasks screen](media/build-tasks.png)