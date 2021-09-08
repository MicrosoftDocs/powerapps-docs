---
title: Power Apps portals version 9.3.4.x
description: Learn about the updates included in Power Apps portals version 9.3.4.x, including fixes, enhancements, and the scope of the release.
author: dileepsinghmicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/15/2021
ms.subservice: portals
ms.author: dileeps
ms.reviewer: tapanm
contributor:
    - tapanm-msft
    - dileepsinghmicrosoft
---

# Power Apps portals version 9.3.4.x

Power Apps portals version 9.3.4.x is in Early Upgrade phase. To keep track of upcoming changes, check the [Message center](/microsoft-365/admin/manage/message-center) for release schedules in your geographical region.

This article describes the features, enhancements, and scope of the release.

## Updates included with version 9.3.4.x

This release includes only an updated portal host, and no solution package updates. The portal host will automatically be updated to version 9.3.4.2 by Microsoft.

Portal host version 9.3.4.2 resolves the following issues:

- Accessibility - "Record has been deleted successfully" banner message disappears automatically without user input when a user selects **Delete** button on an Entity List record.

- Accessibility - Keyboard focus goes to **Redeem Invitation** tab item after pressing Enter key on the **Register** button.

- Custom JavaScript defined on the homepage is executing when any page is opened in a modal pop-up.

- When a code component (control) is added on a web form, an error is shown in the browser console.

- If a Bing map configuration is set on an Entity form, it gets displayed even if **Map Enabled** setting isn't enabled.

- If a note is added with multiple lines in a model-driven app, it shows in a single line on the portal.

- When strict request validation mode is enabled on the portal, a generic error is shown if a special character is added in a field on the form. After this change, a validation error is shown.

- Power BI authentication error logs are available in diagnostics logging to help debug configuration issues.

- If certain types of site settings are added multiple times in configuration, the portal throws a server error during startup. After this change, the duplicate settings are ignored, and the first value is picked. This behavior leads to unwanted results if you have duplicate site settings present in the configuration with different values.

- The focus is going to the start of the page when the **Esc** key or **Cancel** button is hit in modal Entity forms.

- Save changes warning message doesn’t show when the Date/Time field is edited on the web form.

- Accessibility - NVDA announces unnecessary tables before announcing search edit box on the search page.

- Accessibility - JAWS/NVDA isn't indicating that a checkbox is required when reading the associated label.

- Accessibility - The tooltip provided for the **New** and **Audio** button on the Captcha isn't accessible using tab key.

- Search results properties are returning as empty in search Liquid tag when it's used on a web template.

- Resolve case option in Entity List action options doesn’t work properly.

- When trying to load a pick-list control with null value on an Entity List, an error is shown on the portal.

- Webpage tracking, web file tracking, and login tracking functionality is retired. More information: [Important changes and deprecations](../important-changes-deprecations.md#tracking-for-web-page-web-file-and-login)

This release also contains performance updates, security fixes, and improves the overall reliability of Power Apps portals.

### See also

[Release updates](../release-updates.md) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4) <br>
[How to Determine the Version of a Microsoft Dynamics 365 Portal](https://support.microsoft.com/topic/how-to-determine-the-version-of-a-microsoft-dynamics-365-portal-d2400fdc-b1dd-597b-feab-87abc805325e) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4)

