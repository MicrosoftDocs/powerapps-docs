---
title: Manage Content Security Policy
description: Learn how to manage Content Security Policy (CSP)
author: nabha

ms.topic: conceptual
ms.custom: 
ms.date: 07/04/2022
ms.subservice: portals
ms.author: nabha
ms.reviewer: ndoelman
contributors:
    - nickdoelman
    - nageshbhat-msft
    - ProfessorKendrick
---

# Manage Content Security Policy

Content Security Policy (CSP) is an extra layer of security that helps detect and mitigate some types of web attacks such as data theft, site defacement, or the distribution of malware. CSP provides an extensive set of policy directives that help control the resources that a site page is allowed to load. Each directive defines the restrictions for a specific type of resource.

When CSP is turned on for a portals website, it helps enhance security by blocking connections, scripts, fonts, and other types of resources that originate from unknown or malicious sources. CSP is turned off by default in portals; however, many websites might require CSP to enhance other security.

For more information about CSP, go to [Content Security Policy Reference](https://content-security-policy.com/).

## Configure CSP

1. Sign in to [Power Apps](https://make.powerapps.com).

1. Ensure that you're in the environment where your portal exists.

1. On the left pane, select **Apps**, and then select the [**Portal Management** app](configure-portal.md).

    :::image type="content" source="media/manage-content-security-policy/portal-management-app.png" alt-text="The Apps menu option for Power Apps, with the Portal Management app selected.":::

1. On the left pane, select **Site Settings**.

1. Create (or update) the **HTTP/Content-Security-Policy** site setting, and set the values you need from the [CSP reference](https://content-security-policy.com/) page, separated by semicolons.

    **Example**

    `script-src 'self' https://js.example.com;style-src 'self' https://css.example.com`

    :::image type="content" source="media/manage-content-security-policy/http-content-security-policy.png" alt-text="The Site Settings menu option for Power Apps.":::

## Enable nonce

Enabling *nonce* (number used once) will block the execution of all inline scripts except those specified within the inline script. A unique cryptographic nonce is generated and added to each script specified in the CSP header. In portals, nonce supports inline scripts and inline event handlers only. For more information about nonce, go to [Using a nonce with CSP](https://content-security-policy.com/nonce/).

To enable nonce in portals, add the **script-src 'nonce';** value to the **HTTP/Content-Security-Policy** site settings.

**Examples**

If you want a strict policy and don't want to allow script loading from sources outside of portals, use the following:

```html
script-src 'self' content.powerapps.com 'nonce'
```

If you want to load scripts from any secure source, use the following:

```html
script-src https: 'nonce'
```

> [!NOTE]
> - When nonce is enabled, **unsafe-eval** will be automatically injected to support the automatic evaluation of unsafe code. To disable the automatic injection of **unsafe-eval**, update the site setting **HTTP/Content-Security-Policy/Inject-unsafe-eval** to **false**.
> - If **unsafe-eval** injection is disabled, the validation of automatically generated fields on [basic](../configure/entity-forms.md) or [advanced](../configure/web-form-properties.md) forms might no longer function correctly.

