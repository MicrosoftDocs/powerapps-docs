<properties
	pageTitle="Register API from Swagger 2.0 API Definition | Microsoft Azure"
	description="Register API from Swagger 2.0 API defition of your existing API"
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
   ms.date="11/11/2015"
   ms.author="guayan"/>

# Register API from Swagger 2.0 API Definition  

There are three ways to register an API so that users can use them from their apps:

1. [From Marketplace](powerapps-register-from-available-apis.md)
2. [From APIs hosted in your App Service Environment](powerapps-register-api-hosted-in-app-service.md)
3. From Swagger 2.0 API definition

This article describes how to register an existing API of yours using Swagger 2.0 API definition.

#### Prerequisites to get started

- Sign up for PowerApps Enterprise
- Create an App Service Environment

## Register an existing API using Swagger 2.0 API definition

It's a common scenario that you've already had some existing APIs in your organization and you want to let users consume them from PowerApps. It's very easy to register such existing APIs. Following are the steps:

1. Prepare the [Swagger 2.0](http://swagger.io) API definition for your existing API. PowerApps leverages Swagger 2.0 as the API definition format to understand the shape of an API. There are tools referenced from the [Swagger 2.0 website](http://swagger.io) which can help you easily author the Swagger 2.0 API definition for your existing API. A few things to notice here:
	a. The ``host`` property should point to the actual endpoint of your existing API without scheme or sub paths, like ``api.contoso.com``.
	b. The ``basePath`` property should be the sub paths if your existing API endpoint if there is any, staring with ``/``, like ``/purchaseorderapi``.
2. Make sure your existing API is accessible by your App Service Environment securely.
	a. If you are comfortable with making your API accessible via internet, you can set up [HTTP basic access authentication](https://tools.ietf.org/html/rfc2617) between your App Service Environment and your existing API. Go [here][14] to see how.
	b. If you want to keep your API within your organization's network, you can set up virtual network on the App Service Environment to access your organization's network securely. Go [here][15] to see how.
3. In the Azure portal, select **PowerApps**. In PowerApps, select **Manage APIs**:  
	![][11]
4. In Registered APIs, select **Add**:
	![][12]
5. In **Add API**, enter the API properties:
	In **Name**, enter a name for your API. Notice that it will be part of the runtime URL of the API, which should be meaningful and unique within your organization.
	In **Source**, select **Import from Swagger 2.0**.
6. In **API definition (Swagger 2.0)**, upload your Swagger 2.0 API definition file.
	![][13]
7. Click **ADD** to complete these steps.

> [AZURE.TIP] When you register an API, you're registering the API to your App Service environment. Once in the app service environment, it can be used by other apps within the same app service environment, especially PowerApps apps.

## Summary and next steps

In this topic, you've seen how to register your own instance of the available APIs PowerApps provides out-of-box. Here are some related topics and resources for learning more about PowerApps.

- [Configure APIs][21]
- [Add a new API, add a connection, and give users access][22]

<!--References-->
[11]: ./media/powerapps-register-existing-api-from-api-definition/registered-apis-part.png
[12]: ./media/powerapps-register-existing-api-from-api-definition/add-api-button.png
[13]: ./media/powerapps-register-existing-api-from-api-definition/add-api-blade.png
[14]: powerapps-configure-apis.md
[15]: https://azure.microsoft.com/documentation/articles/app-service-app-service-environment-intro/
[21]: powerapps-configure-apis.md
[22]: powerapps-create-new-connector.md