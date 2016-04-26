<properties
	pageTitle="Overview of the SendGrid connection | Microsoft PowerApps"
	description="See the available SendGrid functions, responses, and examples"
	services=""	
	suite="powerapps"
	documentationCenter="" 	
	authors="MandiOhlinger"	
	manager="erikre"	
	editor="" 
	tags="" />

<tags
ms.service="powerapps"
ms.devlang="na"
ms.topic="article"
ms.tgt_pltfrm="na"
ms.workload="na"
ms.date="04/25/2016"
ms.author="mandia"/>

#  SendGrid

![SendGrid](./media/connection-sendgrid/sendgridicon.png)

SendGrid Connection Provider lets you send email and manage recipient lists.

You can display this information in a text box on your app. You can display one function, multiple functions, or even combine different functions. For example, you can create an expression that combines the User Name and Phone Number, and then display this information in your app.

This topic shows the available functions.

##  What you need to get started

- Access to the [PowerApps portal][1] or install [PowerApps][2]
- Add the [connection](../add-manage-connections.md)
- Create an app from a [template](../get-started-test-drive.md), from [data](../get-started-create-from-data.md), or from [scratch](../get-started-create-from-blank.md)

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[SendEmail](connection-sendgrid.md#sendemail) | Sends an email using SendGrid API (Limited to 10,000 recipients) |
|[AddRecipientToList](connection-sendgrid.md#addrecipienttolist) | Add an individual recipient to a recipient list |


## SendEmail
Send email: Sends an email using SendGrid API (Limited to 10,000 recipients) 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|request| |yes|Email message to send|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
| Property Name | Data Type | Required |
|---|---|---|
|message|string|No |Status message from send email response |


## AddRecipientToList
Add recipient to list: Add an individual recipient to a recipient list 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|listId|string|yes|Unique id of the recipient list|
|recipientId|string|yes|Unique id of the recipient|

#### Output properties
None. 


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.

[1]: https://web.powerapps.com
[2]: http://aka.ms/powerappsinstall