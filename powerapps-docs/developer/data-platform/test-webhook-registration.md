---
title: "Test WebHook registration with request logging site (Microsoft Dataverse) | Microsoft Docs" # Intent and product brand in a unique string of 43-59 chars including spaces
description: "Use a request logging site to examine the contextual data passed with a WebHook." # 115-145 characters including spaces. This abstract displays in the search result.
ms.custom: ""
ms.date: 03/18/2021
ms.reviewer: "pehecke"
ms.service: powerapps
ms.topic: "article"
author: "JimDaly" # GitHub ID
ms.subservice: dataverse-developer
ms.author: "jdaly" # MSFT alias of Microsoft employees only
manager: "ryjones" # MSFT alias of manager or PM counterpart
search.audienceType: 
  - developer
search.app: 
  - PowerApps
  - D365CE
---
# Test WebHook registration with request logging site

[!INCLUDE[cc-terminology](includes/cc-terminology.md)]

Before you create or configure a service to consume WebHooks, you should test what kind of data the service will receive so that you can know what kind of data you will need to process. For this purpose, you can use one of several request logging sites. For the purpose of this example, we will use [WebHook Tester](https://WebHook.site) to configure a target for the WebHook requests.

Use the following steps:

1. Go to [https://WebHook.site](https://WebHook.site). In the top right-hand corner you will see a green **Copy** button.
    ![WebHook Tester copy button.](media/WebHook-tester-copy-button.png)
1. Use the **Copy** button to copy the URL. Keep this page open.
1. Use the Plug-in Registration tool to register a new WebHook as described in [Register a WebHook](register-web-hook.md). 
    1. Use the URL you copied in step 2 as the **Endpoint URL**. 
    1. Set a name and any authentication properties you want. WebHook Tester will not evaluate these values in the way that an actual site that will process the data should, but you can see how they will be passed through.
1. Use the Plug-in Registration tool to register a step using the WebHook you created in step 4 as described in [Register a step for a WebHook](register-web-hook.md#register-a-step-for-a-webhook). 
    1. Make sure to use an event that you can easily perform by editing data in the Microsoft Dataverse application, such as updating a contact table.
1. Use the Dataverse app to perform the operation to trigger the event.
1. After you trigger the event, return to the WebHook Tester page from step 2. You should see that the page has been updated to show the data passed in the request:

    ![An example of the request logged on the WebHook Tester web site.](media/WebHook-tester-example.png)

    > [!TIP]
    > Use the **Format JSON** option to make the JSON returned in the body of the request easier to read.

## Next steps

[Use WebHooks to create external handlers for server events](use-WebHooks.md)

### See also
[Register a WebHook](register-web-hook.md)

[!INCLUDE[footer-include](../../includes/footer-banner.md)]