---
title: "Use environment variables in solutions | MicrosoftDocs"
description: "Use environment variables to migrate application configuration data in solutions."
Keywords: environment variables, variables, model-driven app, configuration data
author: caburk
ms.author: caburk
ms.reviewer: matp
manager: kvivek
ms.date: 05/27/2020
ms.service: powerapps
ms.topic: article
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Environment variables overview 

[!INCLUDE[cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

Applications often require different configuration settings or input parameters when deployed to different environments. Environment variables store the parameter keys and values, which then serve as input to various other application objects. Separating the parameters from the consuming objects allows you to change the values within the same environment or when you migrate solutions to other environments. The alternative is leaving hard-coded parameter values within the components that use them. This is often problematic; especially when the values need to be changed during application lifecycle management (ALM) operations. Because environment variables are solution components, you can transport the references (keys) and change the values when solutions are migrated to other environments.

Benefits of using environment variables:
- No need to manually edit configurable values in a production environment.
- Provide new values while **importing solutions** to other environments.
- Store configuration for the **data sources** used in canvas apps and flows. For example, SharePoint Online site and list parameters can be stored as environment variables; therefore allowing you to connect to different sites and lists in different environments without needing to modify the apps and flows.
- Package and transport your customization and configuration together and manage them in a single location.
- One environment variable can be used across many different solution components - whether they're the same type of component or different. For example, a canvas app and a flow can use the same environment variable. When the value of the environment variable needs to change, you only need to change one value. 
- Additionally, if you need to retire a data source in production environments, you can simply update the environment variable values with information for the new data source. The apps and flows do not require modification and will start using the new data source.
- Granular level security managed by [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro).
- Unlimited number of variables (max solution size is 29 MB).
- Service the definitions and the values independently or together.
- Supported by [SolutionPackager](/powerapps/developer/data-platform/compress-extract-solution-file-solutionpackager) and [DevOps](/powerapps/developer/data-platform/build-tools-overview) tools enable continuous integration and continuous delivery (CI/CD).
- The environment variables can be unpacked and stored in source control. You may also store different environment variables values files for the separate configuration needed in different environments. Solution Packager can then accept the file corresponding to the environment the solution will be imported to. 
- Support for localization of the display strings.
- When compared to storing configuration data as record data in custom tables, solution import is far simpler and more performant than handling row data.

## How do they work?

Environment variables can be created and modified within the modern solution interface, automatically created when connecting to certain data sources in canvas apps, or by [using code](/powerapps/developer/data-platform/work-with-data). You can also export and import environment variables using Microsoft Excel. Once environment variables are present in an environment, you can then use them as inputs when authoring canvas apps, Power Automate flows, when developing plug-ins, as well as many other places such as adding a Power BI dashboard to a model-driven app. 

### Create an environment variable in a solution

1. Sign in to Power Apps, and then on the left panes select **Solutions**. 
2. On the command bar, select **New** and then select **Environment variable**. 
3. On the left pane, complete the following columns, and then select **Save**:  
   - **Display name**. Enter a name for the environment variable. 
   - **Name**. The unique name is automatically generated from the **Display name**, but you can change it. 
   - **Data Type**. Select from **Decimal number**, **Text**, **JSON**, **Two options**, or **Data source**. 
   >[!NOTE]
   >If **Data source** is the selected type, you'll also need to select the **connector**, a valid **connection** for the selected connector, and the **parameter type**. For certain parameters such as SharePoint lists, you'll also need to select a parent data source environment variable such as the SharePoint site. Once saved, these will be related in the database. 
   - **Current Value**. Also known as the value. This column is optional and is a part of the environment variable value table. Set the value when you'd like to override the default value in your current environment. Remove the value from your solution if you don't want to use it in the next environment. The values are also separated into separate JSON files within the solution.zip file that is exported. 
   - **Default Value**. This column is part of the environment variable definition table and is not required. The default value is used if there is no current value. 
  

      Separation of default value and current value allows you to service the definition and the default value separately from the value. For example, an application publisher may list their offer on App Source with a default value. Then optionally, the customer can provide a new value. When the application publisher publishes updates to the application, the value set by the customer will not be overwritten. 

      > [!div class="mx-imgBorder"] 
      > ![New environment variable](media/new-environment-variable.png)

      >[!NOTE]
      > A value can't exist without a definition. The interface only allows creation of one value per definition.

## Use data source environment variables in canvas apps
### Use pre-existing data source environment variables

Environment variables can be reused across other apps and even different types of resources like cloud flows. You may wish to first create them within your solution and later use them while authoring canvas apps and cloud flows.
1. Follow the steps above for **Create an environment variable in a solution**
2. Edit or create a canvas app from your solution.
4. Add a **new** data source for SharePoint online.
5. Select the **Advanced** tab
6. You'll see a filtered list of environment variables that you have access to and that match the parameter being set. For example, when you select the SharePoint site, you'll see a list of all data source environment variables with **Connector** = SharePoint and **Parameter type** = Site. The same is true when selecting SharePoint lists for a given site. 


### Automatically create data source environment variables when connecting to data

This option provides simplicity and ensures environment variables will always be used for data sources such as SharePoint online. However, some customers prefer to provide their own schema names and therefore should create them from solutions.
1. Edit or create a canvas app from your solution.
2. Select **File** > **Settings** > **General** and enable the setting to **Automatically create environment variables when adding data sources**.
3. Add a **new** data source for SharePoint online.
4. Select a SharePoint **site**, then one or more **lists**. You do not need to select the **Advanced** tab.
   >[!NOTE]
   >To prevent creation of duplicate environment variables, you'll be prompted to use the existing environment variable when duplicates are identified. You may de-select the option to use the existing environment variable if creation of a duplicate is desired. 
5. Select **save**. 

>[!NOTE]
>Pre-existing canvas apps will not automatically use data source environment variables. Remove the data source(s) from the app and add them back using the above steps to upgrade these apps to use environment variables. 

## Use environment variables in Power Automate cloud flows

Environment variables can't be automatically created when authoring flows. However, environment variables are not limited to those of type = **data source**. All types of environment variables can be used in triggers and actions.
1. Follow the steps above for **Create an environment variable in a solution**
2. Edit or create a cloud flow from a solution. 
3. When you provide a value for the parameter, scroll down and select **Enter a custom value**. Directly entering a value will not use environment variables. 
4. Environment variables that you have access to are listed in the **Dynamic content** section of the card.
5. Select the appropriate environment variable.

>[!NOTE]
>The environment variables are currently listed under **Parameters** and the list is not currently filtered based on matching data types.

 
## Enter new values while importing solutions

The modern solution import interface includes the ability to enter values for environment variables. This sets the value property on the `environmentvariablevalue` table.

You will **not** be prompted if the environment variables already have either a default value or value present; whether values are part of your solution or are already present in the target environment.
   >[!NOTE]
   > You may remove the value from your solution before exporting the solution. This ensures the existing value will remain in your development environment, but will not get exported in the solution. This approach allows a new value to be provided while importing the solution into other environments.  



## Notifications
A notification is displayed when the environment variables do not have any values. This is a reminder to set the values so that components dependent on environment variables do not fail. 


## Security

The `environmentvariabledefinition` table is [user or team owned](/powerapps/maker/common-data-service/types-of-tables). When you create an application that uses environment variables, be sure to assign users the appropriate level of privilege to this table. Permission to the `environmentvariablevalue` table is inherited from the parent `environmentvariabledefinition` table and therefore does not require separate privileges. More information: [Security in Dataverse](/power-platform/admin/wp-security).

## Current limitations

- SharePoint online is currently the only data source supported for environment variables of type "data source" within canvas apps. However, Common data service (now Dataverse) will be available shortly for when canvas apps connect to Dataverse environments outside the current environment. Other types of environment variables may be used within canvas apps by retrieving them as you would recrod data via Common data service connection. Note: the former does not require a premium license whereas the latter does. 
- Interacting with environment variables via custom code requires an API call to fetch the values; there is not a cache exposed for 3rd party code to leverage. 
- Azure Key Vault integration for secret management. While on our roadmap, currently environment variables should'nt be used to store secure data such as passwords and keys.
- Specialized tasks for environment variables of type **data source** are not yet available within the [Power Platform Build Tools tasks](https://docs.microsoft.com/power-platform/alm/devops-build-tool-tasks). However, you may add your own custom tasks to achieve the same result. 

## Frequently asked questions
**How can I view where environemnt variables are being used?**
Either through clicking **Show dependencies** in the solution interface, while authoring components, or in source control and in the solution file by viewing the app or flow metadata. 

**Are data source environment variables the same as connections?**
No. Although they're related. A connection represents a credential or authentication required to interact with the connector. Data source environment variables store parameters that are required by one or more actions in the connector and these parameters often vary depending on the action. For example, a SharePoint online connection does not store any information about sites, lists, document libraries, etc.  

**Can data source environment variables be used with shared connections such as SQL Server with SQL authentication?**
Generally no. Shared connections such as SQL server with SQL authentication store the parameters required to connect to data within the connection. For example, the Server and Database name are provided when creating the connection and therefore are always derived from the connection. 
Data source environment variables are used for connectors that rely on user based authentication such as Azure Active Directory because the parameters cannot be derived from the connection. For these reasons SQL Server with SQL authtication, which is a shared connection, will not use data source environment varibles but SQL Server with AAD authentication, which is a personal connection will. 

**Can my automated ALM pipeline use different values files for different environments?**
Yes, solution packager accepts file name as input parameters so your pipeline can pack a different values file into the solution depending on the environment type it’s executing against.

**What if someone inadvertently deletes a value?**
If not already prevented by dependency system, runtime will use the last known value as a fallback.

**If a value is changed, when does the new value get used in canvas apps and cloud flows?**
For canvas apps, the new value will be used during the next session. For example, closing the app and then playing it again. 
With cloud flows, the flows must currently be de-activated and re-activated in order to use the updated value. 

**Are premium licenses required?**
No. While ALM requires Dataflex (or Dynamics 365 for Customer Engagement), use of premium connectors is not required. The one caveat is if you're using the Common data service connector to interact with environment variables as you would with other data records like Accounts or Contacts. Previously this was the only way to use environment variables in canvas apps and flows.  

**Can I use all types of environment variables in DataVerse for Teams?**
Yes.


### See also
[Power Apps Blog: Environment variables available in preview!](https://powerapps.microsoft.com/blog/environment-variables-available-in-preview/)
[Use plug-ins to extend business processes](https://docs.microsoft.com/powerapps/developer/data-platform/plug-ins) </BR>
[Web API samples](https://docs.microsoft.com/powerapps/developer/data-platform/webapi/web-api-samples) </BR>
[Create Canvas app from scratch using Dataverse.](https://docs.microsoft.com/powerapps/maker/canvas-apps/data-platform-create-app-scratch) </BR>
[Create a flow with Dataverse](https://docs.microsoft.com/flow/connection-cds)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
