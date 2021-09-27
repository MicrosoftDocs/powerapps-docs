---
title: Add and configure the timeline control in Power Apps | MicrosoftDocs
description: "Learn how to add and configure the timeline control to use in a model-driven app"
ms.custom: ""
ms.date: 09/23/2021
ms.reviewer: "matp"
ms.service: powerapps
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "how-to"
author: "lalexms"
ms.subservice: mda-maker
ms.author: "laalexan"
manager: "kvivek"
tags: 
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Set up the timeline control

[!INCLUDE [cc-data-platform-banner](../../includes/cc-data-platform-banner.md)]

The timeline helps app users see all activity history. The timeline control is used to capture activities like notes, appointments, emails, phone calls, and tasks to ensure that all interactions with the related table are tracked and visible over time. Use the timeline to quickly catch up on all of the latest activity details.

:::image type="content" source="media/timeline-on-account-form.png" alt-text="Timeline in app for the account table main form":::

The timeline control provides an easy and immersive experience to view information related to a table, such as accounts or contacts, which gives users a better understanding and helps them deliver more personalized service in an efficient and effective manner.

This experience gives app makers the ability to configure the information displayed on the timeline to help users access information and create new activity records, such as emails and tasks directly from the timeline quickly so they can deliver more personalized service.

## Add a timeline

A timeline control is located on a form within table. Any timeline control that's on a form can be configured. For example, an account table has three standard forms, and each of those forms can have a timeline that can be configured. Notice that there can be only one timeline per form.

### Display a custom table in a timeline

For custom tables to appear in the list of activities that can be added to a timeline control, make sure that when you create the table you configure the following settings:
- Set the table **Type** as **Activity**.
- Check the **Enable attachments** setting if you want app users to be able to add attachments and notes to the custom activity record.

More information: [Create a custom table](../data-platform/data-platform-create-entity.md)

### Add the timeline component to a form

