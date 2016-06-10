<properties
	pageTitle="Overview of the Azure Service Bus connection | Microsoft PowerApps"
	description="See the available Azure Service Bus functions, responses, and examples"
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

#  Azure Service Bus

![Azure Service Bus](./media/connection-azure-servicebus/servicebusicon.png)

Connect to Azure Service Bus to send and receive messages. You can perform actions such as send to queue, send to topic, receive from queue, receive from subscription, etc.

You can display this information in a text box on your app. For example, you can get a message from a queue or topic, add a text box, and then display this message in your app in the text box.

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[SendMessage](connection-azure-servicebus.md#sendmessage) | Sends message to Azure Service Bus queue or topic |
|[GetMessageFromQueue](connection-azure-servicebus.md#getmessagefromqueue) | Gets a new message from Azure Service Bus queue |
|[GetMessageFromTopic](connection-azure-servicebus.md#getmessagefromtopic) | Gets a new message from Azure Service Bus topic subscription |



## SendMessage
Send message.: Sends message to Azure Service Bus queue or topic.

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|message| |yes|Service Bus message, including the following properties: <ul><li>ContentData (required): Content of the message</li><li>ContentType (optional): Content type of the message content</li><li>ContentTransferEncoding (optional): Content Transfer Encoding of the Message. Options include: <ul><li>\"none\"</li><li>\"base64\"</li></ul></li><li>Properties (optional): Key-value pair of all brokered message properties and user properties</li></ul>|
|entityName|string|yes|Name of the queue or topic|

#### Output properties
None.


## GetMessageFromQueue
When a message is received in queue: Gets a new message from Azure Service Bus queue.

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|queueName|string|yes|Name of the queue.|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|ContentData|string|Yes |Content of the message |
|ContentType|string|No |Content type of the message content |
|ContentTransferEncoding|string|No |Content Transfer Encoding of the Message. Options include: <ul><li>\"none\"</li><li>\"base64\"</li></ul> |
|Properties|object|No |Key-value pair of all brokered message properties and user properties |


## GetMessageFromTopic
When a message is received in topic subscription: Gets a new message from Azure Service Bus topic subscription.

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|topicName|string|yes|Name of the topic.|
|subscriptionName|string|yes|Name of the topic subscription.|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
|ContentData|string|Yes |Content of the message |
|ContentType|string|No |Content type of the message content |
|ContentTransferEncoding|string|No |Content Transfer Encoding of the Message. Options include: <ul><li>\"none\"</li><li>\"base64\"</li></ul> |
|Properties|object|No |Key-value pair of all brokered message properties and user properties |


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
