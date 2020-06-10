---
title: 
description: 
author: iaanw
manager: shellha
ms.service: powerapps
ms.topic: conceptual
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 6/10/2020
ms.author: iawilt
search.audienceType: 
  - maker
search.app: 
  - PowerApps
ms.custom: ce06032020

---

# Add geospatial components to your app (Preview)

[!INCLUDE [cc-beta-prerelease-disclaimer.md](../../includes/cc-beta-prerelease-disclaimer.md)]

You can add a number of geospatial components to your canvas app to support scenarios that involve mapping locations and addresses.

Components are groups of controls that can answer the need for a specific scenario.

You can read more about components and how to build your own in [the Power Apps developer library](/powerapps/developer/component-framework/custom-controls-overview).

The following pre-built components can be used for geospatial and mapping scenarios:

- [Interactive map](geospatial-component-map.md)
- [Address input](geospatial-component-input-address.md)

## Prerequisites

1. An admin must [enable the geospatial features in the Power Platform Admin Center](#enable-the-geospatial-features-for-the-environment) for the environment. This requires reviewing and agreeing to specific terms of service.
2. [Enable the geospatial features for each app](#enable-the-geospatial-features-for-each-app).

>[!NOTE]
> These geospatial components are currently an experimental preview feature that is only available in [https://preview.create.powerapps.com](https://preview.create.powerapps.com) on a [Power Apps Preview Program environment](/power-platform/admin/preview-environments).

### Enable the geospatial features for the environment

Before you can use geospatial features in your apps, an admin must enable access to the features for the environment where you want to create your app.

The geospatial features require additional terms of use that must be reviewed and agreed to.

1. Open the [Power Platform admin center](https://admin.powerplatform.microsoft.com).

1. On the **Environments** tab, select the environment you want to use for your apps, and then select **Settings** from the top menu.

    ![Environment selected in the Power Platform admin center](./media/geospatial/ppac-environment.png "Environment selected in the Power Platform admin center")

1. Expand **Product** and select **Features**.

    ![Screenshot of environment settings with Features selection highlighted](./media/geospatial/ppac-settings.png "Screenshot of environment settings with Features selection highlighted")

1. Under **Geospatial services (preview)**, set the toggle switch to **On**. A terms of service notice will appear. Read through the terms of service, and if you agree, select the checkbox **I agree to the terms of service**, and then **Enable**.

    ![Screenshot of the terms of service](./media/geospatial/ppac-tos.png)

    >[!IMPORTANT]
    >You must read and agree to the terms of service before you can use geospatial features. The following are the terms of service:  
    >  
    >These features use mapping capabilities that are powered by a third party, TomTom(tm), and operate outside your tenant's geographic region, compliance boundary, or national cloud instance.  
    >
    >Microsoft shares the address and location queries with TomTom(tm). The name of the customer or end user who entered the query is not shared.
    >
    >This feature is non-regional and the queries you provide may be stored and processed in the United States or any other country in which Microsoft or its subprocessors operate.
    >
    >Additional licensing requirements might be required to enable this feature.  

    ![Screenshot of the geospatial services toggle switch to On](./media/geospatial/ppac-geo-on.png "Screenshot of the geospatial services toggle switch to On")

1. Click **Save** at the bottom of the settings page.

    ![Screenshot of the save button](./media/geospatial/ppac-save.png "Screenshot of the save button")

### Enable the geospatial features for each app

1. Open the app for editing in Power Apps Studio at [https://create.powerapps.com](https://create.powerapps.com).

2. Select **File** from the top menu.

    ![Select File](./media/augmented-overview/augmented-overview-file.png "Select File")

3. Go to the **Settings** tab, select **Advanced settings**, and scroll down to find the **Geospatial features** option. Set the option to **On**.

    ![Set the Geospatial features switch to on](./media/geospatial/enable-geo.png "Set the Geospatial features switch to on")

4. Return to editing your app by selecting the back arrow icon.

    ![Select the back arrow icon](./media/augmented-overview/augmented-overview-back.png "Select the back arrow icon")

5. Open the **Insert** pane to see the geospatial components:
    - **Address input** is under **Input**
    - **Map** is under **Media**

    ![See the address input component under Input](./media/geospatial/insert-address-input.png "See the address input component under Input")  

    ![See the map component under Media](./media/geospatial/insert-map.png "See the map component under Media")

## Next steps

Start installing the components in your apps:

- Visualize and interpret location data with the **[Interactive map](geospatial-component-map.md)** component.
- See dynamic address suggestions as you type with the **[Address input](geospatial-component-input-address.md)** component.
