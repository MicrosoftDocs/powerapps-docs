---
title: Notify Manager on completion of inspection
description: Learn about the changes that would be required to notify the manager on completion of an inspection.
author: navjotm
ms.service: powerapps
ms.topic: conceptual
ms.custom: 
ms.date: 08/16/2021
ms.author: namarwah
ms.reviewer: tapanm
contributors:
  - joel-lindstrom
  - navjotm
  - tapanm-msft
  - sbahl10
---

# Notify manager on completion of inspection

The Inspections sample app allows users to create and perform inspections in the app. There are three apps - one per persona to perform, manage, and review Inspections. The three apps are&mdash;Inspections, Manage Inspections and Review Inspections.

Let’s say you're using inspections to investigate a report of a problem in an area. And for unresolved issues, you want to notify the manager of the person responsible for the area so that they can provide the employee with coaching. In this article, we'll learn how to send a notification to the manager of the person responsible for the location being inspected.

The outcome is that the Inspection app can be used to verify that employees are maintaining an area, and provide notification to management if there are issues. For example, the store manager may want to know if the supervisor of the electronics section of a store is properly maintaining the area of their store and if an issue is found, send their manager an email.

> [!NOTE] Before you begin, read [Customize the Inspection app](customize-inspections.md).

## Prerequisites

To complete this lesson, we'd need the ability to log in into Microsoft Teams that will be available as part of select Microsoft 365 subscriptions, and will also need to have the Inspections sample app for Microsoft Teams installed. This app can be installed from https://aka.ms/TeamsInspection.

## Login into the Manage Inspections app

1. Login into Teams, and select Power Apps from the left-pane.

1. Select **Build** tab from the top.

1. Select **Manage Inspections** to open the app in the editor.

![Select Manage Inspections app](media/notify-manager-on-completion-of-inspections/select-manage-inspections-app.png "Select Manage Inspections App")

### Add a new field to the Locations table

Next, we'll add a responsible person column to the location table so we can choose the responsible person for the area.

1. On the Home screen, select **See more** under the **Recent apps** section.

    ![Select See more under the Recent apps section](media/notify-manager-on-completion-of-inspections/select-see-more.png "Select See more under the Recent apps section")

1. Go to the **Installed apps** tab, and select **See all**.

    ![Select See all option](media/notify-manager-on-completion-of-inspections/installed-apps-see-all-option.png "Select See all option")

1. Select **Area Inspection Location**.

    ![Select Area Inspection Location table](media/notify-manager-on-completion-of-inspections/area-inspection-location-from-list-of-objects.png "Select Area Inspection Location table")

1. Select **Add Column** on the top-left.

1. Enter the following column details, and then select **Done** to create the **Responsible User** column.

   - Display name – **Responsible User**
   - Data type – **Lookup**
   - Related table – **User**

    ![Add Responsible User column](media/notify-manager-on-completion-of-inspections/add-responsible-user-column.png "Add Responsible User column")

    > [!NOTE] Users must log in to the app one time before they can be selected from the user table.

1. On the **Build** tab under Installed apps, select **Manage Inspections**.

1. Select **Area Inspection Locations** from the left-pane, and then select **Edit**.

    ![Edit Area Inspection Locations Table](media/notify-manager-on-completion-of-inspections/edit-area-inspection-locations-table.png "Edit Area Inspection Locations Table")

    The **Responsible User ID** column gets added to the **Area Inspection Locations** table.

1. Update the **Area Inspection Location** with the Responsible User values.

    ![Responsible User column in the Area Inspection Locations table](media/notify-manager-on-completion-of-inspections/responsible-user-column-in-area-inspection-location-table.png "Responsible User column in the Area Inspection Locations table")

### Add Responsible User field on the Items Screen on Locations table

Now that we've added the responsible user to the location, we'll now display it on the Items screen.

1. The Responsible User field needs to be added to the Display, Edit, and New sections of the Items Screen. The controls for each of these are all on the same screen but their visibility is controlled by variables. Open the **Items Screen** by selecting it in the Tree view and select the container **conAreaDetails**.

1. Press down the **Ctrl** key, and select the label **Title**.

    ![Copy Title label](media/notify-manager-on-completion-of-inspections/copy-title-label-from-Locations-screen.png "Copy Title label")

1. Copy the Title label control by highlighting it, and selecting **Ctrl + C** to copy it.

