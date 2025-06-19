---
title: "Use environment variables frequently asked questions | MicrosoftDocs"
description: "Find the frequently asked questions about environment variables that are used to migrate application configuration data in solutions."
Keywords: environment variables, variables, model-driven app, configuration data
author: caburk
ms.subservice: dataverse-maker
ms.author: caburk
ms.reviewer: matp
ms.date: 10/24/2024
ms.topic: overview
search.audienceType: 
  - maker
contributors:
  - shmcarth
  - asheehi1
---
# Environment variables frequently asked questions

In this article find the frequently asked question (FAQs) for environment variables.

## Why can't I see the value for my environment variable?

If the environment variable is in a managed solution, you won't be able to see the value unless you look inside of the **Default solution**. This behavior is by design, since the environment variable value is an unmanaged customization.

## How can I view where environment variables are being used?

Either through selecting **Show dependencies** in the solution interface, while authoring components, or in source control and in the solution file by viewing the app or flow metadata. 

## Are data source environment variables the same as connections?

No. Although they're related. A connection represents a credential or authentication required to interact with the connector. Data source environment variables store parameters that are required by one or more actions in the connector and these parameters often vary depending on the action. For example, a SharePoint Online connection doesn't store any information about sites, lists, or document libraries. Therefore calling the connector requires both a valid connection and some additional parameters. 

## Can data source environment variables be used with shared connections such as SQL Server with SQL authentication?

Generally no. Shared connections with SQL Server store the parameters required to connect to data within the connection. For example, the Server and Database name are provided when creating the connection and therefore are always derived from the connection.

Data source environment variables are used for connectors that rely on user based authentication such as Microsoft Entra ID because the parameters can't be derived from the connection. For these reasons authentication with SQL Server, which is a shared connection, won't use data source environment variables. 

## Can my automated ALM pipeline use different values files for different environments?

Yes. Solution packager accepts file name as input parameters so your pipeline can pack a different values file into the solution depending on the environment type it’s executing against.

### What if someone inadvertently deletes a value?

If not already prevented by dependency system, runtime uses the last known value as a fallback.

## If a value is changed, when does the new value get used in canvas apps and cloud flows?

It may take up to an hour to fully publish updated environment variables because the value is pushed into the apps and flows asynchronously.

## Are premium licenses required?

No. While ALM requires Dataverse (or Dynamics 365 for Customer Engagement), use of premium connectors isn't required. The one caveat is if you're using the Dataverse connector to interact with environment variables as you would with other data records like accounts or contacts. Previously this was the only way to use environment variables in canvas apps and flows.  

## Is there a limit to the number of environment variables I can have?

No, there is no hard limit to the number of environment variables allowed in an environment, but user experience will become difficult when there are too many environment variables to select from.

## Can environment variable display names and descriptions be localized?

Yes.

## Should I use environment variables instead of storing configuration data in custom tables?

Yes if your configuration data isn't relational. Environment variables should be used for key: value pairs and when the value likely needs to different in other environments. Other tools such as the Configuration migration utility are better suited for migration of relational configuration data stored within custom tables. Unlike other configuration data, environment variables are migrated within solutions and therefore much simpler to manage and more performant to import. 

## How do I remove a value from an environment variable?

You might want to remove the value of an environment variable from your solution before exporting the solution. Then, the existing value remains in your development environment, but isn't exported in the solution. This approach allows a new value to be provided while importing the solution into another environment.

To remove the value, follow these steps:

1. In the solution where the environment variable is located select the environment variable to display the properties.
1. Under **Current Value**, select **...** > **Remove from this solution**.

    :::image type="content" source="media/remove-value-env-var.png" alt-text="Remove the value from an environment variable":::

## Can I use environment variables in custom connectors?

Yes. [Environment variable support in custom connectors](/connectors/custom-connectors/environment-variables)

## See also

[Environment variables overview](EnvironmentVariables.md)