1. Sign into [Power Apps](https://make.powerapps.com), and then go to the **Dataverse** section.
1. Select **Tables**, open the table you want, and then select the **Forms** tab.
1. Open the form where you want to add or configure a timeline.
1. In the form designer, select **Components** from the left navigation, and then scroll down to the **Timeline** component on the left side. Drag and drop it into a section on the form.
   ![Adding or removing a timeline from an entity form.](media\timeline-add-or-remove-entity-from-form-1b.png "Adding or removing a timeline from an entity form")
1. Make the changes you want to the timeline settings. More information: [Configure the timeline component](#configure-the-timeline-component)
1. Before you can view any configuration changes on the table form, you must save and publish your updates on the timeline component. Select **Save**, and then select **Publish** to make your form changes available on the table form for the environment.

Note the following when you work with the timeline control in the form designer.
- If the timeline control is unavailable to add to a form, it means a timeline already exists on the form. You can only have one timeline per form.
- To remove the timeline component from a form, select the **Timeline** component area, and then press the Delete key.
- Since the timeline component relies exclusively on underlying related data, **Almost there** is displayed in the timeline section.
- Because you are in a create and/or edit state on the form, there is no underlying data, so the timeline section is blank in the form designer.

## Configure the timeline component

The timeline component is rich in features and functionality that can be configured and tailored to support specific business needs. The timeline is comprised of features and functionality that you configure in the timeline component, which is then displayed in the table form.

### Display options

This section describes the settings available in the Display options area of the timeline control settings.

#### Timeline component name

The **Name** column under the **Properties** tab in **Display options** is the unique name of the timeline control and is only used by the app maker to reference.

>[!NOTE]
> - The **Name** column has limitations. For example, you can't use spaces between words. Instead, you must use an underscore (_)
> - You can't change the default heading label that is displayed as **Timeline** on the form during app runtime.

#### Records shown on page

This section allows you to control the number records that appear before displaying **Load more** at the bottom of the section.

|Form designer configuration View || Form designer display View |
|-------------------|-|--------------|
![Configure Records shown on page](media\timeline-records-shown-on-page-display-options-1a.png "Configure Records shown on page")| | ![Display Records shown on page](media\timeline-records-shown-on-page-display-options-1b.png "Display Records shown on page")|
|The default setting on the **Records shown on page** column is set to 10 records, but you can change it to display up to 50 records. || 1. Per the default setting shown in this example, the form displays a maximum of 10 records. <BR> 2. Once records exceed 10, the **Load more** option appears at the bottom of the form.|
|||

#### Record types to show

There are three primary record types: Activities, notes, and posts. All record types are enabled by default.

- Activities. Activities can have a large number of customizable subactivity record types to support business needs. Depending on what you've installed, the administrator can create, add, and display a number of different customized subactivity record types under the **Activity** section of the dropdown menu on the timeline.
- Notes. Notes allow you to capture details related to the table record. For example, you can use notes to capture thoughts, summarize information, and provide feedback on a case, and then update the case details later.
- Posts There are two types of posts: auto and user:
   - **Auto Posts** are system-generated posts that notify you of account activity that has occurred.
   - **User Posts** allow you to leave a message for another user on a record.
   > [!NOTE]
   > Posts require a Dynamics 365 app, such as Dynamics 365 Customer Service.

##### Enable these record types to be displayed in the timeline

|Form designer configuration view | | Form designer display view  |
|-------------------|--|--------------|
|![Display options for Timeline](media\timeline-record-types-shown-display-options-2b.png "Display options for Timeline")||![Display options - Record types shown](media\timeline-record-types-shown-display-options-3b.png "Display options - Record types shown")|
|To enable **Record types shown** for **Activities**, **Notes**, and **Posts** on a form, check the box next to the record type.||1. To confirm that the record type is displaying on the form, select **Create a timeline record** ![Create a timeline record icon.](media\timeline-create-a-record-icon.png "Create a timeline record icon") in the top-right nav in the timeline, and a dropdown menu that displays the list of enabled record types will appear.<BR>2. When **Activities** are enabled, you'll see **Activity** record types for appointments, email, phone calls, and tasks.<BR> 3. When **Notes** are enabled, you'll see the note record types on the form.<BR> 4. When **Posts** are enabled, you'll also see the post record types on the form.|

> [!Note]
> Activities and notes are standard entities. If additional solutions have been imported into the environment, other tables may also be displayed.

#### Activity, notes, post icons and date / timestamp display on timelines

The timeline shows a simple icon before the activity, note, post, and custom table, making it easy for you to identify the record type.

Dates and timestamps always appear on each record on the bottom-right side of the preview, and are always viewable.

### Advanced

This section describes the settings available in the Advanced area of the timeline control settings. The **Advanced** settings apply to all record types.

When enabling and disabling **Advanced** features, you won't be able to view updates (even though it may appear that there's activity occurring on the timeline component) until you save and publish your configuration updates and refresh the table form.

**Advanced** covers common settings that span across an activity, note, or post, which are the three primary record types that appear in the timeline section.

#### Quick entry record type and sort order default

The following is a detailed overview of the **Advanced** configuration options, starting with selecting your **Quick entry record type**:

|Form designer configuration View | |Form designer display View |
|-------------------|--|------------|
|![Configure Quick entry record type and sort order default](media\timeline-quick-entry-record-type-and-sort-order-default-display-settings-advanced-2a.png "Configure Quick entry record type and sort order default")| |![Display Quick entry record type and sort order default](media\timeline-quick-entry-record-type-and-sort-order-default-display-settings-advanced-3b.png "Display Quick entry record type and sort order default")|
|1.Select **Advanced** to expand this area in the configuration view. The **Quick entry record** type provides you with quick access to create either a **Note** or a **Post**. The default setting for this setting is set to **Notes**.<BR> 2.The **Sort order default** setting controls the order of how all data is sorted on the timeline. The default setting for this setting is set to Descending. ||1. When you select **Notes**, it will display under the **Search** bar in the timeline. Also, you will see a paperclip ![Paperclip icon.](media\timelilne-paperclip-icon.png "Paperclip icon") icon that allows you to attach files. You can only attach files to Notes.<BR>2.	If you select **Posts** it also will display under the **Search** bar in timeline.|

#### Enable filter pane

Using filters provides a quick option to sort and look for specific data quickly.

|Form designer configuration View | |Form designer display View |
|-------------------|--|-------------|
|![Configure filter pane](media\timeline-enable-filter-pane-display-options-advanced-2a.png "Configure Enable filter pane")||![Enable filter pane](media\timeline-enable-filter-pane-display-options-advanced-3b.png "Enable filter pane")| |The **filter pane** setting allows you to enable or disable filter functionality on timeline. It is enabled by default.|| Enable the **filter pane** by checking the box next to the setting.  This will enable the filter icon to display on the timeline.  <BR><BR> To disable the **filter pane**, clear the box next to the setting and the filter icon will no longer appear on the timeline.   |
|||

#### Filter records on timeline

Filters are valuable for sorting data. You can quickly filter activities, notes, and posts with multiple options to see what matters to you. The filter is available for the activities, notes, posts, and custom tables that are present in the timeline. The timeline filters and displays the records and the count that are present in the timeline.

When you select filters based on an activity status then those activities, notes, and posts are displayed in your timeline. You can customize data using data filters and either choose to keep filters in place or clear them when you are done.

- When the **Filter** icon is transparent ![Transparent filter icon.](media\timeline-filter-icon.png "Transparent filter icon") on the table form, it means no items have been selected, therefore the filter pane is empty.<br>

- When the **Filter** icon is dark ![Dark filter icon](media\timeline-filter-applied-1.png "Dark filter icon"), it means filters have been set. To view which filters have been designated, select the ![Filter icon](media\timeline-filter-icon.png "Filter icon") **Filter** icon and the filter pane will display the filters that have been set.</li>

- Choose how you want to filter data by selecting the box next to the filter.<br>

- Clear filters by selecting the **Clear all filters** ![Clear all filters icon.](media\timeline-clear-all-filters-icon.png "Clear all filters icon") icon on the filter pane.

The following category and subcategory options are available on the filer menu:

|Category                   |Subcategory                            |
|---------------------------|----------------------------------------|
|Record type                |<li>Notes</li>                     <li>Activities</li><li>Posts</li>                     |
|Activity type              |<li>Appointment</li><li>Campaign Activity<sup>1<sup></li> <li>Campaign Response<sup>1<sup></li><li>Email</li><li>Fax</li><li>Case Resolution<sup>1<sup></li><li>Letter</li><li>Opportunity Case<sup>1<sup></li>   <li>Order Case<sup>1<sup></li><li>Phone Call</li><li>Quote Close<sup>1<sup></li>           <li>Recurring Appointment</li><li>Social Activity</li><li>Task</li>   <li>Project Service Approval<sup>1<sup></li><li>Booking Alert<sup>1<sup></li><li>Conversation</li><li>Session</li><li>Customer Voice survey invite<sup>1<sup></li><li>Customer Voice survey response<sup>1<sup></li><li>Custom activities (made available by imported solutions)</li>|
|Activity status            |<li>Active</li><li>Overdue</li>       <li>Closed</li>                         |
|Activity status reason     |Allows you to filter using specific status reasons. The values are a unique list of all of the status reasons from the activities in the timeline. The status reasons will change depending on the activity. If there are multiple activities on the timeline that have the same status reason, it will be reflected once, but then the number next to it will indicate how many occurrences of that status reason appear in the timeline.                       |
|Activity due date (active) |<li>Next 30 days</li><li>Next 7 days</li><li>Next 24 hours</li><li>Last 24 hours</li><li>Last 7 days</li>   <li>Last 30 days</li>                   |
|Posts by                   |<li>Auto post</li><li>Users</li>                          |
|Modified date              |<li>Last 24 hours</li><li>Last 7 days</li><li>Last 30 days</li>                   |

<sup>1</sup> Requires a Dynamics 365 app

#### Expand filter pane 

The **Expand filter pane** setting provides quick access to sorting options within the timeline.  It is enabled by default.

|Form designer configure view | |Form designer display view |
|---------------|--|------------|
|![Configure filter pane ](media\timeline-expand-filter-pane-display-options-advanced-3a.PNG "Configure filter pane")| |![Enable filter pane ](media\timeline-expand-filter-pane-display-options-advanced-2b.PNG "Enable filter pane")| 
The <B>Expand filter pane by default</B> setting displays an expanded filter pane at the top of the form anytime it is opened and refreshed.  It is disabled by default.||Enable the **Expand filter pane** by checking the box next to the setting. This enables the filter pane to appear at the top of the form anytime the form is opened and refreshed.<BR><BR>To disable the **Expand filter pane**, clear the box next to the setting and the filter pane will not appear on the timeline.|

#### Enable search bar

You can search for records in the timeline. When you search for a phrase in the timeline, it searches in the title of the record or body and description column of the record then displays the record for you.

|Form designer configure view | | Form designer display view |
|---------------|-|-------------|
|![Configure search bar](media\timeline-enable-search-bar-display-options-advanced-3a.PNG "Configue search bar")| |![Enable search bar](media\timeline-enable-search-bar-display-options-advanced-2b.PNG "Enable search bar")| 
|Select **Enable search bar** to enable the **Search timeline** bar functionality. It is enabled by default.||Enable the search bar setting to display a **search bar** at the top of the timeline.<BR><BR>Disable the search bar by clearing the box next to the setting and the search bar won't appear on the timeline.| 

#### Expand all records in timeline

**Expand all records by default** displays all activities in an expanded view in timeline. 

|Form designer configure view |  |Form designer display view |
|---------------|---|------------|
|![Configure Expand all records in timeline](media\timeline-expand-all-records-display-options-advanced-2a.PNG "Configure Expand all records in timeline")||![Enable Expand all records in timeline](media\timeline-expand-all-records-display-options-advanced-2b.PNG "Enable Expand all records in timeline")||
|Select **Expand all records** to set the default view to display all records in the expanded view format in the form each time the timeline is opened. **Expand all records** is disabled by default.||1. When enabled, the **Expand all records** icon is displayed in the top-right corner of the timeline nav. <BR>2. Records can be expanded or collapsed by using the **Expand all records** icon. When expanded, all records are displayed in the expanded view in the form each time it is opened. When you clear **Expand all records**, it no longer displays activities in an expanded view.<BR><BR> When disabled, the **Expand all records** icon won't display in the top-right nav of the timeline. Records will always be displayed in a collapsed view.|
  
#### Edit filter pane

You can configure the default filters that are applied when a form loads or is refreshed using **Edit filter pane**. Remove filter groups by turning the setting **Off**. Users can remove the default filters to see all the records unless **Enable filter pane** is disabled.

![Edit filter pane.](media\edit-filter-pane.png "Edit filter pane setting")

#### Expand records with images in timeline

You can send and receive records with images, but they won't display when the record is collapsed. Records with images must be expanded to be viewed.

![Expand records with images in timeline.](media\timeline-expand-records-with-images-display-optiones-advanced-2b.png "Expand records with images in timeline")
1. Records when collapsed provide a visual summary. To expand an individual record, select anywhere on the timeline record to expand and collapse a record view. In the bottom-right corner of the record there is a caret:
   - When the caret is facing downward (˅), the record is collapsed.
   - When the caret is facing upward (^), the record is expanded.

2. Records with images might display the following notice: <BR>
   This email has been blocked due to potentially harmful content. View full email content.
3. When you select the message, the warning goes away and the image appears.

If you don’t see a message and the image isn't displayed, see [Timeline FAQs](/power-platform/user/faq-for-timeline-and-activity.md) for more information.

#### Enable “What you’ve missed” summary

**What you’ve missed** helps you stay on top of updates and changes made to records by displaying updates at the top of the timeline when you access a record.

|Form designer configure view | | Form designer display view|
|---------------|--|-------------|
|![Configure “What you’ve missed” summary](media\timeline-what-you-missed-display-options-advanced-11a.png "Configure “What you’ve missed” summary")| |![Disable “What you’ve missed” summary](media\timeline-what-you-missed-display-options-advanced-11b.png "Disable “What you’ve missed” summary") |
|The **What you’ve missed** setting displays new records you haven't seen. It's disabled by default. To enable it, select the box next to the setting. To disable it, clear the box next to the setting ||Once enabled, when you view an account record, a box appears at the top of the timeline section, notifying you of updates.<BR><BR> When disabled, notifications aren't displayed when you access an account.| 

### Record settings

This section describes the settings available in the Record settings area of the timeline control settings. The **Record types to show** setting determines the record types that are affected by the **Record settings** described here.

**Record settings** let you manage the settings within the record types.
- The **Activities** record type is tied to **Activities** in record settings.
- **Notes** record type is tied to **Notes** in record settings.
- **Posts** record type is tied to **Posts** in record settings.

To enable or disable a record type, simply select or clear the checkbox. Then, that record type will either display or no longer appear in the **Record settings** section.

![Display options - Advanced - Record Settings.](media\timeline-record-settings-display-options-advanced-1a.png "Display options - Advanced - Record Settings")

1. When **Posts** is checked in the **Record types to show** section, it's enabled in the **Record settings** section below.
2. When **Posts** is cleared in the **Record types to show** section, it's disabled in the **Record settings** section below.

#### Configure activity record types

When you expand the **Activities record settings** on the timeline component section a list is displayed of all the activity types that can be either enabled or disabled on the table form.

|Form designer configuration view ||Form designer display view|
|-------------------|-|-----------|
|![How to configure activity record types](media\timeline-how-to-configure-activity-record-types-display-options-advanced-11a.png "How to configure activity record types")||![Activity record types](media\timeline-how-to-configure-activity-record-types-display-options-advanced-11d.png "activity record types")|
|1. Expand and view **Activities** under the **Record settings** section using the caret (^).<BR> 2. A list of **Activity types** is displayed in the expanded view. <BR> 3. You can enable or disable an activity by selecting an activity type. For example, enable **Email**.<BR><BR> To enable an **Activity type**, check the box next to **Enable** and select **Done**.<BR><BR>To disable an **Activity type**, clear the box next to **Enable**, and then select **Done**. This disables all other items in the box and disables the activity type from displaying on the timeline.  This also disables the activity type from being created or viewed in the timeline.  || 1. When enabled, an **Activity type** appears under the **Create a timeline record** ![Create a timeline record.](media\timeline-create-a-record-icon.png "Create a timeline record"). <BR> 2. The activity type is displayed as an option the user can choose from the dropdown menu. <BR> 3. Also, the **Activity type** record is displayed in the body of the timeline.| 

> [!NOTE]
> A check mark appears to the right, next to enabled **Activity types**. Additional record type settings are disabled until they're enabled under that specific record type.

#### Enable status tags on activity record types

Status tags match the status filter that display in the timeline to help you to see at a glance if the state of an activity record is **Active**, **Overdue**, or **Closed** on an activity, such as a task, appointment, or email. The administrator can enable or disable status tags for any **Activity type** in the **Record settings**. Status tags are enabled by default.

|Form designer configuration view | | Form designer display view|
|-------------------|--|------------|
|![Enable status tags on activity record types](media\timeline-enable-status-tags-on-activity-record-types-display-options-advanced-11a.png "Enable status tags on activity record types")||![Display status tags on activity record types](media\timeline-enable-status-tags-on-activity-record-types-display-options-advanced-11b.png "Display status tags on activity record types")|
| To display email status tags, check the box next to **Enable status tag**. ||  When enabled, status tags such as **Active**, **Overdue**, or **Closed** appear in the timeline next to that activity record.    |

#### Enable the ability to create directly from timeline

App makers have the ability to enable activity types so they can be created directly on the timeline. Having the ability to quickly select and create an activity, such as email, tasks, and appointments, helps to streamline productivity.  

|Form designer configuration view | | Form designer display view |
|-------------------|--|-------------|
|![Configure the ability to create directly from timeline](media\timeline-enable-ability-to-create-directly-from-timeline-11a.png "Configure the ability to create directly from timeline") || ![Display the option to create directly from timeline](media\timeline-enable-ability-to-create-directly-from-timeline-11b.png "Display the option to create directly from timeline") |
|	To allow users to create activity types directly from the timeline, check the box next to **Create directly from timeline**.||	When enabled, the activity type will appear in a dropdown box on the  **Create a timeline record** ![Icon for create a timeline record.](media\timeline-create-a-record-icon.png "Icon for create a timeline record") icon in the top-right of the timeline.|

#### Create and use card forms in timeline

Records are displayed using the default setting for each activity type. However, if you want to display record information for an appointment or email, for example, you can either edit the existing card form, use a different card form from record settings, or customize your own.

|Form designer configure view ||Form designer display view|
|---------------|--|------------------|
|![Create and use card forms in timeline](media\timeline-create-and-use-card-forms-display-options-advanced-101a.png "Create and use card forms in timeline")||![Display the option to create and use card forms in timeline](media\timeline-create-and-use-card-forms-display-options-advanced-1111b.png "Display the option to create and use card forms in timeline") |
|You can change the default card settings to a different card form if one has been created.  ||If you create a new card form, you must go to the parent table and add the new form of card type there before it will appear in the timeline list for configuration.  If **Default** is displayed, you are not using the card form.  You can not use the **Email card form** in a timeline unless you select and publish it first.|

> [!NOTE]
> Not all activity types allow you to create card types, so the default selection will be you’re only option for those records.

#### Customize a card from within timeline

All card forms are separated into the following four sections:

![Display options - Advanced - How to customize a card in timeline.](media\timeline-customize-card-form-display-option-advanced-2a.png "Display options - Advanced - How to customize a card in timeline")

Legend

1. **ColorStrip Section**: This section doesn't appear on the timeline record. The **ColorStrip** is located on the left of the card form.
2. **Header Section**: This section is displayed n the timeline record; however, only the first two columns are displayed on the timeline record. For this example, only the **Subject** and **Modified On** columns are visible.
3. **Details Section** This section is displayed on timeline record; however, only the first three columns are displayed on the timeline record. For this example, only the **To**, **CC** and **Description** columns are visible on the timeline record.
4. **Footer Section.** This section isn't displayed on the timeline record.
5. **Table Columns** You can select which columns you want to add to your card form from the column options listed on the right. You can customize your card form by dragging and dropping the columns you want to use into the sections you want that column to appear in on the timeline record.

Each individual card form must be customized for each activity record, such as email, tasks, posts, and so forth.

**Header Section**

The card **Header** displays the title/subject in your timeline email form. You can have up to six columns in the **Header** section, but only the first two columns will be seen on the timeline record. Empty columns will be ignored by the form in all sections.

|Form designer configuration view || Form designer display view|
|-------------------|-|------------|
|![Customize a card form in timeline - Header](media\timeline-create-and-use-card-forms-header-1a.png "Customize a card form in timeline - Header")||![Card form in timeline - Header Display](media\timeline-create-and-use-card-forms-header-display-1a.png "Card form in timeline - Header Display")|
| **Column 1** <BR>1. Regardless of the column you choose for this section, it will appear as a bold header at the top of your timeline record. For this example, we selected **Subject** for this column. <br><BR>**Column 2** <BR>2. Again, regardless of the column you choose for this section, this column will always appears in the bottom-right corner of the timeline record. For this example, **Modified On** is selected for this column. ||**Column 1**<BR>1. Column 1 from the card header is always displayed in this section of the timeline record.<BR><BR>**Column 2**<BR>2. Column 2 from the card header is always displayed in this section of the timeline record. |  	

**Details Section**

The card **Details** section displays in the body of your the timeline email record. You can have up to four columns in the **Details** section, but only the first three columns are viewable on the timeline record.

|Form designer configuration view ||Form designer display view|
|------------------|--|-----------|
|![Customize a card form in timeline - Details section](media\timeline-create-and-use-card-forms-details-1a.png "Customize a card form in timeline - Details section") | |![Display the card form in timeline - Details section](media\timeline-create-and-use-card-forms-details-display-1a.png "Display the card form in timeline - Details section")|
|The card details will always appear below the header regardless of the column you choose.<BR><BR>**Column 1**<BR>1. In the card details Column 1 acts as a subheader on the timeline record. For this example, **To** is selected for this column.<BR><BR>**Column 2**<BR>2. This column will only display one line of text in a summary view on the timeline record.  When you expand your timeline record,  content in this column is fully displayed and formatted. For this example, **CC** is selected for this column.<BR><BR>**Column 3**<BR>3. This column follows the content of Column 2 and is part of the main body of your timeline record that is only viewable when you expand the record. For this example, **Description** is selected for this column.||**Column 1**<BR>1. This column always displays in this section and acts as a subheader on the timeline record. <BR><BR>**Column 2**<BR>2. This column always displays in this section and only displays one line of text in the summary view but when expanded, content is fully displayed. <BR><BR>**Column 3**<BR>3. This column will always display in this section and is only viewable when the record is expanded.|	

**Footer Section**<br>
This section isn't visible on the timeline record.  

|Form designer configuration view | |Form designer display view|
|-------------------|--|-----------|
|![Customize a card form in timeline - Footer section.](media\timeline-create-and-use-card-forms-details-footer-1a.png "Customize a card form in timeline - Footer section")| ||
|**Column 1**<BR>1. For this example, we selected **Owner** for this column.<br><BR>**Column 2**<BR>2. For this example, we selected **Regarding** for this column.<br><BR>**Column 3**<BR>3. For this example, we selected **Priority** for this column.| |These column are not visible on the timeline record |

#### Set the date to use when sorting activities in timeline

How users view data is important, and setting a default display view of the data varies based on the needs of your business. App makers can choose how data is sorted and create a default setting for **Activity types** in **Record settings**. **Last Updated** is on all activities, which is why it is set as the default in ascending order.

![How to set date in the sort activities by feature in timeline.](media\timeline-how-to-set-date-in-sort-activities-by-feature-1a.png "Display options - Advanced - How to set date in the sort activities by feature in timeline")

Legend

1. The **Sort activity by** setting in the **Activities record settings** allows you to control how data is sorted in timeline.  
2. The **Sort activities by** column displays a list when selected. You can select from this list how you want your data to be sorted and displayed on timeline in the form.<BR><BR>

##### Sort date

Some dates can only exist on specific types of activities. For example, **Date sent** or **Date delivery last attempted** only apply to email. If you sort by such dates, then non-email activities end up grouped together without any ordering. You can't create a custom date column, but if you need more flexibility, you can use **Sort date**, which is empty by default and requires that you populate it for each activity record with the date you want to use for sorting. Some of the ways you can populate the date are by using Microsoft Power Automate, business rules, or Javascript.

When using Sort date, keep in mind the following:
- If you set a value in **Sort date**, you can use it for more customized sorting, but be aware that you have to populate it for every activity record or it won't work. The sort date has to be configured for each timeline instance, and must be set up for all three main forms in the account table.
- If the **DateTime** column is on the same calendar day, the date won't be displayed if **DateTime** was earlier in the day compared to current time.
- The sort date is not based on a 24-hour period, but rather, compares the **DateTime** column value with the current date and time (based on the user's preferred time zone). If the value entered occurred earlier in the day, the date isn't displayed.

#### Set create activities form type in the timeline

![How to set create activities form type in timeline.](media\timeline-how-to-set-create-activities-form-type-1a.png "How to set create activities form type in timeline")

1. **Create activities using** lets you choose which type of form users will work in based on your business needs.  
2. Select **Quick create form** or **Main form**. There are some activities that don't support quick create forms, such as email, and will use a main form. More information: [Create or edit model-driven app quick create forms for a streamlined data entry experience](/powerapps/maker/model-driven-apps/create-edit-quick-create-forms) and [Create or edit a model-driven app main form for an table](/powerapps/maker/model-driven-apps/create-edit-main-forms).  

#### Set the activity rollup type in timeline

The activity rollup type can be configured for timelines on forms for the account and contact tables. The available types of rollups are **Extended**, **Related**, and **None**. Activity rollup only affects accounts and contacts in Dynamics 365 apps, such as Dynamics 365 Customer Service applications. To only show activities that are directly related to the table in timeline, select **None**.

More information is on rollup types is available from [RollupType EnumType](/dynamics365/customer-engagement/web-api/rolluptype).

![Activity rollup type.](media\activity-rollup-type.png "Activity rollup type")

### Timeline performance

Only enable the activities that you need on the form. If you select more than 10 **Activity types**, a warning notice displays to let you know that the number of activity types you have selected impacts the performance of your timeline. To improve timeline performance, consider limiting activity types to 10 or less.

![Timeline performance impact.](media\timeline-performance-impacts-1a.png "Timeline performance impact")

### Notes on timeline

|Form designer configuration view | |Form designer display view|
|-------------------|-|------------|
|![Notes on timeline](media\timeline-notes-1a.png "Notes on timeline") | | ![Notes on timeline - Runtime](media\timeline-notes-3.png "Notes on timeline - Runtime")|
|The **Notes** section expands when enabled and allows you to:<BR>1. **Sort notes by** date created or date modified. The **Modified On** date is the default setting. <BR>2. Add a relative web resource path in the **Rich text editor configuration URL** column for customized note capability. More information: [Add the rich text editor control to a model-driven app](/powerapps/maker/model-driven-apps/rich-text-editor-control) ||1. When enabled, Notes can be access via the **Create a timeline record** ![Create a timeline record.](media\timeline-create-a-record-icon.png "Create a timeline record") icon.<BR>2. A dropdown list appears where you can access **Notes**.<BR>3. Use **Notes** to create a note to add to a record using rich text editing.|
  
#### Configure the form for notes

In the **Notes** area, under **Configure form**, select**Default form** to configure how information is displayed in notes, such as relevant users and dates, and whether or not to include labels. This enables you to increase or reduce the number of timeline records that appear onscreen.

:::image type="content" source="media/timeline-configure-form-notes.png" alt-text="Configure the form for notes":::

- Header
  - Label option: Hide, show, or show on hover the label, "Created by" or "Modified by".
  - Label: Select the **Use default label** checkbox label to display the label "Note modified by". Clear the checkbox to display the label "Modified by".
  - Data column: Select to show either the user who created the note or the user who modified the note. The label changes to match the data column you selected.
  - Display option: Always show, show on expand, or hide this header containing the user who created or modified the note.
- Body1
  - Label option: Show or hide the label of the note.
  - Display option: Always show, show on expand, or hide the body text.
- Body2
  - Label option: Show or hide the label of the note.
  - Display option: Always show, show on expand, or hide the body text.
- Footer
  - Label option: Show or hide the label, "Created on", "Modified on", or "Overridden on".
  - Data column: Select to show the createdon, modifiedon, or overridenon date.
  - Display option: Always show, show on expand, this footer containing the createdon, modifiedon, or overridenon date.

### Posts on timeline

To enable rich text posts on the timeline, contact [Microsoft Support](/power-platform/admin/get-help-support). 

> [!NOTE]
> Posts are only available with certain Dynamics 365 apps, such as Dynamics 365 Customer Service.

|Form designer configuration view | | Form designer display view|
|-------------------|--|------------|
|![Posts on timeline](media\timeline-posts-1a-rich-text.png "Posts on timeline") ||![Posts on timeline - Runtime](media\timeline-posts-1b.png "Posts on timeline - Runtime")|
|The **Posts** the section expands when enabled and allows you to:<br>1. **Sort notes by** date created or date modified. The **Created On** date is the default setting.<BR>2. Add a relative web resource path in the **Rich text editor configuration URL** column for customized post capability. More information: [Add the rich text editor control to a model-driven app](/powerapps/maker/model-driven-apps/rich-text-editor-control) || 1. When enabled, posts can be accessed by selecting **Create a timeline record** ![Create a timeline record.](media\timeline-create-a-record-icon.png "Create a timeline record").<BR>2. A dropdown menu displays, and you can access **Posts**.<BR>3. Use **Posts** to create a post to add to a record.<BR><BR> When date **Created On** is used to sort posts on the timeline, the location in the timeline remains constant even when there are responses to that post. <BR><BR> When date **Modified On** is used to sort posts on the timeline, the location in the timeline adjusts to the top when there are responses to that post. <BR><BR> **NOTE**: The timeline doesn't automatically refresh when post replies are added.|

#### Configure the form for posts

You can configure how information is displayed in posts, such as relevant users and dates, and whether or not to include labels. This enables you to increase or reduce the number of timeline records that appear onscreen.

![Configure the form for posts.](media\timeline-configure-form-posts.png "Configure the form for posts")

Go to your timeline configuration in [make.powerapps.com](https://make.powerapps.com "make.powerapps.com"), scroll down to the **Posts** section containing the **Configure form** column, and edit the following column in the default form:

- Header
  - Label option: Hide, show, or show on hover the label, "Created by" or "Modified by".
  - Label: Select the **Use default label** checkbox label to display the label.
  - Data column: Select to show the user who created the post. The label changes to match the data column you selected.
  - Display option: Always show, show on expand, or hide this header containing the user who created the post.
- Body2
  - Label option: Show or hide the label of the post.
  - Display option: Always show, show on expand, or hide the body text.
- Footer
  - Label option: Show or hide the label, "Created on", "Modified on", or "Overridden on".
  - Data column: Select to show the createdon or modifiedon date.
  - Display option: Always show, show on expand, this footer containing the createdon or modifiedon date.

## Configure mentions in notes and posts on timeline

To enable mentions in notes and posts, contact [Microsoft Help + support](/power-platform/admin/get-help-support.md). You can also temporarily try out this feature before asking Microsoft to enable it by appending the following text string to your current browser session URL:

```
     &flags=FCB.TimelineWallRichTextPosts=true,FCB.TimelineNotesRichTextMentions=true

```

When the rich text editor is enabled, users can mention other users and entities in notes and posts using the **@** and **#** symbols. Configuration for the rich text editor is available in the maker experience in **Power Apps**: [make.powerapps.com](https://make.powerapps.com "make.powerapps.com"). The users and entities that are displayed are pulled from the configuration file provided in the **Rich text editor configuration URL** column. More information: [Use the rich text editor control in Power Apps](/powerapps/maker/model-driven-apps/rich-text-editor-control)

By default, the **@** symbol returns matches with the first name, last name, or email address of system users starting with the search string.

By default, the **#** symbol returns matches with the account and contact name table records starting with the search string.

As an administrator, you can configure additional entities to appear when a user types these symbols. Adding more entities to the default configured entities may result in slower load times, so only add the entities that are required by your organization. You can add the following additional entities:

- "systemuser"
- "contact"
- "competitor"
- "lead"
- "account"
- "incident"
- "opportunity"
- "knowledgearticle"

To configure additional entities, add and modify the following code to the configuration file you are using for rich text notes and posts:

```
     "defaultSupportedProps": {
        "pcfmentions" : {
            "markerMap" : {
                "@" : ["systemuser"],
                "#" : ["account", "contact"]
            },
            "calloutWidthInpx" : "300px",
            "debounceInms" : 250
        }
      }

```
The "systemser" table will persist for **@** and the "account" and "contact" entities for **#** regardless of how the file is edited.

<!-- 
## Configure dashboard timelines

Timelines can be configured and put on a dashboard. However, the configuration available for timeline applied to a dashboard is limited to the functionality provided by the legacy designer experience. The new form designer experience on dashboards is not available. 

> [!NOTE]
> Capabilities on a dashboard timeline are different than those in an embedded dashboard timeline.  
Dashboard timelines contain records related to the current user. This means each user will see a different set of information when viewing the same dashboard timeline. Notes are not available on the dashboard.

This following image shows the General tab, where you can modify the timeline control properties:

:::image type="content" source="media/timeline-control-properties-general.png" alt-text="Timeline control properties General tab":::

The following image shows the Activities tab, where you can modify the Timeline Control properties:

:::image type="content" source="media/timeline-control-properties-activities.png" alt-text="Timeline control properties Activities tab":::  -->

## Configure auto-post messages to display on the timeline

> [!NOTE]
> The auto-post functionality is only available with environments that are configured for **Enable Dynamics 365 apps**.

You can configure which auto-post messages will appear on the timeline when a system event occurs. The auto-post configuration replaces the legacy Activity Feed Configuration and Activity Feed Configuration Rules.

To configure the auto-post messages that should be displayed:

1. In Customer Service Hub, go to **Service Management**, and under **Timeline settings**, select **Auto-post rules**.
2. Select which auto-post rules to make active using the grid and **Activate** and **Deactivate** buttons at the top.

When a system event corresponding to an active rule occurs, an auto-post message will display on the timeline.

![Auto-post rules timeline settings.](media\timeline_auto-post_rules.png "Auto-post rules timeline settings")

If you are using a Dynamics 365 app other than Customer Service Hub or Customer Service workspace, you need to add your own sitemap. To add your own sitemap in your app:

1. Open your app in the app designer in **Power Apps**: [make.powerapps.com](https://make.powerapps.com "make.powerapps.com")
1. On the app designer command bar, select **Add page**, select **Table based view and form**, and then select **Next**.
1. In the **Table** list, select **Post Rule Configuration**, and then select **Add**.
   > [!NOTE]
   > If you don't have the Post Rule Configuration table, you're environment doesn't have the required Dynamics 365 app installed.
1. Select **Save**, and then select **Publish**.

## Create and add custom activities to timeline

You can create custom tables that display on a timeline. More information: [Display a custom table in a timeline](#display-a-custom-table-in-a-timeline) 

## Configure blocked attachment file types in timeline

Power platform administrators can configure the file types that are blocked from being added as file attachments.

1. Find the **Set blocked file extensions for attachments** systems setting. More information: [Open the System Settings dialog box General tab](/power-platform/admin/system-settings-dialog-box-general-tab#open-the-system-settings-dialog-box)
1. In the text box of blocked file attachments, type the file extension type you want to block for attachments (for example, ".pdf"). Separate file types with a semi-colon.
1. Select **OK**.

### See also

[FAQs for timeline control](faqs-timeline-control.md) 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
