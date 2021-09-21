---
title: Add and configure the timeline control in Power Apps | MicrosoftDocs
description: "Learn how to add and configure the timeline control to use in a model-driven app"
ms.custom: ""
ms.date: 09/10/2021
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

The timeline helps agents see all customer interaction history across channels, personnel, and the support lifecycle. The timeline is used across Dynamics 365 applications to capture activities like notes, appointments, emails, tasks, and more, to ensure that all interactions with the customer are tracked and visible over time. You can use the timeline to quickly catch up on all of the latest activity details with the customer to provide the most personalized support experience.  

The timeline control provides an easy and immersive experience to view information related to an entity, such as cases, accounts, or contacts, which gives users a better understanding and helps them deliver more personalized service in an efficient and effective manner.

This experience gives system administrators the ability to configure the information displayed on the timeline to help users access information and create new activity records, such as emails and tasks directly from the timeline quickly so they can deliver more personalized service.

## Navigate to timeline configurations

Timelines are located on forms within entities. To access timeline configurations, you must start with the entity list. You can access the entity list a couple of ways, depending on the model-driven app you are using.	

### Access entities list via Power Apps

Steps:
1. Go to **Power Apps** URL: [make.powerapps.com](https://make.powerapps.com "make.powerapps.com")
2. Go to **Data** section.
3. Select **Entities**

  ![Access entities list via Power Apps.](media\timeline-access-option-2a.png "Access entities list via Power Apps")

> [!Important]
> When accessing timeline, if you are not taken to the new form designer experience in Power Apps, you are not using the latest experience.

### Select an entity form for timeline configuration

Every instance of the timeline that’s applied on a form can be configured. For example, an Account entity will have forms, and each form can have a timeline that can be configured. However, there’s only one timeline per form.  

To begin, select the entity and form where you want to add and configure your timeline. 

#### Select an entity for timeline configuration example:
![Select an entity for timeline configuration.](media\timeline-configuration-1a.png "Select an entity for timeline configuration")
1. Timelines can be added to any entity.
2. In this example, we selected the **Account** entity.

#### Select a form for timeline configuration example:
![Select a form for timeline configuration.](media\timeline-configuration-2a.png "Select a form for timeline configuration")

1. In this example, we selected **Forms** under the **Account** entity, which displayed a list of **Form types**. 
2. Since timelines can only be used on **Main** form types, we selected **Account for Interactive experiences**. 

### Add or remove a timeline from an entity form

Use the following steps to add or remove a timeline from an entity form:

1. Timeline is a component, so you'll need to access **Components** in PowerApps to configure it. 

2. Select a **Main** form type. A landing page is displayed.

3. Scroll down to the **Timeline** component on the left-hand navigation, then drag and drop it in a section on the form. 
<ul><li> If the <b>Timeline</b> component is greyed out, it means a timeline already exists on the form. You can only have one timeline per form. </li>
<li> To remove the <b>Timeline</b> component from a form, highlight the inside of the **Timeline** component area and hit the <b>Delete</b> key.  This will remove the <b>Timeline</b> component from the form.</li></ul>

![Adding or removing a timeline from an entity form.](media\timeline-add-or-remove-entity-from-form-1b.png "Adding or removing a timeline from an entity form")

> [!Note] 
> Since the timeline component relies exclusively on underlying related data, it will always say **Almost there** when added to the timeline section. 
> Also, as we are in a create and/or edit state on the form, there is no underlying data, so the area is blank.

## Understand the timeline component on the form

In the body of the entity form located in the center, there is an area titled **TIMELINE**. Within this section is another area titled **Timeline**. The following outlines and clarifies the different between these two sections.

#### Timeline component section resides in the Maker App
![Understand the timeline component on the form.](media\timeline-component-1a.png "Understand the timeline component on the form")
1. The outside section (titled **TIMELINE**) is what houses the **Timeline** component. 
2. When **TIMELINE** is selected, the **Display options** under the **Properties** tab in the right nav change to support the **Maker App**.

#### Timeline component section access
![Understanding the timeline component on the form.](media\timeline-component-2a.png "Understanding the timeline component on the form")

1. Inside the **TIMELINE** section is where the **Timeline** component is located.
2. When the **Timeline** component is selected, the **Display options** under the **Properties** tab in the right nav changes to support the **Timeline** component.

## Configure the timeline component

The timeline component is rich in features and functionality that can be configured and tailored to support specific business needs. The Timeline form is comprised of features and functionality that you configure in the timeline component, which is then displayed in the entity form.

The following overview provides a detailed breakdown of each timeline feature, what it supports, how it is configured, and how it is displayed in the corresponding timeline section on the entity form:

- **Display options** 
  - [Timeline component name](#timeline-component-name)
  - [Records shown on page](#records-shown-on-page)
  - [Record types shown](#record-types-shown) 
  - [Advanced](#advanced)

- **Record settings** 
  - [Activities](#activities)
  -	[Notes](#notes)
  -	[Posts](#posts)

- **[How to create and add custom activities](/powerapps/maker/model-driven-apps/set-up-timeline-control#enable-custom-activity-in-timeline)**

## Display options 

### Timeline component name

The **Name** field under the **Properties** tab in  **Display options** serves only for Admin reference. 

| Configuration View | | Display View   |
|--------------------|--|---------------|
|![Configure Timeline component name](media\timeline-component-name-display-options-1a.png "Configure Timeline component name")||  ![Display  Timeline component name](media\timeline-component-name-display-options-1c.png "Display Timeline component name")|
|The timeline **Name** field allows you to create a unique name as a maker's reference. In this example, we changed the **Name** field to **Timeline_for_ Account**. | | The name, **Timeline_for_Account**, doesn't display on the rendered form. The name is for administrator reference only. |
|||

>[!NOTE]
> The **Name** field has limitations. For example, you can't use spaces between words. Instead, you must use an underscore (_).	

### Records shown on page

This section allows you to control the number records that appear before displaying **Load more** at the bottom of the section.

|Configuration View || Display View |
|-------------------|-|--------------|
![Configure Records shown on page](media\timeline-records-shown-on-page-display-options-1a.png "Configure Records shown on page")| | ![Display Records shown on page](media\timeline-records-shown-on-page-display-options-1b.png "Display Records shown on page")|
|The default setting on the **Records shown on page** field is set to 10 records, but you can set it to any number (there isn't a limit). || 1. Per the default setting shown in this example, the form displays a maximum of 10 records, but you can display up to 50 records. <BR> 2. Once records exceed 10, the **Load more** option appears at the bottom of the form.|
|||

### Record types shown

There are three primary record types: activities, notes, and posts. All record types are enabled by default.

#### Activities
Activities can have a large number of customizable subactivity record types to support business needs. Depending on what you have installed, the administrator can create, add, and display a number of different customized subactivity record types under the **Activity** section of the dropdown menu on the timeline. 

#### Notes
Notes allow you to capture details related to the entity record. For example, you can use notes to capture thoughts, summarize information, and provide feedback on a case, and then update the case details later. 

#### Posts
There are two types of posts: auto and user.

   - **Auto Posts** are system-generated posts that notify you of account activity that has occurred.
   
   - **User Posts** allow you to leave a message for another user on a record.

#### Enable these record types to be displayed in the timeline
|Configuration View | | Display View  |
|-------------------|--|--------------|
|![Display options for Timeline](media\timeline-record-types-shown-display-options-2b.png "Display options for Timeline")||![Display options - Record types shown](media\timeline-record-types-shown-display-options-3b.png "Display options - Record types shown")|
|To enable **Record types shown** for **Activities**, **Notes**, and **Posts** on a form, check the box next to the record type.||1. To confirm that the record type is displaying on the form, select **Create a timeline record** ![Create a timeline record icon.](media\timeline-create-a-record-icon.png "Create a timeline record icon") (Create a timeline record icon) in the top-right nav in the timeline, and a dropdown menu that displays the list of enabled record types will appear.<BR>2. When **Activities** are enabled, you'll see **Activity** record types for appointments, email, phone calls, and tasks.<BR> 3. When **Notes** are enabled, you'll see the Note record types on the form.<BR> 4. When **Posts** are enabled, you'll also see the Post record types on the form.|

> [!Note]
> Activities, notes, and posts are standard entities. If your administrator or system customizer has configured other entities, they'll also be displayed.

### Activity, notes, post icons and date / timestamp display on timelines

The timeline shows a simple icon before the activity, post, note, and custom entity, making it easy for you to identify the record type. 

Dates and timestamps always appear on each record on the bottom-right side of the preview, and are always viewable.

## Advanced

The **Advanced** feature works across and is independent of all record types, and is collapsed by default. 

When enabling and disabling **Advanced** features, you won't be able to view updates (even though it may appear that there's activity occurring on the timeline component) until you save and publish your configuration updates and refresh the entity form. 

**Advanced** covers common settings that span across an activity, note, or post, which are the three primary record types that appear in the timeline section.

### Quick entry record type and sort order default

The following is a detailed overview of the **Advanced** configuration options, starting with selecting your **quick entry record type**:

|Configuration View | |Display View |
|-------------------|--|------------|
|![Configure Quick entry record type and sort order default](media\timeline-quick-entry-record-type-and-sort-order-default-display-settings-advanced-2a.png "Configure Quick entry record type and sort order default")| |![Display Quick entry record type and sort order default](media\timeline-quick-entry-record-type-and-sort-order-default-display-settings-advanced-3b.png "Display Quick entry record type and sort order default")|
|1.Select **Advanced** to expand this feature in the configuration view. The **Quick entry record** type provides you with quick access to create either a **Note** or a **Post**.  The default setting for this feature is set to **Notes**.<BR> 2.The **Sort order default** feature controls the order of how all data is sorted on the timeline. The default setting for this feature is set to Descending. ||1. When you select **Notes**, it will display under the **Search** bar in timeline. Also, you will see a paperclip ![Paperclip icon.](media\timelilne-paperclip-icon.png "Paperclip icon") icon that allows you to attach files. You can only attach files to Notes.<BR>2.	When you select **Posts** it also will display under the **Search** bar in timeline.|

### Enable filter pane

Using filters provides a quick option to sort and look for specific data quickly. 

|Configuration View | | Display View |
|-------------------|--|-------------|
|![Configure filter pane](media\timeline-enable-filter-pane-display-options-advanced-2a.png "Configure Enable filter pane")||![ Enable filter pane](media\timeline-enable-filter-pane-display-options-advanced-3b.png "Enable filter pane")| |The **filter pane** feature allows you to enable or disable filter functionality on timeline. It is enabled by default.|| Enable the **filter pane** by checking the box next to the feature.  This will enable the filter icon to display on the timeline.  <BR><BR> To disable the **filter pane**, uncheck the box next to the feature and the filter icon will no longer appear on the timeline.   |
|||

### Filter records on timeline

Filters are valuable for sorting data. You can quickly filter activities, posts, and notes with multiple options to see what matters to you. The filter is available for the activities, posts, notes, and custom entities that are present in the timeline. Timeline filters and displays the records and the count that are present in the timeline.

When you select filters based on an activity status then those activities, notes, and posts are displayed in your timeline. You can customize data using data filters and either choose to keep filters in place or clear them when you are done.

- When the **Filter** icon is transparent ![Transparent filter icon.](media\timeline-filter-icon.png "Transparent filter icon") on the entity form, it means no items have been selected, therefore the filter pane is empty.<br>

- When the **Filter** icon is dark ![Dark filter icon](media\timeline-filter-applied-1.png "Dark filter icon"), it means filters have been set. To view which filters have been selected, click on the ![Filter icon](media\timeline-filter-icon.png "Filter icon") **Filter** icon and the filter pane will display showing which filters have been set.</li>

- You can choose how you want to filter data by selecting the box next to the filter.<br>

- You can clear filters by using the **Clear all filters** ![Clear all filters icon.](media\timeline-clear-all-filters-icon.png "Clear all filters icon") icon on the filter pane.

The following category and subcategory options are available on the filer menu:

|Category                   |Subcategory                            |
|---------------------------|----------------------------------------|
|Record type                |<li>Notes</li>                     <li>Posts</li><li>Activities</li>                     |
|Activity type              |<li>Appointment</li><li>Campaign Activity</li> <li>Campaign Response</li><li>Email</li><li>Fax</li><li>Case Resolution</li><li>Letter</li><li>Opportunity Case</li>   <li>Order Case</li><li>Phone Call</li><li>Quote Close</li>           <li>Recurring Appointment</li><li>Social Activity</li><li>Task</li>   <li>Project Service Approval</li><li>Booking Alert</li><li>Conversation</li><li>Session</li><li>Customer Voice survey invite</li><li>Customer Voice survey response</li><li>Custom activities (as configured by your administrator)</li>|
|Activity status            |<li>Active</li><li>Overdue</li>       <li>Closed</li>                         |
|Activity status reason     |Allows you to filter using specific status reasons. The values are a unique list of all of the status reasons from the activities in the timeline. The status reasons will change depending on the activity. If there are multiple activities on the timeline that have the same status reason, it will be reflected once, but then the number next to it will indicate how many occurrences of that status reason appear in the timeline.                       |
|Activity due date (active) |<li>Next 30 days</li><li>Next 7 days</li><li>Next 24 hours</li><li>Last 24 hours</li><li>Last 7 days</li>   <li>Last 30 days</li>                   |
|Posts by                   |<li>Auto post</li><li>Users</li>                          |
|Modified date              |<li>Last 24 hours</li><li>Last 7 days</li><li>Last 30 days</li>                   |


### Expand filter pane 

The **Expand filter pane** feature provides quick access to sorting options within the timeline.  It is enabled by default.

|Configure View | |Display View |
|---------------|--|------------|
|![Configure filter pane ](media\timeline-expand-filter-pane-display-options-advanced-3a.PNG "Configure filter pane")| |![Enable filter pane ](media\timeline-expand-filter-pane-display-options-advanced-2b.PNG "Enable filter pane")| 
The <B>Expand filter pane by default</B> feature displays an expanded filter pane at the top of the form anytime it is opened and refreshed.  It is disabled by default.||Enable the **Expand filter pane** by checking the box next to the feature.  This will enable the filter pane to appear at the top of the form anytime the form is opened and refreshed.<BR><BR>To disable the **Expand filter pane**, uncheck the box next to the feature and the filter pane will not appear on the timeline.|

### Enable search bar

You can easily search for records in the timeline. When you search for a phrase in the timeline, it searches in the title of the record or body and description fields of the record then displays the record for you. 

|Configure View | | Display View |
|---------------|-|-------------|
|![Configure search bar](media\timeline-enable-search-bar-display-options-advanced-3a.PNG "Configue search bar")| |![Enable search bar](media\timeline-enable-search-bar-display-options-advanced-2b.PNG "Enable search bar")| 
|The **search bar** feature enables the **Search timeline** bar functionality. It is enabled by default.||Enable the **search bar** feature and it will display a **search bar** at the top of the timeline form.<BR><BR>Disable the search bar by unchecking the box next to the feature and the search bar will no longer display on the timeline.| 

### Expand all records in timeline

**Expand all records by default** displays all activities in an expanded view in timeline. 

|Configure View |  |Display View |
|---------------|---|------------|
|![Configure Expand all records in timeline](media\timeline-expand-all-records-display-options-advanced-2a.PNG "Configure Expand all records in timeline")||![Enable Expand all records in timeline](media\timeline-expand-all-records-display-options-advanced-2b.PNG "Enable Expand all records in timeline")||
|You can enable the **Expand all records** feature by checking the box next to the feature. This sets the default view to display all records in the expanded view format in the form each time the timeline is opened. The **Expand all records** is disabled by default.||1. When enabled, the **Expand all records** icon is displayed in the top-right corner of the timeline nav. <BR>2. Records can be expanded or collapsed by using the **Expand all records** icon. When expanded, all records are displayed in the expanded view in the form each time it is opened. When you clear the box next to the **Expand all records** feature, it no longer displays activities in an expanded view.<BR><BR> When disabled, the **Expand all records** icon will not display in the top-right nav of the timeline. Records will always be displayed in a collapsed view.|	
  
### Edit filter pane

You can configure the default filters that are applied when a form loads or is refreshed using **Edit filter pane**. You can remove filter groups by toggling the setting to **Off**. Users can remove the default filters to see all the records unless **Enable filter pane** is disabled.

![Edit filter pane.](media\edit-filter-pane.png "Edit filter pane setting")

### Expand records with images in timeline

You can send and receive records with images, but they won't display when the record is collapsed. Records with images must be expanded to be viewed.

![Expand records with images in timeline.](media\timeline-expand-records-with-images-display-optiones-advanced-2b.png "Expand records with images in timeline")
1. Records when collapsed provide a visual summary. To expand an individual record, click anywhere on the timeline record to expand and collapse a record view.  In the bottom-right corner of the record there is a caret:  
> - When the caret is facing downward (˅), the record is collapsed.
> - When the caret is facing upward (^), the record is expanded.

2. Records with images will often display the following notice: <BR>
![Expand records with images in timeline at runtime.](media\timeline-expand-records-with-images-display-optiones-advanced-1a.png "Expand records with images in timeline at runtime")
3. When you select the message, the warning goes away and the image appears. 

If you don’t see a message and the image isn't displayed, see [Timeline FAQs](/power-platform/user/faq-for-timeline-and-activity.md) for more information.

### Enable “What you’ve missed” summary

**What you’ve missed** helps you stay on top of updates and changes made to records by displaying updates at the top of the timeline when you access a record. 

|Configure View | | Display View|
|---------------|--|-------------|
|![Configure “What you’ve missed” summary](media\timeline-what-you-missed-display-options-advanced-11a.png "Configure “What you’ve missed” summary")| |![Disable “What you’ve missed” summary](media\timeline-what-you-missed-display-options-advanced-11b.png "Disable “What you’ve missed” summary") |
|The **What you’ve missed** feature displays new records you haven't seen. It's disabled by default. To enable it, select the box next to the feature. To disable it, uncheck the box next to the feature ||Once enabled, when you view a customer’s account, a box will appear at the top of the timeline section, notifying you of updates.<BR><BR> When disabled, notifications aren't displayed when you access an account.| 

## Record settings

The **Record types to show** feature is tied to the **Record settings** that support activities, notes, and posts in the timeline.

**Record settings** lets you manage the settings within the record types. 
- The **Activities** record type is tied to **Activities** in record settings.
- **Notes** record type is tied to **Notes** in record settings.
- **Posts** record type is tied to **Posts** in record settings.

To enable or disable a record type, simply select or deselect the box, and then that record type will either display or no longer appear in the **Record settings** section.

**Example:**
![Display options - Advanced - Record Settings.](media\timeline-record-settings-display-options-advanced-1a.png "Display options - Advanced - Record Settings")

1. When **Posts** is checked in the **Record types to show** section, it's enabled in the **Record settings** section below.
2. When **Posts** is unchecked in the **Record types to show** section, it's disabled in the **Record settings** section below.

### Configure activity record types

When you expand the **Activities record settings** on the timeline component section a list will display showing all the activity types that can be either enabled or disabled on the entity form. 

|Configuration View ||Display View|
|-------------------|-|-----------|
|![How to configure activity record types](media\timeline-how-to-configure-activity-record-types-display-options-advanced-11a.png "How to configure activity record types")||![Activity record types](media\timeline-how-to-configure-activity-record-types-display-options-advanced-11d.png "activity record types")|
|1. Expand and view **Activities** under the **Record settings** section using the caret (^).<BR> 2. A list of **Activity types** is displayed in the expanded view. <BR> 3. You can enable or disable activity by selecting an activity type. In this example, we selected **Email**<BR><BR> To enable an **Activity type**, check the box next to **Enable** and select **Done**.<BR><BR>To disable an **Activity type**, uncheck the box next to **Enable** and select **Done**. This will grey out all other items in the box and disable the activity type from displaying on the timeline.  This also disables the activity type from being created or viewed in the timeline.  || 1. When enabled, an **Activity type** will appear under the **Create a timeline record** ![Create a timeline record.](media\timeline-create-a-record-icon.png "Create a timeline record"). <BR> 2. The activity type will be displayed as an option the user can choose from the dropdown menu. <BR> 3. Also, the **Activity type** record is displayed in the body of the timeline.| 

> [!NOTE]
> A checkmark appears to the right, next to enabled **Activity types**. Additional record type settings are disabled until they're enabled under that specific record type.

### Enable status tags on activity record types

Status tags match the status filter that display in the timeline to help you to see at a glance if the state of an activity record is **Active**, **Overdue**, or **Closed** on a task, appointment, or email. The administrator can enable or disable status tags for any **Activity type** in the **Record settings**. Status tags are enabled by default.

|Configuration View | | Display View|
|-------------------|--|------------|
|![Enable status tags on activity record types](media\timeline-enable-status-tags-on-activity-record-types-display-options-advanced-11a.png "Enable status tags on activity record types")||![Display status tags on activity record types](media\timeline-enable-status-tags-on-activity-record-types-display-options-advanced-11b.png "Display status tags on activity record types")|
| To display email status tags, check the box next to **Enable status tag**. ||  When enabled, status tags such as **Active**, **Overdue**, or **Closed** will appear in the timeline next to that activity record.    |

### Enable the ability to create directly from timeline

Administrators have the ability to enable activity types so they can be created directly on the timeline. Having the ability to quickly select and create an activity, such as email, tasks, and appointments, helps to streamline productivity.  

|Configuration View | | Display View |
|-------------------|--|-------------|
|![Configure the ability to create directly from timeline](media\timeline-enable-ability-to-create-directly-from-timeline-11a.png "Configure the ability to create directly from timeline") || ![Display the option to create directly from timeline](media\timeline-enable-ability-to-create-directly-from-timeline-11b.png "Display the option to create directly from timeline") |
|	To allow users to create activity types directly from timeline, check the box next to **Create directly from timeline**.||	When enabled, the activity type will appear in a dropdown box on the  **Create a timeline record** ![Icon for create a timeline record.](media\timeline-create-a-record-icon.png "Icon for create a timeline record") icon in the top-right nav in the timeline.|

### Create and use card forms in timeline

Records are displayed using the default setting for each activity type. However, if you want to display record information for an appointment or email, for example, you can either edit the existing card form, use a different card form from record settings, or customize your own. 

|Configure View ||Display View|
|---------------|--|------------------|
|![Create and use card forms in timeline](media\timeline-create-and-use-card-forms-display-options-advanced-101a.png "Create and use card forms in timeline")||![Display the option to create and use card forms in timeline](media\timeline-create-and-use-card-forms-display-options-advanced-1111b.png "Display the option to create and use card forms in timeline") |
|You can change the default card settings to a different card form if one has been created.  ||If you create a new card form, you must go to the parent entity and add the new form of card type there before it will appear in the timeline list for configuration.  If **Default** is displayed, you are not using the card form.  You can not use the **Email card form** in timeline unless you select and publish it first.|

> [!NOTE]
> Not all activity types allow you to create card types, so the default selection will be you’re only option for those records.

### Customize a card from within timeline

All card forms are broken out into the following four sections:

![Display options - Advanced - How to customize a card in timeline.](media\timeline-customize-card-form-display-option-advanced-2a.png "Display options - Advanced - How to customize a card in timeline")

Legend

1. **ColorStrip Section.** This section doesn't appear on the timeline record. The **ColorStrip** is located on the left of the card form.<br>
2. **Header Section.** This section is displayed on the timeline record; however, only the first two fields are displayed on the timeline record. For this example, only the **Subject** and **Modified On** fields are visible.<br>
3. **Details Section.** This section is displayed on timeline record; however, only the first three fields are displayed on the timeline record. For this example, only the **To**, **CC** and **Description** fields are visible on the timeline record.<br>
4. **Footer Section.** This section isn't displayed on the timeline record.<br>
5. **Entity Fields.** You can select which fields you want to add to your card form from the field options listed on the right. You can customize your card form by dragging and dropping the fields you want to use into the sections you want that field to appear in on the timeline record.

Each individual card form must be customized for each activity record, such as email, tasks, posts, and so forth. 

**Header Section**

The Card Header displays the title/subject in your timeline email form. You can have up to six fields in the Header section, only the first two  fields will be seen on the timeline record. Also empty fields will be ignored by the form in all sections.

|Configuration View || Display View|
|-------------------|-|------------|
|![Customize a card form in timeline - Header](media\timeline-create-and-use-card-forms-header-1a.png "Customize a card form in timeline - Header")||![Card form in timeline - Header Display](media\timeline-create-and-use-card-forms-header-display-1a.png "Card form in timeline - Header Display")|
| **Field 1** <BR>1. Regardless of the field you choose for this section, it will appear as a bold header at the top of your timeline record. For this example, we selected **Subject** for this field. <br><BR>**Field 2** <BR>2. Again regardless of the field you choose for this section as well, this field will always appears in the bottom-right corner of the timeline record. For this example, we selected **Modified On** for this field. ||**Field 1**<BR>1. Field 1 from the card header is always displayed in this section of the timeline record.<BR><BR>**Field 2**<BR>2. Field 2 from the card header is always displayed in this section of the timeline record. |  	

**Details Section**

The Card Details section displays in the body of your the timeline email record. You can have up to four fields in the **Details** section, but only the first three fields are viewable on the timeline record.

|Configuration View ||Display View|
|------------------|--|-----------|
|![Customize a card form in timeline - Details section](media\timeline-create-and-use-card-forms-details-1a.png "Customize a card form in timeline - Details section") | |![Display the card form in timeline - Details section](media\timeline-create-and-use-card-forms-details-display-1a.png "Display the card form in timeline - Details section")|
|The Card Details will always appear below the Header regardless of the field you choose.<BR><BR>**Field 1**<BR>1. In the card details Field 1 acts as a subheader on the timeline record. For this example, we selected **To** for this field.<BR><BR>**Field 2**<BR>2. This field will only display one line of text in a summary view on the timeline record.  When you expand your timeline record,  content in this field is fully displayed and formatted. For this example, we selected **CC** for this field.<BR><BR>**Field 3**<BR>3. This field follows the content of Field 2 and is part of the main body of your timeline record that is only viewable when you expand the record. For this example, we selected **Description** for this field.||**Field 1**<BR>1. This field always displays in this section and acts as a subheader on the timeline record. <BR><BR>**Field 2**<BR>2. This field always displays in this section and only displays one line of text in the summary view but when expanded, content is fully displayed. <BR><BR>**Field 3**<BR>3. This field will always display in this section and is only viewable when the record is expanded.|	

**Footer Section**<br>
This section isn't visible on the timeline record.  

|Configuration View | |Display View|
|-------------------|--|-----------|
|![Customize a card form in timeline - Footer section.](media\timeline-create-and-use-card-forms-details-footer-1a.png "Customize a card form in timeline - Footer section")| ||
|**Field 1**<BR>1. For this example, we selected **Owner** for this field.<br><BR>**Field 2**<BR>2. For this example, we selected **Regarding** for this field.<br><BR>**Field 3**<BR>3. For this example, we selected **Priority** for this field.| |These fields are not visible on the timeline record |

### Set the date to use when sorting activities in timeline

How you view data is important, and setting a default display view of your data varies based on the needs of your business. Admins can choose how data is sorted and create a default setting for **Activity types** in **Record settings**. **Last Updated** is on all activities, which is why it is set as the default in ascending order.

![How to set date in the sort activities by feature in timeline.](media\timeline-how-to-set-date-in-sort-activities-by-feature-1a.png "Display options - Advanced - How to set date in the sort activities by feature in timeline")

Legend

1. The **Sort activity by** feature in the **Activities record settings** allows you to control how data is sorted in timeline.  
2. The **Sort activities by** field displays a list when selected. You can select from this list how you want your data to be sorted and displayed on timeline in the form.<BR><BR>

#### Sort date
Some dates can only exist on specific types of activities. For example, **Date sent** or **Date delivery last attempted** only apply to email. If you sort by such dates, then non-email activities end up grouped together without any ordering. You can't create a custom date field, but if you need more flexibility, you can use **Sort date**, which is empty by default and requires that you populate it for each activity record with the date you want to use for sorting. Some of the ways you can populate the date are by using Microsoft Power Automate (previously Microsoft Flow), business rules, or Javascript. 

> [!IMPORTANT]
> If you set a value in Sort date, you can use it for more customized sorting, but be aware that you have to populate it for every activity record or it won't work. Sort date has to be configured for each timeline instance, and must be set up for all three main forms in the Account entity.


### Set create activities form type in timeline

![How to set create activities form type in timeline.](media\timeline-how-to-set-create-activities-form-type-1a.png "How to set create activities form type in timeline")

1. The **Create activities** feature allows you to choose which type of form you want to work in based on your business needs.  
2. **Quick create form** appears in a model on the right. There are some activities that don't support quick create that will always use email, for example. For more information, see [Create or edit model-driven app quick create forms for a streamlined data entry experience](/powerapps/maker/model-driven-apps/create-edit-quick-create-forms).
<BR>**Main form** navigates you to the activity entity main form. For more information, see [Create or edit a model-driven app main form for an entity](/powerapps/maker/model-driven-apps/create-edit-main-forms).  

> [!NOTE]
> If a **quick create** form for an activity has not been created, then the main form will be used. If **quick create** form is not supported, such as with email, the **main form** will always be used. 

### Set the activity rollup type in timeline

The activity rollup type can be configured for timelines on forms for the **Account, Contact and Opportunity** entity. The available types of rollups are **Extended**, **Related**, and **None**. Activity rollup only affects accounts and contacts in CRM applications. To only show activities that are directly related to the entity in timeline, select **None**.

More information is on rollup types is available from [RollupType EnumType](/dynamics365/customer-engagement/web-api/rolluptype).

![Activity rollup type.](media\activity-rollup-type.png "Activity rollup type")


### Timeline performance impacts

Only enable the activities that you need on this form. If you select more than 10 **Activity types**, a warning notice displays to let you know that the number of activity types you have selected impacts the performance speed on your timeline. To improve timeline performance speed, consider limiting activity types to 10 or less. 

![Timeline performance impacts.](media\timeline-performance-impacts-1a.png "Timeline performance impacts")

## Notes on timeline

|Configuration View | |Display View|
|-------------------|-|------------|
|![Notes on timeline](media\timeline-notes-1a.png "Notes on timeline") | | ![Notes on timeline - Runtime](media\timeline-notes-3.png "Notes on timeline - Runtime")|
|The **Notes** the section expands when enabled and allows you to:<BR>1. **Sort notes by** date created or date modified. The **Modified On** date is the default setting. <BR>2. Add a relative web resource path in the **Rich text editor configuration URL** field for customized note capability. More information: [Add the rich text editor control to a model-driven app](/powerapps/maker/model-driven-apps/rich-text-editor-control) ||1. When enabled, Notes can be access via the **Create a timeline record** ![Create a timeline record.](media\timeline-create-a-record-icon.png "Create a timeline record") icon.<BR>2. A dropdown will appear where you can access **Notes**.<BR>3. Use the Notes feature to create a note to add to a record using rich text editing.|
  
### Configure form for notes

You can configure how information is displayed in notes, such as relevant users and dates, and whether or not to include labels. This enables you to increase or reduce the number of timeline records that appear onscreen.

![Configure the form for notes.](media\timeline-configure-form-notes.png "Configure the form for notes")

Go to your timeline configuration in [make.powerapps.com](https://make.powerapps.com "make.powerapps.com"), scroll down to the **Notes** section containing the **Configure form** field, and edit the following fields in the default form:

- Header
  - Label option: Hide, show, or show on hover the label, "Created by" or "Modified by".
  - Label: Select the **Use default label** checkbox label to display the label "Note modified by". Deselect the checkbox to display the label "Modified by".
  - Data field: Select to show either the user who created the note or the user who modified the note. The label changes to match the data field you selected.
  - Display option: Always show, show on expand, or hide this header containing the user who created or modified the note.
- Body1
  - Label option: Show or hide the label of the note.
  - Display option: Always show, show on expand, or hide the body text.
- Body2
  - Label option: Show or hide the label of the note.
  - Display option: Always show, show on expand, or hide the body text.
- Footer
  - Label option: Show or hide the label, "Created on", "Modified on", or "Overridden on".
  - Data field: Select to show the createdon, modifiedon, or overridenon date.
  - Display option: Always show, show on expand, this footer containing the createdon, modifiedon, or overridenon date.

## Posts on timeline

To enable rich text posts on timeline, contact [Microsoft Support](/power-platform/admin/get-help-support). 

> [!NOTE]
> Posts are currently only available for CRM applications.

|Configuration View | | Display View|
|-------------------|--|------------|
|![Posts on timeline](media\timeline-posts-1a-rich-text.png "Posts on timeline") ||![Posts on timeline - Runtime](media\timeline-posts-1b.png "Posts on timeline - Runtime")|
|The **Posts** the section expands when enabled and allows you to:<br>1. **Sort notes by** date created or date modified. The **Created On** date is the default setting.<BR>2. Add a relative web resource path in the **Rich text editor configuration URL** field for customized post capability. More information: [Add the rich text editor control to a model-driven app](/powerapps/maker/model-driven-apps/rich-text-editor-control) || 1. When enabled, posts can be accessed via **Create a timeline record** ![Create a timeline record.](media\timeline-create-a-record-icon.png "Create a timeline record") icon.<BR>2. A dropdown menu displays, and you can access **Posts**.<BR>3. Use the Post feature to create a post to add to a record.<BR><BR> When date **Created On** is used to sort posts on the timeline, the location in the timeline remains constant even when there are responses to that post. <BR><BR> When date **Modified On** is used to sort posts on the timeline, the location in the timeline adjusts to the top when there are responses to that post. <BR><BR> **NOTE**: The timeline doesn't automatically refresh when post replies are added.|

### Configure form for posts

You can configure how information is displayed in posts, such as relevant users and dates, and whether or not to include labels. This enables you to increase or reduce the number of timeline records that appear onscreen.

![Configure the form for posts.](media\timeline-configure-form-posts.png "Configure the form for posts")

Go to your timeline configuration in [make.powerapps.com](https://make.powerapps.com "make.powerapps.com"), scroll down to the **Posts** section containing the **Configure form** field, and edit the following fields in the default form:

- Header
  - Label option: Hide, show, or show on hover the label, "Created by" or "Modified by".
  - Label: Select the **Use default label** checkbox label to display the label.
  - Data field: Select to show the user who created the post. The label changes to match the data field you selected.
  - Display option: Always show, show on expand, or hide this header containing the user who created the post.
- Body2
  - Label option: Show or hide the label of the post.
  - Display option: Always show, show on expand, or hide the body text.
- Footer
  - Label option: Show or hide the label, "Created on", "Modified on", or "Overridden on".
  - Data field: Select to show the createdon or modifiedon date.
  - Display option: Always show, show on expand, this footer containing the createdon or modifiedon date.

## Configure mentions in notes and posts on timeline

To enable mentions in notes and posts, contact [Microsoft Help + support](/power-platform/admin/get-help-support.md). You can also temporarily try out this feature before asking Microsoft to enable it by appending the following text string to your current browser session URL:

```
     &flags=FCB.TimelineWallRichTextPosts=true,FCB.TimelineNotesRichTextMentions=true

```

When the rich text editor is enabled, users can mention other users and entities in notes and posts using the **@** and **#** symbols. Configuration for the rich text editor is available in the maker experience in **Power Apps**: [make.powerapps.com](https://make.powerapps.com "make.powerapps.com"). The users and entities that are displayed are pulled from the configuration file provided in the **Rich text editor configuration URL** field. More information: [Use the rich text editor control in Power Apps](/powerapps/maker/model-driven-apps/rich-text-editor-control)

By default, the **@** symbol returns matches with the first name, last name, or email address of system users starting with the search string.

By default, the **#** symbol returns matches with the account and contact name entity records starting with the search string.

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
The "systemser" entity will persist for **@** and the "account" and "contact" entities for **#** regardless of how the file is edited.

## Save and publish timeline updates and changes

Before you can view any configuration changes on the entity form, you must first save and publish your updates on the timeline component. 

![Save and publish timeline updates and changes.](media\timeline-save-and-publish-updates-and-changes-1b.png "Save and publish timeline updates and changes")

1.	Before you can publish, you must **Save** any changes you've made in the timeline component.
2.	After your configuration changes are saved, you can  **Publish** them, which makes them live in your timeline environment and viewable.

## Configure dashboard timelines

Timelines can be configured and put on a dashboard. However, the configuration available for timeline applied to a dashboard is limited to the functionality provided by the legacy designer experience. The new form designer experience on dashboards is not available. 

> [!NOTE]
> Capabilities on a dashboard timeline are different than those in an embedded dashboard timeline.  
Dashboard timelines contain records related to the current user. This means each user will see a different set of information when viewing the same dashboard timeline. Notes are not available on the dashboard.

This following image shows the General tab, where you can modify the Timeline Control properties:

![Timeline Control Properties General tab.](media\timeline-control-properties-general.png "Timeline Control Properties General tab")

The following image shows the Activities tab, where you can modify the Timeline Control properties:

![Timeline Control Properties Activities tab.](media\timeline-control-properties-activities.png "Timeline Control Properties Activities tab")

## Configure auto-post messages to display on the timeline

> [!NOTE]
> The auto-post functionality is only available for CRM applications and is not available for CDS-only organizations.

You can configure which auto-post messages will appear on the timeline when a system event occurs. The auto-post configuration replaces the legacy Activity Feed Configuration and Activity Feed Configuration Rules.

To configure the auto-post messages that should be displayed:

1. In Customer Service Hub, go to **Service Management**, and under **Timeline settings**, click **Auto-post rules**.
2. Select which auto-post rules to make active using the grid and **Activate** and **Deactivate** buttons at the top.

When a system event corresponding to an active rule occurs, an auto-post message will display on the timeline.

![Auto-post rules timeline settings.](media\timeline_auto-post_rules.png "Auto-post rules timeline settings")

If you are using a CRM app other than CSH or CSw, you need to add your own sitemap. To add your own site map in your app:

1. Open your app in the App Designer in **Power Apps**: [make.powerapps.com](https://make.powerapps.com "make.powerapps.com")
2. Click the pencil icon to open the Sitemap Designer.
3. Click the + symbol and select **Subarea** from the dropdown list.
4. In the **Entity** dropdown list, select **Post Rule Configuration entity**, and enter a **Title**.
5. Click **Save** and then click **Publish**.

![Add a subarea in the Sitemap Designer.](media\timeline_sitemap_designer_subarea.png "Add a subarea in the Sitemap Designer")

## Create and add custom activities to timeline

You can create custom entities to display on the timeline by enabling specific options during the creation of the entity. See the [How to create and add custom activities](/powerapps/maker/model-driven-apps/set-up-timeline-control#enable-custom-activity-in-timeline) for a step-by-step guide.

## Configure blocked attachment file types in timeline

You can configure the file types that are blocked from being added as file attachments.

1. Go to **Settings** > **Advanced settings** > **Settings** > **Administration** > **System Settings**.
2. In the **System Settings** dialog, under the **General** tab, scroll down to **Set blocked file extensions for attachments**.
3. In the field, type the file extension type you want to block for attachments (for example, ".pdf"). Separate file types with a semi-colon.
4. Select **OK**.

### See also

[FAQs for timeline control](faqs-timeline-control.md) 


[!INCLUDE[footer-include](../../includes/footer-banner.md)]
