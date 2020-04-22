---
title: Overview of Regional Emergency Response sample solution for Power Platform | Microsoft Docs
description: Provides an overview of Regional Emergency Response Solution.
author: KumarVivek
manager: annbe
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/15/2020
ms.author: kvivek
ms.reviewer: kvivek
searchScope:
  - PowerApps
---
# Regional Emergency Response - Power Platform sample solution

The Regional Emergency Response sample solution provides a set of capabilities for regional medical organizations to collect and manage data for situational awareness of available beds and supplies, COVID-19 related patients, staffing, and pending discharges from all the hospitals in a state or region.

The main components of the Hospital Emergency Response solution are:

- **Web app for regional organization admins**: Use the app to manage the master data for each parent medical organization in the state or region, where each parent medical organization has one or more hospital systems that report data to the regional medical organization. The regional organization admin can add and manage admin users for each parent organization so that the latter can can use a web portal to report data for their medical organization.

- **Web portal for parent organization admins and users**: Parent organization admins can use the web portal to quickly add and manage users in their organization and also add and manage master data for their hospital systems including regions and facilities. The web portal is also used by healthcare workers to quickly view, add and manage data related to bed capacity, staff, equipments supplies and COVID-19 patients.

- **Dashboards for healthcare decision makers**: Use dashboards to quickly view important data and metrics that will help you in efficient decision making.
    - Regional organization admins can view the dashboards in their Power BI tenant.
    - Parent organization admins can view the dashboards in the web portal.

## Licensing requirements

- Power Apps license
- Power BI license

Contact your local Microsoft account representative for questions related to licensing.

See also: [Licensing overview for Power Platform](https://docs.microsoft.com/power-platform/admin/pricing-billing-skus)

## Start here

|Task | Target audience|See|
|--|--|--|
|Deploy the sample solution and set up users and security|Regional organization IT admin|[Deploy the Regional Hospital Emergency Response solution](deploy.md)|
|Use the admin app to configure and manage master data and create/manage portal users|Regional organization Business admin|[Configure Regional Hospital Emergency Response solution](configure.md#configure-and-manage-master-data-for-your-organization)|
|Use the portal to add/manage portals users for their hospitals, set up and manage master data for their hospitals, and view dashboard for insights and metrics.|Parent organization Business admin|[Administer the Regional Emergency Response portal](portals-admin-reporting.md)
|Use the admin app to track feedback from mobile app|Business/IT admin|[View and manage app feedback](configure-data-reporting.md#view-and-manage-app-feedback)|
|Use dashboards for insights and decision making|Business admin|[View Common Data Service dashboards](configure-data-reporting.md#view-common-data-service-dashboards)<br/><br/>[View Power BI dashboard](configure-data-reporting.md#view-power-bi-dashboard)|


## Report issues

To report an issue with the Regional Emergency Response sample app, visit <https://aka.ms/rer-issues>.


### Disclaimer 

This app is a sample and may be used with Microsoft Power Platform for dissemination of reference information only. This app is not intended or made available for use as a medical device, clinical support, diagnostic tool, or other technology intended to be used in the diagnosis, cure, mitigation, treatment, or prevention of disease or other conditions, and no license or right is granted by Microsoft to use this app for such purposes. This app is not designed or intended to be a substitute for professional medical advice, diagnosis, treatment, or judgement and should not be used as such. Customer bears the sole risk and responsibility for any use of this app. Microsoft does not warrant that the app or any materials provided in connection therewith will be sufficient for any medical purposes or meet the health or medical requirements of any person. 

Sample data included in this app are for illustration only and are fictitious.  No real association is intended or inferred.
