---
title: Understand the Inspection app architecture | Microsoft Docs
description: Learn about the architecture of the Inspection sample app.
author: navjotm
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 04/06/2021
ms.author: namarwah
ms.reviewer: tapanm
---

# Understand Inspection app architecture

In this article, you'll learn about the collections and global variables used by the [Inspection](inspection.md) app, and understand how to use them effectively. If you want to learn more about how to install, and use the Inspection sample app instead, go to [Inspection sample apps](inspection.md).

## Prerequisites

To understand and use information in this article, you'll need to know about different controls, features, and capabilities of canvas apps.

- [Create and update a collection in a canvas app](../maker/canvas-apps/create-update-collection.md)
- [Collect, Clear, and ClearCollect functions in Power Apps](../maker/canvas-apps/functions/function-clear-collect-clearcollect.md)
- [Understand canvas-app variables in Power Apps](../maker/canvas-apps/working-with-variables.md)
- [Add and configure a canvas-app control in Power Apps](../maker/canvas-apps/add-configure-controls.md)
- [Add a screen to a canvas app and navigate between screens](../maker/canvas-apps/add-screen-context-variables.md)

You'll also need to know about how to [install](use-sample-apps-from-teams-store.md), and [use](inspection.md) the Inspection sample app.

## Data model

The following diagram explains the data model used by the Inspection sample app.

![Inspection sample app data model](media/inspection-architecture/data-model.png "Inspection sample app data model")

| Table name | Description |
| - | - |
| Area Inspection | An inspection is, most generally, an organized examination or formal evaluation exercise. This table holds the inspection checklist results using the area inspection step when an inspection is performed using a checklist/form. |
| Area Inspection Step | An inspection step is one of the checklist item result of an inspection, and holds the outcome and notes of that particular inspection step. |
| Area Inspection Location | An inspection location is place or item or audit that the user needs to inspect. All the inspection steps are performed on this location or item. One inspection can have multiple inspection steps which depends on number of checklist steps that are made available for the inspection. |
| Area Inspection Checklist | A checklist is a list of all the things that you need to do while inspecting. It holds multiple Checklist steps, and is connected to the type of the inspection. During the inspection, all the associated checklists are available to the user to choose and perform the inspection. |
| Area Inspection Checklist Step | Checklist steps are the steps that are performed in a sequential order while inspecting an item/area using a checklist. Each checklist step is associated to only one checklist. A series of checklist steps make one checklist. |
| Area Inspection Image | All the images that are taken or uploaded during the inspection are stored in this table, and these images are associated to area inspection steps. |
| Area Inspection Location | This table holds the information of the area, asset, or items that needs to be inspected. |
| Area Inspection Location Type | This table holds the type or category that the area, asset, or item is aligned to. Based on the type of area, asset, or item, the associated checklists is made available for the user to start the inspection. |
| User Setting | User settings are used to store user preferences pertaining to seeing the Power Apps splash screen every time they login to the app. There is one record for each user. |
| User Setting | Team settings are used to store Team, Channel and Planner preferences while using the application. |

### Collections

The following table lists the collections used by the inspection apps.

| Collection name       | Description                                                                                                   | Where used                                                                |
|-----------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| colLocalization       | Used to build a localization lollection based on the user's language.                                            | App OnStart                                                |
| colMenuAreaTypes      | Used to populate the collection with all area types.                                                           | App OnStart                                                |
| colAreaTypes          | Used to collect all area types and their associated Planner bucket Id.                                         | App OnStart                                                |
| colLocationTypeIcons  | Used to collect the name and order of the icons used in the app.                                               | App OnStart                                                |
| colWeekInspections    | To collect the total number of inspections in the last 7 days from **Active Area Inspections - Last 7 Days** view | App OnStart                                                |
| colWeekIssues         | To collect the total number of issues recorded in the last 7 days.                                       | App OnStart                                                |
| colTeamDurations      | To collect the team inspection duration in minutes                                                            | App OnStart                                                |
| colUserDurations      | To collect the logged in user’s inspection duration in minutes.                                                | App OnStart                                                |
| colStepOutcomes       | To collect the outcome and notes of inspection steps.                                                          | App OnStart                                                |
| colPlannerTasks       | To collect the list of Planner tasks in a particular plan based on the Plan and Group ID.                    | OnVisible property of the Welcome screen                                   |
| tasksforme            | To collect the list of Planner Tasks assigned to the logged in User.                                           | OnVisible property of the Welcome screen                                   |
| tasksforall           | To collect the list of Planner Tasks assigned to all the Users.                                                | OnVisible property of the Welcome screen                                   |
| overdue               | To collect the list of Planner Tasks assigned to the logged in user that are overdue.                         | OnVisible property of the Welcome screen                                   |
| ColGroupFroms         | To collect the available locations for the selected area type.                                                 | OnVisible property of the Forms screen                                     |
| colFormChecklistSteps | To collect the checklist steps for a selected location.                                                        | Items property of the individual area checklist gallery on Overview screen. |
| colAreaPlannerTasks   | To collect the task, step and the inspection IDs.                                                                 | OnSelect property of Add Task button on the Task Creation screen.           |
| colPlannerBuckets     | To collect the list of Planner buckets in a particular plan based on the Plan and Group IDs.                  | OnSelect property of Add Task button on the Task Creation screen.           |
| colTaskAssignments    | To collect the Planner task owners.                                                                            | OnSelect property of Add Task button on the Task Creation screen.           |
| colChecklistSteps     | To collect the inspection checklist steps for performing the inspection.                                      | OnVisible of the Checklist Step screen.                                     |

### Global variables

The following table lists the global variables used by the inspection apps.

| Variable name                   | Type     | Description                                                                                                                                                                                                |
|---------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| gblAppLoaded                    | Boolean  | To check if the app is completely loaded.                                                                                                                                                              |
| gblUserLanguage                 | Text     | To check the logged in user’s language.                                                                                                                                                                     |
| gblWorkType                     | Text     | To fetch the work type from app settings (inspection, audit, or walk).                                                                                                                                      |
| gblThemeDark                    | Boolean  | To check if the Teams theme is set to Dark.                                                                                                                                                            |
| gblThemeHiCo                    | Boolean  | To check if the Teams theme is set to High Contrast.                                                                                                                                                   |
| gblIsHostClientMobile           | Boolean  | To check if the host client is Mobile.                                                                                                                                                          |
| gblAppMobileOnDesktop           | Boolean  | To check if the host client is a desktop, or web.                                                                                                                                                   |
| gblMobileMode                   | Boolean  | To set the value to true if the host client is Android or iOS.                                                                                                                                             |
| localeID                        | Text     | Locale value to populate Planner URL.                                                                                                                                                                       |
| gblParamTeamId                  | Text     | To set the Group ID from Planner.                                                                                                                                                                           |
| gblParamChannelId               | Text     | To set the Channel ID from Planner.                                                                                                                                                                         |
| gblParamTenantId                | Text     | To set the Tenant ID from Planner.                                                                                                                                                                          |
| gblRecordSettings               | Record   | To check Teams settings for current team and channel ID.                                                                                                                                                    |
| gblCheckLabelSettings           | Number   | To get the number of area type labels from the **Area Inspection Labels** view.                                                                                                                              |
| areaLabel                       | Text     | To set area label and area type label from settings. If no settings exist, use area and area type.                                                                                                          |
| gblCurrUserEmail                | Text     | To fetch the current user’s email ID.                                                                                                                                                                       |
| gblCurrUser                     | Record   | To fetch the current user’s record.                                                                                                                                                                         |
| gblTotalInspectionCount         | Number   | To fetch the total inspection count in the last 7 days.                                                                                                                                                     |
| gblCurrentUserInspectionCount   | Number   | To get the total inspection count for the current in the last 7 days.                                                                                                                                       |
| gblCurrentUserIssueCount        | Number   | To get the issue count for the current in the last 7 days.                                                                                                                                                  |
| gblTotalIssueCount              | Number   | To get the total issue count in the last 7 days.                                                                                                                                                            |
| gblTeamAvgTime                  | Number   | To get the average team inspection time.                                                                                                                                                                    |
| gblUserAvgTime                  | Number   | To get current user’s inspection duration.                                                                                                                                                                 |
| gblUpdateInspectionCount        | Boolean  | Variable to control updating of inspection count when a user navigates to the Welcome screen.                                                                                                               |
| gblGroupSelectedLocation        | Record   | Variable to control the selected area when starting an inspection for a group.                                                                                                                              |
| gblPlannerPlanID                | Text     | To get the Planner ID from parameters.                                                                                                                                                                      |
| gblPlannerGroupID               | Text     | To get the Group ID from parameters.                                                                                                                                                                        |
| gblSettingSharePointLocation    | Text     | To get the SharePoint location from  parameters.                                                                                                                                                             |
| gblSkipFormNav                  | Boolean  | Variable to control the back navigation from the summary screen based on number of related forms. If 1, then navigate back to assets screen, if more than 1, then navigate back to forms screen. |
| gblFormStepsCount               | Number   | To check the number of checklist steps in the selected form.                                                                                                                                                |
| gblDisplayNoStepWarning         | Boolean  | To display a warning if the number of checklist steps in the selected form is zero.                                                                                                                        |
| gblDisplayNoLocationWarning     | Boolean  | To display a warning if the number of locations in the selected group is zero.                                                                                                                             |
| gblselectedareainspection       | Boolean  | Variable to store the selected inspection.                                                                                                                                                                  |
| gblSelectedChecklist            | Record   | Variable to collect areas within the selected group and the forms relevant to that group.                                                                                                                   |
| gblSelectedGroup                | Record   | Set the value of the particular item If the selected group has more than 1 form.                                                                                                                           |
| gblLocationType                 | Record   | Variable to store the selected the location type.                                                                                                                                                               |
| gblSelectedLocation             | Record   | Variable to store the selected location.                                                                                                                                                                    |
| LastSynced                      | DateTime | Variable to set the last synchronization time.                                                                                                                                                                       |
| gblInspectionPatchComplete      | Boolean  | To reset the variable to be prepared for the next inspection.                                                                                                                                               |
| gblBackNav                      | Boolean  | To check whether last half completed inspection is being continued.                                                                                                                                         |
| gblSelectedGroupID              | Guid     | Variable to store the Guid of the selected group.                                                                                                                                                           |
| gblExpandVar                    | Boolean  | Variable to collapse all step instructions when the user navigates to the checklist steps. screen                                                                                                           |
| gblFocusStep                    | Guid     | Variable to set the selected record to control the scroll of the gallery in the checklist steps screen to that record.                                                                      |
| gblSelectedStepImage            | Record   | Variable to enlarge the step image.                                                                                                                                                                         |
| gblViewEnlargedImage            | Boolean  | Variable to set enlarged image visibility to true/false.                                                                                                                                                    |
| gblLastInspection               | Record   | Variable to get the newly created inspection.                                                                                                                                                               |
| gblResetTimer                   | Boolean  | Timer to reset the gallery so the gallery scrolls to the selected record.                                                                                                                                   |
| gblSelectedStep                 | Record   | Variable to set the focus at the last step being performed.                                                                                                                                                |
| currentPhoto                    | Image    | Variable to store the selected photo to be enlarged.                                                                                                                                                        |
| gblAppSetting_inputMobileOnWeb  | Boolean  | Variables to scale fonts for mobile-oriented apps, running in desktop.                                                                                                                                      |
| gblAppSetting_inputMobile       | Boolean  | Variables to scale fonts for mobile-oriented apps.                                                                                                                                                          |
| gblAppSetting_inputScaleFontsBy | Number   | Use this variable for scaling all fonts by a fixed amount.                                                                                                                                                  |
| gblAppColors                    | Record   | Variable to set the color value in the app.                                                                                                                                                                 |
| gblAppSizes                     | Record   | Variable to set the size values in the app.                                                                                                                                                                 |
| gblAppStyles                    | Record   | Variable to set the styling values in the app.                                                                                                                                                              |
| gblSelectedLocationType         | Record   | Variable to get the selected location type record.                                                                                                                                                         |
| gblSelectedLocationTest         | Text     | Variable to get the name of the selected location. type                                                                                                                                                     |
| gblTaskcreated                  | Boolean  | Variable to check whether a task is created or not.                                                                                                                                                        |
| gblFocusStep                    | Text     | Global variable to set the focus on the inspection checklist screen.                                                                                                                                        |
| Taskid                          | Record   | Variable used to set the ID of the created Planner task to the record.                                                                                                                                      |
| gblFirstGroupLocation           | Table    | Variable to store the image of the first area in the selected group.                                                                                                                                        |
| gblImage1                       | Record   | Variable to set the primary image of the selected item.                                                                                                                                                     |
| gblGroupLocation                | Text     | Variable to pass the group location while creating a new task.                                                                                                                                              |

