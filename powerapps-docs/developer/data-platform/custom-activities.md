---
title: "Custom activities (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Custom activities support the communication needs of a business such as instant messaging (IM) and Short Message Service (SMS)" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/25/2018
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "mayadumesh" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Custom activities

In Microsoft Dataverse, you can create custom activities to support the communication needs of a business such as instant messaging (IM) and Short Message Service (SMS). To create a custom activity in Dataverse, create a custom table, and specify it as an activity table using the <xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsActivity> property.  
  
 However, unlike other custom tables, you can’t specify a primary column for a custom activity because, by default, each custom activity must have a primary column named ”Subject”.  
  
 When you create a custom activity, all the properties and privileges of the `activitypointer` table are inherited for the custom activity. Further, all the activity party types become available for the custom activity, and as a result the corresponding properties are also inherited.  
  
 You can create 1-to-Many (1:N) relationships for a custom activity just like any other activity, and also update the existing relationships.  
  
## Privileges and access rights 
 
 You require the same set of Dataverse privileges and access rights to work with custom activities as those required to work with custom entities. For more information about custom tables, see [Customize table definition](customize-entity-metadata.md).  
  
## Creating a custom activity  
 To create a custom activity, set the values of the properties listed in the following table.  
  
|Property name|Value|Notes|  
|-------------------|-----------|-----------|  
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsActivity>|`true`|Specify the custom table as an activity table.|  
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsAvailableOffline>|`true`|A custom activity table must have offline availability.|  
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.IsMailMergeEnabled>|`false`|A custom activity table cannot have mail merge enabled.|  
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.OwnershipType>|<xref:Microsoft.Xrm.Sdk.Metadata.OwnershipTypes>. TeamOwned<br />or<br /><xref:Microsoft.Xrm.Sdk.Metadata.OwnershipTypes>. UserOwned|A custom activity table can be either team-owned or user-owned.|  
|<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata>.<xref:Microsoft.Xrm.Sdk.Metadata.EntityMetadata.ActivityTypeMask>|0 - None<br />or<br />1 – Communication Activity|(Optional) Specify whether a custom activity should appear in the activity menus in the web application.<br /><br /> -   Specify **0 (None)** to hide it from appearing in the activity menus. The custom activity will appear in the associated grids of only those entities with which it is associated (has relationship).<br />-   Specify **1 (Communication Activity)** to make it appear in the activity menus.<br /><br /> If you do not specify this property, the custom activity is created with the default property value: 1. That is, the custom activity is available in the activity menus. Moreover, `ActivityTypeMask` can be set at the activity creation time only, and once set, cannot be modified.|  
|<xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>.<xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.HasActivities>|`false`|A custom activity table must not have a relationship with activities.|  
|<xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>.<xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.HasNotes>|`true`|A custom activity table must have a relationship to notes.|  
|<xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>. <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.PrimaryAttribute>|<xref:Microsoft.Xrm.Sdk.Metadata.AttributeMetadata.SchemaName> is “Subject”.|The schema name of the `PrimaryAttribute` for all activities must be “Subject”.|  
  
## Example  
 The following sample shows how you can create a custom activity.  
  
```csharp
String prefix = "new_";

String customEntityName = prefix + "instantmessage";

// Create the custom activity table.
CreateEntityRequest request = new CreateEntityRequest
{
    HasNotes = true,
    HasActivities = false,
    PrimaryAttribute = new StringAttributeMetadata
    {
        SchemaName = "Subject",
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
        MaxLength = 100,
        DisplayName = new Label("Subject", 1033)
    },
    Entity = new EntityMetadata
    {
        IsActivity = true,
        SchemaName = customEntityName,
        DisplayName = new Label("Instant Message", 1033),
        DisplayCollectionName = new Label("Instant Messages", 1033),
        OwnershipType = OwnershipTypes.UserOwned,
        IsAvailableOffline = true,

    }
};

_serviceProxy.Execute(request);

//Entity must be published
``` 

### See also  
 [Activity tables](activity-entities.md)   
 [ActivityPointer (activity) table](activitypointer-activity-entity.md)   


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
