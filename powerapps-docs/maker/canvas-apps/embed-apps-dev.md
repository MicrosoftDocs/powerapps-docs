---
title: Integrate canvas apps into websites and other services
description: Learn about how to embed canvas apps in websites and other services.
author: gregli-msft
manager: kvivek
ms.service: powerapps
ms.subservice: canvas-developer
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: 
ms.date: 04/13/2020
ms.author: gregli
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Integrate canvas apps into websites and other services
The apps that you build are often most useful when they're available right where people do their work. By embedding canvas apps in an iframe, you can integrate those apps into websites and other services, such as Power BI or SharePoint.

In this topic, we'll show you how to set parameters for app embedding; then we'll embed our Asset Ordering app in a website.

![Power BI dashboard with embedded app.](./media/embed-apps-dev/embed-dashboard.png)

Keep the following restrictions in mind:

- Only Power Apps users in the same tenant can access the embedded app.
- To access Power Apps using Internet Explorer 11, you must turn off Compatibility View.

You can also integrate canvas apps into SharePoint Online without using an iframe. More information: [Use the Power Apps web part](https://support.office.com/article/use-the-powerapps-web-part-6285f05e-e441-408a-99d7-aa688195cd1c).

## Set URI parameters for your app
If you have an app you want to embed, the first step is to set parameters for the Uniform Resource Identifier (URI), so that the iframe knows where to find the app. The URI is in the following form:

```
https://apps.powerapps.com/play/[AppID]?source=iframe
```
For GCC users

```
https://apps.gov.powerapps.us/play[AppID]?source=iframe
```

> [!IMPORTANT]
> As of August 2019, the URI format has changed from https://web.powerapps.com/webplayer to https://apps.powerapps.com/play. Please update any embedded iframes to use the new URI format. References to the previous format will be redirected to the new URI to ensure compatibility.
>
> Previous format:
> 
> https\://web.powerapps.com/webplayer/iframeapp?source=iframe&appId=/providers/Microsoft.PowerApps/apps/[AppID]

The only thing you have to do is substitute the ID of your app for [AppID] in the URI (including '[' & ']'). We'll show you how to get that value shortly, but first here are all the parameters available in the URI:

* **[appID]** - It provides the ID of the app to run.
* **tenantid** - is an optional parameter to support guest access and determines which tenant to open the app from. 
* **screenColor** - is used to provide a better app loading experience for your users. This parameter is in the format [RGBA (red value, green value, blue value, alpha)](../canvas-apps/functions/function-colors.md) and controls the screen color while the app loads. It is best to set it to the same color as your app's icon.
* **source** - does not affect the app, but we suggest you add a descriptive name to refer to the source of the embedding.
* Lastly, you can add any custom parameters you want using the [Param() function](../canvas-apps/functions/function-param.md), and those values can be consumed by your app. They are added to the end of the URI, such as `[AppID]?source=iframe&param1=value1&param2=value2`. These parameters are read only during launch of the app. If you need to change them, you must relaunch the app. Note that only the first item after [appid] should have a "?"; after that use the "&" as illustrated here. 

### Get the App ID
The app ID is available on powerapps.com. For the app you want to embed:

1. In [powerapps.com](https://powerapps.microsoft.com), on the **Apps** tab, click or tap the ellipsis ( **. . .** ), then **Details**.
   
    ![Go to app details.](./media/embed-apps-dev/details.png)
1. Copy the **App ID**.
   
    ![Copy app ID from details.](./media/embed-apps-dev/app-id.png)
1. Substitute the `[AppID]` value in the URI. For our Asset Ordering app, the URI looks like this:
   
    ```
    https://apps.powerapps.com/play/76897698-91a8-b2de-756e-fe2774f114f2?source=iframe
    ```

You may need to allow pop-ups in browser when you embed an app in your website that uses [Launch()](functions/function-param.md) function to launch a webpage or an app.

## Embed your app in a website
Embedding your app is now as simple as adding the iframe to the HTML code for your site (or any other service that supports iframes, such as Power BI or SharePoint):

```html
<iframe width="[W]" height="[H]" src="https://apps.powerapps.com/play/[AppID]?source=website&screenColor=rgba(165,34,55,1)" allow="geolocation; microphone; camera"/>
```

Specify values for the iframe width and height, and substitute the ID of your app for `[AppID]`.

> [!NOTE]
> Include `allow="geolocation; microphone; camera"` in your iframe HTML code to allow your apps to use these capabilities on Google Chrome.

The following image shows the Asset Ordering app embedded in a Contoso sample website.

![Contoso website with embedded app.](./media/embed-apps-dev/contoso-website.png)

Keep the following points in mind for authenticating users of your app:

- If your website uses Azure Active Directory (AAD) based authentication, no additional sign-in is required.
- If your website uses any other sign-in mechanism or is not authenticated, your users see a sign-in prompt on the iframe. After they sign-in, they will be able to run the app as long as the author of the app has shared it with them.

As you can see, embedding apps is simple and powerful. Embedding enables you to bring apps right to the places you and your customers work – websites, Power BI dashboards, SharePoint pages, and more.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]