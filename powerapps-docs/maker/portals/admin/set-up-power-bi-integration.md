---
title: "Set up Power BI integration with your portal | MicrosoftDocs"
description: "Learn how to set up Power BI integration with your portal."
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/27/2020
ms.author: tapanm
ms.reviewer:
---

# Set up Power BI integration

Power BI is one of the best tools to deliver insights with simple and interactive visualization. To view dashboards and reports from Power BI on web pages in a portal, you must enable Power BI visualization from the Power Apps Portals admin center. You can also embed dashboards and reports created in the new workspace of Power BI by enabling the Power BI Embedded service integration.

> [!NOTE]
> - You must have an appropriate Power BI license.
> - To use Power BI Embedded service, you must have an appropriate Power BI Embedded license. For more information, see [Licensing](https://docs.microsoft.com/power-bi/developer/embedded-faq#licensing).
> - Ensure **Embed content in apps** is *Enabled* in your Power BI tenant [Developer settings](https://docs.microsoft.com/power-bi/guidance/admin-tenant-settings#developer-settings). When disabled, portal can't render embedded Power BI dashboard or report.

## Enable Power BI visualization

Enabling Power BI visualization allows you to embed dashboards and reports on web pages in a portal by using the *powerbi* Liquid tag.

1.	Open [Power Apps Portals admin center](admin-overview.md).

2.	Go to **Set up Power BI integration** > **Enable Power BI visualization**.

    > [!div class=mx-imgBorder]
    > ![Enable Power BI visualization](../media/enable-power-bi-visualization.png "Enable Power BI visualization")

3.	Select **Enable** in the confirmation message. While Power BI visualization is being enabled, the portal restarts and will be unavailable for a few minutes. A message appears when Power BI visualization is enabled.

Customizers can use the [powerbi](../liquid/portals-entity-tags.md#powerbi) Liquid tag to embed Power BI dashboards and reports on web pages in a portal. While embedding the Power BI content, customizers can use [filter parameters](https://docs.microsoft.com/power-bi/service-url-filters) to create personalized views. More information: [powerbi Liquid tag](../liquid/portals-entity-tags.md#powerbi)

### Disable Power BI visualization

1.	Open [Power Apps Portals admin center](admin-overview.md).

2.	Go to **Set up Power BI integration** > **Disable Power BI visualization**.

    > [!div class=mx-imgBorder]
    > ![Disable Power BI visualization](../media/disable-power-bi-visualization.png "Disable Power BI visualization")

3. Select **Disable** in the confirmation message. While Power BI visualization is being disabled, the portal restarts and will be unavailable for a few minutes. A message appears when Power BI visualization is disabled.

## Enable Power BI Embedded service

Enabling the Power BI Embedded service allows you to embed dashboards and reports created in the new workspace of Power BI. The dashboards and reports are embedded on webpages in a portal by using the powerbi Liquid tag.

**Prerequisites**: Before enabling the Power BI Embedded service, ensure that you have created your dashboards and reports in the new workspace in Power BI. After creating the workspace, provide admin access to the global administrator so the workspaces are displayed in the Power Apps Portals admin center. For more information on creating new workspaces and adding access to them, see [Create the new workspaces in Power BI](https://docs.microsoft.com/power-bi/service-create-the-new-workspaces).

**Power BI Embedded service limitations**: For information on limitations, see [Considerations and limitations](https://docs.microsoft.com/power-bi/developer/embed-service-principal#considerations-and-limitations).

> [!NOTE]
> Ensure that Power BI visualization is enabled for the powerbi Liquid tag to work.

1. Open [Power Apps Portals admin center](admin-overview.md).

2. Go to **Set up Power BI integration** > **Enable Power BI Embedded service**.

    > [!div class=mx-imgBorder]
    > ![Enable Power BI Embedded service](../media/enable-powerbi-embedded-button.png "Enable Power BI Embedded service")

3. In the **Enable Power BI Embedded service integration** window, select, and move the Power BI workspaces from which dashboards and reports need to be displayed in your portal to the **Selected workspaces** list.

    > [!div class=mx-imgBorder]
    > ![Select Power BI workspaces](../media/enable-powerbi-embedded-window.png "Select Power BI workspaces")
    
    > [!NOTE]
    > After you add workspaces to the **Selected workspaces** list, the databases and reports are rendered after a few minutes.
    

4. Select **Enable**. While Power BI Embedded service is being enabled, the portal restarts and is unavailable for a few minutes. A message appears when Power BI Embedded service is enabled.

You must now create a security group, and add it to your Power BI account. For more information, see [Create security group and add to Power BI account](#create-security-group-and-add-to-power-bi-account).

### Create security group and add to Power BI account

After enabling the Power BI Embedded service integration, you must create a security group in Azure Active Directory, add a member to it, and then add the security group in Power BI through the Power BI admin portal. This allows the dashboards and reports created in new Power BI workspaces to be displayed in the portal.

> [!NOTE]
> You must sign in with the same Global administrator account that you used to enable the Power BI Embedded service.

**Step 1: Create a security group**

1. Sign in to the [Azure portal](https://portal.azure.com) using a Global administrator account for the directory.

2. Select **Azure Active Directory**, **Groups**, and then select **New group**.

3. On the **Group** page, enter the following information:

    - **Group type**: Security.

    - **Group name**: Portal Power BI Embedded service.

    - **Group description**: This security group is used for Portal and Power BI Embedded service integration.

    - **Membership type**: Assigned.

      > [!div class=mx-imgBorder]
      > ![Create security group for Power BI Embedded service](../media/powerbi-embed-security-group.png "Create security group for Power BI Embedded service")

4. Select **Create**.

**Step 2: Add a group member**

**Prerequisite**: Before adding a member to the security group, you must have the portal's application ID with you. The portal's application ID is available on the **Portal Details** tab in [Power Apps Portals admin center](admin-overview.md).

1. Sign in to the [Azure portal](https://portal.azure.com) using a Global administrator account for the directory.

2. Select **Azure Active Directory**, and then select **Groups**.

3. From the **Groups - All groups** page, search for the **Portal Power BI Embedded service** group, and select it.

    > [!div class=mx-imgBorder]
    > ![Search and select the security group for Power BI Embedded service](../media/search-security-group.png "Search and select the security group for Power BI Embedded service")

4. From the **Portal Power BI Embedded service Overview** page, select **Members** from the **Manage** area.

5. Select **Add members**, and enter the portal's application ID in the text box.

6. Select the member from the search result, and then choose **Select**.

    > [!div class=mx-imgBorder]
    > ![Add member in the security group for Power BI Embedded service](../media/add-member-powerbi-embed.png "Add member in the security group for Power BI Embedded service")

**Step 3: Power BI setup**

1. Sign in to [Power BI](https://powerbi.microsoft.com) using a Global administrator account for the directory.

2. Select **Settings** in the top right of the Power BI service, and choose **Admin portal**.

    > [!div class=mx-imgBorder]
    > ![Select Admin portal in Power BI service](../media/select-admin-portal.png "Select Admin portal in Power BI service")

3. Select **Tenant settings**.

4. Under the **Developer settings** section, select **Allow service principals to use Power BI APIs**.

5. In the **Specific security groups** field, search for the **Portal Power BI Embedded service** group, and select it.

    > [!div class=mx-imgBorder]
    > ![Add security group in Power BI Admin portal](../media/add-sg-powerbi.png "Add security group in Power BI Admin portal")

6. Select **Apply**.

Customizers can now use the [powerbi](../liquid/portals-entity-tags.md#powerbi) Liquid tag to embed Power BI dashboards and reports from new Power BI workspaces on webpages in a portal. To use Power BI Embedded service, the authentication type must be specified as **powerbiembedded**. While embedding the Power BI content, customizers can use [filter parameters](https://docs.microsoft.com/power-bi/service-url-filters) to create personalized views. More information: [powerbi Liquid tag](../liquid/portals-entity-tags.md#powerbi).


### Manage the Power BI Embedded service

1. Open [Power Apps Portals admin center](admin-overview.md).

2. Go to **Set up Power BI integration** > **Manage Power BI Embedded service**.

    > [!div class=mx-imgBorder]
    > ![Manage Power BI Embedded service](../media/manage-powerbi-embedded-button.png "Manage Power BI Embedded service")

3. In the **Manage Power BI Embedded service integration** window, remove, or move the Power BI workspaces from which dashboards and reports need to be displayed in your portal to the **Selected Workspaces** list.

    > [!div class=mx-imgBorder]
    > ![Select Power BI workspaces](../media/manage-powerbi-embedded-window.png "Select Power BI workspaces")
    
    > [!NOTE]
    > After removing the workspaces from the **Selected Workspaces** list, it can take up to 1 hour to reflect the changes. Until then, the databases and reports are rendered on the portal without any issues.

4. Select **Save**.

### Disable the Power BI Embedded service

1.	Open [Power Apps Portals admin center](admin-overview.md).

2.	Go to **Set up Power BI integration** > **Manage Power BI Embedded service**.

    > [!div class=mx-imgBorder]
    > ![Manage Power BI Embedded service](../media/manage-powerbi-embedded-button.png "Manage Power BI Embedded service")

3. In the **Manage Power BI Embedded service integration** window, select **Disable Power BI Embedded service integration**.

    > [!div class=mx-imgBorder]
    > ![Disable Power BI Embedded service](../media/disable-powerbi-embedded-window.png "Disable Power BI Embedded service")

4. Select **Save**.

5. Select **OK** in the confirmation message. While Power BI Embedded service is being disabled, the portal restarts and is unavailable for a few minutes. A message appears when Power BI Embedded service is disabled.

## Privacy notice  

[!INCLUDE[cc_privacy_powerbi_tiles_dashboards](../../../includes/cc-privacy-powerbi-tiles-dashboards.md)]

### See also

[powerbi Liquid tag](../liquid/portals-entity-tags.md#powerbi)<br> 
[Add a Power BI report or dashboard to a webpage in portal](add-powerbi-report.md)
