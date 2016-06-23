<properties
	pageTitle="List of connections | Microsoft PowerApps"
	description="Overview of all the available connections you can use to build PowerApps"
	services=""
	suite="powerapps"
	documentationCenter=""
	authors="AFTOwen"
	manager="erikre"
	editor=""
    tags=""/>

<tags
	ms.service="powerapps"
	ms.workload="na"
	ms.tgt_pltfrm="na"
	ms.devlang="na"
	ms.topic="get-started-article"
	ms.date="06/06/2016"
	ms.author="anneta"/>

# Connections list

In PowerApps, connect to data in Office 365, Dropbox, Twitter and other common SaaS and enterprise services. Review these options to identify possibilities, and check back to discover what's been added recently. Each connector has specific functions described in the topic for that connector.

Just getting started with adding connections in PowerApps? Learn how to add [connections](add-manage-connections.md) and [data sources](add-data-connection.md) in your apps.

Ready to take it to the next level? Create [custom APIs](register-custom-api.md) and connect to them within your apps.

## Available connections

|&nbsp;|&nbsp;|&nbsp;|&nbsp;|&nbsp;|
|---|---|---|---|---|
[![API Icon][servicebusicon]][servicebusdoc] | [**Azure Service Bus**][servicebusdoc] <br/> Send messages from Service Bus Queues and Topics and receive messages from Service Bus Queues and Subscriptions || [![API Icon][sqlicon]][sqldoc] | [**Azure SQL database**][sqldoc]  <br/> Create and update data |
| [![API Icon][blobicon]][azureblobdoc] | [**Azure Storage Blob**][azureblobdoc] <br/>Manage files in your blob container || [![API Icon][boxicon]][boxDoc] | [**Box**][boxDoc] <br/>Upload, get, delete, and list files, among other tasks|
| [![API Icon][dropboxicon]][dropboxdoc] | [**Dropbox**][dropboxdoc] <br/> Get, delete, and list files, among other tasks || [![API Icon][crmonlineicon]][crmonlinedoc] | [**Dynamics CRM Online**][crmonlinedoc] <br/>Do more with your data |
| [![API Icon][excelicon]][exceldoc] | [**Excel**][exceldoc] <br/> Display data in a table, update the file, and more || [![API Icon][facebookicon]][facebookdoc] | [**Facebook**][facebookdoc] <br/> Post to a timeline, get a page feed, and more |
| [![API Icon][ftpicon]][ftpdoc] | [**FTP**][ftpdoc] <br/> Upload and get files among other tasks on an FTP/FTPS server || [![API Icon][githubicon]][githubdoc] | [**GitHub**][githubdoc] <br/> Manage your issues |
| [![API Icon][googledriveicon]][googledrivedoc] | [**Google Drive**][googledrivedoc] <br/> Interact with your data || [![API Icon][mailchimpicon]][mailchimpdoc] | [**MailChimp**][mailchimpdoc]  <br/> Create campaigns, manage your lists, and more |
| [![API Icon][microsofttranslatoricon]][microsofttranslatordoc] | [**Microsoft Translator**][microsofttranslatordoc] <br/> Translate text into different languages | | [![API Icon][office365icon]][office365outlookdoc] | [**Office 365 Outlook**][office365outlookdoc] <br/> Send and receive emails, manage your calendar, and manage your contacts |
| [![API Icon][office365icon]][office365usersdoc] | [**Office 365 Users**][office365usersdoc] <br/> View profile information, get direct reports, and more || [![API Icon][office365icon]][office365videodoc] | [**Office 365 Video**][office365videodoc] <br/> Check the status of a video, return channels, and more |
| [![API Icon][onedriveicon]][onedrivedoc] | [**OneDrive**][onedrivedoc] <br/> Upload and manage files || [![API Icon][onedriveforbusinessicon]][onedriveforbusinessdoc] | [**OneDrive for Business**][onedriveforbusinessdoc] <br/> Upload and manage files |
| [![API Icon][salesforceicon]][salesforcedoc] | [**Salesforce**][salesforcedoc] <br/> Manage accounts, leads, opportunities, and more ||  [![API Icon][sendgridicon]][sendgriddoc] | [**SendGrid**][sendgriddoc] <br/> Send email and manage recipient lists |
| [![API Icon][sftpicon]][sftpdoc] | [**SFTP**][sftpdoc]  <br/> Upload, get, and delete files, among other tasks || [![API Icon][sharepointicon]][sharepointdoc] | [**SharePoint Online**][sharepointdoc]  <br/> Manage list items |
| [![API Icon][slackicon]][slackdoc] | [**Slack**][slackdoc]  <br/> Post messages to Slack channels || [![API Icon][smtpicon]][smtpdoc] | [**SMTP**][smtpdoc]  <br/> Send email with attachments|
| [![API Icon][twilioicon]][twiliodoc] | [**Twilio**][twiliodoc]  <br/> Send and get messages, get available numbers, and more || [![API Icon][twittericon]][twitterdoc] | [**Twitter**][twitterdoc]  <br/> Get timelines, post tweets, and more |

