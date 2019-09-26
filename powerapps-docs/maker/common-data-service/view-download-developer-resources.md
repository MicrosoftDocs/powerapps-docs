---
title: "View or download developer resources for PowerApps and Common Data Service | MicrosoftDocs"
description: "Find developer resources and service endpoint URLs PowerApps and Common Data Service"
keywords: ""
ms.date: 09/25/2019
ms.service: powerapps
ms.custom: 
ms.topic: article
ms.assetid: e200d242-ff3f-48e5-af32-aed050e02441
author: Mattp123
ms.author: matp
manager: kvivek
ms.reviewer: 
ms.suite: 
ms.tgt_pltfrm: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# View or download developer resources

This page provides resources for developers and information about the specific instance you are working on. 

## View the Developer Resources page for your environment

1. From the PowerApps portal select the ![Settings Button](../../administrator/media/settings-button-nav-bar.png) Settings button and choose **Advanced customizations**.

    ![Advanced Customizations](media/advanced-customizations-menu.png)

1. Within the **Advanced customizations** panel, choose the **Developer Resources** link:<br />![Developer Resources Link](media/developer-resources-link.png)

## Getting Started 

This section provides links for developers to find resources. The following resources are available:


|Link |Description|
|---------|---------|
|[Developer Center](https://go.microsoft.com/fwlink/?LinkId=551006).|Start here for developer docs on PowerApps and Common Data Service.|
|[PowerApps Community/Forums](https://powerusers.microsoft.com/t5/PowerApps-Community/ct-p/PowerApps1)|Ask and answer questions in the PowerApps community.|
|[NuGet Packages](https://www.nuget.org/profiles/crmsdk)|Discover NuGet packages to add SDK assemblies to your projects.|
|[Download Tools](/powerapps/developer/common-data-service/download-tools-nuget)|Tools that you will need are available to download from NuGet. Use the PowerShell script on this page to get the latest versions.|
|[Sample Code](https://go.microsoft.com/fwlink/?LinkId=553007)|A GitHub repo for PowerApps samples.|
|[Developer Overview](https://go.microsoft.com/fwlink/?LinkId=550995)|Link to a topic providing an overview for developers.|

## Connect your apps to this instance of Common Data Service

This section provides information you need to connect to your Common Data Service instance.

### Instance Web API

This is the URL for the Web API for your instance. The Web API is an OData v4 RESTful API. You can also download the service document that describes the metadata and operations available in your instance. More information: [Developer Documentation: Use the Common Data Service Web API](/powerapps/developer/common-data-service/webapi/overview)

### Organization Service

This is the URL for the SOAP endpoint for the Organization Service for your instance.
You can download the WSDL for this service here, but usually you will use the CrmSvcUtil.exe code generation tool to build entity classes for .NET projects. More information: 
- [Developer Documentation: Generate early-bound entity classes using the code generation tool (CrmSvcUtil.exe)](/powerapps/developer/common-data-service/org-service/generate-early-bound-classes)
- [Developer Documentation: Use the Organization Service to read and write data or metadata](/powerapps/developer/common-data-service/org-service/overview)

### Instance Reference Information

This information uniquely describes your instance. There is a GUID **ID** and a **Unique Name**.
This information is needed when you use Azure extensions with your instance.
More information: [Developer Documentation: Azure extensions for Dynamics 365](/dynamics365/customer-engagement/developer/azure-extensions)

## Connect your apps to the Common Data Service Discovery Service

Because people may have access to multiple Common Data Service environments, the discovery services allow for retrieving the available environments that a person can access based on their user credentials.

### Discovery Web API

This is the endpoint address for the RESTful OData v4 version of the discovery service to use for your instance. You can also download the service document here.
More information: [Developer Documentation: Discover the URL for your organization using the Web API](/powerapps/developer/common-data-service/webapi/discover-url-organization-web-api)


### Discovery Service

This is the endpoint address for the SOAP version of the discovery service to use for your instance. You can also download the service document here.
More information: [Developer Documentation: Discover the URL for your organization using the Discovery Service](/dynamics365/customer-engagement/developer/org-service/discover-url-organization-organization-service)
  
