---
title: Power Apps portals version 9.3.6.x
description: Learn about the updates included in Power Apps portals version 9.3.6.x, including fixes, enhancements, and the scope of the release. 
author: dileepsinghmicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 07/02/2021
ms.subservice: portals
ms.author: dileeps
ms.reviewer: tapanm
contributor:
    - tapanm-msft
    - dileepsinghmicrosoft
---

# Power Apps portals version 9.3.6.x

Power Apps portals version 9.3.6.x is in Early Upgrade phase. To keep track of upcoming changes, check the [Message center](/microsoft-365/admin/manage/message-center) for release schedules in your geographical region.

This article describes the features, enhancements, and scope of the release.

## Updates included with version 9.3.6.x

This release includes only an updated portal host, and no solution package updates. The portal host will automatically be updated to version 9.3.6.5 by Microsoft.

Portal host version 9.3.6.5 resolves the following issues:

- Sorting isn't enabled on related table columns in a list. After this release, sorting can be enabled on related table columns by creating a site setting named **Site/EnableSortingOnLinkedEntities**, and setting its value as **true**.
- Calendar Control - "Specific Timezone" option in the "Time Zone Display Mode" dropdown isn't honored, and the time is displayed according to default browser timezone of the portal user. After this release, this setting will be honored.
- Custom plugin error doesn't show when the error occurs on a referenced table. For example, when uploading a file to annotation table on a basic form.
- Code components - Sometimes when the value of a control is changed, updated value isn't shown on the form.
- Advanced form - Configuration to set a target for **New** button in lookup dialog points to active advanced form instead of basic form; and doesn't work when set. This change will also require the portal package/solution version to be upgraded to 9.2.2103 or later.
- Advanced form - Added check for use of only unique advanced form steps in an Advanced Form.
- Power BI integration - Azure AD guest users aren't able to access embedded Power BI components.
- Captcha control - No alternative text is available for Captcha image, leading to screen readers being unable to inform users about using a shortcut for playing audio. After this release, the Captcha image will have an alternative text that will inform users to use a keyboard shortcut to play the audio describing the image.
- Accessibility - Sorting dropdown on search page isn't visible at 400% zoom.
- Accessibility - Blank values present in option set dropdowns aren't announced as blank.
- Accessibility - No main landmark is present on the generic error page.
- Accessibility - Search field and search button on lookup modal dialog aren't readable by screen readers.
- Accessibility - Screen Reader isn't narrating the descriptive information about the dates present in the calendar while navigating in Calendar shortcut keys.
- Accessibility - Selecting validation error message for Date/Time field isn't redirecting focus to that field.
- Accessibility - User is unable to access the "Time Picker" control that's present inside the Date/Time calendar control using the keyboard.
- Accessibility - Focus is lost in Date/Time calendar control when using navigation buttons present in the control.
- Accessibility - When focus lands on the "Calendar" icon in Date/Time calendar control, the narrator reads as "Choose date" instead of "Choose date and time".
- Accessibility - Unable to access some controls like "Select month",  "Select year", "Previous", and "Next" in Date/Time calendar control using the keyboard.
- Accessibility - Error message isn't displayed when the wrong format is given manually in Date/Time calendar control.
- Accessibility - Narrator/NVDA isn't reading role of "Choose Date" button in Date/Time calendar control.
- Accessibility - "Previous" (<) and "Next" (>) controls under calendar button in Date/Time calendar control are set as group control.
- Accessibility - No error message is provided to JAWS/NVDA when the maximum number of characters has been reached on a text field.
- Accessibility - Screen readers don't announce search results on lookup modal dialog.
- Accessibility - Keyboard focus isn't landed on the error message link after accessing the Next button in an advanced form without selecting the mandatory field rendered as a checkbox.
- Accessibility - Screen reader/NVDA isn't narrating the displayed error message information completely upon invoking the Submit button on the page while navigating using down arrow mode.
- Accessibility - Error is displayed visually, but isn't automatically announced by the screen reader when pressing Next in an advanced form without entering any text.

This release also contains performance updates, security fixes, and improves overall reliability of Power Apps portals.

### See also

[Release updates](../release-updates.md) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4) <br>
[How to Determine the Version of a Microsoft Dynamics 365 Portal](https://support.microsoft.com/topic/how-to-determine-the-version-of-a-microsoft-dynamics-365-portal-d2400fdc-b1dd-597b-feab-87abc805325e) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4)

