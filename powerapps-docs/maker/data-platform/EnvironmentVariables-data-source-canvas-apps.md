---
title: "Use data source environment variables in canvas apps | MicrosoftDocs"
description: "Use environment variables to store data sources in canvas apps."
Keywords: environment variables, variables, canvas app, app, configuration data
author: caburk
ms.subservice: dataverse-maker
ms.author: caburk
ms.reviewer: matp
ms.date: 01/31/2025
ms.topic: how-to
search.audienceType: 
  - maker
contributors:
  - shmcarth
  - asheehi1
---
# Use data source environment variables in canvas apps

In this article, you'll learn about using data source environment variables in canvas apps. You can either use pre-existing data source environment variables, or create data source environment variables automatically when connecting to data.

## Use pre-existing data source environment variables

Environment variables can be reused across other apps and even different types of resources like cloud flows. You might wish to first create them within your solution and later use them while authoring canvas apps and cloud flows.

1. Follow the steps to [manually create an environment variable in a solution](EnvironmentVariables.md#manually-create-an-environment-variable-in-a-solution).
1. Edit or create a canvas app from your solution.
1. Add a **new** data source for SharePoint online.
1. Select the **Advanced** tab. You'll see a filtered list of environment variables that you have access to and that match the parameter being set. For example, when you select the SharePoint site, you'll see a list of all data source environment variables with **Connector** as **SharePoint** and **Parameter type** as **Site**. The same is true when selecting SharePoint lists for a given site. 
1. Select the desired environment variable(s), and then select **Connect.**

> [!IMPORTANT]
>
> - If an environment variable from a different solution is selected, a dependency will exist on the solution containing the environment variable. Therefore, be sure to either: 
> - Add the environment variable to your current solution prior to exporting. 
> - Ensure the solution containing the environment variable is imported to the destination environment before your current solution is imported.

## Automatically create data source environment variables when connecting to data

This option provides simplicity and ensures environment variables will always be used for data sources, such as SharePoint Online. However, some customers prefer to provide their own schema names and therefore should create them from solutions.

> [!NOTE]
> Pre-existing canvas apps will not automatically use data source environment variables. Remove the data source from the app and add them back using the above steps to upgrade these apps to use environment variables. 

1. Edit or create a canvas app from your solution.
1. Select **Settings** > **General** and enable the setting to **Automatically create environment variables when adding data sources**.
1. Add a **New** data source for SharePoint online.
1. Select a SharePoint **site**, one or more **lists**, and then **Connect**.

    > [!NOTE]
    > To prevent creation of duplicate environment variables, you'll be prompted to use the existing environment variable when duplicates are identified. You can clear the option to use the existing environment variable if creation of a duplicate is desired. 

1. Select **Save**. 

### See also

[Create canvas app from scratch using Dataverse.](/powerapps/maker/canvas-apps/data-platform-create-app-scratch) </BR>
[Use environment variables in Power Automate solution cloud flows](environmentvariables-power-automate.md)  <br>
[Environment variables overview](EnvironmentVariables.md) </BR>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
