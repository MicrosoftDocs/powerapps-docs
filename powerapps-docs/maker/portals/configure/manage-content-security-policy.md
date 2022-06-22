﻿---
title: Manage content security policy
description: Learn how to manage content security policy
author: nabha

ms.topic: conceptual
ms.custom: 
ms.date: 06/15/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - nageshbhat-msft
    - ProfessorKendrick
---

# Manage content security policy (CSP)

Content security policy (CSP) is an extra layer of security that helps detect and mitigate some types of web attacks such as data theft, site defacement, or the distribution of malware. CSP provides an extensive set of policy directives that help control the resources that a site page is allowed to load. Each directive defines the restrictions for a specific type of resource.

When CSP is turned on for a portals web site, it helps enhance security by blocking connections, scripts, fonts, and other types of resources that originate from unknown or malicious sources. CSP is turned off by default in portals; however, many websites might require CSP to enhance other security.

For more information about CSP, see [Content Security Policy Reference](https://content-security-policy.com/).

## Configure CSP

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Ensure that you're in the appropriate environment where your portal exists.

1. On the left pane, select **Apps** and locate the [**Portal Management** app](configure-portal.md).

    :::image type="content" source="media/manage-content-security-policy/portal-management-app.png" alt-text="The Apps menu option for Power Apps with the the Portals Management App selected":::

1. Select **Portal Management** and then select **Site Settings** on the left pane.

1. Create or update the **HTTP/Content-Security-Policy** site setting and set the required values mentioned in the [CSP reference](https://content-security-policy.com/) separated by semicolons.

    **Example**

    `script-src 'self' https://js.example.com;style-src 'self' https://css.example.com`

    :::image type="content" source="media/manage-content-security-policy/http-content-security-policy.png" alt-text="The Site Settings menu option for Power Apps.":::

## Enable Nonce

Enabling nonce (number used once) will block the execution of all inline scripts except those specified within the inline script. A unique cryptographic nonce is generated and added to each script specified in the CSP header. The Nonce in portals supports inline scripts and inline event handlers only.

For more information about nonce, see [Using a nonce with CSP](https://content-security-policy.com/nonce/).

To enable Nonce in Portals, add the **script-src 'nonce';** value to the **HTTP/Content-Security-Policy** site settings.

**Examples**

If you want a strict policy and don't want to allow script loading from sources outside of portals:

`script-src 'self' content.powerapps.com 'nonce'`

If you want to load scripts from any secure source:

`script-src https: 'nonce'`

> [!NOTE]
> - unsafe-eval will be auto injected to support auto generated eval validation when **nonce** is enabled. To disable unsafe-eval auto injection, add/update site setting **HTTP/Content-Security-Policy/Inject-unsafe-eval** to **false**.
> - If unsafe-eval injection is disabled, auto-generated field validation on [basic](../configure/entity-forms.md) and [advanced](../configure/web-form-properties.md) forms may no longer function correctly.




