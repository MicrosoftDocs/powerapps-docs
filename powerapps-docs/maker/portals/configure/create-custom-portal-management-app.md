---
title: "Create custom Portal Management app for Power Apps portal | MicrosoftDocs"
description: "Learn how to create a custom Portal Management app for Power Apps portal."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 03/24/2020
ms.author: tapanm
ms.reviewer: sandhan
---

# Create custom Portal Management app

The [overview](configure-portal.md) introduces **Portal Management** app to help you get started with the advanced portal configuration. In this walk-through, you'll learn how to create a custom **Portal Management** app for additional customization, or if you accidentally deleted the default **Portal Management** app.

## How to create a custom Portal Management app

To create a custom **Portal Management** app:

1. Sign-in to [Power Apps](https://make.powerapps.com).

1. Select **Create** from the left navigation.

1. Select **Model-driven app from blank**:

    ![Create model-driven app from blank](media/create-model-driven-app.png)

1. Select **Create**:

    ![Create button](media/create-button.png)

    Selecting **Create** button opens app designer with **Create a New App** form:

    ![App designer](media/app-designer.png)

1. Enter a name for the app. For example, *Portal Management (custom)*:

    ![App name](media/app-name.png)

    The *Unique Name* for the app is automatically updated. 

1. If required, enter description.

1. Uncheck *Use Default Image* for *Icon* and select image file as *adx_nav_portals_32.png*:

    ![Image icon](media/icon.png)

1. Check *Use existing solution to create the App*:

    ![Use existing solution](media/use-existing-solution.png)

1. Verify all the settings and then select **Next**:

    ![Verify and next](media/verify-next.png)

1. Select *Dynamics 365 Portals - Portal base* as the solution for *Select Solution* drop down option:

    ![Select solution](media/select-solution.png)

1. Select *Dynamics 365 Portals* as the sitemap for *Select Sitemap* drop down option:

    ![Select sitemap](media/select-sitemap.png)

1. Verify selections and then select **Done**:

    ![Verify and done](media/verify-done.png)

1. After the app opens in **App Designer**, select **Publish**:

    ![Publish the app](media/publish.png)

1. Close the **App Designer** browser tab.

1. Open [Power Apps](https://make.powerapps.com).

1. Select **Apps** from left navigation.

1. You can see the new **Portal Management** custom app created:

    ![Maker apps](media/maker-apps.png)

1. Hover over the new app name and select to open the new **Portal Management** custom app:

    ![Select new app](media/select-pma.png)

1. Verify the settings in the new **Portal Management** custom app:

    ![Verify settings](media/custom-pma.png)

## Next steps

[Configure site settings](configure-site-settings.md)

### See also

[FAQ - How to delete a portal?](https://docs.microsoft.com/powerapps/maker/portals/faq#how-do-i-delete-a-portal-completely-after-it-is-provisioned)
