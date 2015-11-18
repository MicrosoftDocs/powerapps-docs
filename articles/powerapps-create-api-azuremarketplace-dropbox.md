<properties
	pageTitle="Add Dropbox API in your App Service Environment| Azure"
	description="Create a new Dropbox API in your organization's App Service Environment"
	services="powerapps"
	documentationCenter="" 
	authors="LinhTran"
	manager="gautamt"
	editor=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na" 
   ms.date="11/05/2015"
   ms.author="litran"/>

#Create a new Dropbox API in your organization's App Service Environment

1. In the Azure portal, click on _Browse_ and select _PowerApps Services_. 
2. In **PowerApps Services**, select **Registered APIs** tile or select it from *Settings*:  
![Browse to registered apis][4]

3. In the **Registered APIs** blade, select **Add** to add a new API
![Add API][5]

4. Enter a descriptive **name** for your API.  
	
5. In **Source**, select **Marketplace** to select a pre-built API. 
	
6. Select **Dropbox** from the marketplace
![select dropbox api][6]

7. Select *Settings - Configure required settings*
![configure dropbox API settings][7]

8. Enter *App Key* and *App Secret* for Dropbox. If you dont already have one, see the section below titled "Register a Dropbox app for use with PowerApps". 
> Note the _redirect URL_ here before starting to register the Dropbox app

9. Click **OK** to close the configure API blade.

10. Click **OK** to create a new Dropbox in your ASE.

On successful completion, a new API is added to your ASE.

<!--References-->
[1]: https://www.dropbox.com/login
[2]: https://www.dropbox.com/developers/apps/create
[3]: https://www.dropbox.com/developers/apps
[4]: ./media/powerapps-create-api-from-marketplace-dropbox/browse-to-registered-apis.PNG
[5]: ./media/powerapps-create-api-from-marketplace-dropbox/add-api.PNG
[6]: ./media/powerapps-create-api-from-marketplace-dropbox/select-dropbox-api.PNG
[7]: ./media/powerapps-create-api-from-marketplace-dropbox/configure-dropbox-api.PNG