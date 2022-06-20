---
title: Configure a site with Content Delivery Network (preview)
description: Configure a site with Content Delivery Network
author: nageshbhat-msft

ms.topic: conceptual
ms.custom: 
ms.date: 06/20/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nageshbhat-msft
    - nickdoelman
    - ProfessorKendrick
---

# Content Delivery Network (preview)

[This topic is pre-release documentation and is subject to change.]

A *content delivery network* is a distributed network of servers that can efficiently deliver web content to users. Content delivery networks store cached content on edge servers in point-of-presence (POP) locations that are close to users, to minimize latency.

:::image type="complex" source="media/configure-cdn/cdn-diagram.png" alt-text="Diagram of the world showing Content Delivery Network servers on three different continents. Each server connects to users who are on, or near to, the continent the server is located on. The three Content Delivery Network servers duplicate static content that's stored in a central application server that floats up in the sky.":::

> [!NOTE]
> - This is a preview feature.
> - [!INCLUDE [cc-preview-features-definition](../../../includes/cc-preview-features-definition.md)]

When you enable CDN on your portal, static content like images, scripts, and style sheet files used to design your portal website will be stored and served from the CDN server closest to your location.  

> [!NOTE] 
> You can also configure a site with Content Delivery Network in Power Pages. More information: [What is Power Pages](/power-pages/introduction)

> [!NOTE]
>
> - You need to be a Portal Administrator to enable the CDN. This feature is available for Power Apps portal.  If you're using the Add-on license then you can't enable CDN. Trial portals aren't supported for CDN. You can't enable the CDN for portals configured with custom domain during preview. 
> - Using a [custom domain name](../admin/add-custom-domain.md) on a site is currently not supported to use CDN.

## Enable Content Delivery Network for a production portal 

Content Delivery Network is available for production Power Apps portals. The steps below detail how to enable it.

1. Open the [Power Platform admin center](https://admin.powerplatform.microsoft.com/environments).

1. Go to **Environments**.  

1. Select the environment where the portal was created. 

1. On the **Resources** card, select **Portals**. 

    :::image type="content" source="media/configure-cdn/resources-card-portals.png" alt-text="The Portals option on the Resources card.":::

1. Select the portal from the available list, and then select **Manage**. 

    :::image type="content" source="media/configure-cdn/manage-portal.png" alt-text="Choosing a portal to manage from the available list.":::

1. Select **Manage Content Delivery Network**.

    :::image type="content" source="media/configure-cdn/manage cdn.png" alt-text="Manage Content Delivery Network item.":::

1. Turn on the **Content Delivery Network** toggle switch.

    :::image type="content" source="media/configure-cdn/turn-on-cdn.png" alt-text="Toggle switch with Content Delivery Network feature enabled.":::

It might take a few minutes to provision Content Delivery Network.

## Enable Content Delivery Network while converting trial to production 

1. In the trial portal, open the [Power Apps portals admin center](../admin/admin-overview.md). 

1. Select **Convert**. 

1. Select the **Enable the Content Delivery Network** checkbox. 

1. Select **Confirm**.
    :::image type="content" source="media/configure-cdn/confirm-cdn.png" alt-text="Message confirming you want to enable Content Delivery Network while converting trial to production.":::

## Disable Content Delivery Network 

1. Open the [Power Platform admin center](https://admin.powerplatform.microsoft.com/environments). 

1. Go to **Environments**.  

1. Select the environment where the portal was created. 

1. On the **Resources** card, select **Portals**. 

1. Select the portal from the available list, and then select **Manage** 

1. Select **Manage Content Delivery Network**.

1. Turn off the **Content Delivery Network** toggle switch. 

    :::image type="content" source="media/configure-cdn/disable-cdn.png" alt-text="Disable Content Delivery Network switch.":::

It might take a few minutes for the process to disable Content Delivery Network.

## Clear the Content Delivery Network cache 

Static website contents are stored on Content Delivery Network servers across geographical locations. You can clear the cached content by using the **Purge cache** command. This action clears the cache from the Content Delivery Network server and the portal website. 

1. Open the [Power Platform admin center](https://admin.powerplatform.microsoft.com/environments) 

1. Go to **Environments**.

1. Select the environment where the portal was created.

1. On the **Resources** card, select **Portals**. 

1. Select **Purge Cache**.

    :::image type="content" source="media/configure-cdn/purge-cache.png" alt-text="The Purge Cache button.":::

## Cache configuration 

Static files are cached based on the file name extensions stored in the **Web files** table in the Portal Management app. By default, Content Delivery Network caches files that have the extensions *css, js, png, svg, jpg, ico, woff2, gif, ttf, woff, eot, otf, tts, jpeg, 7z, mp3,* and *mp4* on the edge server. A maker can override the default list by updating the site settings. 

1. Open the [Power Apps](https://make.powerapps.com/) home page. 

1. Select the environment where the portal was created.

1. On the left pane, select **Apps**. 

    :::image type="content" source="media/configure-cdn/apps-section.png" alt-text="The Apps section.":::

1. Select the **Portal Management** app. 

1. Go to **Site Settings**.

1. In the **ContentDeliveryNetwork/FileExtensions** site setting, update or add to the list of file name extensions you want to be cached. 

    :::image type="content" source="media/configure-cdn/cdn-files.png" alt-text="List of files to be cached.":::

## Privacy notice 

Enabling the Content Delivery Network service stores your site files on servers across multiple geographical locations and delivers the files from the server closest to your site visitors. When a user makes a request to the webpage of the site, the nearest Content Delivery Network server in the Microsoft global network receives the request and forwards it to the back-end application server. Static files in the page response are cached on the Content Delivery Network server. Subsequent requests to static files of the webpage are delivered from the cached content on the Content Delivery Network server, and dynamic page content is forwarded and delivered from the application server.

> [!NOTE] 
> Only files that are part of a webpage that can be accessed by anonymous users are stored on Content Delivery Network servers; authenticated files are always delivered from the application server. An administrator can configure the  list of static files to be stored on servers based on their file name extensions.

A portal administrator can disable Content Delivery Network at any given point to stop the service, and all the files cached on the Content Delivery Network servers will be removed.  

Content Delivery Network is powered by [Azure Front Door](/azure/frontdoor/standard-premium/overview) to provide a fast, reliable, and modern cloud content delivery network.

> [!NOTE] 
> For more information about other Azure service offerings, go to the  [Microsoft Azure Trust Center](https://azure.microsoft.com/support/trust-center/).