1. Use **Ctrl + V** to paste the label.

1. Update the properties of the new label

    | Property | Value |
    | - | - |
    | Text | “Responsible User” |
    | X | `txtArea_EditTitle.X+txtArea_EditTitle.Width+20` |
    | Y | `If(gblEditLocation \|\| gblAddLocation, 107+150, 61+90)`

1. Rename control to **lblAreaDetails_ResponsibleIUser**.

1. Copy and paste the label that says Backstage and update the properties:

    | Property | Value |
    | - | - |
    | Text | `gblLocation.'Responsible User'.'Full Name'` |
    | X | `txtArea_EditTitle.X+txtArea_EditTitle.Width+20` |
    | Y | `If(gblEditLocation \|\| gblAddLocation, 136+150, 91+90)` |

1. Rename control to **lblArea_ResponsibleUser**.

    The screen then looks like this.

    ![Responsible User field on Locations screen](media/notify-manager-on-completion-of-inspections/responsible-user-field-on-locations-screen.png "Responsible User field on Locations screen")

1. Press **Alt** key, and select the **Edit** label on the top-right of the **Items** screen. The Title label is same as created above.

1. Copy and paste the textbox that says **Ambient**, and update the properties:

    | Property | Value |
    | - | - |
    | Default | `If(gblAddLocation, "", gblLocation.'Responsible User'.’Full Name’)` |
    | X | `txtArea_EditTitle.X+txtArea_EditTitle.Width+20` |
    | Y | `If(gblEditLocation \|\| gblAddLocation, 136+150, 91+90)` |
    | Hint Text | "Full Name" |
1. Rename control to **txtArea_EditResponsibleUser**.

    The screen then looks like this.

    ![Locations Screen](media/notify-manager-on-completion-of-inspections/locations-screen.png "Locations Screen")

1. Now, press **Alt** key, and select **Cancel** on the top-right. And then press **Alt** key, and select the **Add location** button on the top-left of the **Items** screen.

    ![Select Add Location button](media/notify-manager-on-completion-of-inspections/select-add-location-button.png "Select Add Location button")

1. Verify that the Responsible User label and the textbox show up while adding a new Location.

    The screen then looks like this.

    ![Responsible User field on the Add Location screen](media/notify-manager-on-completion-of-inspections/responsible-user-field-on-add-location-screen.png "Responsible User field on the Add Location screen")

1. Select the **Save** button, and on the **OnSelect** property, add the following formula to the Patch functions `, 'Responsible User': txtArea_EditResponsibleUser in the two places shown below -`.

    ![Update patch with Responsible User definition](media/notify-manager-on-completion-of-inspections/update-patch-with-responsible-user-definition.png "Update patch with Responsible User definition")

    ![Update second patch with Responsible User definition](media/notify-manager-on-completion-of-inspections/update-second-patch-with-responsible-user-definition.png "Update second patch with Responsible User definition")

Whenever a location is created or updated now, the **Responsible User** value will also be captured and saved on the **Location** record.

### Publish the Manage Inspections app

All the changes to the Manage Inspections app are completed. The app can now be published by selecting the **Publish to Teams** button on the top-right.

![Publish to Teams](media/notify-manager-on-completion-of-inspections/publish-to-teams.png "Publish to Teams")

![Confirm publishing to Teams](media/notify-manager-on-completion-of-inspections/confirm-publishing-manage-inspections-to-teams.png "Confirm publishing to Teams")

![Add to Channel](media/notify-manager-on-completion-of-inspections/add-to-channel.png)

## Edit the inspection app

Now that we've added the field to the Manage Inspections app, we'll create a process to notify the manager of the responsible user when there's an issue.

After publishing the Manage Inspections app, select the **Back** button to go back to the **Build** > **Installed Apps** screen > Select **Inspection**.

![Select Inspection App](media/notify-manager-on-completion-of-inspections/select-inspection-app.png "Select Inspection App")

### Add a Flow to send an Email to the Manager

1. From the Tree View, select the **Review Screen**.

1. Select the **Continue Inspection** (btnContinueSubmitInspection) button.

1. Select the OnSelect property option, copy the entire formula from the formula bar, and then paste it in a text editor.

