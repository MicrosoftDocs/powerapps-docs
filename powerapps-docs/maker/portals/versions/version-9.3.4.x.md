---
title: Power Apps portals version 9.3.4.x
description: Learn about the Power Apps portals version 9.3.4.x and the changes.
author: dileepsinghmicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/15/2021
ms.author: dileeps
ms.reviewer: tapanm
contributor:
    - tapanm-msft
    - dileepsinghmicrosoft
---

# Power Apps portals version 9.3.4.x

Power Apps portals version 9.3.4.x is in Early Upgrade phase. To know the release schedule, check the [Message center](/microsoft-365/admin/manage/message-center) for release schedule in your geographical region.

This article describes the features, enhancements, and scope of the release.

## Updates included with version 9.3.4.x

This release includes only an updated portal host, and no solution package updates. The portal host will automatically be updated to version 9.3.4.2 by Microsoft.

Portal host Version 9.3.4.2  resolves the following issues:

- Accessibility - "Record has been deleted successfully" banner message disappears automatically without user input when a user selects **Delete** button on an entity list record.

- Accessibility - Keyboard focus goes to **Redeem Invitation** tab item after pressing enter key on **Register** button.

- Custom JavaScript defined on the Home is executing when any page is opened in a modal popup.

- When a code component (control) is added on a web form, an error is shown in the browser console.

- If a Bing map configuration is set on an entity form, it gets displayed even if **Map Enabled** setting isn't enabled.

- If a note is added with multiple lines in model-driven app, it shows in a single line on the portal.

- When strict request validation mode is enabled on portal, a generic error is shown on the portal if a special character is added on a field on the form. After this change, a validation error is shown.

- Power BI authentication error logs are available in diagnostics logging to help debug configuration issues.

- If certain types of site settings are added multiple times in configuration, portal throws a server error during startup. After this change, the duplicate settings are ignored, and the first value is picked. This behavior leads to unwanted results if you have duplicate site settings present in the configuration with different values.

- The focus is going to start of the page when **Esc** key, or **Cancel** button is hit in modal entity forms.

- Save changes warning message doesn’t show when the datetime field is edited on the web form.

- Accessibility - NVDA announces unnecessary tables before announcing search edit box on the search page.

- Accessibility - JAWS/NVDA isn't indicating that a checkbox is required when reading the associated label.

- Accessibility: The tooltip provided for the **New** and **Audio** button on the Captcha isn't accessible using tab key.

- Search results properties are returning as empty in search liquid tag when it's used on a web template.

- Resolve case option in entity list action options doesn’t work properly.

- When trying to load a pick-list control with null value on entity list, an error is shown on the portal.

This release also contains performance, security fixes and improves overall reliability of Power Apps portals.

### See also

[Release updates](../release-updates.md) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4) <br>
[How to Determine the Version of a Microsoft Dynamics 365 Portal](https://support.microsoft.com/topic/how-to-determine-the-version-of-a-microsoft-dynamics-365-portal-d2400fdc-b1dd-597b-feab-87abc805325e) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4)
