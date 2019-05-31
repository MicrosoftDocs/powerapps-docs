---
title: Understand model-driven app components in PowerApps | MicrosoftDocs
description: "Understand various components of a model-driven app such as data, UI, logic, and visualization."
Keywords: fields, attributes, model-driven app
author: anneta
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
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
Applications and Flows often require different configuration settings across environments. Environment variables provide the cability to transport your application configuration data with solutions. Environment variables act as configurable input parameters and allow you to manage configuration data separately - instead of hard-coding values within your customizations or using various tools to transport record data. Because they're solution components, performance is much better than using data import.

Benefits of using Environment variables:
- No need to manually edit things in a production environment
- Configure in one place and reference like a parameter - even reference a single variable from multiple solution components
- Update values without a code change
- Granular level security managed by CDS
- Managed properties can be set to block editing the values
- The number of variables is unlimited (although the max solution size is 29 MB)
- Service definitions and values separately or together via solutions
- Supported by Solution Packager and DevOps tooling enabling CI/CD
- Localization and dependency tracking are supported

# How they work
Environment variables support CRUD operations through our interface and programatically via the SDK. A separate JSON file is created within your solution package, which can also be managed in source control. We also support export to Excel from a model-driven app. After creating Environment variables in the Common Data Service or Dynamics 365 Customer Engagement, you can consume them in plugins, Flows, and other components.

## Default value
This field is part of the Environment variable definition entity is not required. Set a default value for the value to be used in production or when the values don't need to be changed for different environments.

## Value
This field is optional and is a part of the "Environment variable value" entity. Also known as a current value or override value. Set this when you'd like to override the default value in your current environment. Remove the value from your solution if you don't want this value used in the next environment. Note, a 1:1 relationship is currently enforced between the Environment variable definition and the Environment variable value. A value also cannot exist without a definition.

Why is there a default value and a value? This allows you to service the definition and default value separately from the current value. It also allows us to extend the functionality in the future to support multiple values scoped to a specific run time context.

## Notifications
When Environment variables do not have any values, users with access to the variables will see a notification. This is a reminder to set the value(s) so that components dependent on variables do not fail. It also allows ISV's to ship variables without values and the customer will be prompted to input the value(s). > [!NOTE]
> We recommend ISV's build their own interfaces when customers are required to provide values. Notifications will help prevent failures if this step is skipped. 


# Current limitations
- Modifying values while using the PowerApps interface to imports solutions
- Caching
- Native support for canvas apps
- Key vault integration for secrets
- Scoping (Environment, user, etc)

### See also
[Use plug-ins to extend business processes](https://docs.microsoft.com/powerapps/developer/common-data-service/plug-ins)
[Web API samples](https://docs.microsoft.com/powerapps/developer/common-data-service/webapi/web-api-samples)