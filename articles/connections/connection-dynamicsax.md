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

#  Connect from Microsoft PowerApps to Dynamics AX

![Dynamics AX Online](./media/connection-dynamicsax/dynamicsaxicon-smaller.png)

Dynamics AX provides an API to work with AX entities. Using this connection, you can connect to your Dynamics AX environment. You can easily build power apps that read, updates and deletes data from Dynamics AX.
This connection supports the following AX versions:

•	Dynamics AX Update1 + hotfix (KB article - https://fix.lcs.dynamics.com/Issue/Resolved?kb=3175021&bugId=3762232&qc=75f75fb7cb5de685683dafada9bdc618a7674bc4e299935b567a28ac02489b5c )

•	Dynamics AX Update 2 ++ versions

This topic shows the available functions.


<properties
pageTitle="Microsoft Dynamics AX Connector | Microsoft Azure"
description="Create Logic apps with Azure App service. The Microsoft Dynamics AX Connector provides a connection to AX Data Entities."
services="app-servicelogic"
documentationCenter=".net,nodejs,java" 	
authors="msftman"
manager="erikre"
editor=""
tags="connectors" />

<tags
ms.service="app-service-logic"
ms.devlang="multiple"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="integration"
ms.date="07/15/2016"
ms.author="deonhe"/>

# Get started with the Microsoft Dynamics AX Connector connector

The Microsoft Dynamics AX Connector provides a connection to AX Data Entities.

To use [any connector](connections-list.md), you first need to create a Powerapp. You can get started by [creating a Powerapp app now](getting-started.md).

## Connect to Microsoft Dynamics AX Connector

Before your Powerapp can access any service, you first need to create a *connection* to the service. A connection provides connectivity between a Powerapp and another service. For example, in order to connect to Dropbox, you first need a Dropbox *connection*. To create a connection, you would need to provide the credentials you normally use to access the service you wish to connect to. So, in the Dropbox example, you would need the credentials to your Dropbox account in order to create the connection to Dropbox. [Learn more about connections]()

## Technical Details

Here are the details about the actions and responses that this connection supports:

## Microsoft Dynamics AX Connector functions

Microsoft Dynamics AX Connector has the following functions:


|Action|Description|
|--- | ---|
|[Get rows](connectors-create-api-microsoftdynamicsaxconnector.md#get-rows)|Retrieves a list of objects of a particular entity type|
|[Create row](connectors-create-api-microsoftdynamicsaxconnector.md#create-row)|Create row|
|[Get object](connectors-create-api-microsoftdynamicsaxconnector.md#get-object)|Retrieves a single object|
|[Delete object](connectors-create-api-microsoftdynamicsaxconnector.md#delete-object)|Deletes an object|
|[Update object](connectors-create-api-microsoftdynamicsaxconnector.md#update-object)|Updates an object|
|[Get list of entities](connectors-create-api-microsoftdynamicsaxconnector.md#get-list-of-entities)|Retrieves a list of entities within an AX instance|
### Function details

Here are the details for the actions and triggers for this connector, along with their responses:



### Get rows
Retrieves a list of objects of a particular entity type


|Property Name| Display Name|Description|
| ---|---|---|
|dataset*|Instance|The AX Online instance for the entities|
|table*|Entity name|Entity name|
|$filter|Filter Query|An ODATA filter query to restrict the number of entries|
|$orderby|Order By|An ODATA orderBy query for specifying the order of entries|
|$skip|Skip Count|Number of entries to skip (default = 0)|
|$top|Maximum Get Count|Maximum number of entries to retrieve (default = 256)|

An * indicates that a property is required

#### Output Details

ItemsList: undefined


| Property Name | Data Type | Description |
|---|---|---|
|value|array|undefined|




### Create row
Create row


|Property Name| Display Name|Description|
| ---|---|---|
|dataset*|Instance|The AX Online instance for the entities|
|table*|Entity name|Entity name|
|item*|Object|Object to create|

An * indicates that a property is required

#### Output Details

Item: undefined


| Property Name | Data Type | Description |
|---|---|---|
|ItemInternalId|string|undefined|




### Get object
Retrieves a single object


|Property Name| Display Name|Description|
| ---|---|---|
|dataset*|Instance|The AX Online instance for the entities|
|table*|Entity name|Entity name|
|id*|Object id|Unique identifier of the object to retrieve|

An * indicates that a property is required

#### Output Details

Item: undefined


| Property Name | Data Type | Description |
|---|---|---|
|ItemInternalId|string|undefined|




### Delete object
Deletes an object


|Property Name| Display Name|Description|
| ---|---|---|
|dataset*|Instance|The AX Online instance for the entities|
|table*|Entity name|Entity name|
|id*|Object id|Unique identifier of the object to delete|

An * indicates that a property is required




### Update object
Updates an object


|Property Name| Display Name|Description|
| ---|---|---|
|dataset*|Instance|The AX Online instance for the entities|
|table*|Entity name|Entity name|
|id*|Object id|Unique identifier of the object to update|
|item*|Object|Object with changed properties|

An * indicates that a property is required

#### Output Details

Item: undefined


| Property Name | Data Type | Description |
|---|---|---|
|ItemInternalId|string|undefined|




### Get list of entities
Retrieves a list of entities within an AX instance


|Property Name| Display Name|Description|
| ---|---|---|
|dataset*|Instance|The AX Online instance for the entities|

An * indicates that a property is required

#### Output Details

TablesList: undefined


| Property Name | Data Type | Description |
|---|---|---|
|value|array|undefined|



## HTTP responses

The functions  above can return one or more of the following HTTP status codes:

|Name|Description|
|---|---|
|200|OK|
|202|Accepted|
|400|Bad Request|
|401|Unauthorized|
|403|Forbidden|
|404|Not Found|
|500|Internal Server Error. Unknown error occurred|
|default|Operation Failed.|



## Next steps ##
- Learn how to [show data from a data source](../add-gallery.md).
- Learn how to [view details and create or update records](../add-form.md).
- See other types of [data sources](../connections-list.md) to which you can connect.
