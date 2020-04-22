---
title: Administer the Regional Emergency Response portal | Microsoft Docs
description: Learn how to configure the Regional Hospital Emergency Response portal.
author: tapanm-msft
manager: kvivek
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/21/2020
ms.author: tapanm
ms.reviewer: tapanm
searchScope:
  - PowerApps
---
# Administer the Regional Emergency Response portal

Hospital staff are challenged to meet an increase in number of patients while managing supply chain during emergency. By using the Regional Emergency Response
portal, administrators can quickly view and update data related to **Users**, **Systems**, **Regions**, and **Facilities**. Stakeholders can view the published insights through dashboards for current status of the health care system and take actions.

## Portal at a glance

Browse to the Power Apps portal to add, edit or delete **Users**, **Systems**, **Regions**, and **Facilities**. The following section walks you through what you can
access, submit, or update as the administrator of the portal.

![Portal at glance](media/portal-at-glance.png)

You can use latest mobile devices and web browsers when using Regional Emergency Response portal except Apple iPad.

## Portal components

Read [Use the Regional Emergency Response portal](portals-user.md) to learn about portal components.

[!include[cc-getting-started](includes/cc-getting-started.md)]

> [!NOTE] 
> Administrators must select **Hospital System, Region** and **Facility** and select **Next** to view the administrative and dashboard settings. When using the portal only for administrative actions such as user management or dashboard reviews, you can select any location. However, if you want to use user components such as **Staff** or **Equipment**, ensure you have selected the correct location.

[!include[cc-manage-user-profile](includes/cc-manage-user-profile.md)]

## Administrative Tasks

You can view all administrative options available to you after selecting **Administration** on home screen:

![Portal Administration](media/portal-admin-screen.png)

### Administrative tasks and description

