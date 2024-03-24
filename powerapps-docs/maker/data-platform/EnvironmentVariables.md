---
title: "Use environment variables in solutions | MicrosoftDocs"
description: "Use environment variables to migrate application configuration data in solutions."
Keywords: environment variables, variables, model-driven app, configuration data
author: caburk
ms.subservice: dataverse-maker
ms.author: caburk
ms.reviewer: matp
ms.date: 01/31/2024
ms.topic: overview
search.audienceType: 
  - maker
contributors:
  - shmcarth
  - asheehi1
  - lancedMicrosoft
---
# Environment variables overview

Environment variables enable the basic application lifecycle management (ALM) scenario of moving an application between Power Platform environments. In this scenario, the application stays exactly the same except for a few key external application references (such as tables, connections, and keys) that are different between the source environment and the destination environment. The application requires the structure of the tables or connections to be exactly the same between the source and the destination environments, with some differences. Environment variables allow you to specify which of these different external references should be updated as the application is moved across environments.

Environment variables store the parameter keys and values, which then serve as input to various other application objects. Separating the parameters from the consuming objects allows you to change the values within the same environment or when you migrate solutions to other environments. The alternative is leaving hard-coded parameter values within the components that use them. This is often problematic; especially when the values need to be changed during ALM operations. Because environment variables are solution components, you can transport the references (keys) and change the values when solutions are migrated to other environments.

> [!NOTE]
> New capabilities for data sources are just now being deployed and may not be available yet in your region.

Benefits of using environment variables:
- Provide new parameter values while **importing solutions** to other environments.
- Store configuration for the **data sources** used in canvas apps and flows. For example, SharePoint Online site and list parameters can be stored as environment variables; therefore allowing you to connect to different sites and lists in different environments without needing to modify the apps and flows.
- Package and transport your customization and configuration together and manage them in a single location.
- Package and transport secrets, such as credentials used by different components, separately from the components that use them.
- One environment variable can be used across many different solution components - whether they're the same type of component or different. For example, a canvas app and a flow can use the same environment variable. When the value of the environment variable needs to change, you only need to change one value. 
- Additionally, if you need to retire a data source in production environments, you can update the environment variable values with information for the new data source. The apps and flows don't require modification and will start using the new data source.
- Supported by [SolutionPackager](/power-platform/alm/solution-packager-tool) and [DevOps](/power-platform/alm/devops-build-tools) tools enable continuous integration and continuous delivery (CI/CD).
- The environment variables can be unpacked and stored in source control. You might also store different environment variables values files for the separate configuration needed in different environments. Solution Packager can then accept the file corresponding to the environment the solution will be imported to.

## How do they work?

Environment variables can be created and modified within the modern solution interface, automatically created when connecting to certain data sources in canvas apps, or by [using code](/powerapps/developer/data-platform/work-with-data). They can also be imported to an environment via solutions. Once environment variables are present in an environment, they can be used as inputs when authoring canvas apps, Power Automate flows, when developing plug-ins, and many other places such as adding a Power BI dashboard to a model-driven app. When these types of objects use environment variables, the values are then derived from the environment variables, and can be changed when solutions are imported to other environments. 

### Create an environment variable in a solution

