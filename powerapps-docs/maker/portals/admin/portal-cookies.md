---
title: Cookies in Power Apps portals
description: Learn about cookies used by Power Apps portals.
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 09/10/2021
ms.subservice: portals
ms.author: nenandw
ms.reviewer: tapanm
contributors:
    - neerajnandwana-msft
    - tapanm-msft
---
 
# Cookies in Power Apps portals

A cookie is a small file sent from the web site to visitor's device by the browser. A single web session may use multiple cookies.

Power Apps portals also use cookies to store information for various purposes. The following table describes the cookies that Power Apps portals uses, and their lifetime.

| Cookie name | Description | Lifetime |
| - | - | - |
| __RequestVerificationToken | Used by the [antiforgery](/dotnet/api/system.web.helpers.antiforgeryconfig.cookiename) system. | Session |
| .AspNet.ApplicationCookie | Used to identify user sessions. A user session starts when a user browses portal for the first time. And ends when the session is closed. [Authentication site settings](../configure/set-authentication-identity.md) can be used to change session expiry time span. | Session |
| adxPreviewUnpublishedEntities | Stores preview **ON/OFF** mode used in classic CMS system for portal administrators. | Session |
| adx-notification | Used in basic form actions to store alert message to be shown on redirection. | Session |
| ARRAffinity | Added automatically by Azure websites and ensures that requests are load balanced between different sites. Doesn't store any of user information. | Session |
| ASP.NET_SessionId | Used to maintain the session of a logged in user to avoid repeated sign-in. | Session |
| ContextLanguageCode | Stores the default language of the user accessing portal within a session and across webpages. The cookie is deleted after session closes. | Session |
| Dynamics365PortalAnalytics | Critical service cookie to analyze service usage anonymously and aggregated for statistical purpose. | 90 days |
| isDSTObserved | Stores a value to indicate if the current moment is in daylight saving time. | Session |
| isDSTSupport | Indicates whether a specified date and time falls in the range of daylight saving time. | Session |
| timeZoneCode | Stores the *timezonecode* field value of *CRM timezonedefinition* table for the current timezone. | Session |
| timezoneoffset | Stores the [timezone difference](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset) between UTC and Local browser time. | Session |

## Frequently asked questions

### Can I deactivate some or all cookies in my portal?

No. If required, consider adding a consent dialog for portal users through external scripts.

### Why can't I use my portal without cookies?

Cookies are required to maintain a portal functional, with the purpose as described in the table above.

### What does the session lifetime mean?

Cookies with the "session" lifetime are only used while the browser is open, and removed after you close the browser.

### What is the data governance policy for cookies in portals?

For information about data governance, data storage and access, read [Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement).

### Do cookies in portals store any personal data?

No.

### Do cookies in portals store my IP address?

No. However, check the terms of your analytics provider if you've configured traffic analysis on your portal. Traffic analysis can be configured through [Portal Management app](../configure/configure-portal.md) > **Administration** > **Enable Traffic Analysis**.

### See also

[Cookie authentication site settings](../configure/set-authentication-identity.md#cookie-authentication-site-settings)

[!INCLUDE[footer-include](../../../includes/footer-banner.md)]