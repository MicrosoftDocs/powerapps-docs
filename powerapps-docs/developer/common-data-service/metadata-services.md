---
title: "Work with metadata using code (Common Data Service for Apps) | Microsoft Docs"
description: "Both the [Web API](webapi/overview.md) and the [Organization service](org-service/overview.md) include capabilities to perform CRUD operations on the entity schema"
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "mayadumesh"
ms.author: "jdaly"
ms.reviewer: "kvivek"
manager: "ryjones"
---

# Work with metadata using code

Both the [Web API](webapi/overview.md) and the [Organization service](org-service/overview.md) include capabilities to perform CRUD operations on the entity schema. While you can perform these operations using code, generally you will use designers to add, update, or delete custom schema elements. Users must have administrator privileges to apply schema changes, but all users can read metadata.

## Why work with metadata?

A more common use for the metadata services is to retrieve metadata about the environment that your extension is running within. Because every environment can be different and schema metadata contains much of the information about how the environment is configured, you may need to retrieve this information to allow for your extensions to adapt to other customizations that are in effect in that environment.

Some examples:
- The number of options available in an optionset attribute can change. Rather than hard-code the values in your environment, consider whether different options are present. You can query the system to determine whether the current environment has different options.
- The display name for an entity can be changed. The default display name for the account entity is *Account*. This could be changed to *Company*. If you want to display a message to a user and refer to the name of an entity, you should not hard-code this but instead use the value that matches what the user is accustomed to seeing and use the display name retrieved from the entity metadata instead.

## Browse the metadata for your organization

Developing a good working understanding of the metadata in the system can help you understand how Common Data Service for Apps platform works. The designers available to edit metadata cannot show all the details found in the metadata. You can install a model-driven app called the *Metadata Browser* which will allow you to view all the hidden entities and metadata properties that are found in the system. More information about the *Metadata Browser*: [Browse the metadata for your organization](browse-your-metadata.md)

## Programmatically work with metadata

For more information about programmatically working with metadata using:
- **Web API**: [Use Web API with CDS for Apps metadata](webapi/use-web-api-metadata.md)
- **Organization service**: [Use Organization service with CDS for Apps metadata](org-service/work-with-metadata.md)