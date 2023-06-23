---
title: App access checker for model-driven apps | Microsoft Learn
description: Describes how to use the app access checker for model-driven apps. 
author: jbujula
ms.author: jbujula
ms.reviewer: matp
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: how-to
ms.date: 06/23/2023
ms.custom: template-how-to
---
# App access checker for model-driven apps

Use the app access checker tool to identify common issues found for a specific user that can occur when running a model-driven app.

Issues found by the app access checker:

- If an app is visible to the user or not.
- The reason why an app is visible or not visible to the user.
- If the user has the required license.

To be able to view and play an app, the user must have:

- Create and edit privileges on the app module table.
- Read privilege and security role association. <!-- Read privilege on what? What does security role association mean? -->
- Read privilege, team association with user, and team associated with security role. <!-- Read privilege on what? What does team association with user and team association with role mean?  -->
- For Dynamics for Sales and Dynamics for Service apps, the user must have that licensing assigned as well.

## How to use the app access checker

Power Platform admins and makers can use the app access checker to search apps based on userid or email address.

Open the diagnostics page in your browser by typing https://*environmentURL*/WebResources/msdyn_AppAccessChecker.html, such as *https://contoso.crm.dynamics.com/WebResources/msdyn_AppAccessChecker.html*. Then enter the user ID or email address in the box and then select **Search**. <!-- How do you find the User ID? -->

## How to interpret the results

- **Visible**.
   - If the user doesn't have read privilege on app module table, none of the apps are visible to the user, and **No** is displayed.
   - If the user has read and/or write privilege on the app module table, then all the apps are visible and **Yes** is displayed.
- **License**.
   - If the user has appropriate licensing to play the app, **Yes** is displayed.
- **Security**.
   - If user has create or write privilege on the app module table, Yes is displayed. If the user isn't associated to one or more security roles assigned to the app, check if the user is member of a team and whether that team is associated with that security role.

### Example results
<!-- Images below have user names. Are they approved fictitious names? -->

User has access to all visible apps in the environment.
:::image type="content" source="media/app-access-checker/user-can-view-apps.png" alt-text="User has access to all visible apps in the environment" lightbox="media/app-access-checker/user-can-view-apps.png":::

User doesn't have visibility or access to any apps in the environment because of missing security role membership associated with the app.
:::image type="content" source="media/app-access-checker/user-no-access.png" alt-text="Assign security roles to app" lightbox="media/app-access-checker/user-no-access.png":::

Two examples where the user has visibility to some apps visible but not others because of missing security role membership associated with the app.
:::image type="content" source="media/app-access-checker/user-access-role.png" alt-text="User has access to some apps visible but not others" lightbox="media/app-access-checker/user-access-role.png":::

:::image type="content" source="media/app-access-checker/user-access-role-2.png" alt-text="Assign missing security roles to user" lightbox="media/app-access-checker/user-access-role-2.png":::

In this example, the user has the required security privilege for the app but doesn't have the required license to access the app.
:::image type="content" source="media/app-access-checker/user-no-license-access.png" alt-text="User doesn't have required license." lightbox="media/app-access-checker/user-no-license-access.png":::

In this example, the user doesn't have the required security privilege, so this tool isn't able to show licensing details.
:::image type="content" source="media/app-access-checker/user-no-security-access.png" alt-text="Missing privileges to run the app" lightbox="media/app-access-checker/user-no-security-access.png":::

If **Security** is **Yes** and **License** is **No** or **Unknown** the issue needs to be investigated by licensing team. <!-- You mean contact Support? -->
:::image type="content" source="media/app-access-checker/user-yes-security-no-license.png" alt-text="Licensing issue is detected." lightbox="media/app-access-checker/user-yes-security-no-license.png":::

## Limitation

- It will not show Details for Outlook App as it is only visible to administrators.
