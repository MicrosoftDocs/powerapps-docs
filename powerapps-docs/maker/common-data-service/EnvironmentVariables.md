---
title: Use environment variables in solutions | MicrosoftDocs
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
# Environment variables overview 
Apps and flows often require different configuration settings across environments. Environment variables as configurable input parameters allow management of data separately compared to hard-coding values within your customization or using additional tools. Because they're solution components, performance is much better than using data import.

Benefits of using environment variables:
- No need to manually edit configurable values in a production environment.
- Configure one or more variables in one place and reference like a parameter across multiple solution components.
- Update values without a code change.
- Granular level security managed by the Common Data Service.
- Managed properties can be set to block editing the definitions and values.
- Unlimited number of variables (max solution size is 29 MB).
- Service the definitions and values independently or together.
- Supported by [SolutionPackager](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/compress-extract-solution-file-solutionpackager) and [DevOps](https://marketplace.visualstudio.com/azuredevops) tools enable continuous integration and continuous delivery (CI/CD).
- Support for localization and dependency tracking.

# How they work
Environment variables support [CRUD](https://docs.microsoft.com/en-us/iis-administration/api/crud) operations through the PowerApps interface and programatically via the SDK. A separate JSON file is created within your solution package for the values, which can also be managed in source control. Export to and import from Excel is supported. After creating the environment variables in the Common Data Service or Dynamics 365 App, you can use them as inputs within plug-ins, flows, and other components.

## Default value
This field is part of the environment variable definition entity and is not required. Set a default value for the production environments or when the values don't need to be changed for different environments.

## Value
Also known as current value or override value, this field is optional and is a part of the "Environment variable value" entity. Set this when you'd like to override the default value in your current environment. Remove the value from your solution if you don't want this value used in the next environment. 

> A 1:1 relationship is currently enforced between the evironment variable definition and the environment variable value. A value cannot exist without a definition.

Separate default value and current value allows you to service the definition and default value separately from the current value. It also allows us to extend the functionality in the future to support multiple values scoped to a specific run time context.

## Notifications
A notification is displayed when the environment variables do not have any values. This is a reminder to set the value(s) so that components dependent on variables do not fail. It also allows partners to ship variables without values and the customer is prompted to input the value(s).

> We recommend partners build their own interfaces when customers are required to provide values. Notifications help prevent failures if this step is skipped. 

# Current limitations
- Modify values during the solution import process.
- Caching.
- Native support for canvas apps.
- Not a secure store for secrets such as passwords.
- Scoping (nvironment, user, etc).
- Dependencies for certain component types.

### See also
[Use plug-ins to extend business processes](https://docs.microsoft.com/powerapps/developer/common-data-service/plug-ins),
[Web API samples](https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/web-api-samples)
