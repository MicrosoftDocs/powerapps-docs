---
title: Manage content security policy
description: Learn how to manage content security policy
author: Nagesh.Bhat

ms.topic: conceptual
ms.custom: 
ms.date: 03/08/2022
ms.subservice: portals
ms.author: Nagesh.Bhat
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - nageshbhat-msft
    - ProfessorKendrick
---

# Manage Content Security Policy (CSP)

Content Security Policy (CSP) is an additional layer of security that helps detect and mitigate some types of web attacks such as data theft, site defacement, or the distribution of malware. CSP provides an extensive set of policy directives that help control the resources that a site page is allowed to load. Each directive defines the restrictions for a specific type of resource.

When CSP is turned on for a portals web site, it helps enhance security by blocking connections, scripts, fonts, and other types of resources that originate from unknown or malicious sources. CSP is turned off by default in portals; however, many websites might require CSP to enhance additional security.

For more information about CSP, see [Content Security Policy Reference](https://content-security-policy.com/).

## Configure CSP

1. Sign in to [Power Apps](https://make.powerapps.com).

2. Ensure that you're in the appropriate environment where your portal exists.

3. On the left pane, select **Apps** and locate the **Portal Management** model-driven app.

    :::image type="content" source="media/manage-content-security-policy/portal-management-app.png" alt-text="The Apps menu option for Power Apps with the the Portals Management App selected":::

4. Select **Portal Management** and then select **Site Settings** on the left pane.

5. Create or update the **HTTP/Content-Security-Policy** site setting and set the required values mentioned in the [CSP reference](https://content-security-policy.com/) separated by semicolons.

    :::image type="content" source="media/manage-content-security-policy/http-content-security-policy.png" alt-text="The Site Settings menu option for Power Apps.":::

## Enable Nonce

Enabling nonce (number used once) will block the execution of all inline scripts except those specified within the inline script. A unique cryptographic nonce is generated and added to each script specified in the CSP header.

To enable Nonce in Portals, add the **script-src 'nonce';** value to the **HTTP/Content-Security-Policy** site settings.
