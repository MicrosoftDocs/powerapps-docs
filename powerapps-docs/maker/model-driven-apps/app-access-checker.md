---
title: App access checker for model-driven apps | Microsoft Learn
description: Describes how to use the app access checker for model-driven apps. 
author: jbujula
ms.author: jbujula
ms.reviewer: matp
ms.service: powerapps
ms.subservice: mda-maker
ms.topic: how-to
ms.date: 07/22/2025
ms.custom: template-how-to
contributors: kevinhiggins-ms
---
# App access checker for model-driven apps

Use the app access checker tool to identify common issues found for a specific user that can occur when running a model-driven app.

Issues found by the app access checker include:

- If an app is visible to the user or not.
- The reason why an app is visible or not visible to the user.
- If the user has the required license.

## How to use the app access checker

Power Platform admins and makers can use the app access checker to search apps based on user principal name (UPN) or email address.

Open the diagnostics page in your browser by typing https://*environmentURL*/WebResources/msdyn_AppAccessChecker.html, such as *https://contoso.crm.dynamics.com/WebResources/msdyn_AppAccessChecker.html*. Then enter the UPN or email address in the box and then select **Search**.

## How to interpret the results

- **Visible**.
   - If the user doesn't have read privilege on the app module table, none of the apps are visible to the user, and **No** is displayed.
   - If the user has read and/or write privilege on the app module table, then all the apps are visible and **Yes** is displayed.
- **License**.
   - If the user has appropriate licensing to play the app, **Yes** is displayed.
   - Select the **details** link on either **Yes** or **No** result for each app to get information on how the user is or isn't able to access.
- **Security**.
   - If the user has create or write privilege on the app module table, **Yes** is displayed. If the user isn't associated to one or more security roles assigned to the app, check if the user is member of a team and whether the team is associated with that security role.

## Licensing terminology and how model-driven apps are accessed

In order for an app to be visible to a user, both the results for **License** and **Security** must be **Yes**. If a user doesn't have an appropriate license, the error message might give information about what **service plans** could be used to give access to the app. Note that **Licenses** aren't the same as service plans. A **License** is what is assigned to users in Microsoft Entra and usually has multiple service plans. For a list of all licenses and what service plans are included, go to the [licensing service plan reference](/entra/identity/users/licensing-service-plan-reference). Referencing the Microsoft Dataverse licensing error message and the service plan reference list can help diagnose user licensing issues. 

Also be aware that Dataverse caches the service plans that are assigned to users, so Microsoft Entra License assignments might not immediately reflect in Dataverse. To update the cached service plan assignments in Dataverse, have users sign out and sign back in. If the issue persists, it could be a result of Microsoft Entra caching, and the user should wait about 30 minutes, then sign out and sign back in again.

### Example results

User has access to all visible apps in the environment.
:::image type="content" source="media/app-access-checker/user-can-view-apps.png" alt-text="User has access to all visible apps in the environment" lightbox="media/app-access-checker/user-can-view-apps.png":::

User doesn't have visibility or access to any apps in the environment because of missing security role membership associated with each app.
:::image type="content" source="media/app-access-checker/user-no-access.png" alt-text="Assign security roles to app" lightbox="media/app-access-checker/user-no-access.png":::

Two examples where the user has visibility to some apps but not others because of missing security role membership associated with the app.
:::image type="content" source="media/app-access-checker/user-access-role.png" alt-text="User has access to some apps visible but not others" lightbox="media/app-access-checker/user-access-role.png":::

:::image type="content" source="media/app-access-checker/user-access-role-2.png" alt-text="Assign missing security roles to user" lightbox="media/app-access-checker/user-access-role-2.png":::

In this example, the user has the required security privilege for the app but doesn't have the required license to access some of the apps.
:::image type="content" source="media/app-access-checker/user-no-license-access.png" alt-text="User doesn't have required license." lightbox="media/app-access-checker/user-no-license-access.png":::

In this example, the user doesn't have the required security privilege, so the app access checker isn't able to show licensing details.
:::image type="content" source="media/app-access-checker/user-no-security-access.png" alt-text="Missing privileges to run the app" lightbox="media/app-access-checker/user-no-security-access.png":::

If **Security** is **Yes** and **License** is **No** or **Unknown** contact Help + support. More information: [Get Help + support](/power-platform/admin/get-help-support)
:::image type="content" source="media/app-access-checker/user-yes-security-no-license.png" alt-text="Licensing issue is detected." lightbox="media/app-access-checker/user-yes-security-no-license.png":::

## Limitation

- App access checker doesn't show details for the Outlook App. This is because that information is only visible to Power Platform administrators.

## Related articles

[Share a model-driven app](share-model-driven-app.md)
