---
title: "Work with metadata using the Organization service (Common Data Service for Apps) | Microsoft Docs"
description: "Describes how to programmatically access and modify the metadata model using the Organization service"
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "powerapps"
ms.topic: "article"
author: "brandonsimons" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Work with metadata using the Organization service

Metadata refers to the structure of entities used to manage data in Common Data Service (CDS) for Apps. <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase> is the base class for classes that contain metadata information. This section describes how to programmatically access and modify the metadata model using the Organization service.

> [!IMPORTANT]
> Adding, removing or changing entities, alternate keys, attributes, or relationships can interfere with normal system operation. If you’re applying changes to a production system we recommend that you schedule these operations when it’s least disruptive to users.

## See also

[Use the Web API with metadata](../webapi/use-web-api-metadata.md)

[Work with metadata using code](../metadata-services.md)