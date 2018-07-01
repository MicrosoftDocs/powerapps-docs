---
title: "<Topic Title> (Common Data Service for Apps) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "<Description>" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 08/01/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
---
# Create Client applications

<!-- https://docs.microsoft.com/en-us/dynamics365/customer-engagement/developer/connect-customer-engagement

This is mostly an orientation topic.
S/b the topic about Creating clients application 
It should introduce the discovery services and authentication

-->

## Create clients using PowerApps

You can create client applications without writing code using canvas and model-driven apps.
More information: [Overview of creating apps in PowerApps](../../maker/index.md)

If the PowerApps options do not meet your requirements, you can create a client application using code.

## Connecting to CDS for Apps

To connect to a CDS for Apps environment you need the URL to the environment and credential information for a user account with access to that environment. The strategy you will use depends on whether you have this information or need to get it from the user of your application.

### Discovery service

People may have access to multiple CDS for Apps environments. Unless your application will only connect to a specific environment, you can allow the user to choose which environment they want to connect to by using their credentials to *discover* which environments their credentials provide them access to. This is the purpose of the discovery web service.

To use the discovery service you must authenticate the user for the discovery service and retrieve the environments that are available for them. Usually you will provide a method for the to choose which environment they want to connect to. The next step is to use the information about that environment to authenticate them a second time for access to that specific environment.

### Authenticaion

When you know which environment to connect the user to, you the must authenticate them with that environment.

<!-- TODO continue on these lines -->