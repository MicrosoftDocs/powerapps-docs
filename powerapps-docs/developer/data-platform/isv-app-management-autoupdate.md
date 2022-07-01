---
title: Auto App Updates | Microsoft Docs
description: Learn about the latest auto update feature for apps.
ms.date: 06/30/2022
author: angela21k
ms.author: angelakim
ms.reviewer: jdaly
suite: powerapps
ms.topic: article
ms.subservice: dataverse-developer
search.audienceType: 
  - developer
search.app: 
  - PowerApps
contributors: 
  - JimDaly
---

# Auto App Updates

App Auto Update is a new feature in public preview that allows automatic updates of applications installed through AppSource. This feature helps both publishers and customers keep software up to date in a simple and controlled way with minimal administrative overhead.  

Automatic updates in the preview will be limited to:  

- **Explicit tenant admin opt-in**: Tenant admin user must opt-in from the Power Platform Admin center to enable the feature. 

- **Pre-approved publishers**: Tenant admin user must indicate which publishers are permitted to automatically update apps in their environment once opted-in from the Power Platform Admin center.

- **Dark hours only**: To further minimize impact, automatic updates will only happen during dark hours defined by either the customer or at geo level.  

## Enabling Auto App Update  

> [!NOTE]
> Publishers do not require additional action to enable automatic updates for their apps. Only tenant admin users are required to act if they want to opt-in to this feature for select publishers.

1. Log into the Power Platform Admin center as an admin user. From the Environments page, select an environment and click on **Settings**.

   :::image type="content" source="media/auto-app-update-0.jpg" alt-text="Power Platform Admin Center Environment":::

1. From the environment settings page, under the **Updates** section, click to open the **App Update Settings** page.  

   :::image type="content" source="media/auto-app-update-1.jpg" alt-text="Power Platform Admin Center Environment Settings":::

1. Toggle the configurator to **'On'** to opt-in to the feature.  From the drop-down list of publishers, select for which publishers you want to automatically update apps.

   :::image type="content" source="media/auto-app-update-2.jpg" alt-text="Configure App Update Settings":::

1. Click **Save** to keep your changes.


## Monitoring Opt-in Environments in ISV Studio 

As a publisher with access to ISV Studio, you can view details about your automatic updates and opt-in rates.
 
1. Login to ISV Studio. From the navigation menu, click on **Analytics** and **Published apps.**
Graphical user interface, application

   :::image type="content" source="media/auto-app-update-3.jpg" alt-text="ISV Studio Published Apps":::
 
1. Select a specific app and click the **Auto Updates** tab to view opt-in rates for publishers and environments, which organizations have opted out, as well as a detailed list of version history.

   :::image type="content" source="media/auto-app-update-4.png" alt-text="ISV Studio Auto Updates":::

1. From the Version Update History table, click **View Details** to view details about the deployment status by region.

   :::image type="content" source="media/auto-app-update-5.jpg" alt-text="ISV Studio Version Update Details":::

> [!NOTE]
> The Cancel Deployment button will cancel automatic updates for any regions with release status in progress or to be scheduled.

### See also

[Introduction to ISV Studio for the Power Platform](isv-app-management.md)  
[Home page](isv-app-management-homepage.md)<br/> 
[App page](isv-app-management-apppage.md)<br/> 
[AppSource checker](isv-app-management-appsource-checker.md)<br/> 
[Connector Certification](isv-app-management-certification.md)


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
