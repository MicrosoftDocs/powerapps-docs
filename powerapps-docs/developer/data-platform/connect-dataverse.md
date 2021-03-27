---
title: "Create client applications (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Introduces the concepts required to create custom client applications that connect to Microsoft Dataverse using code." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/23/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "paulliew" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Create client applications

You can create client applications without writing code using canvas and model-driven apps.
More information: [Overview of creating apps in Power Apps](../../maker/index.md)

If the Power Apps options do not meet your requirements, you can create a client application using code.

## Connecting to Microsoft Dataverse

To connect to a Dataverse environment you need the URL to the environment and credential information for a user account with access to that environment. The strategy you will use depends on whether you have this information or need to get it from the user of your application.

### Discovery service

Users may have access to multiple Dataverse environments. Unless your application will only connect to a specific environment, you can allow the user to choose which environment they want to connect to by using their credentials to *discover* which environments their credentials authorize them to use.

To use the Discovery service you must authenticate the user for the Discovery service and retrieve the environments that are available for them. Usually you must implement some way for them to choose which environment they want to connect to. The next step is to use the information about that environment to authenticate them a second time for access to that specific environment.

More information: [Discovery service](discovery-service.md)

### Authentication

When you know which environment to connect the user to, you the must authenticate them with that environment.

More information: [Authentication with Dataverse web services](authentication.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]