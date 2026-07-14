---
title: "Associate and disassociate table rows using the SDK for .NET (Microsoft Dataverse) | Microsoft Docs"
description: "Learn how to associate and disassociate table rows using the SDK for .NET" 
ms.date: 12/13/2024
ms.reviewer: "pehecke"
ms.topic: how-to
author: MsSQLGirl
ms.author: jukoesma
search.audienceType: 
  - developer
contributors:
  - PHecke
  - JimDaly
---

# Associate and disassociate table rows using the SDK for .NET

[!INCLUDE[cc-terminology](../includes/cc-terminology.md)]

Table rows are associated to each other using lookup columns on the related table row. The simplest way to associate two rows in a one-to-many relationship is to use an <xref:Microsoft.Xrm.Sdk.EntityReference> to set the value of a lookup column on the related row.

The simplest way to disassociate two rows in a one-to-many relationship is to set the value of the lookup column to `null`.

Relationships using a many-to-many relationship also depend on lookup columns on the *intersect entity* that supports the many-to-many relationship. Relationship are defined by the existence of rows in that intersect entity. While you can interact with the intersect entity directly, it's much easier to use the API to do this task for you.

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

The following example creates a relationship and associates a primary entity with a collection of related entities.

:::code language="csharp" source="~/../PowerApps-Samples/dataverse/orgsvc/CSharp-NETCore/Relationships/AssociateDisassociate/Program.cs" id="AssociateDisassociate":::
Complete code sample: [AssociateDisassociate](https://github.com/microsoft/PowerApps-Samples/blob/master/dataverse/orgsvc/CSharp-NETCore/Relationships/AssociateDisassociate/Program.cs)

If you wanted to use the <xref:Microsoft.Xrm.Sdk.Messages.AssociateRequest>, you would use the following code. A benefit of using the request instead of the service client method is that the request supports the [use of optional parameters](../optional-parameters.md).

```csharp
AssociateRequest request = new AssociateRequest()
{
RelatedEntities = relatedEntities,
Relationship = relation,
Target = primaryEntity
};

service.Execute(request);
```

Let's say we are associating a primary entity (a contact) with three related entities (accounts). This single association operation shown above is the same as three separate update operations where the [Account](../reference/entities/account.md).[PrimaryContactId](../reference/entities/account.md#BKMK_PrimaryContactId) lookup column is set. Instead, the simpler service client method or request call is using the [account_primary_contact](../reference/entities/contact.md#BKMK_account_primary_contact) relationship which establishes a many-to-one entity relationship on each related account and a one-to-many entity relationship on the contact.

If you examine the properties of the relationship columns, you can see that the `ReferencingEntity` value is `account` and the `ReferencingAttribute` value is `primarycontactid`.

## Use the Disassociate method or DisassociateRequest

The <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Disassociate*> method or the <xref:Microsoft.Xrm.Sdk.Messages.DisassociateRequest> with the <xref:Microsoft.Xrm.Sdk.IOrganizationService>.<xref:Microsoft.Xrm.Sdk.IOrganizationService.Execute*> method are just the reverse of the way that you associate table rows.

You can view an example `Disassociate` method call in the previously shown code sample. If you wanted to use the <xref:Microsoft.Xrm.Sdk.Messages.DisassociateRequest>, the code would look like this:

```csharp
DisassociateRequest request = new DisassociateRequest()
{
RelatedEntities = relatedEntities,
Relationship = relation,
Target = primaryEntity
};

service.Execute(request);
```

### See also

[Create table rows using the SDK for .NET](entity-operations-create.md)<br />
[Retrieve a table row using the SDK for .NET](entity-operations-retrieve.md)<br />
[Update and delete table rows using the SDK for .NET](entity-operations-update-delete.md)<br />

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
