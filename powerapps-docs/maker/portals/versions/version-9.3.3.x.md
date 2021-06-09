---
title: Power Apps portals version 9.3.3.x
description: Learn about the Power Apps portals version 9.3.3.x and the changes.
author: dileepsinghmicrosoft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 03/18/2021
ms.author: dileeps
ms.reviewer: tapanm
contributor:
    - tapanm-msft
    - dileepsinghmicrosoft
---

# Power Apps portals version 9.3.3.x

Power Apps portals version 9.3.3.x is generally available. To know the release schedule, check the [Message center](/microsoft-365/admin/manage/message-center) for release schedule in your geographical region.

In this article, you'll learn about:

- Features and enhancements included in this update.
- Scope of the release.

For a full list of all portal updates released to date and their corresponding KB articles, go to [Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4).

## Updates included with version 9.3.3.x

This release includes only an updated portal host and no solution package
updates. The portal host will automatically be updated to version 9.3.3.7 by
Microsoft.

Portal host Version 9.3.3.7 resolves the following issues:

-   Tooltip isn't defined for “Next/previous” links present under the Entity
    List.

-   When using duration control in Edit mode in portal, it doesn't allow users
    to type in a custom value.

-   When using duration control in read-only mode in portal, custom duration
    values aren't displayed.

-   Custom Plugin Errors aren't displayed when updating annotation records on
    the Portal

-   Can't access Files in the SharePoint subfolder with in sub folder.

-   When adding custom plugin error for the profile page, the error messages aren't shown.

-   Quick view form renders with its own scroll bar in the page

-   File containing "&" in the file name cannot be downloaded from portal.

-   Custom Plugin Errors aren't displayed when user is trying to delete a
    record from the portal.

-   Calendar Control is rendering events twice on the portal when the timezone
    is set to GMT+5:30pm

-   Password validation Error Message in French Language contains some English
    words

-   Pagination doesn't work properly in Sharepoint grid when a user deletes the
    file from the top.

-   Custom JavaScript defined on the Home page is executing when a page is
    opened in modal popup.

-   Default value set for Currency Field isn't populating on Webform step.

-   While adding duplicate record/existing record to the sub grid that has N:N
    relationship, user is getting an error "cannot insert duplicate key"
    intermittently.

-   Invalid date is getting displayed when Finnish language is selected in
    Portals.

-   "Unsaved Changes" warning appears after the form with unsaved changes is
    closed.

-   When the keyboard focus moves to the "First Name" text box on Profile page,
    color contrast ratio of border with its background is less than 3:1.

-   Narrator isn't announcing the status message after updating the "Profile"
    information.

-   Keyboard focus isn't visible when a user navigates to the grid shown in the
    lookup dialog.

-   Keyboard focus isn't in logical order after deleting any Note from Timeline
    control.

-   NVDA announces "Next/Preview Page" Button on timeline control as a link.
    After this release, they'll be announced as a button.

-   NVDA announces unnecessary tables before announcing Search edit box on
    lookup dialog box.

-   After pressing Esc key to collapse the tooltip, the whole lookup dialog is
    collapsed.

-   When keyboard focus is on "Launch lookup modal" button, tooltip isn't
    appearing.

-   The tooltip provided for the "New" and "Audio" button on Captcha control isn't accessible using tab key.

-   At 400% Zoom mode, facet panel present on Search page gets truncated.

-   Error message is announced multiple times along with other content when sign-in button is activated without Username and Password.

-   If ViewId or ChartId is null, then a proper error message isn't shown on
    chart liquid tag.

-   NVDA isn't recognizing the 'Main' landmark in the 'Home' page, while
    navigating using NVDA landmark short cut key 'D'.

-   VoiceOver isn't narrating role for the dates along with it respective day.

- Password field's HTML ID on the login page is changed to enable accessibility scenarios. Any JavaScript that depends on the HTML ID of this field might not work after the upgrade.

    > [!NOTE]
    > Using HTML IDs of the Login and Password fields from the login page in custom JavaScripts is not supported. These IDs can change in the future releases.

- Entity List isn't loading on Internet Explorer 11 intermittently.

This release also contains performance, security fixes and improves overall
reliability of Power Apps portals.

### See also

[Release updates](../release-updates.md) <br>
[Portal Capabilities for Microsoft Dynamics 365 Releases](https://support.microsoft.com/topic/portal-capabilities-for-microsoft-dynamics-365-releases-81f5fcc9-ef72-8b2e-5b4b-29e9840fb5c4) <br>
[How to Determine the Version of a Microsoft Dynamics 365 Portal](https://support.microsoft.com/topic/how-to-determine-the-version-of-a-microsoft-dynamics-365-portal-d2400fdc-b1dd-597b-feab-87abc805325e)
