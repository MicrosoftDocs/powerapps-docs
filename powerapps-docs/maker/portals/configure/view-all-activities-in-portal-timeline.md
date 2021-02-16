---
title: "View activities in a portal timeline | MicrosoftDocs"
description: "Instructions to view all activities in a portal Timeline."
author: sandhangitmsft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 06/25/2020
ms.author: sandhan
ms.reviewer: tapanm
---

# View activities in a portal timeline

While working on a case or interacting with a customer, you might create an activity such as an appointment, an email, or a phone call. When you navigate to the Timeline in your support portal, you might not find this activity because by default all activities aren't displayed in portal Timeline. 

To view all activities in a portal Timeline: 

1. Set the **CustomerSupport/DisplayAllUserActivitiesOnTimeline** site setting to true.  
    
    > [!NOTE]
    > If **DisplayAllUserActivitiesOnTimeline** site setting does not exist, you can create a new setting with this name.

2. If not present, add the activity type to include in the view filter:  
    1. Go to [**Settings**](https://docs.microsoft.com/power-platform/admin/admin-settings#app-settings) > **Customizations** > **Customize the System**.
    2. Select **Activity** entity and expand **Views**.
    3. Edit the **Portal Timeline View**.
    4. Update the **Edit Filter Criteria** and add the required activity type such as **Appointment, Email, or Phone Call**.
    5. **Save** and **Publish** the customizations. 

    > [!IMPORTANT]
    > Preparing customizations may take some time. If you see a message that the browser page has become unresponsive, wait for the page to become responsive, and don't close it.

3. Since this change is a portal metadata change, [clear the server-side cache](../admin/clear-server-side-cache.md) to ensure the updated data is displayed on the portal.

> [!NOTE]
> Portal timeline doesn't show inline images in the timeline control. For example, images embedded within emails don't appear on the portal timeline.


[!INCLUDE[footer-include](../../../includes/footer-banner.md)]