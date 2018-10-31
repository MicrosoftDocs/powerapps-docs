---
title: "Work with data using code in Common Data Service for Apps (PowerApps) | Microsoft Docs" 
description: "CDS for Apps provides two web services that you can use to interact with data: Web API and Organization Service." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "JimDaly" # GitHub ID Temp owner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Work with data using code in Common Data Service for Apps

Common Data Service (CDS) for Apps has [entities](entities.md) that are used to model and manage business data. You can use standard entities or create your own custom entities to store data. 

## Use web services to work with data

CDS for Apps provides two web services that you can use to interact with data: **Web API** and **Organization Service**. Choose the one that best matches the requirement and your skills. 

![Flow diagram to choose web service](media/whentousewebapi.png)

### Web API

The Web API is an OData v4 RESTful endpoint. Use this for any programming language that supports HTTP requests and authentication using OAuth 2.0.

More information: [Use the Common Data Service for Apps Web API](webapi/overview.md) 

### Organization service

Use the .NET Framework SDK assemblies for projects that involve writing plug-ins or workflow extensions. 

More information: [Use the Common Data Service for Apps Organization Service](org-service/overview.md)

> [!NOTE]
> Use the Xrm.Tooling assemblies if you are creating a Windows client application. More information: [Build Windows client applications using the XRM tools](xrm-tooling/build-windows-client-applications-xrm-tools.md)
