<properties
	pageTitle="Overview of the Salesforce  connection | Microsoft PowerApps"
	description="See the available Salesforce functions, responses, and examples"
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
ms.date="08/13/2016"
ms.author="anneta"/>

# Connect from Microsoft PowerApps to Salesforce#

![Salesforce](./media/connection-salesforce/salesforceicon.png)

Manage data from Salesforce by using controls in an app. For example,  display the name and the contact information of a lead in text boxes, and add other controls to create, update, and delete items in your accounts, campaigns, and more.

- For information about how to create an app, see [Generate an app automatically](get-started-create-from-data.md) or [Create an app from scratch](get-started-create-from-blank.md).	These topics are written for Excel, but the same principles apply to Salesforce.
- For information about how to add data from Salesforce to an existing app, see [Add a data connection](add-data-connection.md).
- See the [list of available connections](../connections-list.md), and learn how to [manage connections](../add-manage-connections.md) in PowerApps.

<!--NotAvailableYet
## View the available functions ##
This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[GetItems](connection-salesforce.md#getitems) | Retrieves Salesforce objects of a certain SObject type (example: 'Lead') |
|[PostItem](connection-salesforce.md#postitem) | Creates a Salesforce object  |
|[GetItem](connection-salesforce.md#getitem) | Retrieves a Salesforce object  |
|[DeleteItem](connection-salesforce.md#deleteitem) | Deletes a Salesforce object  |
|[PatchItem](connection-salesforce.md#patchitem) | Updates a Salesforce object |
|[GetOnNewItems](connection-salesforce.md#getonnewitems) | Triggers a flow when an object is created in Salesforce |
|[GetOnUpdatedItems](connection-salesforce.md#getonupdateditems) | Triggers a flow when an object is modified in Salesforce |
|[GetTables](connection-salesforce.md#gettables) | Retrieves Salesforce object types (SObjects) |


## GetItems
Get objects: Retrieves Salesforce objects of a certain SObject type (example: 'Lead')

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Salesforce SObject type (example: 'Lead')|
|$skip|integer|no|Number of entries to skip (default = 0)|
|$top|integer|no|Maximum number of entries to retrieve (default = 256)|
|$filter|string|no|An ODATA filter query to restrict the number of entries|
|$orderby|string|no|An ODATA orderBy query for specifying the order of entries|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|value|array|No | |


## PostItem
Create object: Creates a Salesforce object

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Salesforce SObject type (example: 'Lead')|
|item| |yes|Salesforce object to create|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|ItemInternalId|string|No | |


## GetItem
Get object: Retrieves a Salesforce object

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Salesforce SObject type (example: 'Lead')|
|id|string|yes|Unique identifier of Salesforce object to retrieve|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|ItemInternalId|string|No | |


## DeleteItem
Delete object: Deletes a Salesforce object

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Salesforce SObject type (example: 'Lead')|
|id|string|yes|Unique identifier of Salesforce object to delete|

#### Output properties
None.


## PatchItem
Update object: Updates a Salesforce object

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Salesforce SObject type (example: 'Lead')|
|id|string|yes|Unique identifier of the Salesforce object to update|
|item| |yes|Salesforce object with changed properties|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|ItemInternalId|string|No | |


## GetOnNewItems
When an object is created: Triggers a flow when an object is created in Salesforce

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Salesforce SObject type (example: 'Lead')|
|$skip|integer|no|Number of entries to skip (default = 0)|
|$top|integer|no|Maximum number of entries to retrieve (default = 256)|
|$filter|string|no|An ODATA filter query to restrict the number of entries|
|$orderby|string|no|An ODATA orderBy query for specifying the order of entries|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|value|array|No | |


## GetOnUpdatedItems
When an object is modified: Triggers a flow when an object is modified in Salesforce

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|table|string|yes|Salesforce SObject type (example: 'Lead')|
|$skip|integer|no|Number of entries to skip (default = 0)|
|$top|integer|no|Maximum number of entries to retrieve (default = 256)|
|$filter|string|no|An ODATA filter query to restrict the number of entries|
|$orderby|string|no|An ODATA orderBy query for specifying the order of entries|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|value|array|No | |


## GetTables
Get object types (SObjects): Retrieves Salesforce object types (SObjects)

#### Input properties
None.

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|value|array|No | |

-->
