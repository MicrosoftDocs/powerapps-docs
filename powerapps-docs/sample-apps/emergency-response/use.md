---
title: Use the Hospital Emergency Response mobile app | Microsoft Docs
description: Walk-through different apps and components for the users of the Hospital Emergency Response sample app template 
author: pankajarora-msft
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 05/13/2020
ms.author: pankar
ms.reviewer: tapanm
searchScope:
  - PowerApps
---

# Use the Hospital Emergency Response mobile app

Hospital staff are challenged to meet an increase in number of
patients while managing supply chain during emergency. By using the Hospital Emergency Response mobile app, frontline workers can quickly view and add data for ventilators, staffing, pending discharges, and COVID-19 related patients.

## Prerequisites

To get started with the mobile app, you need to download the Power Apps Mobile on your
device using the device's app store.

- **Download** the [**Power Apps Mobile**](https://powerapps.microsoft.com/downloads)
    - For **Apple** devices with iOS such as iPhone and iPad, use [**App store**](https://aka.ms/powerappsios)
    - For **Android** devices, use [**Google Play**](https://aka.ms/powerappsandroid)
- Ensure your organization has deployed and configured the Hospital Emergency Response mobile app as explained in [Deploy and configure the app](deploy-configure.md).

After you install the Power Apps Mobile, open the app from your device and
sign in with your company's Azure Active Directory account. You can view all
apps shared to you by your organization once you sign in. For more information, see [Power Apps mobile device sign
in](https://docs.microsoft.com/powerapps/user/run-app-client#open-power-apps-and-sign-in).

## Demo: Use the Hospital Emergency Response mobile app

Watch how to use the Hospital Emergency Response mobile app.

<br/>

> [!VIDEO https://www.youtube.com/embed/H1u6SYt3UsQ]

## Hospital Emergency Response mobile app

![Hospital Emergency Response mobile app](media/use/app-launcher.png)

The Hospital Emergency Response mobile app has a modular structure with different apps as applicable to your role. Open the Hospital Emergency Response mobile app from the Power Apps Mobile, select your **Hospital system**, **Region, Facility**, and select **Next** to get started.

> [!NOTE]
> When you launch the Hospital Emergency Response mobile app or any of
its components for the *first time*, you will be asked for your consent to allow the app to read your *Office 365 Users* profile and your *Location*. You must select **Allow** before you can start using the selected app. For more information, see [give consent](https://docs.microsoft.com/powerapps/user/run-app-client#give-consent).

## App components

![Hospital Emergency Response mobile app components](media/use/app-components.png)

The Hospital Emergency Response sample solution app consists of multiple apps for enhanced user experience. Depending on your role, you may see one or more components in the **Hospital Emergency Response mobile app**.

- **Bed capacity**
    <br> Collect bed information such as licensed beds, ICU beds, pediatric ICU/Acute Care beds, and other bed capacity data.

- **COVID-19 stats**
    <br> Collect status on how many patients are under investigation for COVID-19 and how many tested positive.

- **Equipment**
    <br> Track equipment information such as ventilators, NIPPV, and PAPR.

- **Staff**
    <br> Collect number of patients and RN status information such as partners, assigned, requested, and unassigned.

- **Supplies**
    <br> Track key supplies to track, manage, and forecast inventory more
    effectively. ​

- **Staffing needs**
    <br> Collect requests for personnel by department, role, and urgency.

- **Discharge planning**
    <br> Collect status and projections on ​patient discharges.

- **Dashboard**
    <br> View the Power BI dashboard for insights and decision making.

> [!NOTE]
> By default, you can track information in the following apps at a *location* level: **COVID-19 stats**, **Equipment**, and **Staff**. In rest of the apps, you can track information at the *facility* level by default. Your admin can change the default tracking level, if required. More information: [Manage tracking level for mobile apps](configure-data-reporting.md#manage-tracking-level-for-mobile-apps)

## Bed capacity

![Bed capacity](media/use/bed-capacity.png)

Submit bed-related information such as licensed beds, ICU (AIIR/non-AIIR) beds, Acute Care (AIIR/non-AIIR) beds and whether the selected facility is staffed to full license bed capacity.

Select **Back** from top-left if you want to go back to the **Hospital Emergency Response app** without submitting any change. **Submit** button submits values you entered.

After you submit the data, select **Home** to go back to **Hospital Emergency Response app**.

### Fields and description

| **Option name**                                               | **Description**                                                                       |
|---------------------------------------------------------------|---------------------------------------------------------------------------------------|
| How many licensed beds are currently in use in this facility? | Number of licensed beds currently in use at this facility.                            |
| # of ICU Beds (AIIR Room) in use               | Number of ICU Beds in Airborne Infection Isolation Room (AIIR Room) currently in use.                                      |
| # of ICU Beds (non-AIIR Room) in use           | Number of ICU Beds (non-AIIR Room) currently in use.                                  |
| # of Acute Care Beds (AIIR Room) in use        | Number of Acute Care Beds (AIIR Room) currently in use.                               |
| # of Acute Care Beds (non-AIIR Room) in use    | Number of Acute Care Beds (non-AIIR Room) currently in use.                           |
| Is facility staffed to its full licensed bed capacity?    | Yes/No If the answer is No, you have the option to select all the reasons that apply: <br> - Staff <br> - Space <br> - PPE <br> - Equipment <br> - Low Patient Volume |
| Are you able to surge beyond licensed beds?              | Yes/No If the answer is No, you have the option to select all the reasons that apply: <br> - Staff <br> - Space <br> - PPE <br> - Equipment <br> - Low Patient Volume  |
| # of surge beds currently in use                         | Number of surge beds currently in use.                                                |
| # of Pediatric ICU Beds (AIIR and non-AIIR) currently in use | Number of Pediatric ICU Beds (AIIR and non-AIIR) currently in use at this facility. |
| # of Pediatric Acute Care Beds (AIIR and non-AIIR) currently in use | Number of Pediatric Acute Care Beds (AIIR and non-AIIR) currently in use at this facility. |  

## COVID-19 stats

![COVID-19 Stats](media/use/covid19-stats.png)

Submit COVID-19 specific details using the **COVID-19 stats** app. You can
update the location-specific patient details such as PUIs, positives, intubated,  and discharged patients.

Select **Back** from top-left if you want to go back to the **Hospital Emergency Response app** without submitting any change. **Submit** button submits values you entered.

After you submit the data, you have the option to go back to the **COVID-19 stats** app to create another record using the **Track another** button. Select **Home** to go back to **Hospital Emergency Response app**.

### Fields and description

| **Field name**  | **Description**                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------|
| Location        | The name and type of the room, ward, or any other specialty location within the selected facility.  |
| PUIs            | Number of patients under investigation.                                                            |
| Positive        | Number of patients positive with COVID-19.                                                         |
| Intubated        | Number of patients intubated.                                                         |
| Discharged        | Number of COVID-19 patients discharged.                                                         |

## Equipment

![Equipment](media/use/equipment.png)

Submit location-specific equipment details using the **Equipment** app. You can update the amount of in-use equipment such as ventilators, NIPPV, and PAPR.

Select **Back** from top-left if you want to go back to the **Hospital Emergency Response app** without submitting any change. **Submit** button submits values you entered.

After you submit the data, you have the option to go back to the **Equipment** app to create another record using the **Track another** button. Select **Home** to go back to **Hospital Emergency Response app**.

### Fields and description

| **Field name**  | **Description**                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------|
| Location        | The name and type of the room, ward, or any other specialty location within the selected facility.  |
| Ventilators            | Number of ventilators in use.                                                            |
| NIPPV        | Number of Noninvasive Positive-Pressure Ventilators in use.                                                         |
| PAPR hoods        | Number of Powered Air-Purifying Respirator (PAPR) hoods in use.                                                         |
| PAPR belts        | Number of PAPR belts in use.                                                         |
| PAPR chargers        | Number of PAPR chargers in use.                                                         |

## Staff

![Staff](media/use/staff.png)

Submit location-specific inventory for Registered nurses, patients, and
equipment. You don't have to enter values for each field on the screen. Enter a number for the field that you need to save in the solution database.

For example, if you need to add number of registered nurses requested as 3,
enter 3 in the **Registered nurses on duty - Requested** field and select
**Submit**. If you also need to update **Registered nurses on duty - Assigned** in use as 6, enter 3 in **Registered nurses on duty - Requested** field, then enter 6 in **Registered nurses on duty - Assigned**, and then select **Submit**.

Select **Back** from top-left if you want to go back to the **Hospital Emergency Response app** without submitting any change. **Submit** button submits values you entered.

After you submit the data, you have the option to go back to the **Staff** app to create another record using the **Track another** button. Select **Home** to go back to **Hospital Emergency Response app**.

### Fields and description

| **Option name**               | **Description**                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------------------|
| Location                      | The name and type of the room, ward, or any other specialty location within the selected facility. |
| Number of patients            | Current total number of patients at the selected location.                                        |
| **Registered nurses on duty** |                                                                                                   |
| *Partners* <br> RN partners/extenders support RNs & patients                   | Number of Registered Nurse partners present at the selected location.                             |
| *Requested* <br> # of RNs requested                  | Number of Registered Nurses requested for the selected location.                                  |
| *Assigned* <br> # of RNs with an assignment                   | Number of Registered Nurses assigned to the selected location.                                    |
| *Unassigned* <br> # of RNs unassigned to any task                  | Number of Registered Nurses not assigned to any task at the selected location.                    |
| **Facility level tracking** |                                                                                                   |
| % of essential care personnel currently absent in this facility                  | Essential care personnel currently absent in percentage format of the total for **entire facility**.                    |

## Supplies

![Supplies](media/use/supplies.png)

Collect the supplies inventory with the **Supplies** app. You can update the supply
component quantities in the entire facility inventory and the daily burn rate
from this app.

> [!NOTE]
> Enter values in both fields, **In stock** and **Used past 24 hr**, before you select **Submit**.

Select **Back** in the top-left if you want to go back to the **Hospital Emergency Response app** without submitting any change. **Submit** button submits values you entered. Select **Home** to go back to **Hospital Emergency Response app** after you submit.

### Fields and description

The supplies app items list may be different depending on your organization
requirements. Refer to your organization resources for descriptions of supply
names.

IT Administrators can add or update the supplies app items list using the
model-driven app for Power Apps. For more information, see [configuration guide](deploy-configure.md).

> [!NOTE]
> The supply inventory item values must be in number format.

## Staffing needs

![Staffing needs](media/use/staffing-needs.png)

Collects labor pool requests for the selected facility. Before you can submit the
labor pool request for a facility, ensure fields marked as *required* (*) are
filled.

Select **Back** from top-left if you want to go back to the **Hospital Emergency Response app** without submitting any change. **Submit** button submits values you entered. Select **Home** to go back to **Hospital Emergency Response app** after you submit.

### Fields and description

| **Field name**           | **Description**                                                                            |
|--------------------------|--------------------------------------------------------------------------------------------|
| Department               | Name of the department requesting the labor request. This field is *required*.             |
| Department location      | Location of the department.                                                                |
| Request type             | Type of the request for labor such as Clinical and Non-clinical. This field is *required.* |
| Role needed              | Role of the requested labor such as sitter or a registered nurse.                          |
| Needed now or next shift | Select a shift for the requested labor, current shift, or an upcoming shift.                |
| How many                 | How many resources needed, in number format.                |
| Details                  | Describe additional details or comments for the labor pool request.                        |

## Discharge planning

![Discharge](media/use/discharge.png)

Submit discharge information and patient status with total number using
the **Discharge planning** app. You can update the discharge details for last 24 hours, current discharge barriers, and the break-up for the barriers. 

Select **Back** from top-left if you want to go back to the **Hospital Emergency Response app** without submitting any change. **Submit** button submits values you entered. Select **Home** to go back to **Hospital Emergency Response app** after you submit.

**Barriers to long stay discharge** automatically updates with total number of patients you enter on the form across all barriers.

### Fields and description

| **Field name**            | **Description**                                                    |
|---------------------------|--------------------------------------------------------------------|
| Authorization             | Number of patients in the authorization process.                   |
| Durable medical equipment | Number of patients using the Durable Medical Equipment.            |
| Guardianship              | Number of patients under guardianship.                             |
| Home + Community Services | Number of patients using Home or Community services.               |
| Placement                 | Number of placements needed.                                       |
| Skilled nursing facility  | Number of skilled nursing facilities.                              |
| **Discharges**            |                                                                    |
| Past 24 h                 | Number of patients expected to be discharged in last 24 hours.  |
| Likely next 24 h          | Number of patients discharged in last 24 hours.                    |

## Dashboard

View the Power BI dashboards for insights and decision making. Selecting this option will open the Power BI dashboard in your mobile device browser.

For detailed info about teh dashboard, see [View Power BI dashboard](configure-data-reporting.md#view-power-bi-dashboard).

Select **Back** from top-left if you want to go back to the **Hospital Emergency Response app** without submitting any change.

## Other options

This section explains other actions you can do with the Hospital Emergency Response
mobile app components.

### End shift - sign out

You can sign out from the app using the profile icon on the upper-left side of
the screen.  

![Sign out](media/use/sign-out.png)

Select the **End shift** button to end your session and sign out.

> [!NOTE]
> *End shift* may not be available if your IT administrator has disabled
device sharing.

### App feedback

You can share your feedback with the **App feedback** option from any Hospital Emergency Response mobile app component. To share your feedback, select your profile from top-left and then select the **Submit feedback** button:

![Provide feedback](media/use/give-feedback.png)

When you select **App feedback**, you have
options to share a praise, an idea or report an issue with the app.

### Switch facility

![Switch facility](media/use/switch-facility.png)

Switch facility anytime by selecting the facility name on the top-right side of the screen. After you select the location name, you're taken to the **Hospital Emergency Response app** screen where you can select a different hospital, region, or facility.

## View the mobile app in your language

[!include[cc-lang](includes/cc-lang.md)]

You can view the Hospital Emergency Response mobile app in one of the supported languages on your mobile device by setting the default language of your mobile device (Apple or Android) to a supported language. See the help documentation for your respective mobile device on how to change the default language for your device.

If you're using the mobile apps on a browser on your computer, select the default language of your browser to a supported language for the Hospital Emergency Response mobile app. For more information, go to [Use Microsoft Edge in another language](https://support.microsoft.com/help/4532129).

## Issues and feedback

- To report an issue with the Hospital Emergency Response mobile app, visit <https://aka.ms/emergency-response-issues>.

- For feedback about the Hospital Emergency Response mobile app, visit <https://aka.ms/emergency-response-feedback>.
