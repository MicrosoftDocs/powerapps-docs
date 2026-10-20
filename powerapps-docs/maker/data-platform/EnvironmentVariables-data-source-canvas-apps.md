---
title: "Use data source environment variables in canvas apps"
description: "Use environment variables to store data sources in canvas apps with Power Apps."
Keywords: environment variables, variables, canvas app, app, configuration data
author: caburk
ms.subservice: dataverse-maker
ms.author: caburk
ms.reviewer: matp
ms.date: 10/09/2026
ms.topic: how-to
ai-usage: ai-assisted
search.audienceType: 
  - maker
contributors:
  - shmcarth
  - asheehi1
---
# Use data source environment variables in canvas apps

In this article, you learn about using data source environment variables in canvas apps. You can either use pre-existing data source environment variables, or create data source environment variables automatically when connecting to data.

## Use pre-existing data source environment variables

You can reuse environment variables across other apps and even different types of resources like cloud flows. You might want to first create them within your solution and later use them while authoring canvas apps and cloud flows. The following steps use SharePoint Online as an example.

1. Follow the steps to [manually create an environment variable in a solution](EnvironmentVariables.md#manually-create-an-environment-variable-in-a-solution).
1. Edit or create a canvas app from your solution.
1. Add a **new** data source for SharePoint online.
1. Select the **Advanced** tab. You see a filtered list of available environment variables that you have access to and that match the parameter being set. For example, when you select the SharePoint site, the list contains data source environment variables with **Connector** as **SharePoint** and **Parameter type** as **Site**. The same is true when selecting SharePoint lists for a given site. If an existing variable doesn't appear, see [Limitations and troubleshooting](#limitations-and-troubleshooting).
1. Select the desired environment variable(s), and then select **Connect.**

> [!IMPORTANT]
>
> - If an environment variable from a different solution is selected, a dependency will exist on the solution containing the environment variable. Therefore, be sure to either: 
>   - Add the environment variable to your current solution prior to exporting. 
>   - Ensure the solution containing the environment variable is imported to the destination environment before your current solution is imported.

## Automatically create data source environment variables when connecting to data

This option provides simplicity and ensures environment variables are always used for data sources, such as SharePoint Online. However, some customers prefer to provide their own schema names and therefore should create them from solutions.

> [!NOTE]
> Pre-existing canvas apps don't automatically use data source environment variables. Remove the data source from the app and add them back using the above steps to upgrade these apps to use environment variables. 

1. Edit or create a canvas app from your solution.
1. Select **Settings** > **General** and enable the setting to **Automatically create environment variables when adding data sources**.
1. Add a **New** data source for SharePoint online.
1. Select a SharePoint **site**, one or more **lists**, and then **Connect**.

    > [!NOTE]
    > To prevent creation of duplicate environment variables, you're prompted to use the existing environment variable when duplicates are identified. You can clear the option to use the existing environment variable if creation of a duplicate is desired. 

1. Select **Save**. 

## Limitations and troubleshooting

An environment variable can exist in your environment without appearing in the Canvas Studio data source picker. Check the following limitations when you can't find a variable.

### Canvas Studio picker limitations

This limitation applies when selecting data source environment variables for supported connectors, including SharePoint and SQL Server. For SQL Server, it applies to connection types that support data source environment variables, such as Microsoft Entra connections.

The Canvas Studio data source picker retrieves only the first page of environment variable definitions and values that match the selected connector and parameter type. It doesn't retrieve subsequent pages. Each Dataverse request returns up to 5,000 matching records, so some variables might not appear in the **Advanced** tab or its search results. Searching for a missing variable doesn't retrieve it from a later page.

This limitation is for the picker, not a limit of 5,000 environment variables in Dataverse. The relevant count is the number of matching definitions or values for each request, not the total number of variables across all connectors in the environment.

To mitigate this limitation, reuse existing variables and remove obsolete variables after checking their dependencies. Don't delete variables that apps or flows still use. If you can't reduce the number of variables, consider a smaller environment that contains the variables and apps you need. Moving variables into different solutions within the same environment doesn't reduce the number of variables in that environment.

### SharePoint-specific configuration checks

In addition to the paging limitation that applies across supported connectors, SharePoint variables must meet these configuration requirements:

- A site variable needs a nonempty **Current Value** or **Default Value** that contains the SharePoint site URL. The picker doesn't list site variables with both values empty.
- A list variable's value must match the unique identifier (GUID) of a list returned for the selected site and connection, not the list's display name. Verify that the connection has access to the list and that the variable contains its identifier.

## See also

[Create canvas app from scratch using Dataverse.](/powerapps/maker/canvas-apps/data-platform-create-app-scratch) </BR>
[Use environment variables in Power Automate solution cloud flows](environmentvariables-power-automate.md)  <br>
[Environment variables overview](EnvironmentVariables.md) </BR>

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
