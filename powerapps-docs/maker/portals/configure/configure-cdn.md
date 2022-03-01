---
title: Configure a site with Content Delivery Network
description: Configure a site with Content Delivery Network
author: nageshbhat-msft

ms.topic: conceptual
ms.custom: 
ms.date: 03/01/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nageshbhat-msft
    - nickdoelman
---

# Content Delivery Network Privacy Notice

## Privacy notice

Enabling the Content Delivery Network (CDN) allows anonymous static files to be cached in the Microsoft global edge network and served from nearest available server.

The static files of an authenticated web page configured using [web page access control rules](webpage-access-control.md) are excluded by the CDN and will be directly served from the application server. 

By default, CDN will cache the files with extension *'css', 'js', 'png', 'svg', 'jpg', 'ico', 'woff2', 'gif', 'ttf', 'woff', 'eot', 'otf', 'tts', 'jpeg', 'coffee', '7z', 'mp3', 'mp4'* in the edge server. This list can be modified any time using the settings.

An administrator can disable the CDN at any given point to stop the service, and all static files will be served directly from the application server. If CDN is disabled for a site, all the files currently cached for that website across the server will be removed.

Power Apps portals CDN is powered by Azure Front Door service to provide fast, reliable, and modern cloud Content Delivery Network.

> [!Note]
> For more information about additional Azure service offerings, see the  [Microsoft Azure Trust Center](https://azure.microsoft.com/support/trust-center/), [Microsoft Azure Front Door](../../../azure/frontdoor/standard-premium/overview)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]