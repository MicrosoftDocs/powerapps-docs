---
title: Configure Regional Hospital Emergency Response app | Microsoft Docs
description: Provides provides detailed instructions for hospital IT admins to deploy and configure the sample app for their organization.
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
# Configure Regional Hospital Emergency Response app

This guide is meant for business admins in regional medical organizations to use the admin app (model-driven app) to perform the following activities:

-   Create and manage master data in entities required for the solution

-   Create and manage portal users (contacts). These users are typically the admins from parent medical organizations that manage one or more hospital systems. These parent medical organization admins use the portal to add and manage users from their hospital system, add and manage data for their hospitals, and view embedded Power BI dashboards for the ir parenet organizations.

## Prerequisites

-   Ensure you have the appropriate security role and access to the admin app (model-driven app). Contact your IT Admin if you are unable to access or use the admin app.

-   Ensure you have access to the sample data. The sample data is available in the deployment package under the **SampleData** folder.

## Add and manage master data

When you sign into the model-driven app, you will see the entities in the left pane where you need to populate the master data. Select the entity in the left navigation pane to view or manage the data.

> [!div class="mx-imgBorder"] 
> ![Populate the master data](media/config-entities-master-data.png "Populate the master data")

-   **Hierarchy area**: Entities in this area can be added either by importing data from the sample data files or manually. The entities under the **Hierarchy** area are listed in the order you should populate data. Also, parent org admins (hospital admins) can view and manage data under the following entities for their hospital from the portal: **Systems**, **Regions**, and **Facilities**.

    > [!NOTE]
    > We provide name and FIPS code for all the counties in the Washington state as sample data that you can import. To obtain data for counties in other states, visit <https://www.census.gov/geographies/reference-files/2018/demo/popest/2018-fips.html>

-   **Admin Entities** area: Data in the **Supplies** entity is added by importing data from the sample data file. You can manually add and manage supplies data later.

