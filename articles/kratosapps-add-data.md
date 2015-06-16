<properties
	pageTitle="Add data in KratosApps Studio"
	description="In KratosApps Studio, add data from users or another external source, such as Excel, Office 365 (including SharePoint), a REST source, an Azure mobile service, Bing, or social media."
	services="kratosapps"
	authors="AFTOwen"
 />

#Add data in KratosApps Studio

Make your app information-rich by adding data from one or more of these sources:

- [your users](kratosapps-add-user-data.md)
- [another app built in KratosApps](kratosapps-share.md)
- Excel and Office365, including [SharePoint lists](kratosapps-share.md)
- search results or automatic translation from Bing
- Facebook, Twitter, or Instagram
- an RSS feed or Coursera
- an Azure mobile service or a REST service

**Prerequisite**

- [Create an app](kratosapps-tutorial-inventory) to understand how to perform basic tasks, such as adding a control.

## Add data from Excel ##

1. Open Excel, and then add data similar to this example:

| Product   | Revenue |
|-----------|---------|
| Violins   | 21000   |
| Trombones | 15000   |
| Bongos    | 14000   |

1. Highlight the cells to which you added data, click the **Home** tab of the ribbon, and then click **Format as Table**.
2. Click a table format, ensure that the **My table has headers** check box is selected in the **Format As Table** dialog box, and then click **OK**.
3. On the **Design** tab of the ribbon, specify a name (such as **Revenue**) in the **Table Name** box, and then save and close the workbook.
4. In KratosApps Studio, press Alt+D to open the list of data sources.
5. Under **Add new source**, click **Excel**.
6. Browse for the workbook from which you want to import data, click it, and then click **Open**.
7. Ensure that the check box for each table that you want to import is selected, and then click **Import Data**.
8. Press Esc, or click the Back button to return to the design workspace.
9. (optional) [Show the data in a gallery](kratosapps-share.md).

## Add data from Office 365 ##

1. In KratosApps Studio, press Alt+D, and then click **Office 365 Preview** in the list of data sources.
2. Click **Connect**, and then sign in.
3. After your app is registered, press Esc to return the design workspace.
4. (optional) Show your **Inbox** in a gallery:
	1. On the **Insert** tab, click **Gallery**, and then click a landscape or portrait **Text Gallery**.
	2. Set the **Items** property of the gallery to this function:
	
		**Office365!Emails("Inbox")!items**