## Manage inspections app

This section explains collections, global variables used by the [Manage inspection](inspection.md#manage-inspections-app) app, and execution details for the app.

### App OnStart

This section explains app OnStart collections, variables, and execution details.

#### OnStart collections

Collections used during app OnStart:

| Collection name | Description |
| - | - |
| colLocalization | Collection of localized text based on user’s language. |
| colLabelSettings | Collection to store the value and icons for labels. |
| colUserSettings | Collection of the user settings from Area Inspection User Settings table |
| colLocationTypeIcons | Collection of location type icons used in the app. |
| colLocConfig | Collection used to set the name and type of the main and the sub sections. |
| colLocTypeSettings –** Used to collect the different setting types
    available in the app.
| colInspections | Collection to store area inspections. |
|colPlannerBuckets | Collection of Planner buckets. |
| colPlannerTasks | Collection of Planner buckets. |
| colCharsWidth | Collection of widths for each character used for auto width labels. |

#### OnStart variables

Variables used during app OnStart:

| Variable name | Description |
| - | - |
| gblAppLoaded | Global variable to check if the app has loaded completely. |
| gblAppContext | Global variable to check the context of where the app is running. |
| gblUserLanguage | Global variable to store the user’s language. |
| gblFirstRun | Global variable to check whether the app is being run for the first time. |
| gblWorkType | Global variable to store type of work. |
| gblSelectedWorkType | Global variable to check the selected type of work. |
| gblParamTeamId | Global variable to set the Planner Group ID from parameters. |
| gblParamChannelId | Global variable to set the Planner Channel ID from parameters. |
| gblThemeDark | Global variable to store if Teams is running in dark mode. |
| gblThemeContrast | Global variable to store if Teams is running in contrast mode. |
| gblAppManager | Global variable check whether the user has the app manager privilege. |
| gblRecordUserSettings | Global variable to store the latest area inspection user settings records for the current user. |
| gblFontSizes | Global variable to store the font sizes used in the app. |
| gblPadding | Global variable to set the padding values. |
| gblScreenHeightMin | Global variable to set the minimum screen height. |
| gblScreenWidthMin | Global variable to set the minimum screen width. |
| gblEditLocation | Global variable to check whether a location is being edited. |
| gblView | Global variable to store the view to be displayed. |
| gblViewInspection | Global variable which indicates an inspection is being viewed.
| gblManageLocationTypes | Global variable to check if location type exists. |
| gblTempAddLocType | Global variable to check for adding location type. |
| gblWarningType | Global variable which controls which warning message to be displayed. |
| gblDisplayWarning | Global variable to control visibility of warning messages. |
| gblAddLocation | Global variable to show or hide location button. |
| gblShowLocationTypeIcons | Global variable to control visibility of location type icons. |
| gblFirstTimeNavigation | Global variable to check whether the user viewing for the first time. |
| gblParamTenantId | Global variable to set the tenant ID from parameters. |
| gblParamLocaleId | Global variable to set the locale ID from parameters. |
| gblCheckLabelSettings | Global variable to store the active area inspection label. |
| gblRecordSettings | Global variable used to set the Team and Channel Id to the Area Inspection Settings table. |
| gblSettingPlannerPlanId | Global variable to get the planner ID from the record settings. |
| gblSettingTeamId | Global variable to get the Team ID from the record settings. |
| gblLocation | Global variable to set the first area inspections location. |
| gblNavToSettings | Global variable to denote navigation to settings from other screens.

#### OnStart execution details

1. When a user accesses the app, the **gblAppLoaded** variable is set to false. The user’s language code is stored in **gblUserLanguage** variable, with "English - US" as the default. The **gblAppContext** checks where the app is running.

1. The user’s language is then used to collect localized text used throughout the app (such as label and button text) in **colLocalization** collection.

1. The value and icons of the labels are stored in the **colLabelSettings** collection. The work type is set using the **gblWorkType** and **gblSelectedWorkType** variables. It's set to inspections if other values do not exist.

1. The channel, group, tenant and locale IDs from the parameter values are stored in the **gblParamTeamId**, **gblParamChannelId**, **gblParamTenantId**, and **gblParamLocaleId** variables.

1. User's Teams theme is checked: Default, Dark, or High Contrast. The **gblThemeDark** and **gblThemeHiCo** variables are set accordingly.

1. The **gblAppManager** variable checks the parameters if the user has a user team role.

1. User details from the Area Inspection User Settings table are collected in **colUserSettings** collection. If no records exist, a new project user setting record is created. If there are multiple area inspection user settings records exist, the oldest record is selected and stored in the **gblRecordUserSettings** variable.

1. Predefined font sizes, padding values, minimum screen height and width values are stored in the **gblFontSizes**, **gblPadding**,
    **gblScreenHeightMin**, and **gblScreenWidthMin** variables.

1. The **gblView** variable which controls the view to be displayed is set to “Locations”.

1. The order, name and the icon values used in the app are collected in the **colLocationTypeIcons** collection. The number of active area inspection labels are stored in the **gblCheckLabelSettings** variable.

1. The main and sub section values are collected in the **colLocConfig** collection. If they are blank, the values are set to area and area type.

1. The team and channel IDs from the area inspection settings are stored in the **gblRecordSettings** variable.

1. The location type settings are collected in the **colLocTypeSettings** collection.

1. If there are no area inspection user settings records (**gblRecordSettings**), the **gblFirstRun** variable is set to true which in turn controls the visibility of the splash dialog.

1. The final values for the Planner and Team ID are stored in the **gblSettingPlannerPlanId** and **gblSettingTeamId** variables.

1. The inspections from the Area Inspections table are stored in the **colInspections** collection.

1. The first area inspection location is set to the **gblLocation** variable**. The Planner buckets and tasks are collected in the **colPlannerBuckets**, and **colPlannerTasks** collections.

1. The size and font of each character used for auto width of header buttons are collected in the **colCharsWidth** collection.

## Locations screen

This section explains app [locations screen](inspection.md#add-locations) collections, variables, and execution details. Locations screen includes the first run experience, the list of locations on the left-pane, and the list of inspections based on the location.

### Displaying the first run experience

This section explains the first run experience for locations.

#### First run experience collections

First run experience for locations doesn't use any variables.

#### First run experience variables

Variables used during the first run experience for locations:

| Variable name | Description |
| - | - |
| locShowCustomize | Local variable to check whether to show customize option. |
| locShowRestricted | Local variable to show locations with restrictions. |
| locShowSetupChannelPlanner | Local variable to show Planner setup channel. |
| locShowSetup | Local variable to show setup option. |
| locShowFirstRun | Local variable to indicate if the current run of the app is the first run for the user. |
| locShowPowerAppsPrompt | Local variable to indicate either to show or hide the splash screen. |

#### First run execution details

1. On visible of project screen a dialog pop-up appears if either of the variables&mdash;**locShowFirstRun** or **locShowPowerAppsPrompt**, are true. If not, the app proceeds with loading the project data.

1. **locShowFirstRun** is set to true/false depending on the project settings records.

### Displaying the list of locations

This section explains the process of displaying the list of locations.

#### Collections used when displaying the list of locations

Collections used when displaying the list of locations:

| Collection name | Description |
| - | - |
| colInspections | Used to collect inspection records. |

#### Variables used when displaying the list of locations

Variables used when displaying the list of locations:

| Variable name | Description |
| - | - |
| locAreaSortOrder | Local variable used to control the sorting order of locations. |
| locInspectionSortBy | Local variable to denote on what field are inspection records sorted by. |

#### Execution details when displaying the list of locations

1. The list of locations in the Area Inspection Locations table are displayed in the **galAreas** gallery along with the location types.

1. The locations can be searched based on their names. Using the sort button toggles the value of **locAreaSortOrder** variable which sorts the locations in ascending or descending order based on the name.

1. Selecting any location in the **galAreas** gallery updates the **locInspectionSortBy** variable to date. The value of the **gblLocation** variable is set to the selected location.

1. The list of area inspections for the selected location is collected in the **colInspections** collection.

1. The **galInspections** gallery displays the list of inspections for the selected location in the descending order of the created-on date.

1. The count of inspection whose review status code is either "Pending Review" or "Pending Action" is displayed next to the locations. This behavior is achieved by filtering the items of the **galAreaInspections** gallery based on the review status code.

#### Displaying the list of inspections based on the selected location

This section explains the process of displaying the list of locations.

#### Collections used when displaying the list of inspections based on the selected location

Collections used when displaying the list of inspections based on the selected location:

| Collection name | Description |
| - | - |
| colInspections | Used to collect inspection records. |

#### Variables used when displaying the list of inspections based on the selected location

Variables used when displaying the list of inspections based on the selected location:

| Variable name | Description |
| - | - |
| locInspectionSortBy | Local variable to denote on what field should the inspection records be sorted. |
| locInspectionSortOrder | Local variable used to control the sorting order of the inspection records. |
| gblLocation | Global variable to store the selected location. |
| gblInspection | Global variable to store the inspection record. |

#### Execution details when displaying the list of inspections based on the selected location

1. The title and the primary image of the location is displayed using the **gblLocation** variable.

1. Location is displayed under the grouped location header using the **gblLocation** variable, if location is part of the group.

1. The **galInspections** gallery displays the list of inspections collected in the **colInspections** collection based on the selected location.

1. The Inspection Form name, Submitted By, Number of ays since the inspection was submitted, Status and the number of issues columns are shown.

1. **locInspectionSortBy** variable is used to control the sorting of the columns.

1. The **gblInspection** variable is filtered for the number of inspections where the issue outcome is as issue.

1. Selecting any of the column headings toggles the value of the **locInspectionSortOrder** variable which ends up sorting the values.

1. Checkbox next to the inspection name is used to select the inspection for deletion. Selecting the checkbox next to the inspection header selects all inspection records.

## Deleting inspections

This section explains collections, variables, and execution details when deleting inspections. Inspections can be deleted from the [locations tab](inspection.md#add-locations) by selecting one or more inspections.

### Collections used when deleting inspections

The following collections are used when deleting inspections.

| Collection name | Description |
| - | - |
| colInspections | Used to collect inspection records. |
| colRemoveInspections | Used to collect deleted inspection records. |

### Variables used when deleting inspections

The following variables are used when deleting inspections.

| Variable name | Description |
| - | - |
| gblDisplayWarning | Global variable to control visibility of warning messages. |
| gblWarningType | Global variable which controls which warning message to be displayed. |

### Execution details when deleting inspections

1. Inspection records can be deleted from the locations screen. Select checkbox next to an inspection to delete one record, or the checkbox from the header to delete all records.

1. **Delete** button is only enabled after one or more inspection records are selected.

1. Selecting **Delete** sets the value of the **gblDisplayWarning** variable to true. This change ends up displaying the **conWarning** container which in turn displays the delete confirmation dialog.

1. The value of **gblWarningType** variable is set to **inspectiondelete** indicating an inspection is being deleted.

1. Selecting **I understand** enables the delete button. And selecting **Delete** sets the **gblDisplayWarning** variable value to false to hide the delete dialog.

1. Deleted inspection record is added to the **colRemoveInspections** collection, and removed from the Area Inspections table. The **colInspections** collection is cleared and collected to have the updated records.

## Editing location types

This section explains collections, variables, and execution details when [editing location types](inspection.md#add-location-types). Location types can be edited from the **Locations** tab upon selecting **Location type**.

### Collections used when editing location types

The following collections are used when deleting inspections.

| Collection name | Description |
| - | - |
| colInspections | Used to collect inspection records. |

### Variables used when editing location types

The following variables are used when deleting inspections.

| Variable name | Description |
| - | - |
| gblEditLocation | Global variable to denote if a location is being edited. |
| gblAreaChanged | Global variable to indicate that the location has been updated. |
| gblLocation | Global variable to store the location in the current context. |
| gblLocType | Global variable to store the location type. |
| gblCurrentLocation | Variable to store the location which is being edited. |
| gblAddLocationImage | Global variable to store the image added as part of a location.

### Execution details when editing location types

1. The location type can be edited by selecting *Edit** Locations screen.

1. Selecting **Edit** updates the value of the **gblEditLocation** variable to true which in turn disables the **galAreas** gallery and hide the **galInspections** gallery.

1. The Title and the Location Type dropdown fields are enabled and can be updated.

1. Selecting to edit picture allows user to upload a new image.

1. Selecting to manage location type button takes the user to location type section on the Settings screen.

1. **Save** is only enabled if fields are updated. Selecting **Save** updates the details to the Area Inspection Locations table.

1. The details are updated to the Area Inspection Locations table. The **gblCurrentLocation** variable is set to the location being edited.

1. The value of **gblAreaChanged** variable is updated to true and the Area Inspection Locations table is refreshed.

1. The location type of the edited location is stored in the **gblLocType** variable.

## Review submitted inspections

This section explains collections, variables, and execution details when [reviewing submitted inspections](inspection.md#review-submitted-inspections).

### Collections used when reviewing submitted inspections

The following collections are used when deleting inspections.

| Collection name | Description |
| - | - |
| colInspections | Used to collect inspection records. |

### Variables used when reviewing submitted inspections

The following variables are used when deleting inspections.

| Variable name | Description |
| - | - |
| gblViewInspection | Global variable to denote if a location is being edited. |
| gblInspection | Global variable for the inspection record in the current context. |
| gblParamTenantId | Global variable to set the tenant ID from parameters. |
| gblParamLocaleId | Global variable to set the locale ID from parameters. |
| gblParamTeamId | Global variable to set the Planner Group ID from parameters. |
| gblSettingPlannerPlanId | Global variable to get the Planner ID from the record settings. |
| gblCurrentLocation | Global variable to store the current location being reviewed. |
| gblLocation | Global variable that denotes the location in the current context. |

### Execution details when reviewing submitted inspections

1. The performed inspections can be reviewed by selecting the required record in the **galInspections** gallery.

1. Selecting an inspection record sets the value of the **gblViewInspection** variable to true which controls the visibility of the **galIssues** and **galNoIssues** galleries.

1. The items property of both the galleries are filtered based on the **gblInspection** value.

    1. **galIssues** gallery for inspections where the outcome is an issue.

    1. **galNoIssues** gallery for inspections where the Outcome is OK or N/A.

1. The users can see the notes, attachments and tasks created while performing the inspection.

1. Selecting the task launches Planner with the selected task open based on the values of the Tenant, Locale, Team and Plan ID collected during the start of the app.

1. The "Review status" field has Pending Review, Pending Action, Closed and Incomplete as choices. Changing the value will update the Area Inscriptions table and the **colInspections** collection with the selected status and saves the record.

1. Selecting **Back** updates the **gblCurrentLocation** and **gblLocation** variables to the location in context taking the user back to the location details view.

### Insights Screen<br>

#### Collections involved

1.  **colInspections** – Used to collect Inspection records

2.  **colTeamDurations** – used to collect the date difference between the
    Inspection start and end dates in minutes.

3.  **colBarChartTemp** – used to collect the Active area inspections grouped by
    owner in the last 7 days

4.  **colBarChart – Used to collect the**

5.  **colLineChartForms –**

6.  **colLineChart –**

7.  **colLocTypesTemp –**

8.  **colInspectionsByLocTypeID –**

#### Variables involved

1.  **gblInspectionsCount** – variable to count the number of inspections

2.  **gblView** – variable to denote the view which is being displayed.

3.  **gblTeamAvgTime** – global variable to store the average completion time of
    Inspections.

4.  **gblAreaChanged –** global variable to indicate that the location has been
    updated

5.  **gblChartView-** global variable to set the default value of the chart view
    to 7 days.

6.  **gblBarChartView –** global variable to set the default value of the Bar
    chart view to 7 days.

7.  **gblFormBarChartView –** global variable to set the default value of the
    Form Bar chart view to 7 days.

8.  **gblLineChartView- –** global variable to set the default value of the Line
    chart view to 7 days.

#### Detailed steps

1.  When the Insights screen is loaded, the **gblInspectionsCount** is used to
    count the total number of inspections to decide if charts should be visible
    or should zero state images be shown. The **gblView** variable is set to
    Insights indicating that the Insights screen is being shown.

2.  The date difference between the Inspection start and end dates in minutes is
    collected in the **colTeamDurations** collection.

3.  The average inspection time (duration of all completed inspections divided
    by the total number of Inspections) is calculated using the
    **colTeamDurations** value and is stored in the **gblTeamAvgTime** variable.

4.  The top contributors bar chart (count of inspections grouped by owner) for
    the last 7 days is collected using the **colBarChartTemp** and
    **colBarChart** collections.

5.  The average inspection time for line chart (inspections time for inspections
    in the last 7 days grouped by form) are collected using the
    **colLineChartForms** and **colLineChart** collections.

6.  The **conInspectionStats** container displays the number of Inspections
    which are Pending review, Pending Action, closed Inspections and the average
    completion time.

7.  The Area Inspections table is filtered based on the Review Status code to
    get the count of Inspections which are Completed, pending review and Pending
    Action.

8.  The **galAvgInspectionTime** gallery displays the average inspection time
    data in the **colLineChart** collection in descending order.

9.  The **colPieChart** displays a Pie chart depicting Open Inspections based on
    the Location type. The legend next to the Pie Chart displays the list of
    Location types which have at least 1 or more Inspections.

10. The **galTopContributors** gallery displays the top contributors’ details
    (who have at least one or more Inspections) from the **colBarChart**
    collection.

11. Each of the charts available can show data based on the past 7, 30 and 60
    days. Users can select required range by clicking on the same.

    -   Selecting the number of days on the Open Inspections Pie Chart will set
        the **gblChartView** variable to either 30 or 60 based on the selection
        made. The open inspection count by location type ID, type and Name for
        the last 30 / 60 days is collected in the **colInspectionsByLocTypeID,
        colInspectionsByLocType** and **colInspectionsByLocTypeName** and the
        Pie Chart data stored in the **colPieChart** collection is refreshed and
        displayed accordingly.

    -   Selecting the number of days on the Avg Inspections time mins Line Chart
        will set the **gblLineChartView** variable to 30 / 60 based on the
        selection made. The average inspections time for inspections in the last
        30 / 60 days grouped by form are collected in the **colLineChartForms**
        and **colLineChart** collections and the data is stored is refreshed and
        displayed accordingly.

    -   Selecting the number of Top Inspection report contributors Bar Chart
        will set the **gblBarChartView** variable to 30 / 60 based on the
        selection made. The count of inspections grouped by owner for the last
        30 / 60 days grouped is collected using the **colBarChartTemp** and
        **colBarChart** collections and the data is stored is refreshed and
        displayed accordingly.

#### Screens

![](media/inspection-architecture/82ee5bdaa5ac39a2546c8fab7c12b51a.png)

### Inspection Forms Screen<br>

#### Displaying the list of Inspection Forms 

##### Collections involved

1.  **colChecklistStepsTemp –** Used to collect Area Inspection Checklist steps
    based on the ID.

2.  **colChecklistSteps –** Used to collect Area Inspection Checklist steps for
    the selected Inspection form.

3.  **colChecklistStepsOutput1 –**

4.  **colChecklistStepsImage –** used to collect the cover image of the
    checklist steps for the selected Inspection form.

##### Variables involved

1.  **gblFormClick** – Local variable used to control the sorting order of
    Locations.

2.  **gblForm** – local variable to denote on what field are inspection records
    sorted by

##### Detailed steps<br>

1.  The list of Inspection forms in the Area Inspection Checklists table are
    displayed in the **galForms** gallery along with the Number of checklist
    steps in the ascending order of their names.

2.  Clicking on any of the location in the **galForms** gallery will update the
    **gblFormClick** variable to true. The **gblForm** variable is set to the
    selected inspection form

3.  The collections **colChecklistStepsTemp**, **colChecklistSteps** ,
    **colChecklistStepsOutput1**  
    and **colChecklistStepsImage** are updated to show the details of the
    selected Inspection form.

4.  Based on the collected information, the checklist steps for the selected
    Inspection form are displayed in the **galFormChecklistSteps** gallery.

Screens

![](media/inspection-architecture/fad44d987322f9fd20b3254acab0c802.png)

#### Displaying the list of Checklist Steps based on the selected Inspection Form 

##### Collections involved

1.  **colChecklistSteps -** Used to collect Area Inspection Checklist steps for
    the selected Inspection form.

2.  **colChecklistStepsImage –** used to collect the cover image of the
    checklist steps for the selected Inspection form.

##### Variables involved

1.  **gblForm –** used to store the Inspection form which is being edited

##### Detailed steps

1.  The title and the location type details are displayed based on the
    **gblForm** variable.

2.  The checklist steps for the selected Inspection form are displayed in the
    **galFormChecklistSteps** gallery based on the values stored in the
    **colChecklistSteps** collection

3.  The title, Action buttons, Instructions and the reference image for each
    checklist step is displayed

Screens

![](media/inspection-architecture/471d40091bfd19c5a3cd30a962696c0a.png)

#### Creating an Inspection Form

##### Collections involved

1.  **colChecklistStepsOutput1** –

2.  **colChecklistSteps – used to collect the checklist steps of an Inspection
    form.**

3.  **colChecklistStepsImage – used to collect the cover image of a checklist
    step.**

4.  **colPatchSteps1 –**

##### Variables involved

1.  **gblAddForm** –

2.  **gblStepChanged** – global variable to indicate that the checklist step has
    been updated

3.  **gblImageChanged –** global variable to indicate that the cover image has
    been updated

4.  **gblTempAdd –**

##### Detailed steps

1.  A new Inspection form can be created by clicking on the “+ New Inspection
    Form” button present above the **galForms** gallery.

2.  On clicking the “+ New Inspection Form” button, the value of the
    **gblAddForm** variable is set to true and the **colChecklistSteps**,
    **colChecklistStepsOutput1** and **colChecklistStepsImage** collections are
    cleared.

3.  As the value of the **gblAddForm** is true, a new Inspection form is
    displayed to the User**.**

4.  A new checklist step can be added by clicking on the “+ Add Step” button
    clicking on

5.  which a new checklist step is added with the Title, Location Types,
    Checklist steps and the reference image being blank.

6.  The Action button values are by default set to Pass, Fail and N/A and can be
    modified by the User as required.

7.  The N/A option can be hidden if desired by clicking on the Step Unhide
    button (imgNAStepUnhide) clicking on which will update the
    **colChecklistStepsOutput1** collection for this step and update the
    **gblStepChanged** value to true.

8.  Adding a new checklist step will update the **colChecklistSteps,
    colChecklistStepsOutput1** and **colChecklistStepsImage** collections with
    the details.

9.  The checklist step can be duplicated by clicking on the Duplicate icon
    present on the respective step. Clicking on which the sequence of the step
    is updated in the collections **colChecklistSteps, colChecklistStepsOutput1,
    colChecklistStepsImage.**

10. The details (Title, Instructions, Action button values and reference image)
    from the parent step is copied to the newly created checklist step and the
    **colChecklistSteps, colChecklistStepsOutput1, colChecklistStepsImage** are
    updated.

11. The Sequence of the Checklist steps can be updated by clicking on the Up and
    Down arrows present next Step.

12. The Up-arrow button is disabled for the first checklist step and the down
    arrow button is disabled for the last step in the gallery (The display mode
    is controlled by the value of **msft_sequence** field).

13. The **colChecklistStepsOutput1, colChecklistStepsImage** and
    **colChecklistSteps** collections are updated based on the value of the
    **msft_sequence** field and the value of **gblStepChanged** is updated to
    true.

14. A new checklist step can be added by clicking on the “+ Add Step” button
    clicking on which will update the **colChecklistSteps,
    colChecklistStepsOutput1** and **colChecklistStepsImage** collections.

15. A new checklist step is created with the Title, Location Types, Checklist
    steps and the reference image being blank.

16. The values of the variables **gblImageChanged, gblTempAdd** and
    **gblStepChanged** are set to true.

17. Clicking on the Delete icon present in each step will remove the checklist
    step and update the **msft_sequence** field in **colChecklistStepsOutput1,
    colChecklistStepsImage** and **colChecklistSteps** collections**.**

18. Once all the required details are entered, clicking on the Save button
    (enabled only when the title, location type and at least 1 checklist step is
    present) will rename the columns in the **colChecklistStepsOutput1** and
    store the details in **colPatchSteps1** collection and the newly created
    checklist steps are updated in the Area Inspection Checklist Steps table and
    the newly created Inspection form is updated to the Area Inspections
    Checklists table.

19. Clicking on the cancel button will **gblStepChanged, gblImageChanged,
    gblAddForm** and **gblEditForm** variables to false and navigate back to the
    Inspection form view with the first record in the **galForms** gallery being
    selected.

Screens

![](media/inspection-architecture/52697ffca26972ba8decdb5cc2d36235.png)

![](media/inspection-architecture/cb827129e120f6a74f95d726b79de2f7.png)

![](media/inspection-architecture/9fc653f6b10726734768d942876a4d48.png)

![](media/inspection-architecture/d7887866169f7c64833eb5ea8e20a78d.png)

![](media/inspection-architecture/9d12e80bbb2bae834f749ffed1dc136e.png)

![](media/inspection-architecture/6b749c8d0135d649a553ad186a3ddee4.png)

![](media/inspection-architecture/24101f898f1afcdc0d0e47b9840d1104.png)

#### Editing an Inspection Form 

##### Collections involved

1.  colChecklistStepsRemoveTemp –

2.  **colChecklistStepsOutput1 –**

3.  **colPatchSteps1 –**

4.  **colChecklistStepsImage – used to collect the cover image of a checklist
    step**

##### Variables involved

1.  **gblEditForm** – variable to indicate that the Inspection form can is being
    edited

2.  **gblAreaChanged –** global variable to check whether a Location (Area) is
    edited

3.  **gblCountSteps-** global variable to count the number of checklist steps

##### Detailed steps

1.  An existing Inspection form can be edited by clicking on the Edit button on
    the Inspection forms screen.

2.  Clicking on the Edit button will update the value of the **gblEditForm**
    variable to true which will in turn disable the **galForms** gallery.

3.  The value of the **gblEditForm** as true indicates that the Inspection form
    is editable and the User can update all the fields.

4.  The users can update the title, location type Duplicate, Delete and
    rearrange the Checklist steps.

5.  Once the required changes are made clicking on the save button will rename
    the columns in the **colChecklistStepsOutput1** and store the details in
    **colPatchSteps1** collection and the modified checklist steps are updated
    in the Area Inspection Checklist Steps table Inspection form is updated to
    the Area Inspections Checklists table.

6.  The removed inspection steps are stored in the **colChecklistStepsRemoveTemp
    collection** and the **gblCountSteps** is used to store the number of
    checklist steps in the selected inspection form and the changed images are
    updated in the **colChecklistStepsImage** collection.

Screens

![](media/inspection-architecture/8432472d2ede0af3b7731a7520e2e032.png)

![](media/inspection-architecture/9b189226021b55f08331c2d5e5422727.png)

#### Duplicating an Inspection Form 

##### Collections involved

1.  **colPatchSteps1**–

2.  colChecklistStepsOutput1 –

3.  colChecklistSteps – used to collect the checklist steps of an Inspection
    form.

##### Variables involved

1.  **gblNewForm** – global variable to indicate that a Inspection form is being
    created.

2.  **gblStepChanged –** global variable to indicate that the checklist step has
    been updated

3.  **gblImageChanged -** global variable to indicate that the cover image has
    been updated

##### Detailed steps

1.  An existing Inspection form can be duplicated by clicking on the Duplicate
    button while it is being edited.

2.  The duplicate button will be disabled if either the value of
    **gblStepChanged** or **gblStepChanged** is true indicating that the
    inspection record cannot be duplicated if any of the steps or image is
    updated and not saved.

3.  Clicking in which will rename the columns in the
    **colChecklistStepsOutput1** and store the details in **colPatchSteps1**
    collection.

4.  The title of the newly created inspection form would be appended with (COPY)
    which is handled by the **gblNewForm** variable and the location type values
    are blank.

5.  The details in the **colChecklistSteps, colChecklistStepsOutput1 and
    colChecklistStepsImage** collections are copied to the duplicated Inspection
    form.

6.  Users can make required changes and save the inspection form.

Screens

![](media/inspection-architecture/8432472d2ede0af3b7731a7520e2e032.png)

![](media/inspection-architecture/7c8599a7ac5b975b727d35361b5132c7.png)

#### Deleting an Inspection Form 

##### Collections involved

1.  **colChecklistSteps** - used to collect the checklist steps of an Inspection
    form.

##### Variables involved

1.  **gblWarningType** – global variable which controls which warning message to
    be displayed.

2.  **gblDisplayWarning –** global variable to control visibility of Warning
    messages

##### Detailed steps

1.  An existing Inspection form can be deleted by clicking on the Delete button
    while it is being edited.

2.  Clicking in which will set the **gblWarningType** variable to **formdelete**
    and the value of **gblDisplayWarning** variable to true thus displaying the
    **conWarning** container which displays the delete confirmation dialog.

3.  Checking the “I Understand button” will enable the Delete button clicking on
    which set the **gblDisplayWarning** value to false hiding the delete dialog
    and remove the deleted Inspection form from the Area Inspection Checklists
    table and the **colChecklistSteps** is also cleared.

Screens

![](media/inspection-architecture/ee94cb895a812523b8ea15bac4e120f6.png)

![](media/inspection-architecture/bc31d3f37effd0f5c6b003bf000eda9b.png)

### About Screen 

#### Collections involved

None

#### Variables involved

**None**  


#### Detailed steps

1.  Clicking the “Customize using Power Apps button” on the **conHeader_About**
    container opens Power Apps tool link in Microsoft teams.

2.  There are help links available in the **galAbout_HelpLinks** gallery.

-   Clicking on the “Learn how to customize this app” button navigates to an
    external link which explains on how to make customizations on the app.

-   Clicking on the “Send us your ideas” button navigates to an external link
    where ideas can be posted for the Milestones app.

-   Clicking on the “Engage with community” button navigates to the Power Apps
    Community.

1.  The **conAbout_AppVideo** container contains the video link which provides
    an overview of the Milestones app.

2.  The gallery **galAbout_OtherApps** contains the links to other Microsoft
    apps.

-   Clicking on the “View app” button navigates to the app page in the Microsoft
    Teams app store.

-   Clicking on the “App Overview” button navigates to the App overview video on
    YouTube.

1.  The **conAbout_Version** gives information about the app versioning

*Screen*  
  


![](media/inspection-architecture/3e676e7891834bf5de0bad2a3187e4a4.png)

### Settings Screen 

#### General Section

##### Collections Used

>   None

##### Variables Uses 

1.  **gblParamTeamId** – global variable to set the Planner Group ID from
    parameters

2.  **gblLocTypeSetting** –

3.  **gblManageLocationTypes**- global variable to denote whether the Location
    Types are being edited.

4.  **gblSettingTeamId**- global variable to get the Team ID from the record
    settings.

5.  **gblRecordSettings –** global variable used to set the Team and Channel Id
    to the Area Inspection settings table.

6.  **gblSettingPlannerPlanId –** global variable to get the planner ID from the
    record settings.

##### Detailed Steps

1.  The Users have the feasibility to update whether only Team owners will be
    able to Add Campaigns and select the channel where messages will be posted.

2.  The list of channels in the dropdown are from the **gblParamTeamId**
    variable.

3.  The list of Planner Instances in the dropdown are from the
    **gblSettingTeamId** variable.

4.  The Save button is enabled when the dropdown value selected or the Team
    Owner restricted value is different from the value stored in the variable
    gblRecordSettings (which is set on start of the app).

5.  On click of the Save button, the details are updated in the Area Inspection
    Settings table. The Notification channel and the planner instance details
    are updated using the **gblSettingPlannerPlanId** variable and will navigate
    to the Locations Screen.

6.  Clicking on the cancel button takes the user back to the previous screen.

##### Screens

![](media/inspection-architecture/c32478a9ad28ce6f6b6ee398ed4bd617.png)

#### Location Type Section

##### Collections Used

1.  **colLocTypeSettings** – Used to collect the different setting types
    available in the app.

2.  colGalIconLocationTypes –

3.  **colGalLocationTypes -**

4.  **colTempGalGroup –**

##### Variables Uses 

1.  **gblShowLocationTypeIcons** – global variable to control the visibility of
    the Location type icons.

2.  **gblTypeChanged** – global variable to indicate that the location type has
    been updated

3.  **gblWarningType** – global variable which controls which warning message to
    be displayed.

4.  **colGroupCounter –** used to store the number of grouped locations
    available

5.  **gblDisplayWarning –** global variable to control visibility of Warning
    messages

##### Detailed Steps

1.  The **galAreaTypes** gallery displays the list of available Location Types
    with the Title, Menu Label, Icon and the cover image.

2.  Clicking on each of the fields allow the user to update the values. Clicking
    on the Update Icon button will set the values of **gblShowLocationTypeIcons
    and gblDisplayWarning** to true thus displaying the **galIconPicker**
    gallery**.**

3.  Clicking on any icon the updated icon is stored in the
    **colGalIconLocationTypes** collection and the value of
    **gblShowLocationTypeIcons** to false thus hiding the icon picker and the
    value of **gblTypeChanged** is set to true thus enabling the save button.

4.  A location type can be deleted by clicking the delete icon next to the
    record. Clicking on which the value of the **gblWarningType** is set to
    **locationtypedelete** in case there are no locations associated with the
    type.

5.  Incase there are locations associated to the type, the value of the
    **gblWarningType** is set to **locationtypenodelete** thus displaying a
    relevant message.

6.  Once the user checks the “I understand” checkbox, The delete button will be
    enabled, Clicking on which the type is removed from the
    **colGalLocationTypes** , **colGalIconLocationTypes** collection and from
    the Area Inspection Location Types table.

7.  Clicking on the “+ Add vehicle type” will create a new record in the
    **colLocationTypes**

    Collection with the name, menu label and cover image being blank.

8.  Clicking on the Save button once all the changes are made will update the
    colLocationTypes and Area Inspection Location Types table.

##### Screens

![](media/inspection-architecture/e2aae0147d1de71e9cb503cc3b3e9f9d.png)

![](media/inspection-architecture/15138fd6f14bc6057b02103b25fa3f8b.png)

![](media/inspection-architecture/1a04fd68fc2ee74592037c97bef9b17a.png)

![](media/inspection-architecture/abe336da99a1b4b50a6567581cea5edd.png)

#### Grouped Location Section

##### Collections Used

1.  **colGalGroups** – Used to collect the list of grouped locations

2.  **colLocTypeSettings** – Used to collect the different setting types
    available in the app.

3.  **colGroupCounter** – used to store the number of grouped locations
    available

4.  **colTempGalGroup** –

##### Variables Uses 

1.  **gblTempAddGroupType –**

2.  **gblGroupChanged –** global variable to indicate that the checklist step
    has been updated

3.  **gblDontChangeAreaType –**

4.  **gblSelectedGroup – global variable which denotes the group which seleted**

5.  **gblResetAreaDropdown – global variable to reset the Area Dropdown**

##### Detailed Steps

1.  The **galGroups** gallery displays the list of available Group Locations
    with the Title, Locations and Location Type Label from the **colGalGroups**
    collection in Ascending order.

2.  The dropdown values for the Locations are from the Area Inspection Locations
    table and the Location type values are from the 'Area Inspection Location
    Types table.

3.  Clicking on the “+ Add Group” button will set the values of
    **gblTempAddGroupType** and **gblGroupChanged** and
    **gblDontChangeAreaType** variables to true.

4.  A new record created in **colGalGroups** is set to **gblSelectedGroup**
    variable and the value of **gblResetAreaDropdown** is set to true.

5.  A new grouped location is created with the title, Location and Location type
    values as blank.

6.  A grouped location can be deleted by clicking on the Delete button next to
    the record, clicking on which will update **gblWarningType** variable to
    locationgroupdelete and gblDisplayWarning true displaying the Delete dialog.

7.  Once the user checks the “I understand” checkbox, the delete button will be
    enabled, Clicking on which the group is removed from the Area inspection
    Groups table, the **colGroupCounter** is set to 1 and the **colGalGroups**
    collection is updated.

##### Screens 

![](media/inspection-architecture/82948c8f06b382ee073ad2a374e0ade1.png)

![](media/inspection-architecture/f076f64f353505cc40252e89db5e0239.png)

![](media/inspection-architecture/44f4b663740c0fff6f940af68b08bb0f.png)

#### Customize Experience Section

##### Collections Used

1.  **colLocConfig**–

2.  **colLocTypeSettings –** Used to collect the different setting types
    available in the app.

##### Variables Uses 

1.  **gblTempAddGroupType –**

2.  **gblLabelChanged-** global variable to indicate that the checklist step has
    been updated

3.  **gblWorkType –** used to store the work type value which is in context

4.  **gblSelectedWorkType –** used to store the selected work type

##### Detailed Steps

1.  The **colLocTypeSettings is used to display the list of available setting
    types in the galSettings** gallery.

2.  Users can update the verbiage used in the app. Inspection, Audit and Walk
    are the available options. Clicking on any of these will update the
    **gblSelectedWorkType** variable to the selected value and
    **gblLabelChanged** to true indicating the Label has been changed and thus
    enabling the Save button.

3.  Users can also update the Main and Sub section names stored in the
    **colLocConfig** collection.

4.  Clicking on the Save button will set the value of the **gblWorkType** to
    **gblSelectedWorkType** and update the Area Inspection Labels table**.**

##### Screens

![](media/inspection-architecture/4a2edcdbb218afd52c7ccbed3aae25e6.png)

Collections
-----------

Use a collection to store data that users can manage in your app. A collection
is a group of items that are similar, such as products in a product list.

### Important Functions

1.  **Collect**: The Collect function adds records to a data source.

2.  **Clear**: The Clear function deletes all the records of a collection. The
    columns of the collection will remain.

3.  **ClearCollect**: The ClearCollect function deletes all the records from a
    collection. And then adds a different set of records to the same collection.
    With a single function, ClearCollect offers the combination of Clear and
    then Collect.

| Collection Name             | Description                                                                                                                     | Screen Used                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| colLocalization             | Used to build a Localization Collection based on the User Language App OnStart                                  | App OnStart                                                       |
| colLabelSettings            | Used to collect the labels and icons used in the app (Inspection, Audit and Walk)                                               | App OnStart                                                       |
| colUserSettings             | Used to collect User Settings CDS record if it exists                                                                           | App OnStart                                                       |
| colLocationTypeIcons        | Used to collect the name and order of the icons used in the app                                                                 | App OnStart                                                       |
| colLocConfig                | Used to collect and set the Name and type of the Main Section and Sub section                                                   | App OnStart                                                       |
| colLocationTypeSettings     |                                                                                                                                 |                                                                                   |
| colInspection               | Used to collect the Location of the Area Inspection                                                                             | App OnStart                                                       |
| colPlannerBuckets           | To collect the list of Planner Buckets in a particular plan based on the Plan and Team ID’s                                     | App OnStart                                                       |
| colPlannerTasks             | To collect the list of Planner Tasks in a particular plan based on the Plan and Team ID’s                                       | App OnStart                                                       |
| colLocationTypes            | To collect the Active Area Inspection Locations types                                                                           | OnSelect property of the Edit icon on the Locations screen                        |
| colLocationTypeCounter      | Used to collect and set the Location Type counter to 1                                                                          | OnSelect property of the Edit icon on the Locations screen                        |
| colGalLocationTypes         | Used to collect the Title, UniqueID, Title, Symbol, Order and Photo of a Grouped Location                                       | OnSelect property of the Edit icon on the Locations screen                        |
| colIconLocationTypeCounter  | Used to collect and set the Icon Location Type counter to 1                                                                     | OnSelect property of the Edit icon on the Locations screen                        |
| colGalIconLocationTypes     |                                                                                                                                 | OnSelect property of the Edit icon on the Locations screen                        |
| colGroupCounter             | Used to collect and set the Group counter to 1                                                                                  | OnSelect property of the Edit icon on the Locations screen                        |
| colGalGroups                | Used to collect the Title, Area Type, Record, Unique ID and Sort Order of an Area inspection Group                              | OnSelect property of the Edit icon on the Locations screen                        |
| colRemoveInspections        | Used to collect the selected Inspection record to be removed from the locations                                                 | Onclick property of the Delete button on the Warning screen of the Locations Page |
| colNewLocation              | Used to collect the Name, Location Type and the Primary Image of a newly added Location                                         | OnClick property of the Save button on the Locations Screen                       |
| colTempGalGroup             |                                                                                                                                 | Helper screen , we only have clear                                                |
| colGroupCount               |                                                                                                                                 | Not Available                                                                     |
| colChecklistStepsTemp       | Used to collect the selected Area Inspection checklist steps                                                                    | OnSelect property of a hidden button on the Inspection Forms screen.              |
| colChecklistSteps           | Used to collect the information of the Checklist steps of an Inspection Form                                                    | OnSelect property of the Inspection form button on the Locations screen.          |
| colChecklistStepsOutput1    |                                                                                                                                 | OnSelect property of the Inspection form button on the Locations screen.          |
| colChecklistStepsImage      | To collect the image of the checklist steps on the Inspection from                                                              | OnSelect property of the Inspection form button on the Locations screen.          |
| colPatchSteps1              | To collect all the details of a selected inspection form to duplicate it as a new Inspection form                               | OnSelect property of the Duplicate button on the Inspection forms screen.         |
| colChecklistStepsRemoveTemp | To collect the information of the deleted checklist step of an Inspection form                                                  | OnSelect property of the Save button on the Inspection forms screen.              |
| colCounter                  |                                                                                                                                 | OnSelect property of the Save button on the Inspection forms screen.              |
| colTeamDurations            | Used to collect Date, Start and End times of an Inspection for calculations                                                     | OnVisible property of the Insights forms screen.                                  |
| colBarChartTemp             | To collect the top contributors bar chart last 7 days - count of inspections which are grouped by owner                         | OnVisible property of the Insights forms screen.                                  |
| colBarChart                 | Used to sort and group information from the top contributors bar chart based on the Owner name and Grouped location             | OnVisible property of the Insights forms screen.                                  |
| colLineChartForms           | To Collect the average inspection time by form line chart - inspections time for inspections in the last 7 days grouped by form | OnVisible property of the Insights forms screen.                                  |
| colLineChart                | Used to sort and group information of the average inspection time by form line chart based on the Form ID and Grouped location  | OnVisible property of the Insights forms screen.                                  |
| colLocTypesTemp             |                                                                                                                                 |                                                                                   |
| colInspectionsByLocTypeID   |                                                                                                                                 |                                                                                   |
| colInspectionsByLocType     |                                                                                                                                 | Gallery on the Helper screen                                                      |
| colInspectionsByLocTypeName |                                                                                                                                 |                                                                                   |
| colLocTypes                 |                                                                                                                                 |                                                                                   |
| colPieChart                 |                                                                                                                                 |                                                                                   |

### Global Variables

| Variable Name                   | Type    | Description                                                                                                            |
|---------------------------------|---------|------------------------------------------------------------------------------------------------------------------------|
| gblAppLoaded                    | Boolean | To check whether the App is completely loaded                                                                          |
| gblAppContext                   | Boolean | To check the context of where the app is running (web, desktop or mobile)                                              |
| gblUserLanguage                 | Text    | To check the logged in User’s Language                                                                                 |
| gblFirstRun                     | Boolean | Variable to check whether the app is being run for the first time after installation                                   |
| gblWorkType                     | Text    | Variable to load work type - inspection, walk, or audit, if none exists, then set it to inspection                     |
| gblSelectedWorkType             | Text    | Variable to store the selected Work type.                                                                              |
| gblParamTeamId                  | Text    | To set the Group ID from Planner                                                                                       |
| gblParamChannelId               | Text    | To set the Channel ID from Planner                                                                                     |
| gblThemeDark                    | Boolean | To check whether the Teams theme is set to Dark                                                                        |
| gblThemeContrast                | Boolean | To check whether the Teams theme is set to High Contrast                                                               |
| gblAppManager                   | Boolean | To check the User team role                                                                                            |
| gblRecordUserSettings           | Record  | Variable to use the Oldest Record in case multiple records exist                                                       |
| gblFontSizes                    | Record  | Used to set the font sizes in the app                                                                                  |
| gblPadding                      | Record  | Used to set padding values in the app                                                                                  |
| gblScreenHeightMin              | Number  | Used to set the minimum Screen height of the app                                                                       |
| gblScreenWidthMin               | Number  | Used to set the minimum Screen Width of the app                                                                        |
| gblEditLocation                 | Boolean | Variable Used to control whether a Location can be edited or not                                                       |
| gblView                         | Text    | Variable to set the view as Locations                                                                                  |
| gblViewInspection               | Boolean | Variable to set the Inspection view                                                                                    |
| gblManageLocationTypes          | Boolean |                                                                                                                        |
| gblTempAddLocType               | Boolean |                                                                                                                        |
| gblWarningType                  | Text    | global variable which controls which warning message to be displayed.                                                  |
| gblDisplayWarning               | Boolean | Variable to hide and show the Warning message while deleting the inspection                                            |
| gblAddLocation                  | Boolean | Variable to show and hide the Add location button                                                                      |
| gblShowLocationTypeIcons        | Boolean | Variable to show and hide location type icons                                                                          |
| gblFirstTimeNavigation          | Boolean |                                                                                                                        |
| gblParamTenantId                | Text    | Variable to set the Tenant ID from Planner                                                                             |
| gblParamLocaleId                | Text    | Variable to set the Locale ID from Planner                                                                             |
| gblCheckLabelSettings           | Number  | To get the number of area type labels from the 'Area Inspection Labels (View)                                          |
| gblRecordSettings               | Record  | To check Teams settings for current team and channel ID                                                                |
| gblLocation                     | Record  | Variable to select the first location available under the Location view                                                |
| colCharsWidth                   | Table   | Variable used for auto width of header buttons                                                                         |
| gblNavToSettings                | Boolean | variable to denote navigation to settings from other screens                                                           |
| gblSettingPlannerPlanID         | Text    | Variable to get the planner ID from the record settings                                                                |
| gblSettingTeamId                | Text    | Variable to get the Team ID from the record settings                                                                   |
| gblSettingSharePointLocation    | Text    | Variable to get the SharePoint location from the record settings                                                       |
| gblEditImage                    | Boolean | Variable to edit an image while adding / editing a location                                                            |
| gblForm                         | Record  | Variable to get the checklist steps of the selected Inspection form                                                    |
| gblDontChangeAreaType           | Boolean | Variable to handle whether the Area type should be allowed to change or not                                            |
| gblResetAreaTypeDropdown        | Boolean | Variable used to reset the Area Type dropdown values                                                                   |
| gblSelectedGroup                | Record  | Variable to store the group which is selected                                                                          |
| gblGroupChanged                 | Boolean | global variable to indicate that the group has been updated                                                            |
| gblLocTypeSetting               | Text    |                                                                                                                        |
| gblGalWorkType                  | Text    |                                                                                                                        |
| gblTypeChanged                  | Boolean | Variable to check whether the location type changed or not                                                             |
| gblLabelChanged                 | Boolean | Variable to check whether the label changed or not                                                                     |
| gblAreaChanged                  | Boolean | Variable to check whether the area is changed or not                                                                   |
| gblIssueImageView               | Boolean |                                                                                                                        |
| gblIssueStepImageSelected       | Boolean |                                                                                                                        |
| gblOkImageView                  | Boolean |                                                                                                                        |
| gblOkStepImageSelected          | Boolean |                                                                                                                        |
| gblResetInspectionGal           | Record  | Variable to reset the Inspections gallery                                                                              |
| gblCurrentLocation              | Guid    | Variable to set the Current location while navigating to the locations screen                                          |
| popupVisible                    | Boolean | Variable to hide and show the popup message                                                                            |
| gblLocType                      | Record  | Variable to store the selected location type                                                                           |
| gblTempAddGroupType             | Boolean | Variable to check whether a new group is being created from the settings screen                                        |
| gblResetAreaDropdown            | Boolean | Variable to reset the Area dropdown when a new group is being created from the settings screen                         |
| gblOriginalAreaType             | Record  | Variable to get the Original Area Type for a selected location                                                         |
| gblAddLocationImage             | Image   | Variable to add the selected image while creating a new location                                                       |
| gblIssueImage                   | Record  |                                                                                                                        |
| gblOKImage                      | Record  |                                                                                                                        |
| Grou                            | Boolean |                                                                                                                        |
| gblInspection                   | Table   | Variable used to check whether the Inspection outcome is an Issue while sorting the Inspections on the location screen |
| gblNav                          | Boolean |                                                                                                                        |
| gblEditForm                     | Boolean | Variable to enable the Add Checklist Step button when the form is being edited                                         |
| gblAddForm                      | Boolean | Variable to enable the Add Checklist Step button when a new Inspection form is being created                           |
| gblStepChanged                  | Boolean | Variable to check when a new Step is added under an Inspection form                                                    |
| gblImageChanged                 | Boolean |                                                                                                                        |
| gblFormClick                    | Boolean |                                                                                                                        |
| gblTempAdd                      | Boolean | Variable to add checklist step fields when the User tries to Add a New Step                                            |
| gblFormForGallerySelection      | Record  |                                                                                                                        |
| gblNewFirstForm                 | Record  |                                                                                                                        |
| gblNewForm                      | Record  | Variable to add a new copy of the Inspection form when the Duplicate button is clicked                                 |
| gblEditStepImage                | Boolean | Variable to handle whether the Checklist Step image should be editable or not                                          |
| gblOne                          | Number  |                                                                                                                        |
| gblCountSteps                   | Number  | To check the count of the number of steps once a checklist step is deleted                                             |
| gblMinStepSeq                   | Table   | Variable used to sort the checklist steps in ascending order                                                           |
| gblStepImaged                   | Boolean |                                                                                                                        |
| gblInspectionsCount             | Number  | Variable used to count the total number of inspections to decide if charts or zero state images should be visible      |
| gblTeamAvgTime                  | Number  | Variable to store the Avg time spent by the team on completing the Inspections                                         |
| gblChartView                    | Text    | Variable to set the default value of the Chart view to 7                                                               |
| gblBarChartView                 | Text    | Variable to set the default value of the Bar Chart view to 7                                                           |
| gblFormBarChartView             | Text    | Variable to set the default value of the Form Bar Chart view to 7                                                      |
| gblLineChartView                | Text    | Variable to set the default value of the Line Chart view to 7                                                          |
| gblAppSetting_inputMobileOnWeb  | Boolean | Variables to Scale fonts for mobile-oriented apps, running in desktop                                                  |
| gblAppSetting_inputMobile       | Boolean | Variables to Scale fonts for mobile-oriented apps                                                                      |
| gblAppSetting_inputScaleFontsBy | Number  | Use this variable for scaling all fonts by a fixed amount                                                              |
| gblThemeHiCo                    | Boolean | To check whether the Teams theme is set to High Contrast                                                               |
| gblAppColors                    | Record  | Variable to set the Color value in the app                                                                             |
| gblAppSizes                     | Record  | Variable to set the Size values in the app                                                                             |
| gblAppStyles                    | Record  | Variable to set the Styling values in the app                                                                          |

Inspection App<br>Story 
========================

OnStart 
--------

### Collections involved

1.  **staticLocalizations–** collection of localized text based on user’s
    language**.**

2.  **colMenuAreaTypes –** collection of all area type with addition to ‘All’.

3.  **colAreaTypes –** collection of available areas / assets types on which a
    user can perform inspection and their associated Planner buckets.

4.  **colLabelSettings –** collection of labels for each of the area / asset
    type

5.  **colLocationTypeIcons -** collection of area / asset type icons.

6.  **colWeekInspections –** collection of total inspections in the last 7 days

7.  **colWeekIssues –** collection of total issues in last 7 days

8.  **colTeamDurations –** collection of all durations for the inspections

9.  **colUserDurations –** collection of all durations for the inpections
    completed by current user

### Variables involved

1.  **gblAppLoaded** – global variable to check if the app has loaded
    completely.

2.  **gblAppContext –** global variable to check the context of where the app is
    running.

3.  **gblUserLanguage** – global variable to store the user’s language.

4.  **gblParamTeamId –** global variable to set the Group ID from Planner

5.  **gblParamChannelId –** global variable to set the Channel ID from Planner

6.  **gblRecordSettings –** global variable used to set the Team and Channel Id
    to the Employee Ideas settings table.

7.  **gblPlannerPlanId –** global variable to store the Planner ID

8.  **gblPlannerGroupId –** global variable to store the Team ID

9.  **gblToday- global** variable to store the present day’s date.

10. **gblUserFirstName –** global variable to store the User’s first name.

11. **gblCurrentUserIssueCount –** global variable to store the number of
    inspection issues that are submitted by the current user for the last 7
    days.

12. **gblTotalIssueCount -** global variable to store the total number of
    inspection issues that are submitted for the last 7 days.

13. **gblTeamAvgTime –** global variable to store the team’s average time spent
    on an inspection

14. **gblUserAvgTime –** global variable to store the user’s average time spent
    on an inspection

15. **gblCurrUser –** global variable to store the current user details

16. **The**

17. **gblWorkType –** global variable to fetch work type from settings to use
    inspection, audit, or walk - if there is no setting, use inspection

18. **gblThemeDark –** global variable to set the app theme to dark if the app
    is running in dark theme else use default theme.

19. **gblThemeHiCo -** global variable to set the app theme to High Contrast if
    the app is running in High Contrast theme else use default theme.

20. **gblIsHostClientMobile –** global variable to check if the user is on
    mobile or not

21. **gblAppMobileOnDesktop –** global variable to check if the user is running
    mobile app on desktop

22. **gblMobileMode-** global variable to check if the user is on Android or IOS

23. **gblCheckLabelSettings** – global variable to check settings record to get
    the labels / verbiage in the app, if there is no such setting app to use
    Area and Area type, else app will get the labels / verbiage it from the
    settings record.

24. **areaLabel –** global variable to hold the verbiage for ‘Area’

25. **areaTypeLabel -** global variable to hold the verbiage for ‘Area Type’

### Detailed Steps

1.  When a user accesses the app, **gblAppLoaded** is set to false. The user’s
    language code is stored in **gblUserLanguage**, with English - US being the
    default one. The gblAppContext where the app is running.

2.  The user’s language is then used to collect localized text used throughout
    the app (e.g. label and button text) in **staticLocalizations** collection.

3.  The Group ID and Channel ID received from Parameters are stored in the
    **gblParamTeamId** and **gblParamChannelId** variables, respectively.

4.  The settings record is fetched using **gblParamTeamId** and
    **gblParamChannelId** variables and stored in **gblRecordSettings**
    variable.

5.  The Planner and Team ID’s are stored in **gblPlannerPlanId** and
    **gblPlannerGroupId** variables.

6.  The app checks for the theme of the Teams and adopt to the Team’s theme by
    knowing the parameters from **gblThemeDark and gblThemeHiCo**

7.  The inspections that are created from last 7 days are being collected in to
    **colWeekInspections** and the issues among these are collected in to
    **colWeekIssues** for statistics that will be display on the first screen of
    the app.

8.  The inspection’s durations for whole team and current user are being
    collected at **colTeamDurations** and **colUserDurations** respectively for
    displaying the statistics of average team’s duration vs current users
    average duration for completing an inspection for last 7 days.

9.  The verbiage used across the app are stored in at **arealabel** and
    **areaTypeLabel** which is fetched from the settings record.

### Welcome Screen<br>

#### Collections involved

1.  **colWeekInspections –** collection of total inspections in the last 7 days
    [works only when the user completes the inspection and return to this
    screen]

2.  **colWeekIssues –** collection of total issues in last 7 days [works only
    when the user completes the inspection and return to this screen]

3.  **colTeamDurations –** collection of all durations for the inspections
    [works only when the user completes the inspection and return to this
    screen]

4.  **colUserDurations –** collection of all durations for the inspections
    completed by current user. [works only when the user completes the
    inspection and return to this screen]

5.  **colPlannerTasks –** collection of planner tasks associated to the planner
    that the application is associated to.

6.  **tasksforme –** collection of planner tasks owned by current user

7.  **tasksforall –** collection of all planner tasks

8.  **overdue –** collection of all overdue tasks owned by the current user

#### Variables involved

1.  **gblTotalInspectionCount-** global variable to store the total number
    active inspections for the last 7 days

2.  **gblCurrentUserInspectionCount –** global variable to store the number of
    active inspections submitted by current user for the last 7 days.

3.  **gblCurrentUserIssueCount –** global variable to store the number of
    inspection issues that are submitted by the current user for the last 7
    days.

4.  **gblTotalIssueCount -** global variable to store the total number of
    inspection issues that are submitted for the last 7 days.

5.  **gblTeamAvgTime –** global variable to store the team’s average time spent
    on an inspection

6.  **gblUserAvgTime –** global variable to store the user’s average time spent
    on an inspection

7.  **gblCurrUser –** global variable to store the current user details

#### Detailed Steps

1.  **gblCurrUser** is used get the first name of the current user and to greet
    the user is greeted with a welcome message on the Insights screen.

2.  **tasksforme, tasksforall** and **overdue** global variables are used in to
    show the planer stats

3.  **gblTotalInspectionCount** and **gblCurrentUserInspectionCount** are used
    to compare the total inspections submitted by the team vs total inspections
    submitted by the current user for the last 7 days. (used only when the user
    returns to this screen after submitting an inspection)

4.  The inspections that are created from last 7 days are being collected in to
    **colWeekInspections** and the issues among these are collected in to
    **colWeekIssues** for statistics that will be display on the first screen of
    the app. (used only when the user returns to this screen after submitting an
    inspection)

5.  **gblTotalIssueCount** and **gblCurrentUserIssueCount** are used to compare
    the total inspection issues submitted by the team vs total inspection issues
    submitted by the current user for the last 7 days. (used only when the user
    returns to this screen after submitting an inspection)

6.  The inspection’s durations for whole team and current user are being
    collected at **colTeamDurations** and **colUserDurations** respectively for
    displaying the statistics of average team’s duration vs current users
    average duration for completing an inspection for last 7 days (used only
    when the user returns to this screen after submitting an inspection)

7.  **gblTeamAvgTime** and **gblUserAvgTime** are used to compare the average
    inspection time by the team vs average inspection time by the current user
    for the last 7 days. (used only when the user returns to this screen after
    submitting an inspection)

#### Screens<br>

![](media/inspection-architecture/a1c8ee64a05404c9b96ca8ecfad747bf.png)

### Items Screen

#### Collections Involved

1.  **colMenuAreaTypes-** collection of all area/asset/Item types including
    ‘All’ as a type where ‘All’ is used to show all the areas/assets/items
    without filtering them with associated Type.

2.  **colSelectedLocation –** collection of the selected area/asset/item

3.  **colFormChecklistSteps-** collection of checklist steps that are going to
    be used for the inspection if there is only one Checklist (form) associated
    to the area’s/ asset’s / item’s type.

4.  **colChecklistSteps-** collection of checklist steps associated to selected
    checklist

#### Variables involved

1.  **gblSkipFormNav –** global variable to control whether the user should be
    navigated to the forms screen or directly to the checklist overview screen.

2.  **gblFormStepsCount** - global variable to store number of checklist steps
    in the selected form.

3.  **gblDisplayNoStepWarning –** global variable to display warning if the
    number of checklist steps for the selected form is zero

4.  **gblSelectedLocation –** global variable to store the selected area / asset
    / item

5.  **gblSelectedChecklist –** global variable to store the checklist associated
    to the type of the selected area / asset / item. Applicable only when there
    is a single checklist for the area / asset / Item type

#### Detailed Steps

1.  **colMenuAreaTypes** is used to show the available area / asset / item types
    by its label and the text will be truncated if the length of the text is
    more than nine letters.

2.  All the areas / assets / items are shown by default on this screen and user
    can pick any area/ asset / item to start the inspection

3.  On selecting any of the area / asset /item type by the menu, the list of the
    areas/ assets / items will be filtered based on the type selected.

4.  On selecting any of the area /asset/ item it is stored at
    **gblSelectedLocation**, if there is only one checklist associated to the
    type then the checklist is stored at **gblSelectedChecklist.**

5.  The associated checklist steps of **gblSelectedChecklist** is collected in
    to **colFormChecklistSteps.**

6.  Based on the number of associated Checklists for the
    **gblSelectedLocation,** the app navigates to either ‘Forms Screen’ in case
    if there are more than one checklist for the type the
    **gblSelectedLocation** is associated to, or navigates to ‘Overview Screen’
    if there is only one checklist.

#### Screens<br>

![](media/inspection-architecture/8bdd264d6bc9e74339dc17086bb46383.png)

### Forms Screen

#### Collections Involved

1.  **ColGroupFroms-** collection of checklists associated to the selected area
    / asset / item’s type.

2.  **colFormChecklistSteps –** collection of checklist steps associated to the
    selected checklist.

#### Variables involved

1.  **gblFormStepsCount -** global variable to store number of checklist steps
    in the selected form.

2.  **gblDisplayNoStepWarning –** global variable to display warning if the
    number of checklist steps for the selected form is zero

3.  **gblSelectedChecklist –** global variable to store the selected checklist.

#### Detailed Steps

1.  On select of any checklist from the available list, **gblSelectedChecklist**
    stores the seleted checklist and the associated checklist steps are
    collected at **colFormChecklistSteps.**

2.  If the checklist steps count if less than or equal to ‘0’ then the app shows
    a warning message as with no steps the user can’t perform an inspection and
    this behavior is controlled by **gblDisplayNoStepWarning** variable.

3.  If the checklist steps count is greater than ‘0’, then the app navigates to
    ‘Overview Screen’.

#### Screens

![](media/inspection-architecture/5e42b576e9b8e05ae2ff415d5c4b8235.png)

![](media/inspection-architecture/e1831856c7ee75bbf3caaca011d1632b.png)

### Overview Screen

#### Collections Involved

1.  **colFormChecklistSteps** - collection of checklist steps that are
    associated to the selected checklist

#### Variables involved

1.  **gblLocationType –** global variable to store the selected area’s / asset’s
    / item’s type.

2.  **gblSelectedLocation –** global variable to store the selected area/ asset
    / item

#### Detailed Steps

1.  On visible of this screen **gblLocationType** is set to the selected area’s
    / asset’s / item’s type.

2.  The screen shows the image of the selected area/ asset/ item using
    **gblSelectedLocation.**

3.  The list of checklists is displayed in a sequential order using the
    collection **colFormChecklistSteps.**

4.  User can either select any of the checklist step to navigate to inspection
    screen with the focus of selected checklist step.

5.  Or the user can click on ‘Begin Inspection’ to start the inspection in the
    sequential order shown.

#### Screens<br>

![](media/inspection-architecture/0adaf12bfe1bbec123efe09e7cac0541.png)

### Checklist Steps Screen

#### Collections Involved

1.  **colActiveInspections**- collection of all active inspections

2.  **colLastInspection –** collection of inspection details used to create
    inspection record.

3.  **colChecklistSteps** - collection of checklist steps.

4.  **colLastInspectionSteps –** collection of checklist steps for the
    inspection being carried out.

5.  **colStepDetails -** collection of variables to control visibility of sub
    components of a checklist step like notes, photo etc..

6.  **colStepOutcomes – c**ollection to hold outcome and notes of inspection
    steps.

7.  **colImages –** collection to store the images uploaded to the inspection
    step.

8.  **colAreaPlannerTasks –** collection to store planner task details.

#### Variables involved

1.  **gblSelectedStepImage –** global variable used to enlarge the image
    uploaded.

2.  **gblViewEnlargedImage –** global variable used to control the visibility of
    enlarged image.

3.  **gblLastInspection -** global variable to hold the newly created
    inspection.

4.  **gblInspectionPatchComplete –** global variable to check if the checklist
    steps are updated with step outcomes into CDS.

#### Detailed Steps

1.  On visible of this screen the checklist steps are loaded for the inspection
    from **colChecklistSteps**

2.  User will select the outcome and add notes and the details are stored at
    **colStepOutcomes.**

3.  **colStepDetails** is used to control the visibility of controls while
    performing an inspection.

4.  When the user uploads an image for an inspection step, the images will be
    stored at **colImages**

5.  Once all the checklist steps are completed by the user, the user proceeds to
    next screen by selecting ‘Review Inspection’ button.

#### Screens<br>

![](media/inspection-architecture/2c35513724b34a0fffdcc0459a5c5d49.png)

### Review Screen

#### Collections Involved

1.  **colLastChecklistSteps** - collection of checklist steps that are
    associated to the Inspection being carried out.

2.  **colStepOutcomes – c**ollection to hold outcome and notes of inspection
    steps.

3.  **colLastInspection –** collection of recent inspection being carried out.

4.  **colLastInspectionSteps –** collection of inspection steps that are
    associated to the inspection being carried out.

5.  **colImages –** collection to store the images uploaded to the inspection
    step.

6.  **colAreaPlannerTasks –** collection to store planner task details.

#### Variables involved

1.  **gblLastInspection –** global variable to hold the newly created
    inspection.

#### Detailed Steps

1.  On visible of this screen it shows all the inspection steps associated to
    the inspection being carried using **colLastChecklistSteps**.

2.  A visual representation based on the outcome of the inspection step will be
    shown on this screen using the collection **colStepOutcomes,** so the user
    knows if any inspection step is incomplete.

3.  If all the steps are steps are completed, the user can click on ‘submit
    inspection’ else can click on ‘continue inspection’ button to complete the
    missed inspection steps.

4.  Onclick of ‘submit inspection’**, colLastInspection** collection is cleared
    so that the collection will be ready for next inspection. And using
    ‘**colLastChecklistSteps**’ collection the app will create inspection steps
    and will associate them to the inspection which will have the information of
    the step outcomes along with the notes.

5.  If there are any images attached to any inspection step, using
    ‘**colImages’** collection the app will create inspection image records and
    will associate to the inspection steps respectively.

6.  If there are any planner tasks for the inspection, using
    ‘**colAreaPlannerTasks’** collection the app will create inspection tasks
    records which will help in associating the planner tasks to the inspection.

#### Screens<br>

![](media/inspection-architecture/4077e596f9002da4ff6bcc6829fa3c99.png)

