<properties
    pageTitle="KratosApps tutorial: PowerFlow Advanced"
    description="Edit an existing PowerFlow to use advanced parameters."
    services="kratosapps"
    authors="aftowen"
 />

<tags
   ms.service="kratosapps"
   ms.devlang="na"
   ms.topic="get-started-article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="10/06/2015"
   ms.author="anneta"/>

# Edit a PowerFlow #
Edit an existing PowerFlow to take action when something happens by taking advantage of advanced parameters.

**Prerequisites**

- Create the PowerFlow in the [Create a PowerFlow article](get-started-powerflow.md)

## Editing advanced parameters

1. Open KratosApps, and then click **Flows** in the right navigation.

2. In the list of PowerFlows, click the edit icon next to one that you created in the previous procedure (the *pencil* icon).

3. Click the `...` icon towards the bottom of the **Send email** step.

    ![Sharepoint triggers](./media/advanced-parameters-powerflow/advanced.png)

4. Click on the **Importance** dropdown. You should see three options: *Low*, *Normal* and *High*. Choose High Importance. 

5. Click the `...` icon again to hide the advanced parameters.

6. Save your PowerFlow by clicking **Done** near the bottom of the screen.

    ![Click the done button](./media/get-started-powerflow/done2.png)

## Adding additional steps ##

In this procedure, you'll add an action in the middle of the flow. This action will save a file in your Dropbox archiving the item in the list.

1. PowerFlows, click the down arrows next to each of the actions to collapse them. Click on the **SharePoint** action to select it. 

2. Click the "+" button and select **Add action**. This will insert an action between the trigger and the **Send email** step.

    ![Collapsed add](./media/advanced-parameters-powerflow/collapsed.png)

3. In the list of actions, search for **Create file**, and click it. As with SharePoint, if you haven't already connected to Dropbox, you will need to provide the credentials for your account too.

4. In the form that appears, type a folder path. To just have the fire created in the root of your dropbox type `/`.

5. Give the file a name. To have the file be unique for each list item you should click on a placeholder (otherwise each list item will override the file).

6. Finally, fill out the content you want in the file. Select as many placeholders from the SharePoint list as you want.

    ![Token added to the field](./media/advanced-parameters-powerflow/dropbox.png)

7. Click **Done**.

8. Finally, you'll want to test the flow. Open the SharePoint online list and on the main page for the list, click **new item**

    ![Adding a row](./media/get-started-powerflow/addrow.png)

9. Specify data in each field of the list item, and click Save.

    Within a minute, you should see a new file in your Dropbox.

## Delete your PowerFlow ##

If you're done with the PowerFlow and don't want to get notifications anymore, then you can delete it from the portal.
1. Open KratosApps, and then click **Flows** in the right navigation.

2. In the list of PowerFlows, click the delete icon next to one that you created in the previous procedure (the *trash can* icon).

    ![Delete confirmation](./media/advanced-parameters-powerflow/delete.png)

3. You'll get a confirmation dialog, asking if you are sure you want to delete your flow. To confirm, type the full name into the text box and click **Delete**.