| **Option name** | **Description**                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------|
| [Add Users](#add-users)       | Create, edit, or deactivate portal users.                                                         |
| [Add System](#add-system)      | Create, edit, or delete systems. |
| [Add Region](#add-region-1)      | Create or delete regions.                              |
| [Add Facility](#add-facility)    | Create, edit, or delete facilities.                        |

### Add Users

Go to **Add Users** to create new users that can administer the portal, view the dashboards, or use the portal as the frontline staff:

![Add users](media/portal-admin-add-user.png)

You can also [view user details](#view-user-details), [change user role](#change-role-for-a-user) and [deactivate user](#deactivate-a-user) from **Add Users**.

#### Search user details

Enter text in the search box to view filtered results for searched users. Wildcard (**\***) search is enabled and you can search for the following fields:

- Full Name

- Email

- Mobile Phone

- Parent Organization

You can use wildcard search and partial terms to view results, including phone numbers.

For example, if you want to search for a user with **Full Name** as **Delores Vasquez**, you can use following sample strings in search:

- Del\*

- \*Del

- Del\*va

To search for **Mobile Phone**, you can use similar text with wildcard replacing characters with numbers.

#### Create User

To create users, select **Create User** button when in **Add Users** form. And then, enter the new user details in the form:

![Create user](media/portal-admin-create-user.png)

Enter **First Name**, **Last Name**, **Email, and **Mobile Phone** and then select a role for the user.

The following section walks through each one of the roles with details of what the member of the role can do:

##### Organizational HealthCare Worker

A Frontline Worker is an employee of a hospital system such as a registered nurse. Frontline Worker works within one or more facilities. The frontline worker collects data across the following areas:

- Bed capacity

- Staff

- Equipment

- Supplies

- COVID-19 Stats

##### Report Viewer

A Report Viewer role is for the users that can view the dashboards available on this portal. Members of Report Viewer role can view the following dashboards:

- System at a glance

- County

- Facility Details

- COVID Patient Details

- Bed Management

- Equipment Details

- Supplies on Hand Details

##### Parent Organization Administrator

A Parent Organization Administrator can create users that can access the organization details using this portal.

Members of Parent Organization Administrator role can:

- Create new users and add them to the **Organizational HealthCare Worker, Report Viewer**, or the **Parent Organization Administrator** roles.

- Change metadata for the organization with:

    - Addition, updates, and deletion of **System**

    - Addition and deletion of **Region**

    - Addition and deletion of **Facility**

#### View user details

You can view user details by selecting the drop-down for the user and then selecting **View details**:

![View user options](media/portal-user-view-user-options.png)

##### Change role for a user

You can add or remove user roles from the user details:

![View user details](media/portal-user-view-details.png)

#### Deactivate a user

Select **Deactivate** from the user drop-down to deactivate a user account:

![View user options](media/portal-user-view-user-options.png)

Deactivated user is no longer shown in the list of users on **Add Users** page.

### Add System

You can add, update, or delete a **System** using the **Add System** form. When you select **Add System**, you can see all existing **Hospital Systems**:

![Add system](media/portal-add-system.png)

#### Search existing systems

Enter text in search box to search for system and filter the list of systems on the form. You can use wildcard search (**\***) combined with text characters for
**System Name** and **Description** fields.

#### View System Details

To view details of a system, select the drop-down menu for a system and then select **View Details**:

![View System](media/portal-view-system-details.png)

System Details page shows **Parent Organization, System Name**, **Description**, and **Regions** within the system:

![System details](media/portal-system-details.png)

You can update a system’s **System Name** and the **Description** fields in the respective text boxes.

##### Add Region

Use the **Add Region** button to add a region to the current system. When you select **Add Region**, you can add region details such as **Region Name** and
**Description**:

![Add region](media/portal-admin-add-region.png)

You can change **System** in the drop-down before you add a region. However, prefer to add a region to a system by first viewing the system that you want to add region to. This is because once you select **Submit**, if the system you selected is different from the details page you have open, you can’t see the region listed in the region section.

#### Create system

To create a system, select **Create**, enter *System Name* and *Description*:

![Create system](media/portal-admin-create-system.png)

#### Delete System

To delete a system, select the drop-down menu and then select **Delete** option:

![Delete system](media/portal-view-system-details.png)

Select **Delete** to delete a system record. You're prompted confirming deletion before the system gets deleted:

![Delete confirm](media/portal-delete-system-confirm.png)

### Add Region

You can add or delete a **Region** using the **Add Region** form. When you select **Add Region**, you can see all existing **Hospital Systems**:

![Add region](media/portal-add-region.png)

#### Search existing regions

Enter text in search box to search for region and filter the list of regions on the form. You can use wildcard search (**\***) combined with text characters for **Region Name, System**, and **Description** fields.

#### Create Region

To create a region, select the **Create** button, select a **System**, and then enter **Region Name** and **Description:**

![Create region](media/portal-admin-create-region.png)

#### Delete Region

To delete a region, select the drop-down menu and then select **Delete** option:

![Delete region](media/portal-admin-delete-region.png)

You're prompted confirming deletion before the region gets deleted:

![Delete region confirm](media/portal-admin-delete-region-confirm.png)

### Add Facility

You can add or delete a **Facility** using the **Add Facility** form. When you select **Add Facility**, you can see all existing **Facilities** with region,
county, and other details:

![Delete confirm](media/portal-admin-add-facility.png)

#### Search existing facilities

Enter text in search box to search for system and filter the list of facilities on the form. You can use wildcard search (**\***) combined with text characters for **Facility Name, Region, and **County Name** fields.

#### Create Facility

To create a facility, select the **Create** button:

![Create facility](media/portal-admin-create-facility.png)

##### Options and description

| **Option name**                                | **Description**                                                                                                                                                                                            |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Facility Name                                  | Name of the facility.                                                                                                                                                                                      |
| Region                                         | Select a region this facility is associated with.                                                                                                                                                          |
| Licensed Beds Total Capacity                   | Total licensed bed capacity, in number format.                                                                                                                                                             |
| ICU Beds (AIIR Room) Total Capacity            | Number of total ICU beds in AIIR (Airborne Infect Isolation Room).                                                                                                                                         |
| Acute Care Beds (AIIR Room) Total Capacity     | Total Acute Care beds (AIIR) capacity, in number format.                                                                                                                                                   |
| Ventilators Total Capacity                     | Total ventilator capacity, in number format.                                                                                                                                                               |
| Supplies List | Select [Supplies List](#supplies-list-for-a-facility) to choose items from the available supplies available at the facility. |
| DOH Number                                     | The Department of Health number for this facility.                                                                                                                                                         |
| Follows Droplet Protocol                       | Select **Yes**/**No**. Relates to the facility following Droplet Precautions for patients known or suspected to be infected with pathogens transmitted by respiratory droplets, such as in COVID-19 cases. |
| Surge Beds Total Capacity                      | Total surge beds capacity, in number format. Surge beds are those that can be staffed above and beyond licensed bed capacity if patients need to be admitted                                               |
| ICU Beds (non-AIIR Room) Total Capacity        | Number of total ICU beds (non-AIIR).                                                                                                                                                                       |
| Acute Care Beds (non-AIIR Room) Total Capacity | Total Acute Care beds (non-AIIR) capacity, in number format.                                                                                                                                               |
| Total Mortuary Capacity | Total mortuary capacity for the facility. **Note**: When set to at least 1, causes field *Number of decedent accommodations currently in use* to be available for the facility's **Bed capacity** form.
| Facility Address                               | Street, City, County, State, and Zip code for the facility location.                                                                                                                                        |
##### Supplies list for a facility

When you select **Supplies List**, you can select individual supply and **Save** the list to associate the available supplies for the facility:

![Supplies list for facility](media/portal-admin-add-facility-supplies.png)

#### Delete Facility

To delete a facility, select the drop-down menu and then select **Delete**
option:

![Delete facility](media/portal-admin-delete-facility.png)

You're prompted confirming deletion before the facility gets deleted:

![Delete facility confirm](media/portal-admin-delete-facility-confirm.png)

#### Edit Facility

To delete a facility, select the drop-down menu and then select **Edit** option:

![Edit facility](media/portal-admin-delete-facility.png)

Update the fields and select **Submit** to save the changes.

## Get Insights

If you are a member of **Report Viewer** role, you’ll see option to view **Dashboards**:

![Get insights](media/portal-admin-get-insights.png)

### Dashboards overview

Dashboards are available for the following insights:

- [System at a glance](#system-at-a-glance)

- [COVID-19 patient details](#covid-19-patient-details)

- [Bed capacity details](#bed-capacity-details)

- [Equipment details](#equipment-details)

- [Supplies details](#equipment-details)

#### Working with reports in Power BI

Before you begin review of available dashboards, get familiar with general report viewing concepts and guidelines:

- Selecting the information icon (i) in any of the summarized area takes you to the respective details page for the area.

- You can also do other actions on reports such as filter and sort data, export the report to PDF and PowerPoint, add a spotlight, and so on. For detailed information about report features in Power BI, see [Reports in Power BI](https://docs.microsoft.com/power-bi/consumer/end-user-reports).

- The most recent or last updated columns in some of these reports show the date and time when the data was last refreshed. It's also easy to identify the freshness by viewing the color of the date and time values in these columns:

- **Black:** Data is refreshed less than 20 hours ago

- **Gray:** Data is refreshed 20 - 24 hours ago

- **Red:** Data is refreshed more than 24 hours ago

### System at a glance

View entire **Hospital System** related statistics in one view with **System at a glance** dashboard:

![Dashboard](media/portal-admin-powerbi-reports.png)

The dashboard displays summary for the following:

- **COVID-19 stats**: View COVID-19 patient summary in numbers with total patients, patients under investigation, positive and intubated patients.

- **Bed capacity**: View the summary data with **Availability** and **Occupancy** for licensed, ICU, Acute, and Surge categories.

- **Beds Availability by County**: View bed availability with total number of beds, ICU/Acute/Surge bed availability and total of all bed availability across all counties.

- **Supplies**: View supply information with days-on-hand for each separately.

- **Equipment**: View ventilators and equipment summary numbers with availability, in-use and needed.

### COVID-19 patient details

View COVID-19 related patient details such as summary of COVID PUIs, positives, intubations. The dashboard also shows details on a per-county basis at bottom.

You can also view counties in map and the counties are color coded for segregation. A graph on the bottom right in dashboard shows COVID-19 positives and PUIs with timelines explaining the recent and past trends:

![patient details](media/portal-admin-powerbi-patients.png)

#### Map

Hover over a county inside the map to see the county-specific COVID-19 PUIs, positives, and intubation numbers:

![Patient map](media/portal-admin-powerbi-map.png)

Similarly, you can hover over the timeline chart to view date-specific numbers in tooltip as you move across dates.

### Bed capacity details

View bed-related insights such as bed availability with licensed, acute, AIIR/non-AAIR, surge, and ICU numbers. You can also view the details in tabular format at bottom with per-county bed data and in percentage format. The map is color coded for counties with lighter color for lower numbers and increasing in darkness as the number increases. The chart on bottom right shows occupancy differences based on dates for trend analysis:

![Bed capacity](media/portal-admin-powerbi-bed-capacity.png)

#### Map

When you hover over map area and point to a county, you can see the county-related information:

![Bed capacity map](media/portal-admin-powerbi-map1.png)

Similarly, you can hover over the timeline chart to view date-specific numbers in tooltip as you move across dates.

### Equipment details

View equipment details on a per-county basis such as ventilators availability and consumption with **Equipment details** dashboard:

![Equipment details](media/portal-admin-powerbi-equipment.png)

You can see the total amount of equipment availability on top left and detailed table on bottom left. The map shows county-specific equipment data with lighter
color with lesser and darker color with higher requirement numbers.

The timeline chart on bottom right shows equipment insights for trend analysis across dates.

#### Map

When you hover over map area and point to a county, you can see the county-related information:

![Equipment map](media/portal-admin-powerbi-equipment-map.png)

Similarly, you can hover over the timeline chart to view date-specific numbers in tooltip as you move across dates.

### Supply details

View supply details on a per-county basis such as ventilators availability and consumption with **Supply details** dashboard:

![Supply details](media/portal-admin-powerbi-supply.png)

You can see the supply details on the left based on **Health System,** map on the right and chart format supply break-up at the bottom.

#### Map

When you hover over map area and point to a county, you can see the county-related information:

![Supply map](media/portal-admin-powerbi-supply-map.png)

Similarly, you can hover over the timeline chart to view date-specific numbers in tooltip as you move across dates.

## General portal options

[!include[cc-general-options](includes/cc-general-options.md)]

## Report issues

To report an issue with the Regional Emergency Response sample app, visit <https://aka.ms/rer-issues>.
