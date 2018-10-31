---
title: Configure entity relationship cascading behavior (Common Data Service for Apps) | Microsoft Docs
description: Configure cascading behaviors for a one-to-many entity relationship in Common Data Service for Apps to preserve data integrity and automate business processes.
services: ''
suite: powerapps
documentationcenter: na
author: "mayadumesh" # GitHub ID
manager: kvivek
editor: ''
tags: ''
ms.service: powerapps
ms.devlang: na
ms.topic: article
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 10/31/2018
ms.author: jdaly
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Configure entity relationship cascading behavior  

 You can configure cascading behaviors for a one-to-many entity relationship to preserve data integrity and automate business processes. Both Web API and organization service support configuring cascading behavior.

## Using Web API to configure cascading behavior

When working with Web API, you can define a One-to-Many relationship using <xref href="Microsoft.Dynamics.CRM.OneToManyRelationshipMetadata?text=OneToManyRelationshipMetadata EntityType" />. This definition includes the name of the intersect entity to be created as well as how the relationship should be displayed in the application by using <xref href="Microsoft.Dynamics.CRM.AssociatedMenuConfiguration?text=AssociatedMenuConfiguration ComplexType" />, <xref href="Microsoft.Dynamics.CRM.Label?text=Label ComplexType" /> and <xref href="Microsoft.Dynamics.CRM.LocalizedLabel?text=LocalizedLabel ComplexType" />. 

More information: [Create a One-to-Many relationship using Web API](webapi/create-update-entity-relationships-using-web-api.md#create-a-one-to-many-relationship).

## Using Organization Service to configure cascading behavior

When you use <xref:Microsoft.Xrm.Sdk.Messages.CreateOneToManyRequest> or <xref:Microsoft.Xrm.Sdk.Messages.UpdateRelationshipRequest> you include an instance of a <xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata> class in the body of the request. In the <xref:Microsoft.Xrm.Sdk.Metadata.OneToManyRelationshipMetadata.CascadeConfiguration> property of that class you use the <xref:Microsoft.Xrm.Sdk.Metadata.CascadeConfiguration> class.  

The `CascadeConfiguration` (<xref:Microsoft.Xrm.Sdk.Metadata.CascadeConfiguration> class or <xref href="Microsoft.Dynamics.CRM.CascadeConfiguration?text=CascadeConfiguration ComplexType" />) contains the properties representing actions that may be performed on the referenced entity in the one-to-many entity relationship. Each property can be assigned one of the values of the <xref href="Microsoft.Dynamics.CRM.CascadeType?text=CascadeType EnumType" />.  

|Value|Application label|Description|  
|-----------|-----------------------|-----------------|  
|Active|Cascade Active|Perform the action on all active referencing entity records associated with the referenced entity record.|  
|Cascade|Cascade All|Perform the action on all referencing entity records associated with the referenced entity record.|  
|NoCascade|Cascade None|Do nothing.|  
|RemoveLink|Remove Link|Remove the value of the referencing attribute for all referencing entity records associated with the referenced entity record.|  
|Restrict|Restrict|Prevent the Referenced entity record from being deleted when referencing entities exist.|  
|UserOwned|Cascade User Owned|Perform the action on all referencing entity records owned by the same user as the referenced entity record.|  
  
 The `CascadeConfiguration` (<xref:Microsoft.Xrm.Sdk.Metadata.CascadeConfiguration> class or <xref href="Microsoft.Dynamics.CRM.CascadeConfiguration?text=CascadeConfiguration ComplexType" />) contains the following properties representing actions that may be performed on the referenced entity in the one-to-many entity relationship.  
  
|Action|Description|Valid options|  
|------------|-----------------|-------------------|  
|Assign|The referenced entity record owner is changed.|Active<br />Cascade<br />NoCascade<br />UserOwned|  
|Delete|The referenced entity record is deleted. **Note:**  The options for this action are limited.|Cascade<br />RemoveLink<br />Restrict|  
|Merge|The record is merged with another record. **Note:**  For referenced entities that can be merged, Cascade is the only valid option. In other cases use NoCascade.|Cascade<br />NoCascade|  
|Reparent|See [About the reparent action](#about-the-reparent-action) later.|Active<br />Cascade<br />NoCascade<br />UserOwned|  
|Share|When the referenced entity record is shared with another user.|Active<br />Cascade<br />NoCascade<br />UserOwned|  
|Unshare|When sharing is removed for the referenced entity record.|Active<br />Cascade<br />NoCascade<br />UserOwned|  
  
<a name="BKMK_ReparentAction"></a>   
### About the reparent action  
 The reparent action is very similar to the share action except that it deals with the inherited read access rights instead of explicit read access rights. The reparent action is when you change the value of the referencing attribute in a parental relationship. When a reparent action occurs, the desired scope of the inherited read access rights for related entities might change. The cascade actions related to the reparent action refer to changes to read access rights for the entity record and any entity records related to it.  

### See also

[Entity relationship metadata](entity-relationship-metadata.md)  

