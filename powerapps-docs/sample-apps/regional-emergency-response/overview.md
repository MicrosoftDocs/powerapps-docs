---
title: Overview of Regional Government Emergency Response and Monitoring solution for Power Platform | Microsoft Docs
description: Provides an overview of Regional Government Emergency Response and Monitoring solution for state and local governments.
author: pankajarora-msft
manager: annbe
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/06/2020
ms.author: pankar
ms.reviewer: kvivek
---
# Regional Government Emergency Response and Monitoring - Power Platform solution for state and local governments

The Regional Government Emergency Response and Monitoring solution provides a set of capabilities for state and local governments to collect and visualize health system data from all the parent organizations and associated hospitals in their network or region to establish situational awareness during emergency responses. The data includes information about available beds, supplies, equipment, COVID-19 patients, and staffing.

The main components of the Regional Government Emergency Response and Monitoring solution are:

- **Web app for regional organization admins**: Use the app to manage the master data for each parent medical organization in the state or region, where each parent medical organization has one or more hospital systems that report data to the regional medical organization. The regional organization admin can add and manage admin users for each parent organization so that the latter can use a web portal to report data for their medical organization.

- **Web portal for parent organization admins and users**: Parent organization admins can use the web portal to quickly add and manage users in their organization and also add and manage master data for their hospital systems including regions and facilities. The web portal is also used by healthcare workers to quickly view, add, and manage data related to bed capacity, staff, equipment, supplies, and COVID-19 patients.

- **Dashboards for healthcare decision makers**: Use dashboards to quickly view important data and metrics that will help you in efficient decision making.
    - Regional organization admins can view the dashboard in their Power BI tenant.
    - Parent organization users can view the dashboard in the web portal.

## Demo: Quick overview

Watch a quick overview of the solution.

<br/>

> [!VIDEO https://www.youtube.com/embed/4WaniuC7pWs]

## Licensing requirements

- Power Apps plan along with Power Apps portal capacity
- Power BI Premium or Pro license

Contact your local Microsoft account representative for questions related to licensing as per your requirements.

See also: 
- [Licensing overview for Power Platform](/power-platform/admin/pricing-billing-skus)
- [Power Apps for US Government](/power-platform/admin/powerapps-us-government)
- [Power BI for US Government](/power-bi/service-govus-overview)

## Start here

|Task | Target audience|See|
|--|--|--|
|Download and deploy the sample solution and set up users and security|Regional organization IT admin|[Deploy the Regional Government Emergency Response and Monitoring solution](deploy.md)|
|Upgrade the sample solution (for orgs with existing installation of the solution)|Regional organization IT admin|[Upgrade the Regional Government Emergency Response and Monitoring solution](upgrade.md)|
|Use the admin app to configure master data, create/manage portal users, and view dashboard|Regional organization business admin|[Use the admin app and dashboard](configure.md)|
|Use the portal to add/manage portals users for their hospitals, set up and manage master data for their hospitals, and view dashboard for insights and metrics.|Parent organization business admin|[Administer the Regional Government Emergency Response and Monitoring portal](portals-admin-reporting.md)|
|Use the portal to quickly view and add data for bed capacity, staffing, equipment, supplies, and COVID-19 patients.|Healthcare workers|[Use the Regional Government Emergency Response and Monitoring portal](portals-user.md)|


## Issues and feedback

- To report an issue with the Regional Government Emergency Response and Monitoring solution, visit <https://aka.ms/rer-issues>.

- For feedback about the Regional Government Emergency Response and Monitoring solution, visit <https://aka.ms/rer-feedback>.


### Disclaimer

This app is a sample and may be used with Microsoft Power Platform for dissemination of reference information only. This app is not intended or made available for use as a medical device, clinical support, diagnostic tool, or other technology intended to be used in the diagnosis, cure, mitigation, treatment, or prevention of disease or other conditions, and no license or right is granted by Microsoft to use this app for such purposes. This app is not designed or intended to be a substitute for professional medical advice, diagnosis, treatment, or judgement and should not be used as such. Customer bears the sole risk and responsibility for any use of this app. Microsoft does not warrant that the app or any materials provided in connection therewith will be sufficient for any medical purposes or meet the health or medical requirements of any person. Sample data included in this app are for illustration only and are fictitious. No real association is intended or inferred.


[!INCLUDE[footer-include](../../includes/footer-banner.md)]