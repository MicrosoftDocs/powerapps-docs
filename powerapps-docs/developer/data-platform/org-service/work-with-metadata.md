---
title: "Work with table definitions using the Organization service (Microsoft Dataverse) | Microsoft Docs"
description: "Describes how to programmatically access and modify table and column definitions using the Organization service"
ms.custom: ""
ms.date: 06/10/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Work with table definitions using the Organization service

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Definitions (metadata) refers to the structure of tables used to manage data in Microsoft Dataverse. <xref:Microsoft.Xrm.Sdk.Metadata.MetadataBase> is the base class for classes that contain definition information. This section describes how to programmatically access and modify the definition model using the Organization service.

> [!IMPORTANT]
> Adding, removing or changing tables, alternate keys, columns, or relationships can interfere with normal system operation. If you’re applying changes to a production system we recommend that you schedule these operations when it’s least disruptive to users.

## See also

[Use the Web API with metadata](../webapi/use-web-api-metadata.md)  
[Work with table definitions using code](../metadata-services.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]