-   **Customers** area: You use the **Portal Users** entity to add and manage portal users. More information: [Manage portal users](#manage-portal-users)

There are two ways in which you can add master data to entities in the app:

1.  Import data using the sample data files.

2.  Manually configure and manage the data.

## Import data using sample files

The sample data files are available in the deployment package (.zip). When you extract the .zip file, the sample data files are available under the **SampleData** folder.

> [!NOTE]
> We provide name and FIPS code for all the counties in the Washington state as sample data that you can import. You should import the **Counties** data using the sample data file into your system before proceeding with importing or managing data in any other entities.

To obtain data about counties in other states, visit <https://www.census.gov/geographies/reference-files/2018/demo/popest/2018-fips.html>

Under the **SampleData** folder, the files are named to denote the sequence in which data should be imported into your app. Otherwise, data import will fail.

-   0_Supplies.xlsx

-   1_Counties.xlsx

-   2_Regional Organization.xlsx

-   3_Parent Organizations.xlsx

-   4_Systems.xlsx

-   5_Regions.xlsx

-   6_Facilities.xlsx

### How to load data from data files

To load sample data from the Excel file to an entity: 

1.  In the left navigation pane of the admin app, select select an entity. For example, select **Parent Org**. 

2.  Select **Import from Excel** to select the data file. 

       > [!div class="mx-imgBorder"] 
       > ![Import from Excel](media/config-import-excel.png "Import from Excel")

3.  Browse to the **SampleData** folder and select the **2_ParentOrgs.xlsx** file and proceed with the wizard steps to import the data.  

4.  After the sample data is imported, you will see the imported records in the entity:

       > [!div class="mx-imgBorder"] 
       > ![Imported records in entity](media/config-imported-records.png "Imported records in entity")

## Manually configure and manage master data for your organization

Admins can use the model-driven app in [Power Apps](https://make.powerapps.com) to create and manage master data for their organization. This data is required for the Emergency Response Solution to work.

To start, you must add master data in the following entities:

-   Supplies

-   Counties

-   Regional Org

-   Parent Orgs

-   Hospital systems managed by each parent org

-   Regions for each hospital system

-   Facilities within each region of a hospital system

> [!IMPORTANT]
> Use the sample data files to import data for **Supplies** and **Counties** entity.

### Regional Org data

This is the regional network organization that will deploy the solution and manage data from various parent organizations.

To create a record:

1.  Select **Regional Org** in the left pane and select **New**.

    > [!div class="mx-imgBorder"] 
    > ![Regional organization data](media/config-region-org.png "Regional organization data")

2.  In the **New Regional Organization** page, specify the organization name:

    > [!div class="mx-imgBorder"] 
    > ![New regional organization](media/config-new-region-org.png "New regional organization")

3.  Select **Save & Close.** The newly created record will be available in the **Regional Org** list.

To edit the record, select the record, update the values as required, and select **Save & Close.**

### Parent Org data

The **Parent Org** entity stores the parent organization that will be using the portals set up by regional org to view and manage data related to parent organization’s hospital systems.

To create a record:

1.  Select **Parent Org** in the left pane and select **New**.

2.  In the **New Parent Organization** page, specify appropriate values:

     > [!div class="mx-imgBorder"] 
     > ![New parent organization](media/config-new-parent-org.png "New parent organization")

    | **Field**                |**Description** |
    |--------------------------|------------------------------------------------------|
    | Regional Organization    | Select a regional org. This list is populated based on the **Regional Org** data you have created earlier. |
    | Parent Organization Name | Specify the parent organization name.      |
    | Description              | Type an optional description.        |
    | Effective Start Data     | Type start date and time for this parent organization.    |
    | Effective End Date       | Type end date and time for this parent organization.         |

3.  Select **Save & Close.** The newly created record will be available in the **Parent Org** list.

To edit the record, select the record, update the values as required, and select **Save & Close.**

### Systems data

The **Systems** entity lets you create and manage entries for Hospital Systems. This allows you to manage multiple hospital systems within the same parent organization.

To create a record:

1.  Select **Systems** in the left pane and select **New**.

2.  In the **New System** page, specify appropriate values:

    > [!div class="mx-imgBorder"] 
    > ![Create systems data](media/config-system-data.png "Create systems data")

    | **Field**           | **Description**        |
    |---------------------|---------------------------------------|
    | System Name         | Type a name for your Hospital.    |
    | Parent Organization | Select a parent org to associate to. This list is populated based on the **Parent Org** data you have created earlier. |
    | Description         | Type an optional description.    |

3.  Select **Save & Close.** The newly created record will be available in the **Systems** list.

To edit the record, select the record, update the values as required, and select **Save & Close.**

### Regions data

The **Regions** entity lets you manage the geographical regions for your hospital systems.

To create a record:

1.  Select **Regions** in the left pane and select **New**.

2.  In the **New Region** page, specify appropriate values:

    > [!div class="mx-imgBorder"] 
    > ![Create new region](media/config-create-region.png "Create new region")

    | **Field**   | **Description**                                  |
    |-------------|---------------------------|
    | System      | Select a hospital system this region is associated with. This list is populated based on the **Systems** data you have created earlier. |
    | Region Name | Type the region name. For example, Seattle.  |
    | Description | Type an optional description. 

3.  Select **Save & Close.** The newly created record will be available in the **Regions** list.

To edit the record, select the record, update the values as required, and select **Save & Close.**

### Facilities data

The **Facilities** entity lets you manage the hospital locations within each region. For example, **Redmond** and **Bellevue** facilities within the **Seattle** region.

To create a record:

1.  Select **Facilities** in the left pane and select **New.**

2.  In the **New Facility** page, specify appropriate values:

    > [!div class="mx-imgBorder"] 
    > ![Create new facility](media/config-new-facility.png "Create new facility")

    | **Field**                    | **Description**            |
    |------------------------------|---------------------------------------------------|
    | Region    | Select a region this facility is associated with. This list is populated based on the **Regions** data you have created earlier.          |
    | Facility Name | Type the facility name.                 |
    | DOH Number    | Type Department of Health number for this facility.     |
    | Follows Droplet Protocol     | Indicates whether the facility follows Droplet Precautions for patients known or suspected to be infected with pathogens transmitted by respiratory droplets, such as in COVID-19 cases. Select **Yes** or **No**. |
    | Description    | Type an optional description.              |
    | Effective Start Data         | Type start date and time for this facility.    |
    | Licensed Bed Capacity    | Type the total licensed bed capacity.    |
    | AIIR Acute Care Capacity     | Type the total number of Acute care beds in AIIR (Airborne Infection Isolation Room).     |
    | AIIR ICU Capacity            | Type the total number of ICU beds in AIIR.       |
    | Total Vents       | Type the number of total vents in the facility.   |
    | Effective End Date           | Type end date and time for this facility.       |
    | Surge Bed Capacity           | Type the number of surge beds the facility can have. Surge beds are those that can be staffed above and beyond licensed bed capacity if patients need to be admitted.                                              |
    | Non-AIIR Acute Care Capacity | Type the total number of Acute care beds in non- AIIR (Airborne Infection Isolation Room).|
    | Non-AIIR ICU Capacity        | Type the total number of ICU beds in non-AIIR.              |
    | Facility Address    | Type the Street, City, County, State, Zip code, Latitude, and Longitude for the facility.   |

3.  Select **Save & Close.** The newly created record will be available in the **Facilities** list.

To edit the record, select the record, update the values as required, and select **Save & Close.**

You can also view and manage the associated **Census**, **COVID**, **Equipment**, **Staffing**, and **Supplies** data entered by the parent organizations for a facility by opening a facility record, and using the respective tabs in the record.

> [!div class="mx-imgBorder"] 
> ![Open a facility record](media/config-facility-record.png "Open a facility record")

## Manage portal users

Use the **Portal Users** entity to add and manage portal users. These portal users are the admins from the various parent organizations hospitals who enter and manage data in the Regional Emergency Response solution for their hospitals and also manage other admin, frontline, or report viewers using the portals.

## Create a portal user

1.  Sign into the admin app.

2.  In the left pane, select **Portal Users**. You see a list of portal users, if they are already added by other admins in your org. Selecting a user will open the details about the user.

3.  Select **New** to create a new portal user. On the **New Contact** page, specify appropriate values

    > [!div class="mx-imgBorder"] 
    > ![Create a portal user](media/config-portal-user.png "Create a portal user")

    | **Field**           | **Description**  |
    |---------------------|-------------------|
    | First Name          | First name of the user.                           |
    | Last Name           | Last name of the user  |
    | Email     | Email of the user where the invitation will be sent.    |
    | Parent Organization | Select a parent organization that this portal user will be associated with. This ensures that the user has access only to the hospital systems data under the selected parent org. If you don’t specify a parent org for the user, she/she will have access to data for all the parent orgs under the regional org. |
    | Hospital System     | Select a hospital for this user. |
    | Region  | Select a region for this user.  |
    | Facility            | Select a facility for this user. |

4.  Save the record. On saving the record, the **Web Roles** area becomes available. Select **Add Existing Web Role.**

5.  In the lookup records page, press enter to displays the existing web roles.

## Report issues

To report an issue with the Regional Emergency Response sample app, visit <https://aka.ms/rer-issues>.