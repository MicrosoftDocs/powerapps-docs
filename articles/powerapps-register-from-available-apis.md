<properties
	pageTitle="Register from Available APIs | Microsoft Azure"
	description="Register from Available APIs"
	services="powerapps"
	documentationCenter="" 
	authors="MandiOhlinger"
	manager="dwrede"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na" 
   ms.date="11/17/2015"
   ms.author="guayan"/>

# Register an API from available APIs

To use these APIs, you must "register" the APIs in the Azure portal. The following options are available: 

There are three ways to register an API so that users can use them from their apps:

- Register an API available APIs
- Register an API hosted within [your App Service Environment][1]
- Register using a [Swagger 2.0 API definition][2]

This article describes what are the available APIs PowerApps provides out-of-box, why you want to register them for your organization, and how to register an API.

#### Prerequisites to get started

- Sign up for [PowerApps Enterprise]()
- Create an [app service environment]()

## Available APIs

Every Microsoft managed APIs you get out-of-box after you sign up for PowerApps is also available for you to register your own instance. This list includes:

- Dropbox
- DynamicsCRM Online
- Excel
- Google Drive
- Microsoft Translator
- Office365 Outlook
- Office3665 Users
- OneDrive
- Salesforce
- SharePoint Online
- Twitter

There are also additional APIs which are only available for you to register your own instance. This list includes:

- Bing Search
- SQL Server
- SharePoint Server

## Why register your own instances

Using the out-of-box Microsoft managed APIs is convenient. Having said that, registering your own instances as IT managed APIs has many benefits. At a high level, we recommend you to do so when you want to: 

- Have full manageability on the APIs, including user access, security when connecting to other systems, API call limits, monitoring and advanced features like policies, and more.
- Access on-premises data since App Service Environment supports virtual networks.
- Set up the APIs for business users, which they may not be able to use by themselves.

The following is a table comparing the capabilities you get in both cases.

| Capability | Microsoft Managed | IT Managed |
| ---------- | ----------------- | ------------ |
| API call limits | Defined by Microsoft | Defined by yourself (via policies) |
| Bring your own key when connecting to SaaS | Not supported | Supported |
| API user access | Enabled for everyone | Fully manageable at AAD user and group level |
| API Monitoring | Not supported | Supported |
| API Policies | Not supported | Supported |
| Connection user access | View only | Fully manageable at AAD user and group level |
| Connection management | View only | Fully manageable |


## How to register from available APIs

Register from available APIs is very simple. Following are the general steps.

1. In the Azure portal, select **PowerApps**. In PowerApps, select **Manage APIs**:  
![][17]
2. In Manage APIs, select **Add**:  
![][18]  
3. In **Add API**, enter the API properties:  
	- In **Name**, enter a name for your API. Notice that the name you enter is included in the runtime URL of the API. Make the name meaningful and unique within your organization.
	- In **Source**, select **From available APIs**:  
	![][19]
4. Click the **API** chevron and then choose the API you want to register from the **Select from available APIs** blade:  
![][20]
5. Follow the available API specific articles to configure additional settings if there is any.
6. Select **ADD** to complete these steps.

> [AZURE.TIP] When you register an API, you're registering the API to your app  service environment. Once in the app service environment, it can be used by other apps within the same app service environment, especially PowerApps.

For specific settings needed for each API, you can follow the API specific articles referenced below:

- [Bing Search][3]
- [Dropbox](4)
- [DynamicsCRM Online](5)
- [Excel](6)
- [Google Drive](7)
- [Microsoft Translator][8]
- [Office365 Outlook](9)
- [Office3665 Users](10)
- [OneDrive](11)
- [Salesforce](12)
- [SharePoint Online](13)
- [SharePoint Server](14)
- [SQL Server](15)
- [Twitter](16)

## Summary and next steps

In this topic, you've seen how to register your own instance of the available APIs PowerApps provides out-of-box. Here are some related topics and resources for learning more about PowerApps.

- [Configure APIs][21]
- [Add a new API, add a connection, and give users access][22]

<!--References-->
[1]: powerapps-register-api-hosted-in-app-service.md
[2]: powerapps-register-existing-api-from-api-definition.md
[3]: powerapps-create-api-azuremarketplace-bingsearch.md
[4]: powerapps-create-api-azuremarketplace-dropbox.md
[5]: powerapps-create-api-azuremarketplace-crmonline.md
[6]: powerapps-create-api-azuremarketplace-excel.md
[7]: powerapps-create-api-azuremarketplace-googledrive.md
[8]: powerapps-create-api-azuremarketplace-microsofttranslator.md
[9]: powerapps-create-api-azuremarketplace-office365-outlook.md
[10]: powerapps-create-api-azuremarketplace-office365-users.md
[11]: powerapps-create-api-azuremarketplace-onedrive.md
[12]: powerapps-create-api-azuremarketplace-saleforce.md
[13]: powerapps-create-api-azuremarketplace-sharepointonline.md
[14]: powerapps-create-api-azuremarketplace-sharepointserver.md
[15]: powerapps-create-api-azuremarketplace-sql.md
[16]: powerapps-create-api-azuremarketplace-twitter.md
[17]: ./media/powerapps-register-from-available-apis/registered-apis-part.png
[18]: ./media/powerapps-register-from-available-apis/add-api-button.png
[19]: ./media/powerapps-register-from-available-apis/add-api-blade.png
[20]: ./media/powerapps-register-from-available-apis/add-api-select-from-marketplace-blade.png
[21]: powerapps-configure-apis.md
[22]: powerapps-create-new-connector.md
