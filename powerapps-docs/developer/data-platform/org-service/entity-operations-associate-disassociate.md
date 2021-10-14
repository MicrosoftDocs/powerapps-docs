---
title: "Associate and disassociate table rows using the Organization Service (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to associate and disassociate table rows using the Organization Service" # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 06/04/2021
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

# Associate and disassociate table rows using the Organization Service

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Table rows are associated to each other using lookup columns on the related table row. The simplest way to associate two rows in a one-to-many relationship is to use an <xref:Microsoft.Xrm.Sdk.EntityReference> to set the value of a lookup column on the related row.

The simplest way to disassociate two rows in a one-to-many relationship is to set the value of the lookup column to null.

Relationships using an many-to-many relationship also depend on lookup columns on the *intersect entity* that supports the many-to-many relationship. These relationship are defined by the existence of rows in that intersect entity. While you can interact with the intersect entity directly, it is much easier to use the API to do this for you.

## Use the Associate method or AssociateRequest

The main value in using the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Associate*> method or the <xref:Microsoft.Xrm.Sdk.Messages.AssociateRequest> with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method is that you can:

- Associate multiple rows in one operation
- Easily associate rows using a many-to-many relationship without concerning yourself with the intersect entity.

To associate table rows with these APIs you need three things:

- An entity reference to the row you want to associate
- The name of the relationship
- One or more references that you want to associate the table row to

Whether the relationship is a one-to-many or many-to-many relationship doesn't matter. The parameters or properties are equivalent.

You can discover the names of the relationships by viewing the customization UI or in the metadata using the Metadata Browser.

More information: 

- [Create and edit 1:N (one-to-many) or N:1 (many-to-one) relationships](../../../maker/data-platform/create-edit-1n-relationships.md)
- [Create and edit many-to-many (N:N) table row relationships](../../../maker/data-platform/create-edit-nn-relationships.md)
- [Browse the metadata for your environment](../browse-your-metadata.md)

The following example will set a specific contact (`jimGlynn`) as the primary contact for all accounts that are in Redmond.


```csharp

// Retrieve the accounts
var query = new QueryByAttribute("account")
{
ColumnSet = new ColumnSet("name")
};
query.AddAttributeValue("address1_city", "Redmond");

EntityCollection accounts = svc.RetrieveMultiple(query);

//Convert the EntityCollection to a EntityReferenceCollection
var accountReferences = new EntityReferenceCollection();

accounts.Entities.ToList().ForEach(x => {
accountReferences.Add(x.ToEntityReference());
});

// The contact to associate to the accounts
var jimGlynn = new EntityReference("contact", 
new Guid("cf76763a-ba1c-e811-a954-000d3af451d6"));

// The relationship to use
var relationship = new Relationship("account_primary_contact");

// Use the Associate method
svc.Associate(jimGlynn.LogicalName, jimGlynn.Id, relationship, accountReferences);
```
Although there is no particular advantage in doing so, if you wanted to use the <xref:Microsoft.Xrm.Sdk.Messages.AssociateRequest>, you can replace the last line with this:


```csharp
// Use AssociateRequest
AssociateRequest request = new AssociateRequest()
{
RelatedEntities = accountReferences,
Relationship = relationship,
Target = jimGlynn
};

svc.Execute(request);
```

This operation is the same as three separate update operations to the [Account](../reference/entities/account.md).[PrimaryContactId](../reference/entities/account.md#BKMK_PrimaryContactId) lookup column, but it is using the [account_primary_contact](../reference/entities/contact.md#BKMK_account_primary_contact) relationship, which is a many-to-one entity relationship on the account and a one-to-many entity relationship on the contact.

If you examine the properties of the relationship columns, you can see that the `ReferencingEntity` value is `account` and the `ReferencingAttribute` value is `primarycontactid`.


## Use the Disassociate method or DisassociateRequest

The <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate*> method or the <xref:Microsoft.Xrm.Sdk.Messages.DisassociateRequest> with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method are just the reverse of the way that you associate table rows.

The following code reverses the associations made in the sample above.


```csharp
// Retrieve the accounts
var query = new QueryByAttribute("account")
{
ColumnSet = new ColumnSet("name")
};
query.AddAttributeValue("address1_city", "Redmond");

EntityCollection accounts = svc.RetrieveMultiple(query);

//Convert the EntityCollection to a EntityReferenceCollection
var accountReferences = new EntityReferenceCollection();

accounts.Entities.ToList().ForEach(x => {
accountReferences.Add(x.ToEntityReference());
});

// The contact to associate to the accounts
var jimGlynn = new EntityReference("contact", 
new Guid("cf76763a-ba1c-e811-a954-000d3af451d6"));

// The relationship to use
var relationship = new Relationship("account_primary_contact");

// Use the Disassociate method
svc.Disassociate(jimGlynn.LogicalName, jimGlynn.Id, relationship, accountReferences);
```
Although there is no particular advantage in doing so, if you wanted to use the <xref:Microsoft.Xrm.Sdk.Messages.DisassociateRequest>, you can replace the last line with this:

```csharp
// Use DisassociateRequest
DisassociateRequest request = new DisassociateRequest()
{
RelatedEntities = accountReferences,
Relationship = relationship,
Target = jimGlynn
};

svc.Execute(request);
```

### See also

[Create table rows using the Organization Service](entity-operations-create.md)<br />
[Retrieve a table row using the Organization Service](entity-operations-retrieve.md)<br />
[Update and delete table rows using the Organization Service](entity-operations-update-delete.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]