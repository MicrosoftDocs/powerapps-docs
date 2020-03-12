---
title: "Set up the timeline control (section) in PowerApps | MicrosoftDocs"
description: "Learn how to set up the timeline control (section) in PowerApps"
ms.date: 03/10/2020
ms.service: powerapps
author: "kabala123"
ms.assetid: 7F495EE1-1208-49DA-9B02-17855CEB2FDF
ms.author: "kabala"
manager: "shujoshi"
search.audienceType: 
  - maker
search.app: 
  - PowerApps
  - D365CE
---

# Set up timeline section (control)

The activities that you use in Timeline to keep track of all your communications with a customer or contact can be customized according to your business or organization requirements.

  > [!div class="mx-imgBorder"]
  > ![Timeline view of activities in PowerApps](../../user/media/TimelineViewOfActivity.png "Timeline view of activities in PowerApps")

  1. Search Records
  2. Take notes
  3. Add info and activities
  4. Filter
  5. More commands
  6. Activity status
  7. Activity icons
  8. Date and time

To learn more, see [Add an appointment, email, phone call, note, or task activity to the timeline](../../user/add-activities.md).

The customization is categorized into the following areas:

- Module
- Activity type
- Field

## Customize modules

The modules are Activities, Posts, and Notes. As a customizer, you can choose which modules you want to show to the users as per your business requirements.

1.	Sign in to your `https://<YourOrgURL>.dynamics.com/apps` environment.

2.  Open a model-driven app, and then on the command bar, select **Settings** ![Settings](../model-driven-apps/media/powerapps-gear.png "Settings") > **Advanced  Settings**.

3.	Go to **Settings** > **Customization** > **Customize the System**. The solution explorer page opens in a new browser window. 

4.	Expand **Entities** under **Components** in the default solution pane.

5.	Select an entity and select **Forms**. For example, select the **Account** entity.

6.	Select the **Account for Interactive experience** record that is a **Main** form type. The **Account for Interactive experience** form opens in a new browser window.

   > [!div class=mx-imgBorder] 
   > ![Select the entity form with interactive experience in the name](media/account-interactive-experience.png "Select the entity form with interactive experience in the name")

   For Unified Interface, you need to use the form name that has `<Entity> for Interactive experience`. The form names for other entities are as follows:

   | Entity | Name |
   |--------------------------|----------------------------------|
   | Account | Account for Interactive experience |
   | Case | Case for Interactive experience |
   | Contact | Contact for Interactive experience |

7.	Double-click the **Conversation Tabs** field in the **Timeline** section. The **Activities Tab Properties** dialog is displayed.

    > [!div class=mx-imgBorder] 
    > ![Double-click the field in the social pane](media/timeline-conversation-tabs-field.png "Double-click the field in the social pane")   

8.	Select the **Show selected** option for the **Show these modules** field in the **Filter by** container.

9.	Select the modules you want to display to the users. Select only the modules that are required by your organization.

