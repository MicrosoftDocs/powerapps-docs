<properties
	pageTitle="Overview of the Office 365 Outlook connection | Microsoft PowerApps"
	description="See how to connect to Office 365 users, step through some examples, and see all the functions"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="RickSaling"
	manager="anneta"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="05/25/2017"
   ms.author="ricksal"/>

#  Office 365 Outlook

![Office 365 Outlook](./media/connection-office365-outlook/office365icon.png)

If you connect to Office 365 Outlook, you can show, send, delete, and reply to email messages, in addition to other tasks.

You can add controls, including buttons and labels, to do these functions in your app. For example, you can add input text boxes on your app that asks for email information, including the recipient, the subject, and the body of the email. Then, add a Send button that sends the email.

This topic shows you how to add Office 365 Outlook as a connection, add Office 365 Outlook as a data source to your app, and use this data in different controls.

**Important**: As of this writing, the calendar operation does not support listing recurring events.

&nbsp;

[AZURE.INCLUDE [connection-requirements](../../includes/connection-requirements.md)]

## Connect to Office 365
1. [Add a data connection](add-data-connection.md) and select **Office 365 Outlook**:  

	![Connect to Office 365](./media/connection-office365-outlook/add-office.png)

1. Select **Connect**, and if prompted to sign in, enter your work account.

The Office 365 Outlook connection has been created, and added to your app. Now, it's ready to be used.


## Use the Office 365 Outlook connection in your app

### Show email

1. On the **Insert** menu, select **Gallery**, and then select a **Text gallery** control.

2. Set its **[Items](../controls/properties-core.md)** property to the following formula:  

	`Office365.GetEmails({fetchOnlyUnread:false})`

	The gallery control is automatically populated with some of your emails.

3. In the gallery, set the **Text** property of the first label to `ThisItem.From`. Set the second label to `ThisItem.Subject`. Set the third label to `ThisItem.Body`. You can also resize the labels.

	The gallery control is automatically populated with the new properties.

4. This function has several optional parameters available. Set the gallery's **Items** property to one of the following formulas:

	`Office365.GetEmails({fetchOnlyUnread:false})`  
	`Office365.GetEmails({fetchOnlyUnread:false, top:2})`  
	`Office365.GetEmails({folderPath:"Sent Items", fetchOnlyUnread:false, top:2})`  
	`Office365.GetEmails({folderPath:"Sent Items", fetchOnlyUnread:false, top:2, searchQuery:"powerapps"})`  
	`Office365.GetEmails({folderPath:"Deleted Items", fetchOnlyUnread:false, top:2, skip:3})`


### Send email

1. On the **Insert** menu, select **Text**, and then select **Text input**. Do this three times to create three different text input controls. Arrange them in a column:  

	![](./media/connection-office365-outlook/threetextinput.png)

2. Rename them to:  

	- **inputTo**
	- **inputSubject**
	- **inputBody**

3. On the **Insert** menu, select **Controls**, and then select **Button**. Set its **[OnSelect](../controls/properties-core.md)** property to the following formula:  

	`Office365.SendEmail(inputTo.Text, inputSubject.Text, inputBody.Text)`

4. Move the button so that it appears under all the other controls, and set its **[Text](../controls/properties-core.md)** property to **"Send email"**.

5. Press F5, or select the Preview button (![](./media/connection-office365-outlook/preview.png)). Type in a valid email address in **inputTo**, and type whatever you want in the other two **Text input** controls.

6. Select **Send email** to send the message. Press Esc to return to the default workspace.

### Send email with attachment(s)

You can create a camera app in which you take pictures and then email the photo images as attachments. For example, a claims adjuster may take photos of an auto accident and send them to the Claims Processing Department. You can also attach many other kinds of files to an email app.

To add attachments to an email, proceed as in the prior step. But in the third step where you call the SendEmail method, you add an additional parameter that specifies the attachment(s).

That parameter looks like this:

			{Attachments: Table({first attachment's properties}, {2nd attachment's properties}, etc.)}

The properties for each attachment are the following:

1. Name: description of this attachment
2. ContentBytes: name of the file to be attached
3. @odata.type: must be defined. You can set it to an empty string.  Note, if you have multiple tables, you only need to set this parameter once.

#### Sample formula

This formula sends email with a single file attached.

			Office365.SendEmail("your.name@contoso.com", "Subject", "Email content", {Attachments:Table({Name:"file1.jpg", ContentBytes:Camera1.Photo, '@odata.type':""})})

And this formula sends email with two attachments.

			Office365.SendEmail("archanan@microsoft.com", "Test", "Blah Blah", {Attachments:Table({Name:"file1.jpg", ContentBytes:Camera1.Photo, '@odata.type':""}, {Name:"AudioFile", ContentBytes:microphone1.audio })})



### Delete email

1. On the **Insert** menu, select **Gallery**, and then select a **Text gallery** control.

2. Set its **[Items](../controls/properties-core.md)** property to the following formula:  

	`Office365.GetEmails({fetchOnlyUnread:false})`

	The gallery control is automatically populated with some of your emails.

3. In the gallery, set the **Text** property of the first label to `ThisItem.Id`. Set the second label to `ThisItem.Subject`. Set the third label to `ThisItem.Body`.
4. Select the first label in the gallery, and rename it to **EmailID**:

	![Close the Options pane](./media/connection-office365-outlook/renameheading.png)

5. Select the third label in the gallery, and add a **Button** (**Insert** menu). Set the button's **OnSelect** property to the following formula:  

	`Office365.DeleteEmail(EmailID.Text)`

5. Press F5, or select the Preview button (![](./media/connection-office365-outlook/preview.png)). Select one of the emails in your gallery, and click the button. <br/><br/> **NOTE** This deletes the selected email from your inbox. So, choose wisely.

6. Press Esc to return to the default workspace.

### Mark email as read

This section uses the same controls as [Delete email](connection-office365-outlook.md#delete-email).

1. Set the button's **OnSelect** property to the following formula:  

	`Office365.MarkAsRead(EmailID.Text)`

2. Press F5, or select the Preview button (![](./media/connection-office365-outlook/preview.png)). Select one of the  unread emails, and click the button.

3. Press Esc to return to the default workspace.


## Helpful links

- For a detailed list of all available functions, including their parameters, see the [Office 365 Outlook reference](https://docs.microsoft.com/en-us/connectors/office365connector/).
- See all the [available connections](../connections-list.md).  
- Learn how to [manage your connections](../add-manage-connections.md).
