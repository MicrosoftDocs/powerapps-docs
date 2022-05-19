---
title: Configure a site with Content Delivery Network
description: Configure a site with Content Delivery Network
author: nageshbhat-msft

ms.topic: conceptual
ms.custom: 
ms.date: 5/11/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nageshbhat-msft
    - nickdoelman
    - ProfessorKendrick
---

# Content Delivery Network 

## Set up content delivery network in portal

A content delivery network (CDN) is a distributed network of servers that can efficiently deliver web content to users. CDNs' store cached content on edge servers in point-of-presence (POP) locations that are close to end users, to minimize latency. 

:::image type="content" source="media/configure-cdn/cdn-diagram.png" alt-text="A diagram of a content delivery network.":::

When you enable CDN on your portal, static content like images, scripts, and style sheet files used to design your portal website will be stored and served from the CDN server closest to your location.  
> [!NOTE]
>  You need to be a Portal Administrator to enable the CDN. This feature is available for Power Apps portal.  If you're using the Add-on license then you can't enable CDN. Trial portals aren't supported for CDN. You can't enable the CDN for portals configured with custom domain during preview. 

## Enable Content Delivery Network for Production portal 

CDN is available for production Power Apps portals. The steps below detail how to enable CDN.

1. Open the [<u>Power Platform Admin Center</u>](https://admin.powerplatform.microsoft.com/environments).

1. Navigate to **Environments**.  

1. Select the Environment where the portal is created. 

1. Select **Portals** on the **Resources** card. 

:::image type="content" source="media/configure-cdn/resources-card-portals.png" alt-text="The portals option on the resources card.":::

1. Select the portal from the available list and select **Manage**. 

:::image type="content" source="media/configure-cdn/manage-portal.png" alt-text="Choosing a portal to manage from the available list.":::

1. Select the **Manage Content Delivery Network** item.

:::image type="content" source="media/configure-cdn/manage cdn.png" alt-text="Manage Content Delivery Network item.":::

1. Turn on the **Content Delivery Network** switch to enable the feature. 

:::image type="content" source="media/configure-cdn/turn-on-cdn.png" alt-text="Toggle switch with Content Delivery Network feature enabled.":::

It may take a few minutes to provision the Content Delivery Network.

## Enable Content Delivery Network while converting trial to production 

1. Open [Power Apps portals admin center](../admin/admin-overview.md) of trial portal. 

1. Select the **Convert** button to initiate trial to prod conversion. 

1. Select **Enable the Content Delivery Network** check box. 

1. Select **Confirm** button.
    :::image type="content" source="media/configure-cdn/confirm-cdn.png" alt-text="Enable CDN converting trial to production.":::

## Disable Content Delivery Network 

1. Open the [<u>Power Platform Admin Center</u>](https://admin.powerplatform.microsoft.com/environments). 

1. Navigate to **Environments**.  

1. Select Environment where Portal is created. 

1. Select on **Portals** inside **Resources** card 

:::image type="content" source="media/configure-cdn/resources-card-portals.png" alt-text="The portals option on the resources card.":::

1. Select the Portal from the available list and select **Manage** 

:::image type="content" source="media/configure-cdn/manage-portal.png" alt-text="Choosing a portal to manage from the available list.":::

1. Select the **Manage Content Delivery Network** item 

:::image type="content" source="media/configure-cdn/manage cdn.png" alt-text="Manage Content Delivery Network item.":::

1. Turn off the **Content Delivery Network** switch to disable the feature 

:::image type="content" source="media/configure-cdn/disable-cdn.png" alt-text="Disable Content Delivery Network switch.":::

It may take a few minutes for the process to disable the Content Delivery Network

## Clear CDN cache 

Static website contents are in CDN servers across the geographical locations. You can clear the cached content using Purge cache button. This action will clear cache from CDN server and portal website. 

1. Open the [<u>Power Platform Admin Center</u>](https://admin.powerplatform.microsoft.com/environments) 

1. Navigate to **Environments**  

1. Select Environment where Portal is created 

1. Select **Portals** inside **Resources** card 

:::image type="content" source="media/configure-cdn/resources-card-portals.png" alt-text="The portals option on the resources card.":::

1. Select the **Purge Cache** button 

:::image type="content" source="media/configure-cdn/purge-cache.png" alt-text="The purge cache button.":::

## Cache Configuration 

Static files are cached based on the file extensions stored in Web files table of Portal Management app. By default, CDN will cache the file with extensions *'css', 'js', 'png', 'svg', 'jpg', 'ico', 'woff2', 'gif', 'ttf', 'woff', 'eot', 'otf', 'tts', 'jpeg', '7z', 'mp3', 'mp4'* in the edge server. A maker can override the default list by updating the site settings. 

1. Open [<u>Power Apps</u>](https://make.powerapps.com/) home page. 

1. Select the appropriate Environment where Portals website is provisioned. 

1. Navigate to the Apps section. 

    :::image type="content" source="media/configure-cdn/apps-section.png" alt-text="The apps section.":::

1. Select the **Portal Management** App. 

1. Navigate to Site Settings  

1. Update/Add **ContentDeliveryNetwork/FileExtensions** with list of file extensions to be cached. 

    :::image type="content" source="media/configure-cdn/cdn-files.png" alt-text="":::



## Privacy notice 

Enabling the Content Delivery Network (CDN) stores your site files in servers across multiple geographical locations and delivers the files from the server closest to your site visitors. When user makes a request to the web page of the site, the nearest CDN server in the Microsoft global network will receive the request and forward it to the backend application server. Static files in the page response will be cached in the CDN server. Subsequent requests to static files of the web page will be delivered from the cached content in the CDN server and dynamic page content will be forwarded and delivered from the application server  

> [!NOTE] 
> Only files part of web page accessible by anonymous user will be stored in the CDN servers, authenticated files will always be delivered from the application server. Administrator can configure list of static files to be stored in servers based on their file extensions  

A portal administrator can disable the CDN at any given point to stop the service, and all the files cached in the CDN servers will be removed.  

CDN is powered by [<u>Azure Front Door</u>](https://docs.microsoft.com/en-us/azure/frontdoor/standard-premium/overview) service to provide fast, reliable, and modern cloud Content Delivery Network.   

> [!NOTE] 
> For more information about other Azure service offerings, see the  [<u>Microsoft Azure Trust Center</u>](https://azure.microsoft.com/support/trust-center/),  [<u>Microsoft Azure Front Door</u>](https://docs.microsoft.com/en-us/azure/frontdoor/standard-premium/overview) 

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]
