---
title: "Use environment variables in solutions | MicrosoftDocs"
description: "Use environment variables to migrate application configuration data in solutions."
Keywords: environment variables, variables, model-driven app, configuration data
author: caburk
ms.subservice: dataverse-maker
ms.author: caburk
ms.author: asheehi1
ms.reviewer: matp
ms.date: 12/06/2023
ms.topic: overview
search.audienceType: 
  - maker
contributors:
  - shmcarth
---
# Use data source environment variables in canvas apps
## Use pre-existing data source environment variables

Environment variables can be reused across other apps and even different types of resources like cloud flows. You may wish to first create them within your solution and later use them while authoring canvas apps and cloud flows.
1. Follow the steps to [Create an environment variable in a solution](/EnvironmentVariables.md#create-an-environment-variable-in-a-solution).
1. Edit or create a canvas app from your solution.
1. Add a **new** data source for SharePoint online.
1. Select the **Advanced** tab. You'll see a filtered list of environment variables that you have access to and that match the parameter being set. For example, when you select the SharePoint site, you'll see a list of all data source environment variables with **Connector** = **SharePoint** and **Parameter type** = **Site**. The same is true when selecting SharePoint lists for a given site. 
2. Select the desired environment variable(s), and then select **Connect.**

>[!IMPORTANT]
>If an environment variable from a different solution is selected, a dependency will exist on the solution containing the environment variable. Therefore, be sure to either: 
> - Add the environment variable to your current solution prior to exporting. 
> - Ensure the solution containing the environment variable is imported to the destination environment before your current solution is imported.

## Automatically create data source environment variables when connecting to data

This option provides simplicity and ensures environment variables will always be used for data sources, such as SharePoint Online. However, some customers prefer to provide their own schema names and therefore should create them from solutions.

1. Edit or create a canvas app from your solution.
1. Select **Settings** > **General** and enable the setting to **Automatically create environment variables when adding data sources**.
1. Add a **New** data source for SharePoint online.
1. Select a SharePoint **site**, one or more **lists**, and then **Connect**.
   >[!NOTE]
   >To prevent creation of duplicate environment variables, you'll be prompted to use the existing environment variable when duplicates are identified. You can clear the option to use the existing environment variable if creation of a duplicate is desired. 
1. Select **Save**. 

>[!NOTE]
>Pre-existing canvas apps will not automatically use data source environment variables. Remove the data source from the app and add them back using the above steps to upgrade these apps to use environment variables. 

### See also
[Create Canvas app from scratch using Dataverse.](/powerapps/maker/canvas-apps/data-platform-create-app-scratch) </BR>
[Environment variables overview.](/EnvironmentVariables.md) </BR>


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
