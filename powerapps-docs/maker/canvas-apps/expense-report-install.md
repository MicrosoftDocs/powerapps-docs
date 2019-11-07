---
title: Install and configure the Expense Report sample for canvas apps | Microsoft Docs
description: Step-by-step instructions for, in PowerApps, installing and configuring the Expense Report sample for canvas apps.
author: matthewbolanos
manager: kvivek
ms.service: powerapps
ms.topic: sample
ms.custom: canvas
ms.reviewer: tapanm
ms.date: 10/29/2019
ms.author: mabolan
search.audienceType: 
  - maker
search.app: 
  - PowerApps
---
# Install and configure the Expense Report sample for canvas apps in PowerApps

Step-by-step instructions for installing and configuring the Expense Report sample. You can also preview the sample app [here](https://aka.ms/previewmyexpenses).

Estimated time to complete these steps: **10-15 minutes**

> [!TIP]
> Watch [this video](https://youtu.be/kJXZPILfbwU) for a demonstration of how to use the Expense Report sample app. 

Track expense reports from submission to approval. Tally line items as individual expenses accrue and submit for approval when ready. This app requires a small amount of setup to make it your own.

![Opening screen of the Expense Report PowerApp](./media/expense-report-install/expense-report-powerapp.png)

> [!TIP]
> Watch [this](https://youtu.be/kJXZPILfbwU) video to see how to use the Expense Report sample.

## Prerequisites

- [Sign up](../signup-for-powerapps.md) for PowerApps.

## Create the Expenses list

This list stores the expense reports.

1. Open a web browser, and navigate to https://admin.microsoft.com.
2. Log in with an account that has permission to create lists.
3. Navigate to the site collection where you want the Expenses list to reside.
4. Click the gear icon in the top right portion of the web page.
5. Click **Add an app**.
6. In the **Find an app** textbox, enter **Custom**.
7. Click the **search icon**.
8. Click the **Custom List** app.
9. In the **Name** textbox, enter **Expenses**.

	> [!IMPORTANT]
	> If you choose a different name for the list, make sure you write it down because you will need to substitute it for Expenses everywhere you see it during the installation and configuration process.

10. Click **Create**.

### Create Cost Center column

1. Click the **Expenses** list.
2. Click the gear icon in the top right portion of the web page.
3. Click **List settings**.
4. Click **Create column**.
5. In the **Column name** textbox enter **Cost Center**.
6. In the **type of information in this column is** radio button list, select **Choice**.
7. In the **Type each choice on a separate line** textbox, enter the following values, each on a separate line: 
	- Microsoft
	- Contoso
8. In the **Default value** textbox, enter **Microsoft**.
9. Click **OK**.

### Create Comments column

1. Click **Create column**.
2. In the **Column name** textbox, enter **Comments**.
3. In the **type of information in this column is** radio button list, select **Multiple lines of text**.
4. Click **OK**.

### Create Status column

1. Click the **Expenses** list.
2. Click the **gear icon** in the top right portion of the web page.
3. Click **List settings**.
4. Click **Create column**.
5. In the **Column name** textbox enter **Status**.
6. In the **type of information in this column is** radio button list, select **Choice**.
7. In the **Type each choice on a separate line** textbox, enter the following values, each on a separate line: 
	- Open
	- Pending
	- Approved
8. In the **Default value** textbox, enter **Open**.
9. Click **OK**.

### Create ApproverName column

1. Click **Create column**.
2. In the **Column name** textbox, enter **ApproverName**.
3. In the **type of information in this column is** radio button list, select **Person or Group**.
4. In the **Require that this column contains information** radio button list, select **Yes**.
5. Click **OK**.

### Create DateSubmitted column

1. Click **Create column**.
2. In the **Column name** textbox, enter **DateSubmitted**.
3. In the **type of information in this column is** radio button list, select **Date and Time**.
4. In the **Require that this column contains information** radio button list, select **Yes**.
5. Click **OK**.

### Create StartDate column

1. Click **Create column**.
2. In the **Column name** textbox, enter **StartDate**.
3. In the **type of information in this column is** radio button list, select **Date and Time**.
4. In the **Require that this column contains information** radio button list, select **Yes**.
5. Click **OK**.

### Create EndDate column

1. Click **Create column**.
2. In the **Column name** textbox, enter **EndDate**.
3. In the **type of information in this column is** radio button list, select **Date and Time**.
4. In the **Require that this column contains information** radio button list, select **Yes**.
5. Click **OK**.

## Create the LineItems list

This list stores the line items that are associated with each expense report.

1. Navigate to the same site collection where you created the Expenses list.
2. Click the gear icon in the top right portion of the web page.
3. Click **Add an app**.
4. In the **Find an app** textbox, enter **Custom**.
5. Click the **search icon**.
6. Click the **Custom List** app.
7. In the **Name** textbox, enter **LineItems**.

	> [!IMPORTANT] 
	> If you choose a different name for the list, make sure you write it down because you will need to substitute it for LineItems everywhere you see it during the installation and configuration process.

8. Click **Create**.
 
### Create Category column

1. Click the **LineItems** list.
2. Click the gear icon in the top right portion of the web page.
3. Click **List settings**.
4. Click **Create column**.
5. In the **Column name** textbox enter **Category**.
6. In the **type of information in this column is** radio button list, select **Choice**.
7. In the **Type each choice on a separate line** textbox enter the following values, each on a separate line: 
	- Food & Beverage
	- Transportation
	- Business needs
8. In the **Default value** textbox, enter **Food & Beverage**.
9. Click **OK**.

### Create Cost column

1. Click **Create column**.
2. In the **Column name** textbox enter **Cost**.
3. In the **type of information in this column is** radio button list, select **Number (1, 10, 100)**.
4. In the **Require that this column contains information** radio button list, select **Yes**.
5. Click **OK**.

### Create Date column

1. Click **Create column**.
2. In the **Column name** textbox enter **Date**.
3. In the **type of information in this column is** radio button list, select **Date and Time**.
4. In the **Require that this column contains information** radio button list, select **Yes**.
5. Click **OK**.

### Create Description column

1. Click **Create column**.
2. In the **Column name** textbox enter **Description**.
3. In the **type of information in this column is** radio button list, select **Multiple lines of text**.
4. In the **Require that this column contains information** radio button list, select **Yes**.
5. In the **Specify the type of text to allow** radio button list, select **Plain text**.
6. Click **OK**.

### Create ReportID column

1. Click **Create column**.
2. In the **Column name** textbox enter **ReportID**.
3. In the **type of information in this column is** radio button list, select **Lookup (information already on this site)**.
4. In the **Require that this column contains information** radio button list, select **Yes**.
5. In the **Get information from** dropdown list, select the **Expense** list you created.
6. In the **In this column** dropdown list, select **ID**.
7. Click **OK**.

### Edit Title column

1. Click the **Title** column link.
2. In the **Require that this column contains information** radio button list, select **No**.
3. Click **OK**.

## Download the Expense Report app

1. In a web browser, navigate to the following link:

    [https://pappsfeprodwestuscontent.blob.core.windows.net/sampleapps/myexpenses/docs/MyExpenses(SP_List).zip](https://pappsfeprodwestuscontent.blob.core.windows.net/sampleapps/myexpenses/docs/MyExpenses(SP_List).zip).

2. Download the Expense Report PowerApps Sample package, and save it to your machine.

## Create connections

1.	In a web browser, navigate to [make.powerapps.com](https://make.powerapps.com?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc).
2.	Sign in by providing the same credentials that you used to sign up.
3.	In the menu on the left, select **Connections**.

### Create an Approvals connection

1.	Click **+ New connection**.
2.	In the **Search** textbox, enter **Approvals**.
3.	Select **Approvals** in the list.
4.	Click **Create**.
	
### Create an Office 365 Outlook connection

1.	Click **+ New connection**.
2.	In the **Search** textbox, enter **Office 365 Outlook**.
3.	Select **Office 365 Outlook** in the list.
4.	Click **Create**.
5.	In the popup window, select the account you logged in with.

### Create a SharePoint connection

1.	Click **+ New connection**.
2.	In the **Search** textbox, enter **SharePoint**.
3.	Select **SharePoint** in the list.
4.	Click **Create**.
5.	In the popup window, select the account you logged in with.

## Import the app

1. In a web browser, navigate to https://make.powerapps.com.
1. Sign in by providing the same credentials that you used to sign up.
1. In left navigation bar, select **Apps**, and then select **Import package(preview)**.

    ![Import package screen](./media/expense-report-install/import-package.png)

1. Select **Upload**, and then select the package that you downloaded earlier.
1. For the **App** and **Flow** resource types, set **IMPORT SETUP** to **Create as new**.
1. For the **SharePoint** and **Outlook** connections, set **IMPORT SETUP** to **Select during import**.

    ![Import settings screen](./media/expense-report-install/import-settings.png)

1. Select the red icon for the **SharePoint Connection**.
1. In the connections list, select the item with your username.

    ![Import settings screen](./media/expense-report-install/import-settings-sharepoint.png)

1. Select **Save**.
1. Select the red icon for the **Approval Connection**.
1. In the connections list, select the item with your username.

    ![Import settings screen](./media/expense-report-install/import-settings-approvals.png)

1. Select **Save**.
1. Select the red icon for the **Office 365 Outlook Connection**.
1. In the connections list, select the item with your username.

    ![Import settings screen](./media/expense-report-install/import-settings-office365outlook.png)

1. Select **Save**.

    > [!TIP] 
    > When you're done, it will look like this:

    ![Import settings screen](./media/expense-report-install/import-settings-done.png)

1. Select **Import**, and then wait until the process is complete.

    ![Import settings screen](./media/expense-report-install/import-done.png)

## Configure the app to use the SharePoint lists

1. In the web browser, select **Apps**.
2. Select the ellipsis (...) next to the Expense Report app.
3. Select **Edit on the web** > **Allow**.

### Delete connections
1. On the **View** tab, select **Data sources**.
1. In the **Data** pane, select the ellipsis (...) next to **Expenses**, and then select **Remove**.
1. Repeat the previous step to remove the **LineItems** data source.

### Expenses list

1. On the **View** tab, select **Data sources**.
1. In the **Data** pane, select **Add data source** > **New connection** > **SharePoint** > **Create**.
1. In the **Recent sites** list, select the SharePoint site where you created the Expenses list.

    > [!TIP] 
    > If the site doesn't appear in the list, type or paste the URL to the SharePoint site in the textbox, and then select **Go**.

1. In the **Search** box at the top of the list, type or paste **Expenses**.
1. Select the checkbox next to **Expenses**, and then select **Connect**.

### LineItems list

1. On the **View** tab, select **Data sources**.
1. In the **Data** pane, select **SharePoint**.
1. In the **Recent sites** list, select the SharePoint site where you created the LineItems list.

    > [!TIP] 
    > If the site doesn't appear in the list, type or paste the URL to the SharePoint site in the textbox, and then select **Go**.

1. In the **Search** box at the top of the list, type or paste **Line Items**.
1. Select the checkbox next to **LineItems**, and then select **Connect**.
1. Select **File** > **Save** > **Publish** > **Publish this version**.

## Modify the flow

1. In left navigation bar, select **Flows**.
1. If prompted to sign in, provide the same credentials that you used to sign up.
1. Near the top of the screen, select **My flows**.
1. Next to the **ApproveExpense** flow, select the pencil icon.

    ![Edit Flow screen](./media/expense-report-install/edit-flow.png)

1. Expand the **Get items** action. 
1. Change the **Site Address** and **List Name** to match the Expenses list that you created in SharePoint.

    ![Edit Flow screen](./media/expense-report-install/edit-flow-getitems.png)

    > [!TIP] 
    > You don’t need to type it manually; you can select it in the drop-down lists.

1. Expand the **Condition**.
1. Expand the **If yes** section.
1. Expand the **Change item status to Approved** action.
1. Change the **Site Address** and **List Name** to match the Expenses list that you created in SharePoint.

    ![Edit Flow screen](./media/expense-report-install/edit-flow-condition-ifyes.png) 

    > [!TIP] 
    > You don’t need to type it manually; you can select it in the drop-down lists.

1. Expand the **If no** section.
1. Expand the **Change item status to Open** action.
1. Change the **Site Address** and **List Name** to match the Expenses list that you created in SharePoint. 

    ![Edit Flow screen](./media/expense-report-install/edit-flow-condition-ifno.png)

    > [!TIP] 
    > You don’t need to type it manually; you can select it in the drop-down lists.

14. Select **Update flow**.

## Play the app

1. In the web browser, select **Apps**.
1. Select the ellipsis (...) next to the Expense Report app, and then select **Open**.

## Next steps
- [Customize a SharePoint list form](https://docs.microsoft.com/powerapps/maker/canvas-apps/customize-list-form)
- [Add and configure a control](https://docs.microsoft.com/powerapps/maker/canvas-apps/add-configure-controls)
- [Edit and manage permissions for a SharePoint list or library](https://support.office.com/article/edit-and-manage-permissions-for-a-sharepoint-list-or-library-02d770f3-59eb-4910-a608-5f84cc297782)