1. Select the **Continue Inspection** button, and select **...** (ellipsis) on the top, and then select **Power Automate**.

    ![Trigger a Flow on the click of Continue Inspection button](media/notify-manager-on-completion-of-inspections/add-flow-on-continue-inspection-button.png "Trigger a Flow on the click of Continue Inspection button")

1. Select **+ Create** to create a new flow on [Power Automate](https://flow.microsoft.com).

### Create a Flow to send an email to the Manager of the Responsible User

1. Select the Power Apps trigger from the list.

1. Create the flow **Send Manager Notification of Completion of Inspection**.

1. Select **Ask in Power Apps** option for the **Get Inspection Record** – Row ID step, and for the **Send an Email** – To step.

    ![Flow steps to send notification](media/notify-manager-on-completion-of-inspections/notification-flow-steps.png "Flow steps to send notification")

    ![Notification flow send email step](media/notify-manager-on-completion-of-inspections/notification-flow-send-email-step.png "Notification flow send email step")

1. Save the flow.

1. Go back to the Power App Studio in Teams.

1. Select this flow created from the available flows list. Most likely, the existing formula on the button will get erased out.

1. Update the **Run Flow** formula as shown below.

    ```powerapps-dot
    SendManagerNotificationofCompletionofInspection.Run(If(
    !IsBlank(gblSelectedLocation.'Responsible User'.'Primary Email'),
    Office365Users.ManagerV2(gblSelectedLocation.'Responsible User'.'Primary
    Email').mail
    ),gblLastInspection.'Area Inspection');
    ```

1. Copy the old Continue button formula back from the text editor from Step 3 of the **Add a Flow to send an Email to the Manager** section before the flow formula used in the previous step.

1. Save the app.

### Publish the Inspection app

All the changes to the Inspection app are completed. The app can now be published by selecting the **Publish to Teams** button on the top-right.

![Inspection App Publish to Teams](media/notify-manager-on-completion-of-inspections/inspection-app-publish-to-teams.png "Inspection App Publish to Teams")

![Confirm publishing Inspections app to Teams](media/notify-manager-on-completion-of-inspections/confirm-publishing-inspections-to-teams.png "Confirm publishing Inspections app to Teams")

![Add Inspection App to Channel](media/notify-manager-on-completion-of-inspections/add-inspection-app-to-channel.png "Add Inspection App to Channel")

## Verify that a manager exists for the Responsible User

1. Open the link admin.microsoft.com.

1. Select Edit a user.

    ![Verify User has a Manager](media/notify-manager-on-completion-of-inspections/verify-user-manager.png "Verify User has a Manager")

1. Select a User and confirm that the user has a Manager assigned.

    > [!NOTE] If you're working on your organization’s environment, then you'd most likely not need this step. But if working from a trial environment, it is better to create another trial user and add that user as the manager to the Responsible user.

## Test the app

1. Select the Welcome screen from the Tree view in the Editor.

1. Select the **Preview** button to run the app.

    ![Preview Inspection App](media/notify-manager-on-completion-of-inspections/preview-inspection-app.png "Preview Inspection App")

1. Select **Perform an Inspection**.

    ![Perform an inspection button](media/notify-manager-on-completion-of-inspections/perform-an-inspection-button.png "Perform an inspection button")

1. Perform the inspection as shown below.

    ![Complete Inspection Demo](media/notify-manager-on-completion-of-inspections/complete-inspection-demo.gif "Complete Inspection Demo")

    The flow should run after the Submit Inspection button is selected.

1. The easiest way to confirm if the flow ran fine is by opening the Power Automate flow and checking the last run.

    ![Flow run history](media/notify-manager-on-completion-of-inspections/flow-runs.png "Flow run history")

    ![Flow successful run steps](media/notify-manager-on-completion-of-inspections/flow-successful-run-steps.png "Flow successful run steps")

1. Confirm that the email was sent to the right address by selecting and expanding the Send an email step from the flow results.

    The email received is as shown below.

    ![Email screenshot](media/notify-manager-on-completion-of-inspections/email-screenshot.png "Email screenshot")

### See also

- [Understand Inspection sample apps architecture](inspection-architecture.md)
- [Customize Inspection sample app](customize-inspections.md)
- [Customize sample apps](customize-sample-apps.md)
- [Sample apps FAQs](sample-apps-faqs.md)
- [Use sample apps from the Microsoft Teams store](use-sample-apps-from-teams-store.md)

[!INCLUDE[footer-include](../includes/footer-banner.md)]