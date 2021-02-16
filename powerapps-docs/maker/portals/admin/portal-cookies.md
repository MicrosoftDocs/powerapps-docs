---
title: "Cookies in Power Apps portals | MicrosoftDocs"
description: "Know the cookies Power Apps portals uses."
author: neerajnandwana-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 10/23/2020
ms.author: nenandw
ms.reviewer: tapanm
---
 
# Cookies in Power Apps portals

A cookie is a small file sent from the web site to visitor's device by the browser. A single web session may use multiple cookies.

Power Apps portals also use cookies to store information for various purposes. The following table describes the cookies that Power Apps portals uses, and their lifetime.

| Cookie name | Description | Lifetime |
| - | - | - |
| __RequestVerificationToken | Used by the [antiforgery](https://docs.microsoft.com/dotnet/api/system.web.helpers.antiforgeryconfig.cookiename) system. | Session |
| .AspNet.ApplicationCookie | Used to identify user sessions. A user session starts when a user browses portal for the first time. And ends when the session is closed. [Authentication site settings](https://docs.microsoft.com/powerapps/maker/portals/configure/set-authentication-identity) can be used to change session expiry time span. | Session |
| adxPreviewUnpublishedEntities | Stores preview **ON/OFF** mode used in classic CMS system for portal administrators. | Session |
| adx-notification | Used in entity form actions to store alert message to be shown on redirection. | Session |
| ARRAffinity | Added automatically by Azure websites and ensures that requests are load balanced between different sites. Doesn't store any of user information. | Session |
| ASP.NET_SessionId | Used to maintain the session of a logged in user to avoid repeated sign-in. | Session |
| ContextLanguageCode | Stores the default language of the user accessing portal within a session and across webpages. The cookie is deleted after session closes. | Session |
| Dynamics365PortalAnalytics | Critical service cookie to analyze service usage anonymously and aggregated for statistical purpose. | 90 days |
| isDSTObserved | Stores a value to indicate if the current moment is in daylight saving time. | Session |
| isDSTSupport | Indicates whether a specified date and time falls in the range of daylight saving time. | Session |
| timeZoneCode | Stores the *timezonecode* field value of *CRM timezonedefinition* entity for the current timezone. | Session |
| timezoneoffset | Stores the [timezone difference](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset) between UTC and Local browser time. | Session |

### See also

[Cookie authentication site settings](https://docs.microsoft.com/powerapps/maker/portals/configure/set-authentication-identity#cookie-authentication-site-settings)


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]