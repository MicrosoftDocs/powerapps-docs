---
title: "How to: Embed a Code App in an Iframe"
description: "Learn how to embed a code app in an iframe within an external host like a model-driven app or custom website. Update Content Security Policy frame-ancestors to allow framing."
ms.author: jordanchodak
author: jordanchodakWork
ms.date: 03/6/2026
ms.reviewer: jdaly
ms.topic: how-to
---
# Embed a code app in an iframe

This article explains how to embed a code app in an iframe within an external host, such as a model-driven app web resource, a custom website, or another service that supports iframes. Because code apps enforce Content Security Policy (CSP) by default, you must update the `frame-ancestors` directive to allow your host to load the app.

> [!NOTE]
> - Only Power Apps users within the same tenant can access an embedded code app. You can't share the iframe URL with users outside your tenant.
> - You can't embed code apps in any native desktop application, which includes Android and iOS. This limitation excludes first-party integrations such as Power Apps in Teams.

## Prerequisites

- You must be an administrator of the Power Platform environment to update CSP settings.
- The code app must be deployed to an environment.

## Get the code app URL

To embed a code app, you need its play URL. The URL takes the following form:

```
https://apps.powerapps.com/play/e/{environmentId}/app/{appId}?tenantid={tenantId}
```

You can find the full URL by opening the app in Power Apps and copying the address from the browser. `tenantId` is an optional query parameter to support guest access and determines which tenant to open the app from.

## Add the iframe to your host

After you get the code app URL, add a `<iframe>` element to the HTML of your host. Substitute your app URL for the `src` value and set the width and height as appropriate for your layout.

```html
<iframe
  width="1200"
  height="800"
  src="https://apps.powerapps.com/play/e/{environmentId}/{appId}"
  title="My code app">
</iframe>
```

> [!NOTE]
> If your code app uses the device geolocation, microphone, camera, fullscreen, or clipboard APIs, include the corresponding permissions in the `allow` attribute:
> ```html
> <iframe ... allow="geolocation; microphone; camera; fullscreen; clipboard-write"></iframe>
> ```

## Configure CSP to allow framing

By default, code apps use the following `frame-ancestors` directive, which restricts which origins can load the app in a frame:

```
frame-ancestors 'self' https://*.powerapps.com
```

If you embed a code app in any host outside of `https://*.powerapps.com`—such as a model-driven app, a Dynamics 365 instance, or a custom website—the browser blocks the frame and logs a CSP violation similar to the following:

```
Refused to frame 'https://<environment>.powerplatformusercontent.com/' because it violates the following Content Security Policy directive: "frame-ancestors 'self' https://*.powerapps.com"
```

To resolve this issue, add your host origin to the `frame-ancestors` directive for the environment. For example:

- For a Dynamics 365 or model-driven app: `https://<your-org>.crm.dynamics.com`
- For a custom domain: `https://contoso.com`

> [!IMPORTANT]
> Custom values merge with the default `frame-ancestors` value. After you save, the effective directive is:
> ```
> frame-ancestors 'self' https://*.powerapps.com https://<your-org>.crm.dynamics.com
> ```

For instructions on how to update the `frame-ancestors` directive by using the Power Platform admin center or the REST API, see [Configure Content Security Policy](content-security-policy.md).

## Related articles

[Configure Content Security Policy](content-security-policy.md)   
[Architecture](../architecture.md)
