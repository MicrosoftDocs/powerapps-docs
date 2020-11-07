---
title: "Create custom table (Common Data Service) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Shows how to programmatically create a custom table in Common Data Service." # 115-145 characters including spaces. This abstract displays in the search result.
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
# Create custom table

[!INCLUDE[cc-data-platform-banner](../../../includes/cc-data-platform-banner.md)]

This topic shows how to programmatically create a custom user-owned table called **Bank Account** and add four different types of columns to it.  
  
You can also create organization-owned custom entities. More information: [Table ownership](/dynamics365/customer-engagement/developer/introduction-entities#entity-ownership)  
  
> [!NOTE]
>  You won’t be able to see this table in the application navigation unless the table properties are edited to set the **Areas that display this table** are set.  
  
<a name="BKMK_CreateCustomTable"></a>   

## Create a custom table  

 The following sample uses the <xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest> to create the table and the <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata><xref:Microsoft.Xrm.Sdk.Messages.CreateEntityRequest.PrimaryAttribute>.  
  
 The `_customEntityName` value is “new_bankaccount”.  
  
```csharp
CreateEntityRequest createrequest = new CreateEntityRequest
{

 //Define the table
 Entity = new EntityMetadata
 {
  SchemaName = _customEntityName,
  DisplayName = new Label("Bank Account", 1033),
  DisplayCollectionName = new Label("Bank Accounts", 1033),
  Description = new Label("An entity to store information about customer bank accounts", 1033),
  OwnershipType = OwnershipTypes.UserOwned,
  IsActivity = false,

 },

 // Define the primary column for the table
 PrimaryAttribute = new StringAttributeMetadata
 {
  SchemaName = "new_accountname",
  RequiredLevel = new AttributeRequiredLevelManagedProperty(AttributeRequiredLevel.None),
  MaxLength = 100,
  FormatName = StringFormatName.Text,
  DisplayName = new Label("Account Name", 1033),
  Description = new Label("The primary column for the Bank Account table.", 1033)
 }

};
_serviceProxy.Execute(createrequest);
Console.WriteLine("The bank account table has been created.");
```  
  
<a name="BKMK_AddStringColumn"></a>   

## Add a String column to the custom table  

The following sample adds a <xref:Microsoft.Xrm.Sdk.Metadata.StringAttributeMetadata> column to the `Bank Account` table.  
  
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
  
<a name="BKMK_AddMoneyColumn"></a>   

## Add a Money column to the custom table  

 The following sample adds a <xref:Microsoft.Xrm.Sdk.Metadata.MoneyAttributeMetadata> column to the `Bank Account` table.  
  
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
  
<a name="BKMK_AddDateTimeColumn"></a>   

## Add a DateTime column to the custom table  

The following sample adds a <xref:Microsoft.Xrm.Sdk.Metadata.DateTimeAttributeMetadata> column to the `Bank Account` table.  
  
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
Console.WriteLine("An date column has been added to the bank account table.");
```
  
<a name="BKMK_AddLookupColumn"></a>
   
## Add a Lookup column to the custom table 
 
 The following sample uses <xref:Microsoft.Xrm.Sdk.Messages.CreateOneToManyRequest> to create a one-to-many relationship with the `Contact` table so that a <xref:Microsoft.Xrm.Sdk.Metadata.LookupAttributeMetadata> column is added to the `Bank Account` table.  
  
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
 [Customize table metadata](../customize-entity-metadata.md)   
 [Which Entities are Customizable?](/dynamics365/customer-engagement/developer/which-entities-are-customizable)   
 [Retrieve, update, and delete tables](/dynamics365/customer-engagement/developer/retrieve-update-delete-entities)   
 [Create and update an table than can be emailed](/dynamics365/customer-engagement/developer/create-update-entity-emailed)   
 [Create a custom activity table](/dynamics365/customer-engagement/developer/create-custom-activity-entity)   
 [Change table Icons](/dynamics365/customer-engagement/developer/modify-icons-entity)   
 [Change table Messages](/dynamics365/customer-engagement/developer/modify-messages-entity)
