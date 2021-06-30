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

Apps and flows often require different configuration settings across environments. Environment variables as configurable input parameters allow management of data separately compared to hard-coding values within your customization or using additional tools. Because they're solution components, performance is much better than importing configuration data as row data.

Benefits of using environment variables:
- No need to manually edit configurable values in a production environment.
- Configure one or more variables in one place and reference like a parameter across multiple solution components.
- Enter different values while importing solutions to other environments. 
- Update values without a code change.
- Granular level security managed by [Microsoft Dataverse](/powerapps/maker/data-platform/data-platform-intro).
- Unlimited number of variables (max solution size is 29 MB).
- Service the definitions and the values independently or together.
- Supported by [SolutionPackager](/powerapps/developer/data-platform/compress-extract-solution-file-solutionpackager) and [DevOps](/power-platform/alm/devops-build-tools) tools enable continuous integration and continuous delivery (CI/CD).
- Support for localization.
- Can be used to control feature flags and other application settings.


## How do they work?
Environment variables can be created and managed through the modern solution interface or by [using code](/powerapps/developer/data-platform/work-with-data). A separate JSON file is created within your solution package for the values, which can also be managed in source control and modified in a build pipeline. Export to and import from Excel is supported. After creating environment variables, you can use them as inputs within plug-ins, flows, and other components. 

### Create an environment variable in Power Apps
1. Sign in to Power Apps, and then on the left panes select **Solutions**. 
2. On the command bar, select **New** and then select **Environment variable**. 
3. On the left pane, complete the following columns, and then select **Save**:  
   - **Display name**. Enter a name for the environment variable. 
   - **Name**. The unique name is automatically generated from the **Display name**, but you can change it. 
   - **Data Type**. Select from **Decimal number**, **Text**, **JSON**, or a **Two option** column. 
   - **Default Value**. This column is part of the environment variable definition table and is not required. Set a default value for the production environments or when the values don't need to be changed for different environments. 
   - **Current Value**. Also known as the override value. This column is optional and is a part of the environment variable value table. Set the value when you'd like to override the default value in your current environment. Remove the value from your solution if you don't want to use it in the next environment. The values are also separated into a separate JSON file within the solution.zip file that is exported. 

      Separation of default value and current value allows you to service the definition and the default value separately from the current value. It also allows us to extend the functionality in the future to support multiple values scoped to a specific run time context.

      > [!div class="mx-imgBorder"] 
      > ![New environment variable](media/new-environment-variable.png)

      >[!NOTE]
      > A value can't exist without a definition. The interface only allows creation of one value per definition.

## Enter new values while importing solutions

The modern solution import interface includes the ability to enter values for environment variables. This sets the value property on the `environmentvariablevalue` table.

You will not be prompted if the environment variables already have either a default value or value present; whether values are part of your solution or are already present in Dataverse.
   >[!NOTE]
   > You may remove the value from your solution before exporting the solution. This ensures the existing value will remain in your development environment, but not get exported in the solution. This approach allows a new value to be set while importing the solution into other environments.  

## Notifications
A notification is displayed when the environment variables do not have any values. This is a reminder to set the values so that components dependent on variables do not fail. It also allows partners to ship variables without values and the customer is prompted to input the values.

>[!NOTE]
> We recommend partners build their own interfaces requiring the customers to provide the values. Notifications help prevent failures if this step is skipped. 

## Security

The environmentvariabledefinition table is [user or team owned](/powerapps/maker/data-platform/types-of-entities). When you create an application that uses environment variables, be sure to assign users the appropriate level of privilege to this table. Permission to the environmentvariablevalue table is inherited from the parent environmentvariabledefinition table and therefore does not require separate privileges. More information: [Security in Dataverse](/power-platform/admin/wp-security).

## Current limitations

- Caching. Plugins will need to run a query to fetch the values. 
- Canvas apps and flows can consume environment variables just like table row data. <!-- In the future we plan to build additional actions into canvas app and flow designers. This will simplify authoring and provide better visibility into environment variables being used by a specific app or flow. -->
- Azure Key Vault integration for secret management. Currently environment variables should'nt be used to store secure data such as passwords and keys.
- Data types are validated in the modern solution interface only, but not currently on the server during the preview. 
- Dependencies are not enforced for certain component types.
- If using Excel to import environment variables, be sure to prepend the publisher prefix to the SchemaName.

### See also
[Power Apps Blog: Environment variables available in preview!](https://powerapps.microsoft.com/blog/environment-variables-available-in-preview/) </BR>
[Use plug-ins to extend business processes](/powerapps/developer/data-platform/plug-ins) </BR>
[Web API samples]/powerapps/developer/data-platform/webapi/web-api-samples) </BR>
[Create Canvas app from scratch using Dataverse.](/powerapps/maker/canvas-apps/data-platform-create-app-scratch) </BR>
[Create a flow with Dataverse](/flow/connection-cds)


[!INCLUDE[footer-include](../../includes/footer-banner.md)] 
