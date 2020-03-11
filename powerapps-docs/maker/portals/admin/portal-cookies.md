---
title: "Cookies in Power Apps portals | MicrosoftDocs"
description: "Know the cookies Power Apps portals uses."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 03/10/2020
ms.author: nenandw
ms.reviewer: tapanm
---
 
# Cookies used by Power Apps portals

A cookie is a small file sent from the web site and stored on visitor's computer by the browser the visitor uses to browse the web site. A single web session may use multiple cookies depending on the architecture and configuration of the web site.

Power Apps portals also use cookies to store information for various purposes. The following section lists and describes the cookies that Power Apps portals uses:

### ARRAffinity

Added automatically by Azure websites and ensures that requests are load balanced between different sites. Doesn't store any of user information.

###  ASP.Net Session Id

Used to maintain the session of a logged in user so that the user doesn't need to sign in again. This is a session cookie - not persistent; and is deleted once session closes.

### Dynamics 365 Portal Analytics

Critical service cookie to analyze service usage anonymously and aggregated for statistical purpose.

### ContextLanguageCode

Stores the default language of the user accessing portal within a session and across webpages. This is a session cookie. In other words, a short term cookie. And is deleted when web site session closes.

### .AspNet.ApplicationCookie

Used to identify user sessions. A single user session begins when a user browses portal for the first time and ends when the session is closed. [Authentication site settings](https://docs.microsoft.com/powerapps/maker/portals/configure/set-authentication-identity) can be used to change session expiry time span.

### __RequestVerificationToken 

Used by the [antiforgery](https://docs.microsoft.com/dotnet/api/system.web.helpers.antiforgeryconfig.cookiename) system.

### adxPreviewUnpublishedEntities

Holds preview **ON/OFF** mode used in classic CMS system for portal administrators.

### adx-notification

Used in entity form actions to store alert message to be shown on redirection.

### timezoneCode

Holds the *timezonecode* field value of *CRM timezonedefinition* entity for the current timezone.

### timezoneoffset

Holds the [timezone difference](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Date/getTimezoneOffset) between UTC and Local browser time.

### isDSTSupport

Indicates whether a specified date and time falls in the range of daylight saving time.

### isDSTObserved

Stores a value to indicate if the current moment is in daylight saving time.

### See also

[Cookie authentication site settings](https://docs.microsoft.com/powerapps/maker/portals/configure/set-authentication-identity#cookie-authentication-site-settings)

