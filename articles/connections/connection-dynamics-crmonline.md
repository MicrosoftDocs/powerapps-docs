<properties
	pageTitle="Overview of the Dynamics 365 connection | Microsoft PowerApps"
	description="Create an app for managing data in Dynamics 365"
	services=""
	suite="powerapps"
	documentationCenter="" 	
	authors="AFTOwen"
	manager="anneta"
	editor=""
	tags="" />

<tags
ms.service="powerapps"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="na"
ms.date="10/20/2016"
ms.author="anneta"/>

# Connect from Microsoft PowerApps to Dynamics 365 #

![Dynamics 365](./media/connection-dynamics-crmonline/dynamicscrmicon.png)

Display information from items within Dynamics 365 in your app. For example, you can add text boxes to your app, and in these text boxes, display a record from a Dynamics entity. You can also use a gallery control within your app to return a list of all entities in an instance of Dynamics 365. In another example, you can add a button that, when selected, creates or deletes a record in an entity.

- For information about how to create an app, see [Generate an app automatically](get-started-create-from-data.md) or [Create an app from scratch](get-started-create-from-blank.md). These topics are written for Excel, but the same principles apply to Dynamics.
- For information about how to add data from Dynamics 365 to an existing app, see [Add a data connection](add-data-connection.md).
- See the [list of available connections](../connections-list.md), and learn how to [manage connections](../add-manage-connections.md) in PowerApps.

<!--NotAvailableYet
## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetItems](connection-dynamics-crmonline.md#getitems) | Get records for an entity |
|[PostItem](connection-dynamics-crmonline.md#postitem) | Create a new record of an entity |
|[GetItem](connection-dynamics-crmonline.md#getitem) | Retrieve the specified record for an entity |
|[DeleteItem](connection-dynamics-crmonline.md#deleteitem) | Delete an record from an entity collection |
|[PatchItem](connection-dynamics-crmonline.md#patchitem) | Update an existing record for an entity |
|[GetTables](connection-dynamics-crmonline.md#gettables) | Used for getting the list of entities present in a Crm instance |


## GetItems
Gets records: Get records for an entity

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Name of CRM Organization Eg: Contoso|
|table|string|yes|Name of the entity|
|$skip|integer|no|Number of entries to skip (default = 0)|
|$top|integer|no|Maximum number of entries to retrieve (default = 256)|
|$filter|string|no|An ODATA filter query to restrict the number of entries|
|$orderby|string|no|An ODATA orderBy query for specifying the order of entries|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|value|array|No | |


## PostItem
Create a new record: Create a new record of an entity

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Name of CRM Organization Eg: Contoso|
|table|string|yes|Name of the entity|
|item| |yes|Record to Create|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|ItemInternalId|string|No | |


## GetItem
Gets a record: Retrieve the specified record for an entity

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Name of CRM Organization Eg: Contoso|
|table|string|yes|Name of the entity|
|id|string|yes|Identifier for the record|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|ItemInternalId|string|No | |


## DeleteItem
Delete a record: Delete an record from an entity collection

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Name of CRM Organization Eg: Contoso|
|table|string|yes|Name of the entity|
|id|string|yes|Identifier for the record|

#### Output properties
None.


## PatchItem
Update an item: Update an existing record for an entity

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Name of CRM Organization Eg: Contoso|
|table|string|yes|Name of the entity|
|id|string|yes|Identifier for the record|
|item| |yes|Record to Update|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|ItemInternalId|string|No | |


## GetTables
Gets entities: Used for getting the list of entities present in a Crm instance

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|dataset|string|yes|Name of CRM Organization Eg: Contoso|

#### Output properties

| Property Name | Data Type | Required | Description |
|---|---|---|---|
|value|array|No | Can output the Name and DisplayName properties |
-->
