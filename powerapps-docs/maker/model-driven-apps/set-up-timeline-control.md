---
title: "Set up the timeline control (section) in PowerApps | MicrosoftDocs"
description: "Learn how to set up the timeline control (section) in PowerApps"
ms.date: 11/22/2019
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

The activities in the Timeline that you use to keep track of all your communications with a customer or contact can be customized as per your business or organization requirements.

The customization is categorized into the following areas:

- Module
- Activity type
- Field

## Customize modules

The modules are Activities, Posts, and Notes. As a customizer, you can choose which modules you want to show to the users as per your business requirements.

1.	Sign in to the Common Data Service platform.

2.	Select **Settings** > **Customization** > **Customize the System**. The solution explorer page opens in a new browser window. 

3.	 Expand **Entities** under **Components** in the default solution pane.

4.	Select an entity and select **Forms**. For example, select the Account entity.

5.	Select the **Account** record that is of **Main** form. The **Account** form opens in a new browser window.

6.	Double-click field the **Social Pane** section. The **Activities Tab Properties** dialog is displayed.

7.	Select **Show selected** option for the **Show these modules** field in the **Filter by** container.

8.	Select the modules you want to display to the users.

9.	Specify the following in the **Additional Options** container.


    | Field/option | Value |
    |------------------------------------------|--------------------------------------------------------------|
    | Default Module for Create Experience | Notes <br> Select the module for which you want the default create experience in the timeline. |
    | Show filter pane | Select the checkbox if you want to show the filter pane for the users. |
    | Expand filter pane by default | Select the checkbox, by default, if you want to show the filter pane in the expanded mode. |
    | Sort | Descending <br> Select the default sorting order based on which the records are displayed on the timeline. |
    | Number of results | 10 <br> The maximum number of records that are displayed on timeline. |

    > [!div class=mx-imgBorder] 
    > ![Set up timeline module](media/timeline-module.png "set up timeline module")

10.	Select **OK**, and then select **Save**.

11.	Select **Publish** to publish the customizations.

## Customize activity

As a customizer, you can choose for which entities you want to show the activities to the users as per your business requirements.

1.	Sign in to the Common Data Service platform.

2.	Select **Settings** > **Customization** > **Customize the System**. The solution explorer page opens in a new browser window. 

3.	 Expand **Entities** under **Components** in the default solution pane.

4.	Select an entity and select **Forms**. For example, select the Account entity.

5.	Select the **Account** record that is of **Main** form. The **Account** form opens in a new browser window.

6.	Double-click field the **Social Pane** section. The **Activities Tab Properties** dialog is displayed.

7.	Select **Show selected** option for the **Show these activities** field in the **Filter by** container.

8.	Select the activities you want to display to the users.

9.	Select an option from the list for the **Sort timeline by** option in the **Data** container. For example, select the **Last Updated** option.

10.	Specify the following in the **Additional Options** container.
    
    | Field/option | Value |
    |------------------------------------------|--------------------------------------------------------------|
    | Display activity header using | Default format. <br> Possible values are Default format and Field Labels. |
    | Create activities using | Quick Create Form <br> Select on how you want the users to create activities. Possible values are **Quick Create Form** and **Main Form**. |
    | Display activities using | Select how you want to display the activities. Possible values are **Default Fields** and **Card Form**.  If you select **Card Form**, then you need to select a card form for the activity.  |
    | Select activity | Email <br> Select an activity from the list.  <br> **Note:** This field appears only when you select **Card Form** for the **Display activities using** field.|
    | Select Card Form | Email Card form <br> Select a card form from the list.  <br> **Note:** This field appears only when you select **Card Form** for the **Display activities using** field. |

    > [!div class=mx-imgBorder] 
    > ![Customize timeline module](media/timeline-activity1.png "Customize timeline module")

12.	Select **OK**, and then select **Save**.

13.	Select **Publish** to publish the customizations.

## Customize field sections

In the timeline section, users see a card for each activity (based on the enabled activities). Each card has the following sections:

   | Section annotation | Section name | Display columns |
   |------------------------------|--------------------------------------|---------------------------------------|
   | A | ColorStrip | ColorStrip section is never displayed to the user. |
   | B | Header | Fields 1 and 2 in from the two columns are displayed to the user. |
   | C | Details | Fields 3, 4, and 5 from the single column are displayed to the user. The field 5 is displayed only when the user expands the card. |
   | D | Footer | Four | Footer section is never displayed to the user. |

**Card configuration screen**

   > [!div class=mx-imgBorder] 
   > ![Timeline card configuration](media/customize-field.png "Timeline card configuration")

**Timeline card collapsed mode**

Fields **1**, **2** from the **Header** section and fields **3** and **4** from the **Details** section are displayed in the collapsed mode.

   > [!div class=mx-imgBorder] 
   > ![Timeline card in collapsed mode](media/timeline-card-collapsed.png "Timeline card in collapsed mode")

**Timeline card expanded mode**

Field **5** from the **Details** section are displayed in the collapsed mode.

   > [!div class=mx-imgBorder] 
   > ![Timeline card in expanded mode](media/timeline-card-expanded.png "Timeline card in expanded mode")

In the activity card, if you want to show any fields that are important to your business, you can customize the fields. Also, you can move the fields from one section to another section, such as from the Header section to the Detail section. 

To learn more, see [Add, configure, move, or delete fields on a form](add-move-or-delete-fields-on-form.md).

## Enable custom activities in timeline for mobile client

When you’ve custom activities that you want to show for users using mobile, then you must enable it. Follow these steps to enable.

### Enable for mobile 

1.	Sign in to the Common Data Service platform.

2.	Select **Settings** > **Customization** > **Customize the System**. The solution explorer page opens in a new browser window. 

3.	 Expand **Entities** under **Components** in the default solution pane.

4.	Select an entity form the list. For example, Account.

5.	Scroll down to Outlook & Mobile section, and select the check box for the following options:

    -	Enable for mobile (according to your requirements)
    -	Read-only in mobile (according to your requirements)

6.	Select **Save**.

7.	Select **Publish** to publish the customizations.

### Select the modules to display

After you select **Enable for mobile** and **Read-only in mobile** options (as per your requirement) for an entity, you need to select the module to display in the timeline. Select **Show all** if you want to show all the modules or select **Show selected** if you want to show one or more modules as per your business requirement. If you select **Show selected**, choose the modules you want to display.
Follow the steps 1-8 described in the [Customize modules](#customize-modules) section, and then save and publish the customizations.

   > [!div class=mx-imgBorder] 
   > ![Select Timeline modules to display](media/timeline-activity.png "Select Timeline modules to display")

## See also

[FAQs for timeline control](faqs-timeline-control.md)