<!--API Documentation-->
[azureblobdoc]: ./connections/connection-azure-blob.md "Connect to Azure blob to manage files in your blob container."
[boxDoc]: ./connections/cloud-storage-blob-connections.md "Connects to Box and display data from an Excel table."
[boxDoc_original]: ./connections/connection-box.md "Connects to Box and can upload, get, delete, list, and more file tasks."
[crmonlinedoc]: ./connections/connection-dynamics-crmonline.md "Connect to Dynamics CRM Online and do more with your CRM Online data."
[dropboxdoc]: ./connections/cloud-storage-blob-connections.md "Connect to Dropbox and display data from an Excel table."
[dropboxdoc_original]: ./connections/connection-dropbox.md "Connect to Dropbox and can get, delete, list, and more file tasks."
[exceldoc]: ./connections/connection-excel.md "Connect to Excel."
[facebookdoc]: ./connections/connection-facebook.md "Connect to Facebook to post to a timeline, get a page feed, and more."
[ftpdoc]: ./connections/connection-ftp.md "Connects to an FTP / FTPS server and do different FTP tasks, including uploading, getting, deleting files, and more."
[googledrivedoc]: ./connections/cloud-storage-blob-connections.md "Connect to GoogleDrive and display data from an Excel table."
[googledrivedoc_original]: ./connections/connection-googledrive.md "Connect to GoogleDrive and interact with your data."
[githubdoc]: ./connections/connection-github.md "Connect to GitHub to manage your issues."
[mailchimpdoc]: ./connections/connection-mailchimp.md "Connect to MailChimp to create new campaigns, manage your lists, and more"
[microsofttranslatordoc]: ./connections/connection-microsoft-translator.md "Connect to Microsoft Translator and translate your text to different languages"
[office365outlookdoc]: ./connections/connection-office365-outlook.md "The Office 365 Connector can send and receive emails, manage your calendar, and manage your contacts using your Office 365 account."
[office365usersdoc]: ./connections/connection-office365-users.md "Connect to Office 365 Users to look up manager information, view profiles, and more"
[office365videodoc]: ./connections/connection-office365-video.md "Connect to Office 365 to check the status of a video, return channels, and more"
[onedrivedoc]: ./connections/cloud-storage-blob-connections.md "Connects to your personal Microsoft OneDrive and display data from an Excel table."
[onedrivedoc_original]: ./connections/connection-onedrive.md "Connects to your personal Microsoft OneDrive and upload, list files, and more."
[onedriveforbusinessdoc]: ./connections/cloud-storage-blob-connections.md "Connects to your Microsoft OneDrive for Business account and display data from an Excel table."
[onedriveforbusinessdoc_original]: ./connections/connection-onedrive-for-business.md "Connects to your Microsoft OneDrive for Business account to upload, list files, and more."
[salesforcedoc]: ./connections/connection-salesforce.md "Connect to your Salesforce account and manage  accounts, opportunities, and more."
[servicebusdoc]: ./connections/connection-azure-servicebus.md "Can send messages from Service Bus Queues and Topics and receive messages from Service Bus Queues and Subscriptions."
[sendgriddoc]: ./connections/connection-sendgrid.md "Connect to SendGrid to send email and manage recipient lists"
[sharepointdoc]: ./connections/connection-sharepoint-online.md "Connects to SharePoint Online to manage documents and list items."
[slackdoc]: ./connections/connection-slack.md "Connect to Slack and post messages to Slack channels."
[sftpdoc]: ./connections/connection-sftp.md "Connects to SFTP and can upload, get, delete files, and more."
[smtpdoc]: ./connections/connection-smtp.md "Connects to a SMTP server and can send email with attachments."
[sqldoc]: ./connections/connection-azure-sqldatabase.md "Connects to Azure SQL Database to create, update entries, and more on an Azure SQL database table."
[twiliodoc]: ./connections/connection-twilio.md "Connects to Twilio and can send and get messages, get available numbers, and more."
[twitterdoc]: ./connections/connection-twitter.md "Connects to Twitter and get timelines, post tweets, and more."
[yammerdoc]: ./connectors-create-api-yammer.md "Connects to Yammer to post messages and get new messages."

<!--Icon references-->
[blobicon]: ./media/connections-list/blobicon.png
[bingsearchicon]: ./media/connections-list/bingsearchicon.png
[boxicon]: ./media/connections-list/boxicon.png
[ftpicon]: ./media/connections-list/ftpicon.png
[crmonlineicon]: ./media/connections-list/dynamicscrmicon.png
[dropboxicon]: ./media/connections-list/dropboxicon.png
[excelicon]: ./media/connections-list/excelicon.png
[facebookicon]: ./media/connections-list/facebookicon.png
[googledriveicon]: ./media/connections-list/googledriveicon.png
[githubicon]: ./media/connections-list/githubicon.png
[mailchimpicon]: ./media/connections-list/mailchimpicon.png
[microsofttranslatoricon]: ./media/connections-list/translatoricon.png
[office365icon]: ./media/connections-list/office365icon.png
[onedriveicon]: ./media/connections-list/onedriveicon.png
[onedriveforbusinessicon]: ./media/connections-list/onedriveforbusinessicon.png
[salesforceicon]: ./media/connections-list/salesforceicon.png
[servicebusicon]: ./media/connections-list/servicebusicon.png
[sendgridicon]: ./media/connections-list/sendgridicon.png
[sftpicon]: ./media/connections-list/sftpicon.png
[sharepointicon]: ./media/connections-list/sharepointicon.png
[slackicon]: ./media/connections-list/slackicon.png
[smtpicon]: ./media/connections-list/smtpicon.png
[sqlicon]: ./media/connections-list/sqlicon.png
[twilioicon]: ./media/connections-list/twilioicon.png
[twittericon]: ./media/connections-list/twittericon.png
[yammericon]: ./media/connections-list/yammericon.png
