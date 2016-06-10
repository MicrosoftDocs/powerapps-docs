<properties
	pageTitle="Overview of the SendGrid connection | Microsoft PowerApps"
	description="See the available SendGrid functions, responses, and examples"
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

#  SendGrid

![SendGrid](./media/connection-sendgrid/sendgridicon.png)

SendGrid lets you send email and manage recipient lists.

You can display this information in a text box on your app. For example, you can add input text boxes that asks the user for the To recipient, From, and more within your app. Then, you can take this user input, and send an email from your app.

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

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
|request| |yes|Email message to send. Options include: <ul><li>From (required): Origination address of your email. Must be a valid email address from your domain</li><li>fromname (optional): Origination name of your email</li><li>to (required): Receiving address of your email. Must include one or more valid comma seperated email addresses</li><li>toname (optional): Comma seperated receiving names of your email. Must match the number of \"to\" email addresses if specified</li><li>subject (required): Subject of your email</li><li>body (required): Content of your email. Supported formats include plain text and HTML</li><li>ishtml (optional): Specify whether the content of the email is HTML or plain text</li><li>cc (optional): CC'ed addresses of your email. Must include one or more valid comma seperated email addresses</li><li>ccname (optional): Comma seperated names of the cc'ed recipients</li><li>bcc (optional): Bcc addresses of your email. Must include one or more valid comma seperated email addresses</li><li>bccname (optional): Comma seperated names of the Bcc'ed recipients</li><li>replyto (optional): Reply To address of your email. Must be a valid email address</li><li>date (optional): Specify the date header of your email (Example: “Thu, 21 Dec 2000 16:01:07 +0200”). Must be a valid date</li><li>headers (optional): Custom email headers in json format</li><li>files (optional): Attachment file content</li><li>filenames (optional): Attachment file names</li></ul>|

#### Output properties

| Property Name | Data Type | Required |Description |
|---|---|---|---|
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
