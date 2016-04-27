<properties
	pageTitle="Overview of the SMTP connection | Microsoft PowerApps"
	description="See the available SMTP functions, responses, and examples"
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
ms.date="04/26/2016"
ms.author="mandia"/>

#  SMTP

![SMTP](./media/connection-smtp/smtpicon.png)

Connect to SMTP to send email.

You can use an app to send email from SMTP. For example, you can add input text boxes that ask the user for the To and Bcc addresses. Then use this information to send an email using your app.

This topic shows the available functions.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## View the available functions

This connection includes the following functions:

| Function Name |  Description |
| --- | --- |
|[SendEmail](connection-smtp.md#sendemail) | Sends an email to one or more recipients. |



## SendEmail
Send Email: Sends an email to one or more recipients. 

#### Input properties

| Name| Data Type|Required|Description|
| ---|---|---|---|
|emailMessage| |yes|Email message with the following options: <ul><li>To: Email address of recipient(s). Separate multiple email addresses using semicolon (;). <br/>Example: recipient1@domain.com;recipient2@domain.com<br/></li><li>Cc: Email address of recipient(s) for carbon copy. Separate multiple email addresses using semicolon (;). <br/>Example:  recipient1@domain.com;recipient2@domain.com<br/></li><li>Subject: Email subject</li><li>Body: Email body</li><li>From: Email address of sender. Example: sender@domain.com</li><li>IsHtml: When this property is set to true, the content of the body will be sent as HTML content.</li><li>Bcc: Email address of recipient(s) for blind carbon copy. Separate multiple email addresses using semicolon(;). <br/><br/>Example: recipient1@domain.com;recipient2@domain.com<br/></li><li>Importance: Importance of the email: High, Normal, or Low</li><li>Attachments: Attachments to be sent along with the email</li></ul>

#### Output properties
None. 


## Helpful links

See all the [available connections](../connections-list.md).  
Learn how to [add connections](../add-manage-connections.md) to your apps.