1. Sign in to Power Apps (make.powerapps.com), and then on the left pane select **Solutions**. [!INCLUDE [left-navigation-pane](../../includes/left-navigation-pane.md)]
1. Open the solution you want or create a new one.
1. On the command bar, select **New** > **More**, and then select **Environment variable**. 
1. On the right pane, complete the following columns, and then select **Save**:  
   - **Display name**. Enter a name for the environment variable. 
   - **Name**. The unique name is automatically generated from the **Display name**, but you can change it. 
   - **Data Type**. Select from **Decimal number**, **Text**, **JSON**, **Two options**, **Data source**, or **Secret**.
     >[!NOTE]
     > 
     > - If **Data source** is the selected type, you'll also need to select the **connector**, a valid **connection** for the selected connector, and the **parameter type**. However, the connection is not stored as part of the environment variable. The connection is only used for retrieving available parameter values such as the SharePoint sites you have access to, or the lists associated with a site. For certain parameters such as SharePoint lists, you'll also need to select a parent data source environment variable such as the SharePoint site. Once saved, these will be related in the database.
     > - If **Secret** is the selected type, additional information to set up and configure Azure Key Vault is needed to allow Power Platform to access the secret.
   - **Current Value**. Also known as the value. This property is optional and is a part of the environment variable value table. When a value is present, it's used, even if a default value is also present. Remove the value from your solution if you don't want to use it in the next environment. The values are also separated into separate JSON files within the exported solution.zip file and can be edited offline. More information: [How do I remove a value from an environment variable?](#how-do-i-remove-a-value-from-an-environment-variable)
   - **Default Value**. This column is part of the environment variable definition table and isn't required. The default value is used if there's no current value. 
  

      Separation of default value and current value allows you to service the definition and the default value separately from the value. For example, an application publisher might list their offer on AppSource with a default value. Then optionally, the customer can provide a new value. When the application publisher publishes updates to the application, the value set by the customer isn't overwritten.

      > [!div class="mx-imgBorder"] 
      > ![New environment variable.](media/new-environment-variable.png)

      >[!NOTE]
      > A value can't exist without a definition. The interface only allows creation of one value per definition.

## Enter new values while importing solutions

The modern solution import interface includes the ability to enter values for environment variables. This sets the value property on the `environmentvariablevalue` table.

Starting with an update on December 7, 2023, all environment variable values are visible when importing solutions (or when [using Pipelines to deploy](/power-platform/alm/run-pipeline)). Environment variables without a default value or value will be prompted for a value, but those otherwise are prefilled with a label beneath the text area denoting the value's source: solution value, target environment value, or default value.

  > [!div class="mx-imgBorder"] 
  > ![Environment variable visibility during solution import.](media/solution-import-environment-variables.png)

> [!NOTE]
> - In some cases, for specific data source environment variable values, an **Access denied** warning may appear if the importing maker does not have access to the connection or source used for the environment variable. This is a non-blocking warning, but something to take note of depending on how you plan to use the environment variable in the target environment.  
> - You may remove the value from your solution before exporting the solution. This ensures the existing value will remain in your development environment, but will not get exported in the solution. This approach allows a new value to be provided while importing the solution into other environments. More information: [How do I remove a value from an environment variable?](#how-do-i-remove-a-value-from-an-environment-variable)

## Notifications

A notification is displayed when the environment variables don't have any values. This is a reminder to set the values so that components dependent on environment variables don't fail. 

## Security

The `environmentvariabledefinition` table is [user or team owned](/powerapps/maker/data-platform/types-of-entities). When you create an application that uses environment variables, be sure to assign users the appropriate level of privilege to this table. Permission to the `environmentvariablevalue` table is inherited from the parent `environmentvariabledefinition` table and therefore doesn't require separate privileges. Privileges for `environmentvariabledefinition` tables are included in Environment Maker and Basic User security roles by default. More information: [Security in Dataverse](/power-platform/admin/wp-security).

## Naming

Ensure environment variable names are unique so they can be referenced accurately. Duplicate environment variable display names make environment variables difficult to differentiate and use. Ensure environment variable names are unique so they can be referenced accurately.
The names **$authentication** and **$connection** are specially reserved parameters for flows and should be avoided. Flow save is blocked if environment variables with those names are used.
If an environment variable is used in a flow and the display name of the environment variable is changed, then the designer shows both the old and new display name tokens to help with identification. When updating the flow, we recommend you remove the environment variable reference and add it again.

## Current limitations

- Validation of environment variable values happens within the user interfaces and within the components that use them, but not within Dataverse. Therefore ensure proper values are set if they're being modified through code. 
- [Power Platform Build Tools tasks](/power-platform/alm/devops-build-tool-tasks) aren't yet available for managing data source environment variables. However, this doesn't block their usage within Microsoft provided tooling and within source control systems.
- Interacting with environment variables via custom code requires an API call to fetch the values; there isn't a cache exposed for non-Microsoft code to use.
- To successfully use environment variables with SharePoint lists, the display name and the logical name for each corresponding column in the source and target environments must match.

## Frequently asked questions

### Why can't I see the value for my environment variable?

If the environment variable is in a managed solution, you won't be able to see the value unless you look inside of the **Default solution**. This behavior is by design, since the environment variable value is an unmanaged customization.

### How can I view where environment variables are being used?

Either through selecting **Show dependencies** in the solution interface, while authoring components, or in source control and in the solution file by viewing the app or flow metadata. 

### Are data source environment variables the same as connections?

No. Although they're related. A connection represents a credential or authentication required to interact with the connector. Data source environment variables store parameters that are required by one or more actions in the connector and these parameters often vary depending on the action. For example, a SharePoint Online connection doesn't store any information about sites, lists, or document libraries. Therefore calling the connector requires both a valid connection and some additional parameters. 

### Can data source environment variables be used with shared connections such as SQL Server with SQL authentication?

Generally no. Shared connections with SQL Server store the parameters required to connect to data within the connection. For example, the Server and Database name are provided when creating the connection and therefore are always derived from the connection.

Data source environment variables are used for connectors that rely on user based authentication such as Microsoft Entra ID because the parameters can't be derived from the connection. For these reasons authentication with SQL Server, which is a shared connection, won't use data source environment variables. 

### Can my automated ALM pipeline use different values files for different environments?

Yes. Solution packager accepts file name as input parameters so your pipeline can pack a different values file into the solution depending on the environment type it’s executing against.

### What if someone inadvertently deletes a value?

If not already prevented by dependency system, runtime uses the last known value as a fallback.

### If a value is changed, when does the new value get used in canvas apps and cloud flows?

It might take up to an hour to fully publish updated environment variables because the value is pushed into the apps and flows asynchronously.

### Are premium licenses required?

No. While ALM requires Dataverse (or Dynamics 365 for Customer Engagement), use of premium connectors isn't required. The one caveat is if you're using the Dataverse connector to interact with environment variables as you would with other data records like accounts or contacts. Previously this was the only way to use environment variables in canvas apps and flows.  

### Is there a limit to the number of environment variables I can have?

No. However, the max size of a solution is 120 MB. See [Create a solution](/power-apps/maker/data-platform/create-solution)

### Can environment variable display names and descriptions be localized?

Yes.

### Should I use environment variables instead of storing configuration data in custom tables?

Yes if your configuration data isn't relational. Environment variables should be used for key: value pairs and when the value likely needs to different in other environments. Other tools such as the Configuration migration utility are better suited for migration of relational configuration data stored within custom tables. Unlike other configuration data, environment variables are migrated within solutions and therefore much simpler to manage and more performant to import. 

### Why is a different connection value than the one I want getting assigned automatically when importing?

In some cases where there are multiple connections available for a single (data source-type) environment variable, there's a by-design implementation to select the first connection in the list of connections available for the environment variable. Because there's usually only one connection associated with an environment variable, this isn't something that usually needs to be validated. Additionally, with recent changes to environment variable value visibility, this is easier to validate upon import.

### How do I remove a value from an environment variable?

You might want to remove the value of an environment variable from your solution before exporting the solution. Then, the existing value remains in your development environment, but isn't exported in the solution. This approach allows a new value to be provided while importing the solution into another environment.

To remove the value, follow these steps:

1. In the solution where the environment variable is located select the environment variable to display the properties.
1. Under **Current Value**, select **...** > **Remove from this solution**.

    :::image type="content" source="media/remove-value-env-var.png" alt-text="Remove the value from an environment variable":::

### Can I use environment variables in custom connectors?

Yes. [Environment variable support in custom connectors](/connectors/custom-connectors/environment-variables)

### See also

[Use data source environment variables in canvas apps](environmentvariables-data-source-canvas-apps.md) <br>
[Use environment variables in Power Automate solution cloud flows](environmentvariables-power-automate.md) <br>
[EnvironmentVariableDefinition table/entity reference](/powerapps/developer/data-platform/reference/entities/environmentvariabledefinition) </BR>
[Web API samples](/powerapps/developer/data-platform/webapi/web-api-samples) </BR>
[Use data source environment variables in Canvas apps](EnvironmentVariables-data-source-canvas-apps.md)</BR>
[Use environment variables in Power Automate solution cloud flows](EnvironmentVariables-power-automate.md)</BR>
[Use Azure Key Vault secrets](EnvironmentVariables-azure-key-vault-secrets.md)</BR>
[Environment variable support in custom connectors](/connectors/custom-connectors/environment-variables)</BR>
[Power Apps Blog: Environment variables available in preview!](https://powerapps.microsoft.com/blog/environment-variables-available-in-preview/) 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
