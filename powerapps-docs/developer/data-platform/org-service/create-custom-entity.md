---
title: "Create custom entity (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Shows how to programmatically create a custom entity in Microsoft Dataverse." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 10/31/2018
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
# Create custom entity

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

This topic shows how to programmatically create a custom user-owned entity called **Bank Account** and add four different types of attributes to it.  
  
You can also create organization-owned custom entities. More information: [Entity ownership](/dynamics365/customer-engagement/developer/introduction-entities#entity-ownership)  
  
> [!NOTE]
>  You won’t be able to see this entity in the application navigation unless the entity properties are edited to set the **Areas that display this entity** are set.  
  
<a name="BKMK_CreateCustomEntity"></a>   

## Create a custom entity  

 The following sample uses the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> to create the entity and the <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata><xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.PrimaryAttribute>.  
  
 The `_customEntityName` value is “new_bankaccount”.  
  
```csharp
CreateEntityRequest createrequest = new CreateEntityRequest
{

 //Define the entity
 Entity = new EntityMetadata
 {
  SchemaName = _customEntityName,
  DisplayName = new Label("Bank Account", 1033),
  DisplayCollectionName = new Label("Bank Accounts", 1033),
  Description = new Label("An entity to store information about customer bank accounts", 1033),
  OwnershipType = OwnershipTypes.UserOwned,
  IsActivity = false,

 },

 // Define the primary attribute for the entity
 PrimaryAttribute = new StringAttributeMetadata
 {
  SchemaName = "new_accountname",
  RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
  MaxLength = 100,
  FormatName = StringFormatName.Text,
  DisplayName = new Label("Account Name", 1033),
  Description = new Label("The primary attribute for the Bank Account entity.", 1033)
 }

};
_serviceProxy.Execute(createrequest);
Console.WriteLine("The bank account entity has been created.");
```  
  
<a name="BKMK_AddStringAttribute"></a>   

## Add a String attribute to the custom entity  

The following sample adds a <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata> attribute to the `Bank Account` entity.  
  
```csharp
CreateAttributeRequest createBankNameAttributeRequest = new CreateAttributeRequest
{
 EntityName = _customEntityName,
 Attribute = new StringAttributeMetadata
 {
  SchemaName = "new_bankname",
  RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
  MaxLength = 100,
  FormatName = StringFormatName.Text,
  DisplayName = new Label("Bank Name", 1033),
  Description = new Label("The name of the bank.", 1033)
 }
};

_serviceProxy.Execute(createBankNameAttributeRequest);
```
  
<a name="BKMK_AddMoneyAttribute"></a>   

## Add a Money attribute to the custom entity  

 The following sample adds a <xref:Microsoft.Xrm.Sdk.Metadata.MoneyAttributeMetadata> attribute to the `Bank Account` entity.  
  
```csharp
CreateAttributeRequest createBalanceAttributeRequest = new CreateAttributeRequest
{
 EntityName = _customEntityName,
 Attribute = new MoneyAttributeMetadata
 {
  SchemaName = "new_balance",
  RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
  PrecisionSource = 2,
  DisplayName = new Label("Balance", 1033),
  Description = new Label("Account Balance at the last known date", 1033),

 }
};

_serviceProxy.Execute(createBalanceAttributeRequest);

```  
  
<a name="BKMK_AddDateTimeAttribute"></a>   

## Add a DateTime attribute to the custom entity  

The following sample adds a <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata> attribute to the `Bank Account` entity.  
  
```csharp
CreateAttributeRequest createCheckedDateRequest = new CreateAttributeRequest
{
 EntityName = _customEntityName,
 Attribute = new DateTimeAttributeMetadata
 {
  SchemaName = "new_checkeddate",
  RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
  Format = DateTimeFormat.DateOnly,
  DisplayName = new Label("Date", 1033),
  Description = new Label("The date the account balance was last confirmed", 1033)

 }
};

_serviceProxy.Execute(createCheckedDateRequest);
Console.WriteLine("An date attribute has been added to the bank account entity.");
```
  
<a name="BKMK_AddLookupAttribute"></a>
   
## Add a Lookup attribute to the custom entity 
 
 The following sample uses <xref:Microsoft.Xrm.Sdk.Messages.CreateOneToManyRequest> to create a one-to-many relationship with the `Contact` entity so that a <xref:Microsoft.Xrm.Sdk.Metadata.LookupAttributeMetadata> attribute is added to the `Bank Account` entity.  
  
```csharp
CreateOneToManyRequest req = new CreateOneToManyRequest()
{
    Lookup = new LookupAttributeMetadata()
    {
        Description = new Label("The referral (lead) from the bank account owner", 1033),
        DisplayName = new Label("Referral", 1033),
        LogicalName = "new_parent_leadid",
        SchemaName = "New_Parent_leadId",
        RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.Recommended)
    },
    OneToManyRelationship = new OneToManyRelationshipMetadata()
    {
        AssociatedMenuConfiguration = new AssociatedMenuConfiguration()
        {
            Behavior = AssociatedMenuBehavior.UseCollectionName,
            Group = AssociatedMenuGroup.Details,
            Label = new Label("Bank Accounts", 1033),
            Order = 10000
        },
        CascadeConfiguration = new CascadeConfiguration()
        {
            Assign = CascadeType.Cascade,
            Delete = CascadeType.Cascade,
            Merge = CascadeType.Cascade,
            Reparent = CascadeType.Cascade,
            Share = CascadeType.Cascade,
            Unshare = CascadeType.Cascade
        },
        ReferencedEntity = "lead",
        ReferencedAttribute = "leadid",
        ReferencingEntity = _customEntityName,
        SchemaName = "new_lead_new_bankaccount"
    }
};
_serviceProxy.Execute(req);
```
  
### See also  
 [Use the IOrganizationService Sample and Helper Code](/dynamics365/customer-engagement/developer/use-sample-helper-code)   
 <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest>   
 [Customize entity metadata](../customize-entity-metadata.md)   
 [Which Entities are Customizable?](/dynamics365/customer-engagement/developer/which-entities-are-customizable)   
 [Retrieve, update, and delete entities](/dynamics365/customer-engagement/developer/retrieve-update-delete-entities)   
 [Create and update an entity than can be emailed](/dynamics365/customer-engagement/developer/create-update-entity-emailed)   
 [Create a custom activity entity](/dynamics365/customer-engagement/developer/create-custom-activity-entity)   
 [Change Entity Icons](/dynamics365/customer-engagement/developer/modify-icons-entity)   
 [Change Entity Messages](/dynamics365/customer-engagement/developer/modify-messages-entity)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]