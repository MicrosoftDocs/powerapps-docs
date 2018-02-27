---
title: Connectors overview | Microsoft Docs
description: Overview of all the available connections you can use to build apps
services: ''
suite: powerapps
documentationcenter: ''
author: archnair
manager: anneta
editor: ''
tags: ''

ms.service: powerapps
ms.workload: na
ms.tgt_pltfrm: na
ms.devlang: na
ms.topic: article
ms.date: 08/28/2017
ms.author: archanan

---
# Overview of connectors for PowerApps
Data is at the core of most apps, including those you build in PowerApps. Data is stored in a *data source*, and you bring that data into your app by creating a *connection*. The connection uses a specific *connector* to talk to the data source. PowerApps has connectors for many popular services and on-premises data sources, including SharePoint, SQL Server, Office 365, Salesforce, Twitter, and more. To get started adding data to an app, see [Add a data connection in PowerApps](add-data-connection.md).

The following table has links to more information about our most popular connectors. For a complete list of connectors, see [All connectors](#all-connectors).

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
| --- | --- | --- | --- | --- |
| ![Common Data Service](./media/connections-list/cdm.png) |[**Common Data Service**](data-platform-intro.md) |&nbsp; |![Office 365 Outlook](./media/connections-list/office365.png) |[**Office 365 Outlook**](connections/connection-office365-outlook.md) |
| ![SharePoint](./media/connections-list/sharepoint.png) |[**SharePoint**](connections/connection-sharepoint-online.md) |&nbsp; |![Excel](./media/connections-list/excel.png) |[**Excel**](connections/connection-excel.md) |
| ![SQL Server](./media/connections-list/sql.png) |[**SQL Server**](connections/connection-azure-sqldatabase.md) |&nbsp; |![OneDrive for Business](./media/connections-list/onedrive.png) |[**OneDrive for Business**](connections/cloud-storage-blob-connections.md) |
| ![Dynamics 365](./media/connections-list/dynamics-365.png) |[**Dynamics 365**](connections/connection-dynamics-crmonline.md) |&nbsp; |![OneDrive](./media/connections-list/onedrive.png) |[**OneDrive**](connections/cloud-storage-blob-connections.md) |
| ![Office 365 Users](./media/connections-list/office365.png) |[**Office 365 Users**](connections/connection-office365-users.md) |&nbsp; |![Dropbox](./media/connections-list/dropbox.png) |[**Dropbox**](connections/cloud-storage-blob-connections.md) |

## Types of connectors
PowerApps has two types of connectors: *standard connectors* like the ones listed above, and *custom connectors*. If you're connecting to a data source that PowerApps supports with a standard connector, use that connector. If you need to connect to another source, like a service that you've built, see [Register and use custom connectors](../developer/register-custom-api.md).

Standard connectors behave differently depending on the type of data source they connect to and how data is returned by that data source:

* Some connectors work with tabular data sources, such as SharePoint, SQL Server, and Excel. When working with these data sources, data is returned to PowerApps as a table. PowerApps uses its own functions, such as [Patch()](../functions/function-patch.md), [Collect()](../functions/function-clear-collect-clearcollect.md), [Update()](../functions/function-update-updateif.md), and so on to interact with the data. Tabular data is also easy to use in forms and galleries, where a field in a table is displayed as a field in a gallery or form. For more information, see the following articles:

    [Understand data sources in PowerApps](working-with-data-sources.md)

    [Generate an app from Excel data](get-started-create-from-data.md)

    [Create an app from scratch](get-started-create-from-blank.md)

    > [!NOTE]
> To connect to data in Excel, the workbook must be hosted in a cloud-storage service like OneDrive. For more information, see [Connect to cloud-storage from PowerApps](connections/cloud-storage-blob-connections.md).

* Other connectors work with function-based data sources, such as Twitter, Facebook, and Office 365 Outlook. When working with these data sources, data is returned to PowerApps based on calling specific functions in the underlying service. For example, with the Twitter connector you call `Twitter.MyFollowers()` to return a list of your followers. You can still use this data in a form or gallery, but it requires a little more work than tabular data. For more information, see [Connect to Twitter from PowerApps](connections/connection-twitter.md).

## All connectors
The following table lists all our connectors. For more information about each connector, see the [Microsoft Connector Reference](https://docs.microsoft.com/connectors/). Premium connectors require PowerApps Plan 1 or Plan 2. For more information, see [PowerApps Plans](https://powerapps.microsoft.com/pricing/).

| &nbsp; | &nbsp; |
| --- | --- |
| 10to8 Appointment Scheduling<br>Act!<br>Adobe Creative Cloud ![Premium connector](./media/connections-list/premium.png)<br>Adobe Sign<br>Amazon Redshift ![Premium connector](./media/connections-list/premium.png)<br>Apache Impala ![Premium connector](./media/connections-list/premium.png)<br>AppFigures<br>Approvals<br>Asana<br>AWeber ![Premium connector](./media/connections-list/premium.png)<br>Azure AD<br>Azure Application Insights<br>Azure Automation<br>Azure Blob Storage<br>Azure Cosmos DB<br>Azure Data Lake<br>Azure Event Grid<br>Azure Event Grid Publish<br>Azure File Storage<br>Azure Log Analytics<br>Azure Log Analytics Data Collector<br>Azure Queues<br>Azure Resource Manager<br>Azure Table Storage<br>Basecamp 2<br>Basecamp 3<br>Benchmark Email ![Premium connector](./media/connections-list/premium.png)<br>Bing Maps<br>Bing Search<br>Bitbucket ![Premium connector](./media/connections-list/premium.png)<br>Bitly<br>Bizzy (H3 Solutions, Inc.)<br>Blogger<br>Box<br>bttn<br>Buffer<br>Calendly ![Premium connector](./media/connections-list/premium.png)<br>Campfire<br>Capsule CRM ![Premium connector](./media/connections-list/premium.png)<br>Chatter ![Premium connector](./media/connections-list/premium.png)<br>Cognito Forms<br>Common Data Service ![Premium connector](./media/connections-list/premium.png)<br>Computer Vision API<br>Content Conversion<br>Content Moderator<br>DB2 ![Premium connector](./media/connections-list/premium.png)<br>Disqus<br>DocFusion365 – SP ![Premium connector](./media/connections-list/premium.png)<br>DocuSign ![Premium connector](./media/connections-list/premium.png)<br>Dropbox<br>Dynamics 365<br>Dynamics 365 for Financials<br>Dynamics for Operations<br>Dynamics NAV<br>Easy Redmine ![Premium connector](./media/connections-list/premium.png)<br>Elastic Forms<br>Event Hubs<br>Eventbrite ![Premium connector](./media/connections-list/premium.png)<br>Excel<br>Face API<br>Facebook<br>File System<br>Flic<br>FlowForma ![Premium connector](./media/connections-list/premium.png)<br>FreshBooks ![Premium connector](./media/connections-list/premium.png)<br>Freshdesk<br>Freshservice ![Premium connector](./media/connections-list/premium.png)<br>FTP<br>GitHub<br>Gmail<br>Google Calendar<br>Google Contacts<br>Google Drive<br>Google Sheets<br>Google Tasks<br>GoToMeeting ![Premium connector](./media/connections-list/premium.png)<br>GoToTraining ![Premium connector](./media/connections-list/premium.png)<br>GoToWebinar ![Premium connector](./media/connections-list/premium.png)<br>Harvest ![Premium connector](./media/connections-list/premium.png)<br>HelloSign ![Premium connector](./media/connections-list/premium.png)<br>HipChat<br>HTTP with Azure AD ![Premium connector](./media/connections-list/premium.png)<br>Informix ![Premium connector](./media/connections-list/premium.png)<br>Infusionsoft ![Premium connector](./media/connections-list/premium.png) |Inoreader<br>Insightly<br>Instagram<br>Instapaper<br>Intercom<br>JIRA ![Premium connector](./media/connections-list/premium.png)<br>JotForm ![Premium connector](./media/connections-list/premium.png)<br>LeanKit ![Premium connector](./media/connections-list/premium.png)<br>LinkedIn<br>LiveChat ![Premium connector](./media/connections-list/premium.png)<br>LUIS<br>Mail<br>MailChimp ![Premium connector](./media/connections-list/premium.png)<br>Mandrill ![Premium connector](./media/connections-list/premium.png)<br>Medium<br>Microsoft Forms<br>Microsoft StaffHub<br>Microsoft Teams<br>Microsoft Translator<br>MSN Weather<br>Muhimbi PDF<br>MySQL ![Premium connector](./media/connections-list/premium.png)<br>Nexmo ![Premium connector](./media/connections-list/premium.png)<br>Notifications<br>Office 365 Bookings<br>Office 365 Groups<br>Office 365 Outlook<br>Office 365 Users<br>Office 365 Video<br>OneDrive<br>OneDrive for Business<br>OneNote (Business)<br>Oracle Database ![Premium connector](./media/connections-list/premium.png)<br>Outlook Customer Manager<br>Outlook Tasks<br>Outlook.com<br>PagerDuty<br>Parserr<br>Paylocity ![Premium connector](./media/connections-list/premium.png)<br>Pinterest<br>Pipedrive ![Premium connector](./media/connections-list/premium.png)<br>Pitney Bowes Data Validation ![Premium connector](./media/connections-list/premium.png)<br>Pivotal Tracker<br>Planner<br>Plivo ![Premium connector](./media/connections-list/premium.png)<br>PostgreSQL ![Premium connector](./media/connections-list/premium.png)<br>Power BI<br>PowerApps Notification ![Premium connector](./media/connections-list/premium.png)<br>Project Online<br>Redmine<br>RSS<br>Salesforce ![Premium connector](./media/connections-list/premium.png)<br>SendGrid<br>Service Bus<br>SFTP<br>SharePoint<br>Skype for Business<br>Slack<br>SmartSheet<br>SMTP<br>SparkPost<br>SQL Server<br>Stripe ![Premium connector](./media/connections-list/premium.png)<br>SurveyMonkey ![Premium connector](./media/connections-list/premium.png)<br>Teamwork Projects ![Premium connector](./media/connections-list/premium.png)<br>Teradata ![Premium connector](./media/connections-list/premium.png)<br>Text Analytics<br>Todoist<br>Toodledo<br>Trello<br>Twilio<br>Twitter<br>TypeForm<br>UserVoice ![Premium connector](./media/connections-list/premium.png)<br>Video Indexer<br>Vimeo<br>Visual Studio Team Services<br>WebMerge<br>WordPress<br>Wunderlist<br>Yammer<br>YouTube<br>Zendesk ![Premium connector](./media/connections-list/premium.png) |

If you have questions about a specific connector, please use the [PowerApps Forums](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1). If you have an idea for a new connector or suggestions for improvement, use [PowerApps Ideas](https://powerusers.microsoft.com/t5/PowerApps-Ideas/idb-p/PowerAppsIdeas).
