<properties
	pageTitle="Register API hosted in App Service Environment | Microsoft Azure"
	description="Register API hosted in App Service Environment"
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

# Register API Hosted in App Service Environment

There are three ways to register an API so that users can use them from their apps:

1. [From Marketplace](powerapps-register-from-available-apis.md)
2. From APIs hosted in your App Service Environment
3. [From Swagger 2.0 API definition](powerapps-register-existing-api-from-api-definition.md)

This article describes how to register an API hosted in your App Service Environment.

#### Prerequisites to get started

- Sign up for PowerApps Enterprise
- Create an App Service Environment

## Overview

We support registering existing APIs hosted anywhere, in the cloud or on-premises, which is really powerful. Having said that, in some scenarios, you may want to develop some new APIs. For example:

- You want to implement some new functionalities for your organization to use.
- You want to build on top of some existing functionalities or data to provide a better experience for users when using it building their apps.

In this case, hosting the API in your App Service Environment lets you leverage all the existing capabilities of [App Service]() and also provides you the best integration experience.

## Develop and deploy an API in App Service Environment

Developing an API in App Service Environment is simple. You choose your favorite programming language to build a web API and use [Swagger 2.0](http://swagger.io) to describe the API definition. For some concrete examples, see:  

- [Create an ASP.NET API app in Azure App Service](https://azure.microsoft.com/documentation/articles/app-service-dotnet-create-api-app/)
- [Build and deploy a Java API app in Azure App Service](https://azure.microsoft.com/documentation/articles/app-service-api-java-api-app/)
- [Build and deploy a Node.js API app in Azure App Service](https://azure.microsoft.com/documentation/articles/app-service-api-nodejs-api-app/)

You also have a lot of options to deploy your web API into App Service Environment, from Visual Studio to continuous deployment via source control system. For more information, see [Deploy a web app in Azure App Service](https://azure.microsoft.com/documentation/articles/web-sites-deploy/).

## Register your API

After the API is deployed to your App Service Environment, registering it is simple. Following are the steps:

1. In the Azure portal, select **PowerApps**. In PowerApps, select **Manage APIs**:  
	![][11]
2. In Manage APIs, select **Add**:  
	![][12]  
3. In **Add API**, enter the API properties:
	In **Name**, enter a name for your API. Notice that it is added to the runtime URL of the API, which should be meaningful and unique within your organization.
	In **Source**, select **Import from API app**.  
	![][13]
4. In **API**, select the API app you want to import from.  
	![][14]
5. Select **ADD** to complete these steps.

> [AZURE.TIP] When you register an API, you're registering the API to your App Service environment. Once in the app service environment, it can be used by other apps within the same app service environment, especially PowerApps.

## Summary and next steps

In this topic, you've seen how to register APIs hosted in the App Service environment. Here are some related topics and resources for learning more about PowerApps:  

- [Configure APIs][21]
- [Add a new API, add a connection, and give users access][22]

<!--Reference-->
[11]: ./media/powerapps-register-api-hosted-in-app-service/registered-apis-part.png
[12]: ./media/powerapps-register-api-hosted-in-app-service/add-api-button.png
[13]: ./media/powerapps-register-api-hosted-in-app-service/add-api-blade.png
[14]: ./media/powerapps-register-api-hosted-in-app-service/add-api-select-from-ase.png
[21]: powerapps-configure-apis.md
[22]: powerapps-create-new-connector.md
