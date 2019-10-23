---
title: "Preview: Use environment variables in solutions | MicrosoftDocs"
description: "Use environment variables to migrate application configuration data in solutions."
Keywords: environment variables, variables, model-driven app, configuration data
author: caburk
ms.author: caburk
manager: kvivek
ms.date: 10/22/2019
ms.service: powerapps
ms.topic: article
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---
# Preview: Environment variables overview 

[!INCLUDE[cc-beta-prerelease-disclaimer](../../includes/cc-beta-prerelease-disclaimer.md)]

Apps and flows often require different configuration settings across environments. Environment variables as configurable input parameters allow management of data separately compared to hard-coding values within your customization or using additional tools. Because they're solution components, performance is much better than importing configuration data as record data.

Benefits of using environment variables:
- No need to manually edit configurable values in a production environment.
- Configure one or more variables in one place and reference like a parameter across multiple solution components.
- Update values without a code change.
- Granular level security managed by [Common Data Service](https://docs.microsoft.com/powerapps/maker/common-data-service/data-platform-intro).
- Unlimited number of variables (max solution size is 29 MB).
- Service the definitions and the values independently or together.
- Supported by [SolutionPackager](/powerapps/developer/common-data-service/compress-extract-solution-file-solutionpackager) and [DevOps](/powerapps/developer/common-data-service/build-tools-overview) tools enable continuous integration and continuous delivery (CI/CD).
- Support for localization.
- Can be used to control feature flags and other application settings.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)] 

## How they work?
Environment variables can be created and managed through the modern solution interface or by [using code](https://docs.microsoft.com/powerapps/developer/common-data-service/work-with-data-cds). A separate JSON file is created within your solution package for the values, which can also be managed in source control and modified in a build pipeline. Export to and import from Excel is supported. After creating environment variables, you can use them as inputs within plug-ins, flows, and other components.

## Default value
This field is part of the environment variable definition entity and is not required. Set a default value for the production environments or when the values don't need to be changed for different environments.

## Value
Also known as the current value or the override value, this field is optional and is a part of the environment variable value entity. Set the value when you'd like to override the default value in your current environment. Remove the value from your solution if you don't want to use it in the next environment. The values are also separated into a separate JSON file within the solution.zip file that is exported. 

>[!NOTE]
> A value can't exist without a definition. The interface only allows creation of one value per definition. 

Separatation of default value and current value allows you to service the definition and the default value separately from the current value. It also allows us to extend the functionality in the future to support multiple values scoped to a specific run time context.

## Notifications
A notification is displayed when the environment variables do not have any values. This is a reminder to set the values so that components dependent on variables do not fail. It also allows partners to ship variables without values and the customer is prompted to input the values.

>[!NOTE]
> We recommend partners build their own interfaces requiring the customers to provide the values. Notifications help prevent failures if this step is skipped. 

## Security
Both the environmentvariabledefinition and environmentvariablevalue entities are [user or team owned](https://docs.microsoft.com/powerapps/maker/common-data-service/types-of-entities). When creating an application that uses Environment variables, be sure to assign users the appropriate level of permission. More information: [Security in Common Data Service](https://docs.microsoft.com/power-platform/admin/wp-security). 

## Current limitations
- Caching. Plugins will need to run a query to fetch the values. 
- Canvas apps and flows can consume Environment variables just like entity record data. In the future we plan to build additional actions into canvas app and flow designers. This will simplify authoring and provide better visibility into environment variables being used by a specific app or flow.
- Azure Key Vault integration for secret management. Currently Environment variables should not be used to store secure data such as passwords and keys.
- Data types are validated in the modern solution interface only, but not currently on the server during the preview. 
- Dependencies are not enforced for certain component types.
- If using Excel to import environment variables, be sure to pre-pend the publisher prefix to the ShemaName.

### See also
[Use plug-ins to extend business processes](https://docs.microsoft.com/powerapps/developer/common-data-service/plug-ins) </BR>
[Web API samples](https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/web-api-samples) </BR>
[Create Canvas app from scratch using Common Data Service.](https://docs.microsoft.com/powerapps/maker/canvas-apps/data-platform-create-app-scratch) </BR>
[Create a flow with Common Data Service](https://docs.microsoft.com/flow/connection-cds)
