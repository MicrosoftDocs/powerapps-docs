---
title: Create a data loss prevention (DLP) policy | Microsoft Docs
description: Walkthrough of how to create a data loss prevention (DLP) policy
services: ''
suite: powerapps
documentationcenter: na
author: SKjerland
manager: kfile
editor: ''
tags: ''

ms.service: powerapps
ms.devlang: na
ms.topic: quickstart
ms.tgt_pltfrm: na
ms.workload: na
ms.date: 03/02/2018
ms.author: sharik

---
# Quickstart: Create a data loss prevention (DLP) policy
To protect data in your organization, PowerApps lets you create and enforce policies that define which consumer services/connectors specific business data can be shared with. These policies that define how data can be shared are referred to as data loss prevention (DLP) policies. DLP policies ensure that data is managed in a uniform manner across your organization, and they prevent important business data from being accidentally published to services such as social media sites.

In this quickstart, you'll learn how to create a DLP policy that prevents data that's stored in your Common Data Service and SharePoint databases from being published to Twitter.

## Prerequisites
To follow this quickstart, the following items are required:
* Either PowerApps Plan 2 or Flow Plan 2. Alternatively, you can sign up for a [free PowerApps Plan 2 trial](https://web.powerapps.com/signup?redirect=marketing&email=).
* Either Environment Admin or Tenant Admin permissions, and permissions to at least one environment. For more information, see [Environments administration in PowerApps](administrator/environments-administration.md).

## Sign in to the PowerApps Admin center
Sign in to the Admin center at [https://home.dynamics.com]([https://admin.powerapps.com).

## Create a DLP policy
1. In the navigation pane, click or tap **Data policies**, and then click or tap **New policy**.

    ![](./media/create-dlp-policy/new-data-policy.png)
2. For the data policy name, enter **Secure Data Access for Contoso**.
3. On the **Environments** tab, select an environment from the drop-down list, and then click or tap **Continue**.

    ![](./media/create-dlp-policy/select-environment.png)
4. On the **Data groups** tab, under **Business data only**, click or tap **Add**.

    ![](./media/create-dlp-policy/data-groups.png)
5. In the **Add connectors** window, click or tap **Common Data Service** and **SharePoint**, and then click or tap **Add connectors** to add them to the **Business data only** group.

    ![](./media/create-dlp-policy/add-connectors.png)
6. Click **Save policy**.

    ![](./media/create-dlp-policy/save-policy.png)
7. The Secure Data Access for Contoso policy is created and appears in the list of data loss prevention policies.
## Next steps
In this quickstart, you learned how to run a canvas-based or model-driven app in a web browser. To learn more about PowerApps, continue to the PowerApps tutorials.

> [!div class="nextstepaction"]
> [PowerApps Tutorials](get-started-create-from-blank.md)
