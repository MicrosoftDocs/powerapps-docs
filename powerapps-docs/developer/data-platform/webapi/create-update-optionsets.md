---
title: "Create and update choices (option sets) using the Web API (Microsoft Dataverse) | Microsoft Docs"
description: "Learn about creating and updating choices in Microsoft Dataverse."
ms.date: 03/11/2022
ms.topic: article
applies_to: 
  - "Dynamics 365 (online)"
author: NHelgren # GitHub ID
ms.author: nhelgren
ms.reviewer: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
contributors:
 - JimDaly
---

# Create and update choices (option sets) using the Web API

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Typically, you use *global* option sets to set table columns so that different columns can share the same set of options, which are maintained in one location. Unlike *local* option sets which are defined only for a specific column, you can reuse global option sets. You will also see them used in request parameters in a manner similar to an enumeration.  
 
> [!NOTE] You can only change an existing managed option set if you are the publisher. In order to make a change such as rename option or delete option on these option sets, an Upgrade must be made to the solution that added the option set. More information: [Upgrade or update a solution](../../../maker/data-platform/update-solutions.md)

When you define a global option set using a POST request to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions`, 
we recommend that you let the system assign a value. You do this by passing a **null** value when you create the 
new `OptionMetadata` instance. When you define an option, it will contain an option value prefix specific to the 
context of the publisher set for the solution that the option set is created in. 
This prefix helps reduce the chance of creating duplicate option sets for a managed solution, 
and in any option sets that are defined in environments where your managed solution is installed. For more information, see [Merge option set options](/power-platform/alm/how-managed-solutions-merged#merge-option-set-options).

## Messages

 The following table lists the messages that you can use with global option sets.  
  
|Message|Web API Operation|  
|--|--|
|`CreateOptionSet`|Use `POST` request to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions`.|
|`DeleteOptionSet`|Use `DELETE` request to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions(`*metadataid*`)`.|
|`RetrieveAllOptionSets`|Use `GET` request to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions`.| 
|`RetrieveOptionSet`|Use `GET` request to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions(`*metadataid*`)`.|   

The following table lists the messages you can use with local and global option sets

|Message|Web API Operation|  
|--|--|
|`DeleteOptionValue`<br />Deletes one of the values in a global option set.|<xref:Microsoft.Dynamics.CRM.DeleteOptionValue?text=DeleteOptionValue Action> 
|`InsertOptionValue`<br />Inserts a new option into a global option set.|<xref:Microsoft.Dynamics.CRM.InsertOptionValue?text=InsertOptionValue Action>| 
|`InsertStatusValue`<br />Inserts a new option into the global option set used in the `Status` column.|<xref:Microsoft.Dynamics.CRM.InsertStatusValue?text=InsertStatusValue Action>|
|`OrderOption`<br />Changes the relative order of the options in an option set.|<xref:Microsoft.Dynamics.CRM.OrderOption?text=OrderOption Action>|
|`UpdateOptionSet`|Use `PUT` request with a <xref:Microsoft.Dynamics.CRM.OptionSetMetadataBase?text=OptionSetMetadataBase EntityType>to *[Organization URI]*`/api/data/v9.0/GlobalOptionSetDefinitions(`*metadataid*`)`<br />Only those properties defined by the `OptionSetMetadataBase` can be updated. This does not include the options. Use other actions to make changes to options.|
|`UpdateOptionValue`<br />Updates an option in a global option set.|<xref:Microsoft.Dynamics.CRM.UpdateOptionValue?text=UpdateOptionValue Action>|
|`UpdateStateValue`<br />Inserts a new option into the option set used in the `Status` column.|<xref:Microsoft.Dynamics.CRM.UpdateStateValue?text=UpdateStateValue Action>|

### See also

[Customize choices](../org-service/metadata-option-sets.md)<br />
[Create and edit global choices overview](../../../maker/data-platform/create-edit-global-option-sets.md)<br />
[Create a choice](../../../maker/data-platform/custom-picklists.md)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
