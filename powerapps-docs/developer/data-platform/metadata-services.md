---
title: "Work with definitions using code (Microsoft Dataverse) | Microsoft Docs"
description: "Both the [Web API](webapi/overview.md) and the [Organization service](org-service/overview.md) include capabilities to perform CRUD operations on the table schema"
ms.custom: ""
ms.date: 03/12/2021
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh"
ms.author: "jdaly"
ms.reviewer: "pehecke"
manager: "ryjones"
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Work with table definitions using code

Both the [Web API](webapi/overview.md) and the [Organization service](org-service/overview.md) include capabilities to perform CRUD operations on the table. While you can perform these operations using code, generally you will use designers to add, update, or delete custom schema elements. Users must have administrator privileges to apply schema changes, but all users can read table definitions.

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

## Why work with table definitions?

A more common use for the table definitions services is to retrieve table definitions about the environment that your extension is running within. Because every environment can be different and schema table definitions contains much of the information about how the environment is configured, you may need to retrieve this information to allow for your extensions to adapt to other customizations that are in effect in that environment.

Some examples:
- The number of options available in choices can change. Rather than hard-code the values in your environment, consider whether different options are present. You can query the system to determine whether the current environment has different options.
- The display name for a table can be changed. The default display name for the account is *Account*. This could be changed to *Company*. If you want to display a message to a user and refer to the name of a table, you should not hard-code this but instead use the value that matches what the user is accustomed to seeing and use the display name retrieved from the table definitions instead.

## Browse table definitions for your organization

Developing a good working understanding of the table definitions in the system can help you understand how Microsoft Dataverse platform works. The designers available to edit table definitions cannot show all the details found in the table definitions. You can install a model-driven app called the *Metadata Browser* which will allow you to view all the hidden tables and table definitions properties that are found in the system. More information about the *Metadata Browser*: [Browse table definitions for your organization](browse-your-metadata.md)

## Programmatically work with table definitions

For more information about programmatically working with table definitions using:
- **Web API**: [Use Web API with Dataverse table definitions](webapi/use-web-api-metadata.md)
- **Organization service**: [Use Organization service with Dataverse table definitions](org-service/work-with-metadata.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]