---
title: "Catalog and CatalogAssignment tables (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Learn how to use the Catalog and CatalogAssignment entities to expose events in your solution"
ms.custom: ""
ms.date: 03/31/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" #TODO: NoOwner
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "kvivek" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---

# Catalog and CatalogAssignment tables (Preview)

Use the [Catalog](reference/entities/catalog.md) and [CatalogAssignment](reference/entities/catalogassignment.md) tables to create a structure to expose actions used in your solution as business events. Microsoft Dataverse Business events is a new capability currently being developed. Business events will enable many scenarios to create integrations with many applications through Dataverse. <!-- Link to release plan topic? -->

Your catalog will describe those events that are relevant to your solution so that people can use them. If you do not catalog the events relevant to your solution, they may not be available to people using your solution.

Use the Catalog table to create a two level hierarchy. This will create a **Catalog** and **Category** group where the second level catalog represents the Catagory.

The first level catalog must represent your solution. Use multiple second-level catalogs to group different categories of functionality within your solution.

For each second-level catalog that represents the categories within your solution, you will use the CatalogAssignment table to specify any Tables, Custom API, or Custom Process actions you want to be exposed.

## Example: Contoso Customer Management

Contoso Customer management solution contains many components. The only components of interest here are: 
- Tables
- Custom API
- Custom Process Action

### Tables

Contoso Customer management is a solution which includes the following tables:


|SchemaName |Display Name  |Description  |
|---------|---------|---------|
|Account|Account|A Dataverse system table|
|Contact|Contact|A Dataverse system table|
|contoso_Membership|Membership|A custom table|

### Custom API
They have also created a number of Custom API which are called by their point-of-sale system, their Web site, and ERP systems to notify Dataverse of events that do not originate within Dataverse:

|UniqueName  |DisplayName  |
|---------|---------|
|contoso_CustomerEnteredStore|Entered Store|
|contoso_CustomerVisitWebSite|Visit Web Site|
|contoso_CustomerPurchasedProduct|Purchased Product|
|contoso_CustomerReturnedProduct|Returned Product|

None of these CustomAPI are bound to an entity.

### Catalog structure

The Contoso Customer management solution catalog looks like this:

|Catalog  |Description  |
|---------|---------|
|Contoso Customer Management|Root Catalog|
|&nbsp;&nbsp;&nbsp;&nbsp;Tables|2nd Level Catalog Category|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Account|CatalogAssignment: Entity|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contact|CatalogAssignment: Entity|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Membership|CatalogAssignment: Entity|
|&nbsp;&nbsp;&nbsp;&nbsp;Customer Events|2nd Level Catalog Category|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Entered Store|CatalogAssignment: CustomAPI|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Visit Web Site|CatalogAssignment: CustomAPI|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Purchase Product|CatalogAssignment: CustomAPI|
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return Product|CatalogAssignment: CustomAPI|


### Events available

With this catalog, the following events will be available:

|Table  |Event  |Why available  |
|---------|---------|---------|
|Account|Create<br />Update<br />Delete| Standard Data Operation |
|Account|GrantAccess<br />ModifyAccess<br />RevokeAccess|User owned entity can be shared.|
|Account|Merge|Account table supports merge operations|
|Contact|Create<br />Update<br />Delete| Standard Data Operation |
|Contact|GrantAccess<br />ModifyAccess<br />RevokeAccess|User owned entity can be shared.|
|Contact|Merge|Contact table supports merge operations|
|Membership|Merge|Account table supports merge operations|
|Membership|Create<br />Update<br />Delete| Standard Data Operation |
|Membership|GrantAccess<br />ModifyAccess<br />RevokeAccess|User owned entity can be shared.|
|N/A|contoso_CustomerEnteredStore|Explicit Catalog Assignment|
|N/A|contoso_CustomerVisitWebSite|Explicit Catalog Assignment|
|N/A|contoso_CustomerPurchasedProduct|Explicit Catalog Assignment|
|N/A|contoso_CustomerReturnedProduct|Explicit Catalog Assignment|

When you make a CatalogAssignement to a table, any system bound operations for that table become available as events.

- Most Tables will support Create, Update, and Delete actions. There are some exceptions.
- User-owned Tables can be shared, and sharing can be changed or revoked. The Actions for those operations will be included with the tables.
- Certain system tables support special operations, such as Merge.
- Any custom table will not have any additional events, unless they are user-owned.

Any Custom API or Custom Process Actions, even if they are bound to a table, must be explicitly assigned.

## Catalog Table Columns

All the available columns and relationships are available in [Catalog table/entity reference](reference/entities/catalog.md).

The following table includes selected columns/attributes of a Catalog table/entity that you can set.


|Display Name<br/>SchemaName<br/>LogicalName|Type|Description  |
|---------|---------|---------|
|Catalog<br/>CatalogId<br/>catalogid|Uniqueidentifier|Unique identifier for catalog instances.|
|Description<br/>Description<br/>description|String|Localized description for catalog instances.<br/>**Required**|
|Display Name<br/>DisplayName<br/>displayname|String|Localized display name for catalog instances.<br/>**Required**|
|Is Customizable<br/>IsCustomizable<br/>iscustomizable|ManagedProperty|Controls whether the Catalog can be customized or deleted.<br/>**Required**|
|Name<br/>Name<br/>name|String|The primary name of the catalog.<br/>**Required**|
|Parent Catalog<br/>ParentCatalogId<br/>parentcatalogid|Lookup|Unique identifier for the Parent Catalog.<br />**Cannot be changed after it is saved.**|
|Unique Name<br/>UniqueName<br/>uniquename|String|Unique name for the catalog.<br/>**Required**<br/>Must begin with a customization prefix.|

> [!NOTE]
> Unless you want to allow people installing your managed solution to modify your catalog, you should set the **Is Customizable** managed property to false.
>
> When you associate a Catalog Assignment to a Catalog, you will not be able to delete the catalog until you remove the catalog assignment.


## CatalogAssignment Table Columns

All the available columns and relationships are available in [CatalogAssignment table/entity reference](reference/entities/catalogassignment.md).

The following table includes selected columns/attributes of a CatalogAssignment table/entity that you can set.

|Display Name<br/>SchemaName<br/>LogicalName|Type|Description  |
|---------|---------|---------|
|Catalog Assignment<br/>CatalogAssignmentId<br/>catalogassignmentid|Uniqueidentifier|Description  |
|catalog<br/>CatalogId<br/>catalogid|Lookup|Description  |
|Is Customizable<br/>IsCustomizable<br/>iscustomizable|ManagedProperty|Description  |
|Name<br/>Name<br/>name|String|Description  |
|Catalog Assignment Object<br/>Object<br/>object|Lookup|Description  |