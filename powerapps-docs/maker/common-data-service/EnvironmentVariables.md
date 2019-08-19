---
title: "Preview: Use environment variables in solutions | MicrosoftDocs"
description: "Use environment variables to migrate application configuration data in solutions."
Keywords: environment variables, variables, model-driven app, configuration data
author: caburk
ms.author: caburk
manager: kvivek
ms.date: 06/27/2019
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

Apps and flows often require different configuration settings across environments. Environment variables as configurable input parameters allow management of data separately compared to hard-coding values within your customization or using additional tools. Because they're solution components, performance is much better than using data import.

Benefits of using environment variables:
- No need to manually edit configurable values in a production environment.
- Configure one or more variables in one place and reference like a parameter across multiple solution components.
- Update values without a code change.
- Granular level security managed by [Common Data Service](https://docs.microsoft.com/en-us/powerapps/maker/common-data-service/data-platform-intro).
- Managed properties can be set to block editing of the definitions and values.
- Unlimited number of variables (max solution size is 29 MB).
- Service the definitions and the values independently or together.
- Supported by [SolutionPackager](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/compress-extract-solution-file-solutionpackager) and [DevOps](https://marketplace.visualstudio.com/azuredevops) tools enable continuous integration and continuous delivery (CI/CD).
- Support for localization and dependency tracking.

> [!IMPORTANT]
> - This is a preview feature.
> - [!INCLUDE[cc_preview_features_definition](../../includes/cc-preview-features-definition.md)] 

# How they work
Environment variables support [CRUD](https://docs.microsoft.com/en-us/iis-administration/api/crud) operations through the PowerApps interface and programatically via the SDK. A separate JSON file is created within your solution package for the values, which can also be managed in the source control. Export to and import from Excel is supported. After creating the environment variables in Common Data Service or Dynamics 365 App, you can use them as inputs within plug-ins, flows, and other components.

## Default value
This field is part of the environment variable definition entity and is not required. Set a default value for the production environments or when the values don't need to be changed for different environments.

## Value
Also known as the current value or the override value, this field is optional and is a part of the environment variable value entity. Set the value when you'd like to override the default value in your current environment. Remove the value from your solution if you don't want to use it in the next environment. 

>[!TIP]
> A 1:1 relationship is currently enforced between the environment variable definition and the environment variable value. A value cannot exist without a definition.

Separate default value and current value allows you to service the definition and the default value separately from the current value. It also allows us to extend the functionality in the future to support multiple values scoped to a specific run time context.

## Notifications
A notification is displayed when the environment variables do not have any values. This is a reminder to set the values so that components dependent on variables do not fail. It also allows partners to ship variables without values and the customer is prompted to input the values.

>[!NOTE]
> We recommend partners build their own interfaces requiring the customers to provide the values. Notifications help prevent failures if this step is skipped. 

# Current limitations
- Modify the values during the solution import process.
- Caching.
- Native support for canvas apps.
- Not a secure store for secrets such as passwords.
- Scoping (such as environment and user).
- Dependency for certain component types.

### See also
[Use plug-ins to extend business processes](https://docs.microsoft.com/powerapps/developer/common-data-service/plug-ins) </BR>
[Web API samples](https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/web-api-samples)
