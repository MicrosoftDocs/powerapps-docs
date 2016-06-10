<properties
	pageTitle="Overview of the Dynamics CRM Online connection | Microsoft PowerApps"
	description="See the available Dynamics CRM Online functions, responses, and examples"
	services=""
	suite="powerapps"
	documentationCenter="" 	
	authors="AFTOwen"
	manager="erikre"
	editor=""
	tags="" />

<tags
ms.service="powerapps"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="na"
ms.date="04/26/2016"
ms.author="anneta"/>

#  Dynamics CRM Online

![Dynamics CRM Online](./media/connection-dynamics-crmonline/dynamicscrmicon.png)

Dynamics CRM Online provides an API to work with entities on Dynamics CRM Online.

You can display information from items within Dynamics in your app. For example, you can add text boxes to your app, and in these text boxes, display a record from a Dynamics entity. You can also use the gallery control within your app to return a list of all entities in a CRM instances. In another example, you can add a button that control that when selected, it creates a new record or deletes a record for an entity.

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

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



## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