10.	Specify the following in the **Additional Options** container.


    | Field/option | Description | Value |
    |------------------------------------------|--------------------------------------------------------------|---------------------------|
    | Default Module for Create Experience | Select the module for which you want the default create experience in the timeline. <br><br> The default value is **Notes**.  | Notes |
    | Show filter pane | Select the checkbox if you want to display the filter icon for the users. If you leave the check box empty, there will be no filters for the users. |  |
    | Expand filter pane by default | Select the checkbox, by default, if you want to show the filter pane in the expanded mode. <br><br> **Note:** When the timeline is displayed on more than one column, the filter pane is displayed as a column alongside the timeline records. Even though you've cleared **Expand filter pane by default** check box in the Timeline configurations, the filter pane will always be displayed to your agents.|
    | Sort | Select the sorting order based on which the records are displayed on the timeline. The sorting is based on the field you choose for Activities. If a field doesn’t exist for the Post, Notes, or Activity, then the sorting is done based on the **Last Updated** field. <br><br> The default sort order is **Descending**.  <br><br> **Note:** changing the sort order will not change the time property visualized in the timeline control. To customize the timeline card form see, [Customize the card form](#customize-the-card-form).  | Descending |
    | Number of results | The maximum number of records that are displayed on the timeline before selecting the **More** option. Each time you select the **More** option, the timeline displays the configured number of records. You can configure a value ranging from 1 to 50. <br><br> The default value is **10**. | 10 |

    > [!div class=mx-imgBorder] 
    > ![Set up timeline module](media/timeline-module.png "set up timeline module")

11.	Select **OK**, and then select **Save**.

12.	Select **Publish** to publish the customizations.

## Customize activity

As a customizer, you can choose which entities you want to show activities to users as per your business requirements. For a better performance, select only the activities that are specific to business, and unselect the activities that aren't used.

1.	Sign in to your `https://<YourOrgURL>.dynamics.com/apps` environment.

2.  Open a model-driven app, and then on the command bar select **Settings** ![Settings](../model-driven-apps/media/powerapps-gear.png "Settings") > **Advanced Settings**.

3.	Go to **Settings** > **Customization** > **Customize the System**. The solution explorer page opens in a new browser window.  

4.	Expand **Entities** under **Components** in the default solution pane.

5.	Select an entity and select **Forms**. For example, select the **Account** entity.

6.	Select the **Account for Interactive experience** record that is a **Main** form type. The **Account Account for Interactive experience** form opens in a new browser window.

    > [!div class=mx-imgBorder] 
    > ![Select the entity form with interactive experience in the name](media/account-interactive-experience.png "Select the entity form with interactive experience in the name")

    For Unified Interface, you need to use the form name that has `<Entity> for Interactive experience`. The form names for other entities are as follows:

    | Entity | Name |
    |--------------------------|----------------------------------|
    | Account | Account for Interactive experience |
    | Case | Case for Interactive experience |
    | Contact | Contact for Interactive experience |

7.	Double-click the **Conversation Tabs** field in the **Timeline** section. The **Activities Tab Properties** dialog is displayed.

    > [!div class=mx-imgBorder] 
    > ![Double-click the field in the social pane](media/timeline-conversation-tabs-field.png "Double-click the field in the social pane") 

8.	Select the **Show selected** option for the **Show these activities** field in the **Filter by** container.

9.	Select the activities you want to display to the users.

10. Select an option from the list for the **Sort timeline by** option in the **Data** container. For example, select the **Last Updated** option.

11.	Specify the following in the **Additional Options** container.
    
    | Field/option | Description |Value |
    |------------------------------------------|------------------------------------------------------------|-------------------|
    | Display activity header using |  Possible values are **Default format** and **Field Labels**. <br><br> **Note:** <ul><li> If you select **Default format**, then you should always select **Default Fields** for the **Display activities using** field. <br> ![Default format and Default fields](media/default-format-default-fields.png "Default format and Default fields") </li> <li> If you select **Field Labels**, then you can either select the **Default Fields** or **Card Form** for the **Display activities using** field. <br> ![Field labels and Default home](media/field-label-card-form.png "Default format and Default fields") </li> <li> When you select **Default format** and select **Card Form** for the **Display activities using** field, then the system ignores the **Card Form** value and uses the **Defaults Fields** to display the activities. </li> <ul>| Default format |
    | Create activities using | Select on how you want the users to create activities. Possible values are **Quick Create Form** and **Main Form**. | Quick Create Form |
    | Display activities using | Select how you want to display the activities. Possible values are **Default Fields** and **Card Form**.  If you select **Card Form**, then you need to select a card form for the activity.  | |
    | Select activity | Select an activity from the list.  <br><br> **Note:** This field appears only when you select **Card Form** for the **Display activities using** field.| Email |
    | Select Card Form | Select a card form from the list.  <br><br> **Note:** This field appears only when you select **Card Form** for the **Display activities using** field. | Email Card form |

    > [!div class=mx-imgBorder] 
    > ![Customize timeline module](media/timeline-activity1.png "Customize timeline module")

12.	Select **OK**, and then select **Save**.

13.	Select **Publish** to publish the customizations.

Since the example considered in this procedure is **Account**, let us see the **Email** activity in the **Timeline** control of an account page.

   | Field | Value |
   |---------------------------|---------------------------|
   | Display activity header using | Default format |
   | Display activities using | Default fields |

   > [!div class=mx-imgBorder] 
   > ![Email activity in timeline](media/timeline-email-activity1.png "Email activity in timeline")

   The default fields for an email activity in the collapsed mode contains the following:

   1. Email from \<Owner\>
   2. Subject
   3. Description
   4. Activity status
   5. Date and time

After modifying the **Email card** form (from the **Email** entity) and updating the options in the **Account for Interactive experience** form in the **Account** entity, you can view see the changes.

   | Field | Value |
   |---------------------------|---------------------------|
   | Display activity header using | Field labels |
   | Display activities using | Card form |
   | Select activity | Email |
   | Select card form | Email Card form |

   > [!div class=mx-imgBorder] 
   > ![Email activity in Timeline](media/timeline-email-activity2.png "Email activity in Timeline")

   The default fields for an email activity in the collapsed mode contains the following:

   1. Owner \<Name\>
   2. Priority
   3. Description
   4. Activity status

Default string for the activities are as follows:

| Activity | Default fields | Image |
|----------------|--------------------------------|------------------------------|
| Appointment | `Appointment from <Owner Name>`| ![Appointment](media/appointment.png "Appointment") |
| Email | `Email from <Owner Name>` | ![Email](media/email.png "Email") |
| Phone Call | `Phone Call from <Owner Name>` <br> When agent initiates a call.| ![Phone Call](media/phonecall-owner.png "Phone Call") | 
| | `Phone Call from <Contact>` <br> When customer initiates a call. | ![Phone Call](media/phonecall-contact.png "Phone Call") |
| Task | `Task modified by <Owner Name>` | ![Task](media/task.png "Task") |
| Note | `Note modified by <Owner Name>` | ![Note](media/note.png "Note") |
| Post | `Post by <Owner Name>` | ![Post](media/post.png "Post") |

## Customize field sections

In the timeline section, users see a card for each activity (based on the enabled activities). Each card displays certain fields in the collapsed and expanded mode. For example, see **Email** activity card in collapsed mode, hover mode, and expanded mode. 

**Email card collapsed mode**: By default, the activity cards are in collapsed mode.


   > [!div class=mx-imgBorder] 
   > ![Timeline card in collapsed mode](media/email.png "Timeline card in collapsed mode")

**Email card hover mode**: When you hover your cursor, you can see few commands that are specific to each of the activity card types.

   > [!div class=mx-imgBorder] 
   > ![Timeline card in collapsed mode](media/email-hover.png "Timeline card in collapsed mode")

**Timeline card expanded mode**: When you select on card, it gets expanded with few commands that are specific to each of the activity card types.

   > [!div class=mx-imgBorder] 
   > ![Timeline card in expanded mode](media/email-expanded.png "Timeline card in expanded mode")

In the card, if you want to show any fields that are important to your business, you can customize the fields. Also, you can move the fields from one section to another section, such as from the **Header** section to the **Detail** section. To learn more, see [Customize the card form](#customize-the-card-form).

### Customize the card form

Any card form has the following sections:

   | Section annotation | Section name | Display columns |
   |------------------------------|--------------------------------------|---------------------------------------|
   | A | ColorStrip | ColorStrip section is never displayed to the user. |
   | B | Header | Fields 1 and 2 in are displayed to the user. |
   | C | Details | Fields 3, 4, and 5 are displayed to the user where Fields 3 and 4 are displayed in the collapsed mode and Field 5 is displayed in the expanded mode. |
   | D | Footer | Footer section is never displayed to the user. |

For example, see **Email form**.

**Email configuration screen**

   > [!div class=mx-imgBorder] 
   > ![Email card configuration](media/customize-field-email.png "Email card configuration")

**Email card collapsed mode**

Fields **1** and **2** from the **Header** section and Fields **3** and **4** from the **Details** section are displayed in the collapsed mode. Fields **3** and **4** in the collapsed mode doesn't show contents in the rich text format.

   > [!div class=mx-imgBorder] 
   > ![Email card in collapsed mode](media/email-card-collapsed.png "Email card in collapsed mode")

**Email card hover mode**

Fields **1** and **2** from the **Header** section and Fields **3** and **4** from the **Details** section are displayed in the hover mode.

   > [!div class=mx-imgBorder] 
   > ![Email card in collapsed mode](media/email-card-hover.png "Email card in collapsed mode")

**Email card expanded mode**

Field **5** from the **Details** section is displayed in the expanded mode. Field **3** in the expanded mode doesn't shown contents in the rich text format, whereas field **4** in the expanded mode shows contents in the rich text format.

   > [!div class=mx-imgBorder] 
   > ![Email card in expanded mode](media/email-card-expanded.png "Email card in expanded mode")

To customize the card form, follow these steps:

1.  Sign in to your `https://<YourOrgURL>.dynamics.com/apps` environment.

2.  Open a model-driven app, and then on the command bar select **Settings** ![Settings](../model-driven-apps/media/powerapps-gear.png "Settings") > **Advanced  Settings**.

3.	Go to **Settings** > **Customization** > **Customize the System**. The solution explorer page opens in a new browser window.  

4.	Expand **Entities** under **Components** in the default solution pane.

5.	Select an entity and select **Forms**. For example, select the **Email** entity.

6.	Select the **Email Card form** record from the list. The **Email Card form** opens in a new browser window.

7.  Add, move, or delete the fields. To learn more, see [Add, configure, move, or delete fields on a form](add-move-or-delete-fields-on-form.md).

   In this procedure, we'll modify **Email Card**. 

   > [!div class=mx-imgBorder] 
   > ![Email card configuration](media/customize-field-email1.png "Email card configuration")

   In the **Header** section, the **Created on** field is replaced with **Priority**.

   Similarly, in the **Details** section, the **Priority** field is removed, and the **Subject** field is moved up.

8.	Select **OK**, and then select **Save**.

9.	Select **Publish** to publish the customizations.

Now, you can view the changes in the **Timeline** control. In the collapsed mode, you can view the changes made to the card.

   > [!div class=mx-imgBorder] 
   > ![Email card configuration](media/email2.png "Email card configuration")

> [!Note]
> If a field doesn't have any value, then in the card, the field value remains empty. 

## Enable custom activity in timeline

While you create a custom entity, you might want to show the custom entity as an activity for your users in the timeline. To show the custom entity as an activity, you need to enable certain options during the creation of a custom entity.

> [!Note]
> Ensure to enable the custom entity as an activity before you create the entity. After you create the custom entity, you can't enable the entity as an activity and display for your users in the **Timeline** control.

To enable a custom activity in timeline, follow these steps.

[Step 1: Create an entity](#step-1-create-an-entity)

[Step 2: Add entity to the model-driven app](#step-2-add-entity-to-the-model-driven-app)

### Step 1: Create an entity

You can create an entity either in [classic mode](#classic-mode) or [Power Apps](#powerapps). 

#### Classic mode

1.	Sign in to your `https://<YourOrgURL>.dynamics.com/apps` environment.

2.  Open a model-driven app, and then on the command bar select **Settings** ![Settings](../model-driven-apps/media/powerapps-gear.png) > **Advanced  Settings**.

3.	Go to **Settings** > **Customization** > **Customize the System**. The solution explorer page opens in a new browser window.  

4.	Select **Entities** under **Components** in the default solution pane.

5.  Select **New** to create an entity. A new browser window is displayed.

6. Enter the required fields as described in the [Create an entity](https://docs.microsoft.com/dynamics365/customerengagement/on-premises/customize/create-entities) topic. 

   > [!Note]
   > The [Create an entity](https://docs.microsoft.com/dynamics365/customerengagement/on-premises/customize/create-entities) topic is even applicable to the Dynamics 365 model-driven apps.

7. Select the areas where you want to display the custom entity.

8. Scroll down to the **Communication & Collaboration** section and select the required options.

9. Scroll down to the **Data Services** section and select **Allow quick create** check box. This option allows you open the entity in a quick create form.

10. Scroll up to the **Entity Definition**, section and select the **Define as an activity entity** check box. This option enables the entity as an activity. 

    > [!Note]
    > Only during the creation of the entity, you can enable this option. Once the entity is created, you can't update this check box.

11. Ensure that the **Display in Activity Menus** check box is also selected.

    > [!Note]
    > This option ensures that the activity is listed in the **Timeline** control menu.

    > [!div class=mx-imgBorder] 
    > ![Display activity](media/display-activity-classicmode.png "Display activity")

12. Select **Save**.

13. Select **Publish** to publish the customizations.

#### PowerApps

Follow the [Create a custom entity](../common-data-service/data-platform-create-entity.md) topic to create an entity using the PowerApps.

After Step 3 in the [Create an entity](../common-data-service/data-platform-create-entity.md#create-an-entity), before saving creating the entity, ensure you perform the following:

1. Expand **More settings** > **Entity type and ownership**.

2. Select the **Activity entity** option from the **Choose entity type** drop-down list.

3. Ensure the **Display in Activity menus** check box is selected.

4. Expand **Create and update settings**.

5. Select the **Enable quick create forms** check box.

    > [!div class=mx-imgBorder] 
    > ![Display activity](media/display-activity-pa.png "Display activity")

6. Select any other required option and then select **Create**.

### Step 2: Add entity to the model-driven app

After you create the entity and enable it as an activity, you need to add the entity to the model-driven app.

1. Sign in to your `https://<YourOrgURL>.dynamics.com/apps` environment.

2. Select the ellipsis (**...**) on a model-driven app tile. For example, **Customer Service Hub** app tile.

3. Select **OPEN IN APP DESIGNER**. The App Designer opens in a new tab.

4. Look for the custom entity you created under **Entity View** in the canvas area.

5. Select **Forms**. The option is displayed in the components pane.

6. Select the check box under under **Quick Create Forms** area. This option uses the quick create form when the user selects **+** button in the **Timeline** control.

    > [!div class=mx-imgBorder] 
    > ![Display activity](media/app-designer-activity.png "Display activity")

7. Select **Save**.

8. Select **Publish**.

## Enable custom activities in timeline for mobile client

When you’ve custom activities that you want to show for users using mobile, then you must enable it. Follow these steps to enable.

### Enable for mobile 

1.	Sign in to your `https://<YourOrgURL>.dynamics.com/apps` environment.

2. Open a model-driven app, and then on the command bar select **Settings** ![Settings](../model-driven-apps/media/powerapps-gear.png) > **Advanced  Settings**.

3.	Go to **Settings** > **Customization** > **Customize the System**. The solution explorer page opens in a new browser window.  

4.	Expand **Entities** under **Components** in the default solution pane.

5.	Select an entity form the list. For example, Account.

6.	Scroll down to **Outlook & Mobile** section, and select the check box for the following options:

    -	Enable for mobile (according to your requirements)
    -	Read-only in mobile (according to your requirements)

7.	Select **Save**.

8.	Select **Publish** to publish the customizations.

### Select the modules to display

After you select **Enable for mobile** and **Read-only in mobile** options (as per your requirement) for an entity, you need to select the module to display in the timeline. Select **Show all** if you want to show all the modules or select **Show selected** if you want to show one or more modules as per your business requirement. If you select **Show selected**, choose the modules you want to display.
Follow the Steps 1-8 described in the [Customize modules](#customize-modules) section, and then save and publish the customizations.

   > [!div class=mx-imgBorder] 
   > ![Select Timeline modules to display](media/timeline-activity.png "Select Timeline modules to display")

## Enable or disable rich-text editor for notes in timeline

Rich-text editor enables users to create rich and well-formatted content for the notes with emphasis. The editor brings common word processor features. To learn more, see [Take notes](https://docs.microsoft.com/dynamics365/customer-service/customer-service-hub-user-guide-basics#take-a-note).

The feature is enabled by default. If you want to disable and enable later for your users, follow the steps:

1.	Sign in to your `https://<YourOrgURL>.dynamics.com/apps` environment.

2. Open a model-driven app, and then on the command bar select **Settings** ![Settings](../model-driven-apps/media/powerapps-gear.png) > **Administration** > **System Settings**.

3. In the **System Settings** dialog, under the **General** tab, scroll down and select or unselect the check box for the **Use rich text to make it easier to format notes created in Timeline.** field.

4. Select **OK**.

    > [!div class=mx-imgBorder] 
    > ![Enable rich-text editor](media/timeline-note-enable-rich-text-editor.png "Enable rich-text editor")

The rich-text editor is enabled or disabled for your users based on the check box selection. 

## See also

[FAQs for timeline control](faqs-timeline-control.md)

[Timeline section in the Customer Service Hub app](https://docs.microsoft.com/dynamics365/customer-service/customer-service-hub-user-guide-basics#timeline)

[Add an appointment, email, phone call, note, or task activity to the timeline](../../user/add-activities.md)
