---
title: How to enable the enhanced email template in Power Apps
description: Turn on the enhanced email template option in Power Apps.
author: mgandham
manager: shujoshi
ms.topic: task
ms.date: 4/25/2022
ms.subservice: end-user
ms.author: gandhamm
search.audienceType: 
  - enduser
search.app: 
  - PowerApps
  - D365CE
---

# Enable the enhanced email template editor page
<!-- Please replace "enable" with "turn on" throughout, IAW the Microsoft Style Guide. Thanks! -->

Turn on the enhanced email template editing experience in apps across your organization. If you need to, you can turn off the enhanced email template page for a specific app. Users of that app see the default email template editor page.

## Enable the enhanced email template editor across all apps

1. In Power Apps, select the environment that contains your solution.

1. Select **Solutions**, and then select the solution in which you want to turn on the enhanced template editing experience.

   > [!NOTE]
   > Don't select the default solution.
<!-- It would be helpful for users to know why not. -->

1. Select **Add Existing** > **More** > **Setting**.

1. Select **Enable the New Email Template Editor**, and then select **Next**.
<!--I couldn't find this in my demo tenant and I looked everywhere I could think of. Is there a prerequisite to being able to see this setting? -->

1. Select **Add** to add the **Enable the New Email Template Editor** setting to your solution.

1. Select **Enable the New Email Template Editor**, and then set **Setting environment value** to **Yes**.

1. Select **Publish all customizations**.

## Disable the enhanced email template for an app
<!-- Please replace "disable" with "turn off" throughout. -->

To force an app to use the default email template editor page, turn off the enhanced template editing experience in that app. First, you'll need to add the app to the solution to which you've added the enhanced email template editing experience.

1. In Power Apps, select **Solutions**, and then select the solution to which you've added the enhanced email template editing experience.

1. Select **Add Existing** > **App** > **Model-driven app**> **Add existing model-driven apps**.

1. Select the app to add it to the solution.

1. Select the solution, and then select **Enable the New Email Template Editor**.

1. In the **Setting app value** section, select **New app value** for the app, and then select **No**.
<!--This really needs a screenshot. -->

1. Select **Save**, and then select **Publish all customizations**.

After you publish the customizations, the app uses the default email template editor.

<!--The example didn't add anything useful. -->
### See also

[How to create an email template  in model-driven apps](email-template-create.md)  
[Customize an email template using the template editor](cs-template-options.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]
