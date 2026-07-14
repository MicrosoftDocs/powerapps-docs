---
title: "Set managed properties for relationships in Power Apps | MicrosoftDocs"
description: "Learn how to set managed properties for a table relationship"
ms.custom: ""
ms.date: 09/19/2024
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: how-to
applies_to: 
  - "Dynamics 365 (online)"
  - "Dynamics 365 Version 9.x"
  - "powerapps"
author: "Mattp123"
ms.assetid: 914c5694-9c80-4424-be89-9f63256b4811
caps.latest.revision: 33
ms.subservice: dataverse-maker
ms.author: "matp"
tags: 
search.audienceType: 
  - maker
---
# Set managed properties for relationships

Managed properties apply when you include a column with a managed solution and import it into another organization. These settings allow a solution maker to have some control over the level of customization that they want to allow people who install their managed solution to have when they customize a table relationship. 

## Set managed properties for a relationship

1. Sign in to [Power Apps](https://make.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc),and select the environment you want.
1. Select **Solutions**, open the solution you want, and then open the table that has the relationship where you want to view the managed properties.
1. Select the relationship, and then select **Advanced** > **Managed properties** on the command bar.  

With relationships, the only managed property is **Allow customizations**. This single setting controls all changes that can be made to the table relationship.  
  
## See also

[Create and edit relationships between tables](create-edit-entity-relationships.md)

[Solutions in Power Apps overview](solutions-overview.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]
