---
title: "Create and update option sets using the Web API (Common Data Service for Apps) | Microsoft Docs"
description: "Learn about creating and updating entity Common Data Service for Apps uses a metadata driven architecture to provide the flexibility to create custom entities and additional system entity attributes."
ms.custom: ""
ms.date: 10/31/2018
ms.reviewer: ""
ms.service: "crm-online"
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
applies_to: 
  - "Dynamics 365 (online)"
caps.latest.revision: 15
author: "brandonsimons" # GitHub ID
ms.author: "jdaly"
manager: "ryjones"
---

# Create and update option sets using the Web API

Typically, you use *global* option sets to set fields so that different fields can share the same set of options, which are maintained in one location. Unlike *local* options sets which are defined only for a specific attribute, you can reuse global option sets. You will also see them used in request parameters in a manner similar to an enumeration.  
  
When you define a global option set using a POST request to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions`, 
we recommend that you let the system assign a value. You do this by passing a **null** value when you create the 
new `OptionMetadata` instance. When you define an option, it will contain an option value prefix specific to the 
context of the publisher set for the solution that the option set is created in. 
This prefix helps reduce the chance of creating duplicate option sets for a managed solution, 
and in any option sets that are defined in organizations where your managed solution is installed. For more information, 
see [Merge option set options](../understand-managed-solutions-merged.md#merge-option-set-options).

 ## Messages  
 The following table lists the messages that you can use with global option sets.  
  
|Message|Web API Operation|  
|--|--|
|CreateOptionSet|Use `POST` request to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions`.|
|DeleteOptionSet|Use `DELETE` request to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions(`*metadataid*`)`.|
|RetrieveAllOptionSets|Use `GET` request to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions`.| 
|RetrieveOptionSet|Use `GET` request to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions(`*metadataid*`)`.|   


The following table lists the messages you can use with local and global option sets

|Message|Web API Operation|  
|--|--|
|DeleteOptionValue</br>Deletes one of the values in a global option set.|<xref href="Microsoft.Dynamics.CRM.DeleteOptionValue?text=DeleteOptionValue Action" />  
|InsertOptionValue</br>Inserts a new option into a global option set.|<xref href="Microsoft.Dynamics.CRM.InsertOptionValue?text=InsertOptionValue Action" />| 
|InsertStatusValue</br>Inserts a new option into the global option set used in the `Status` attribute.|<xref href="Microsoft.Dynamics.CRM.InsertStatusValue?text=InsertStatusValue Action" />|
|OrderOption</br>Changes the relative order of the options in an option set.|<xref href="Microsoft.Dynamics.CRM.OrderOption?text=OrderOption Action" />|
|UpdateOptionSet|Use `PUT` request with a <xref href="Microsoft.Dynamics.CRM.OptionSetMetadata?text=OptionSetMetadata EntityType" /> to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions(`*metadataid*`)/Microsoft.Dynamics.CRM.OptionSetMetadata`<br />For a local option set use *[Organization URI]*`/api/data/v9.0/EntityDefinitions(`*metadataid*`)/Attributes(`*metadataid*`)/Microsoft.Dynamics.CRM.PicklistAttributeMetadata/OptionSet`.|
|UpdateOptionValue</br>Updates an option in a global option set.|<xref href="Microsoft.Dynamics.CRM.UpdateOptionValue?text=UpdateOptionValue Action" />|
|UpdateStateValue</br>Inserts a new option into the option set used in the `Status` attribute.|<xref href="Microsoft.Dynamics.CRM.UpdateStateValue?text=UpdateStateValue Action" />|

### See also

[Customize option sets](../org-service/metadata-option-sets.md)