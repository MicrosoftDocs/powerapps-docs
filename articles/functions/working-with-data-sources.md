<properties
	pageTitle="PowerApps: Working with Data Sources"
	description="Reference information for working with connections and data sources"
	services=""
	suite="powerapps"
	documentationCenter="na"
	authors="gregli-msft"
	manager="dwrede"
	editor=""
	tags=""/>

<tags
   ms.service="powerapps"
   ms.devlang="na"
   ms.topic="article"
   ms.tgt_pltfrm="na"
   ms.workload="na"
   ms.date="11/10/2015"
   ms.author="gregli"/>

# Working with Data Sources in PowerApps #

Data Sources are an extension of [Tables](working-with-tables.md) that use [connections](file-name.md) to retrieve and store information in a service.  You can use data sources to read and write data in Excel workbooks, SharePoint lists, SQL Server tables, and many other services.

## Data sources ##

As we learned in [Working with Tables](working-with-tables.md), Tables in PowerAops are values, just as a number or a string is a value. Tables are not stored anywhere. The structure and data of a table cannot be modified directly, only derivative tables created through a formula. 

Some of the most interesting tables are stored for later retrieval and sharing.  PowerApps provides "connections" to read and write stored data.  Within a connection, multiple tables of information can be exposed.  You will select which tables to use in your PowerApp and each will become a separate *data source*  

A Data Source is an extension of a table and can be used in any context that a table is used.  Just like a table, it has records, columns, and properties that can be used in formulas.  In addition:

- The data source has the same column names and data types as the underlying table in the connection.
- The data source is loaded from the service automatically when the app is loaded.  The author can force a refresh with the **[Refresh](function-refresh.md)** function.
- Records can be created, modified, and deleted.  As changes are made to the data source, those changes are pushed back to the underlying table in the service.
	- Records can be created with the **[Patch](function-patch.md)**, and **[Collect](function-collect.md)** functions.  
	- Records can be modified with the **[Patch](function-patch.md)**, **[Update](function-update.md)**, and **[UpdateIf](function-update.md)** functions. 
	- Records can be removed with the **[Remove](funciotn-remove-removeif.md)** and **[RemoveIf](function-remove-removeif.md)** functions.
	- Errors when working with a data source are available through the **[Errors](function-errors.md)** function. 
- The **[DataSourceInfo](function-datasourceinfo.md)**, **[Defaults](funciton-defautls.md)**, and **[Validate](function-validate.md)** functions provide information about the data source that authors can use to optimize the user experience.

PowerApps cannot be used to create or modify a data source, the table must already exist in a service elsewhere.  To create a new table, for example in an Excel workbook stored on OneDrive, you would use Excel Online on OneDrive first to create a workbook and then create a connection to it from PowerApps.  [Collections](#Collections) can be created and modified in PowerApps but are only temporary.

## Displaying records from a data source ##
![](media/working-with-data-sources/reading-from-a-datasource.png)
When reading the information in a data source, the diagram above shows the flow of information:

- The information is stored and shared through a storage service, in this case a SharePoint list of an Office 365 site.
- A connection is used to make this information available to PowerApps.  The connection takes care of authentication of the PowerApps user to access the information.
- When the app is started or the **Refresh** function invokes, information is drawn from the connection into a data source in the PowerApp for local use.
- Formulas are used to read the information and expose it in controls that the user can see. You can display the records of a data source by using a Gallery control on a screen and wiring the **Items** property to the data source: **Gallery!Items = DataSource**.  You wire controls within the gallery, to the gallery, using the controls' **Default** property.  
- The data source is also a table.  So you can use **Filter**, **Sort**, **AddColumns**, and other functions to refine and augment the data source before it is used as a whole.  You can also use the **Lookup**, **First**, **Last**, and other functions to work with individual records.

For example, let's walk through the steps to display our SharePoint list: 

1. Create a connection to an Office 365 site.  We are using Office 365 and SharePoint lists in this example, but you can use any connection that supports data sources.
2. Add the connection to your app.  You will be asked which table you would like to use from the connection.  In this case, we are using the Customers SharePoint List and the Data Source name will default to **Customers**.
3. Insert a screen.  Rename it to **BrowseScreen**.
4. Insert a Text Gallery to the screen.  This will include Label controls within the Gallery to display individual properties of each record.
5. Set the Items property of the Gallery to the Data Source that was added in step 2, named **Customers**.  You can use the **[Order](function-order.md)** function to order the records in the gallery, and the **[Filter](function-filter.md)** function to select which records to show.
6. You will see the Customers SharePoint list displayed in the Gallery.  You can scroll through the many records.
7. You can modify the columns that are shown by changing the **Text** properties of the label controls in the gallery.  You can also rearrange the labels and add additional labels.
8. Preview the app.  You should now be able to browse and edit records of the SharePoint list.  

The SharePoint list can be modified outside of the PowerApp by other users.  When the app loads it will read the SharePoint list and can be refreshed later with the **[Refresh](function-refresh.md)** function.

## Modifying a record in a data source ##

In the last section, we showed you how to read a data source.  Note that the arrows in the diagram above are one way.  Changes to a data source are not pushed back through the same formulas in which the data was retrieved.  Instead, new formulas are used.  Often a different screen is used for editing a record than browsing records, especially on a mobile device.

Note that in order to modify an existing record of a data source, the record must have originally come from the data source.  The record may have traveled through a gallery or context variable, and any number of formulas, but its origin should be traceable back to the data source.  This is important since additional information travels with the record that uniquely identifies it, ensuring that you modify the right record.    

![](media/working-with-data-sources/writing-to-a-datasource.png)
The diagram above shows the flow of information to update a data source:

- A Gallery control can also provide a container for input controls, such as a Input Text and Slider controls.  As with the browse screen, the **Items** property is used but for a single record often takes the form of **Gallery!Items = Table( EditRecord )**.
- Each input control exposes an **Update** property.  This property maps the user's input to a specific property of the record.
- The Gallery aggregates the **Update** property of each of the controls within it, and exposed this as an **Updates** property.
- A Button or Image control on the screen is used to submit changes to the data source's service.  You use a formula based on the **Patch** function from the **OnSelect** formula of the control.
- Sometimes there will be issues.  A network connection may be down, or a validation check is made by the service that the PowerApp didn't know about.  The **Errors** function is used to check if there was an issue and retrieve information about the issue.  In some cases, such as conflicting edits by another user, the **Revert** function may be needed to reload the record and clear the error.

Let's continue our walk through and add a screen for editing records: 

3. On our browse screen, in the first item of the gallery control, add a button control and label it "Edit".  Set the **OnSelect** property to the formula **Navigate( EditScreen, Transition!None, { EditRecord: ThisItem } )**.  You will see an error because the EditScreen does not yet exist, but it will in the next step.
4. Insert another screen.  Name it **EditScreen**.  This will resolve the error on the BrowseScreen.
4. Insert a Card Gallery on the screen.  
	- Rename it **EditGallery**.  
	- Set its **Items** property to **Table( EditRecord )**  
5. Add a section for each record property that the user will be able to change.
6. Insert an Input Text box:  
	- Name it **NameControl**.
	- Set its **Default** property to **Name**.  This is the name of the column in the SharePoint list.  We are mapping the column into the control. 
	- Set its **Update** property to a record **{ *Name*: *NameControl!Text* }**.  This is aggregated with other control **Update** properties in the gallery to form the **EditGallery!Updates** property.  We are mapping the control back to the column.
7. Insert a second Input Text box:  
	- Name it **SizeControl**.
	- Set its **Default** property to **T-Shirt Size**.  This is the name of the column in the SharePoint list.  We are mapping the column into the control. 
	- Set its **Update** property to a record **{ *T-Shirt Size*: *SizeControl!Text* }**.  This is aggregated with other control **Update** properties in the gallery to form the **EditGallery!Updates** property.  We are mapping the control back to the column.
7. Insert a button outside the Card Gallery.  Label it "Save" and set its **OnSelect** property to **Patch( Customers, EditRecord, EditGallery!Updates ); Back()**
8. Preview the app.  You should now be able to browse and edit records of the SharePoint list.  Changes can be observed on the SharePoint site too.

## Validation ##

Before making a change to a record, the app should do what it can to make sure the change will be acceptable.  There are two reasons for this:

- *Immediate feedback to the user*.  The best time to fix a problem is right when it happens, when it is fresh in the user's mind.  Literally with each touch or keystroke, red text can appear that identifies an issue with their entry.
- *Less network traffic and less user latency*.  More issues detected in the PowerApp means fewer conversations over the network to detect and resolve issues.  Each conversation takes time during which the user needs to wait before they can move on.

PowerApps offers three tools for validation:

- The data source can provide information about what is valid and not valid.  For example, the minimum and maximum values for a number, or if an entry is required.  You can access this information with the **[DataSourceInfo]()** function.  
- The **[Validate](function-validate.md)** function uses this same information to check the value of a single column or of an entire record.
- Authors can add app specific validation with the **[Valid]()** property of input controls.  The formula for this property should evaluate to *true* if the validation passes.  The **[Valid]()** property of a gallery is a logical **[And]()** of the **[Valid]()** properties of all the input controls within it.

Let's continue our walk through and add validation to our screen: 

1.  Let's add a commonly used red asterisk to indicate that a field is required: 
	-  Insert a label control on our edit screen, just above the **NameControl**.
	-  Place a single asterisk ("*") in this label.
	-  Set the **Color** to **Color!Red**.
	-  Set the **Visible** property of this label to **DataSourceInfo( Customers, DataSrouceInfo!Required, "Name" )**.  When true, this will show the red asterisk to indicate that the control requires a value.
2.  Let's check that the Name control is filled in before we **Patch**:
	-  Modify the **OnSubmit** property of the "Save" button to check if the **EditGallery** believes the record is valid.  The **Validate** function checks for required fields using the same information that helped **DataSourceInfo** show the red asterisk:
		- **if( IsEmpty( Validate( Customers, EditRecord, EditGallery!Updates) ), Patch( Customers, EditRecord, EditGallery!Updates ); Back() )**.  
4.  Let's add a check that the "T-Shirt Size" has one of three possible values:
	-  Set the **Valid** property of the **Size** control to **Size!Text = "Small" || Size!Text = "Medium" || Size!Text = "Large"**.  This value will automatically be include in the **Valid** property for the gallery.
	-  Again change our **Patch** formula to now include a check for **Valid** properties in the **EditGallery**: 
		- **if( EditGallery!Valid && IsEmpty( Validate( Customers, EditRecord, EditGallery!Updates) ), Patch( Customers, EditRecord, EditGallery!Updates ); Back() )**.

## Error handling ##

Great, you've validated your record.  Time to update that record with **Patch**!

But, alas, there may still be a problem.  The network is down, validation at the service failed, the user does not have the right permissions, just to name a few of the possible errors your app may encounter.  Your app needs to respond appropriately to error situations, providing feedback to the user, and a means for them to make it right.  

When errors occur with a data source, PowerApps records the error information and makes it available through the **Errors** function.  Errors are associated with the records that had the problems.  If the problem is something the user can fix, such as a validation problem, they can resubmit the record and the errors will be cleared.

If an error occurs when creating a record with **Patch** or **Collect**, there is no record to associate any errors with.  In this case, *blank* will be returned by **Patch** and can  used as the record argument to **Errors**.  Creation errors are cleared with the next operation.

The **Errors** function returns a table of error information.  This information can include the column information, if the error can be attributed to a particular column.  Use column level errors messages in label controls that are close to where the column is located on the edit screen.  Use record level error messages, where the **Column** in the error table is *blank*, in a location close to the "Save" button for the entire record.  

Continuing our example:

1. Insert a label control on the **EditScreen**.  Set its text property to **Lookup( Errors( Customers, EditRecord ), IsBlank( Column ) )!Message**.  This will show any errors for the **EditRecord**, recalculated as updates are attempted.  The **Filter** call reduces what is shown here to record level errors, as opposed to errors that can be attributed to a single column.  Before a change is made and if a change is successful, this formula will return *blank*.
 
2. Change the **OnSelect** for the "Save" button to: 

	**if( EditGallery!Valid && IsEmpty( Validate( Customers, EditRecord, EditGallery!Updates) ), 
	UpdateContext( { EditReturn: Patch( Customers, EditRecord, EditGallery!Updates ) } );<br> if( IsEmpty( Errors( Customers, EditReturn ) ), Back() )**.  

	That is a mouthful, let's break it down:
	- We have the validation logic from before, to prevent us from doing the **Patch** until we are ready.
	- We are doing the same core **Patch** we were doing previously.  But in addition, we are capturing the result from **Patch** in a new context variable and if there is a problem, this will be *blank*.
	-  We are passing this return value to **Errors**.  If there are no errors, **Errros** will return *blank*, **IsEmpty** will be true, and we will navigate **Back** to where we came from.  The change was successful.
	- If there was a problem, we will stay on this screen.

If there is a problem, the user will remain on the screen, and the label we inserted in step 1 will display a message to the user.  They can take corrective actions and click "Save" again. 
 
For extra credit, there are problems that the user cannot fix by changing the controls on the **EditScreen**, for example if another user has changed a record on the server and now there are conflicting edits.  In addition to error messages, the **Errors** function also returns an **ErrorKind** that can indicate this situation and others.  Use this information to make a button visible that will "Reload" the record by invoking **Revert** on the record.  The user's edits will be lost, they will need to reapply them after the record has been reloaded.    

## Screens working together ##

Now that we have our main building block screens, let's bring it all together.  A simple and common app pattern for interacting with a data source consists of three screens:

- **Browse Screen**.  A scrollable surface displaying multiple records, offering search and sorting capabilities.  The user uses this screen to find the record they are looking for.
- **Details Screen**.  To make the browse screen efficient and show lots of records at a time, only a few properties from each record can be displayed.  To drill into a record, the details screen offers more or all of the properties of the record in a format that is designed for viewing one record at a time.  
- **Edit Screen**.  Often the most efficient way to view a record is not the same as the most efficient way to edit a record.  Labels should be replaced input text boxes that are larger and designed for editing, numeric properties can be edited with a slider control, etc.  The edit screen provides a user experience optimized for editing.  The edit screen is also used to create new records.

This is the pattern that "App from Data" uses when creating a new app in PowerApps. We recommend that you create one of these apps and examine the formulas for more details.  This is also a great starting point for customizing an app for your needs. 

This pattern is but one of many possibilities.  PowerApps is designed to help you create a unique experience that fits your situation very well.  The functionality on these screens can be broken apart, rearranged, and combined in new ways.  For example, you may want to break the edit screen for large records into separate more bite size screens, or you may want to make changes to a record directly from the browse screen.  Examine the apps that are created from "Start from Template" too, they are all unique in how they structure their screens.

The diagram below shows these three screens, and how they are wired together to create the app's overall experience:

![](media/working-with-data-sources/screens-working-together.png)

- It all starts with the browse screen.  This is usually the first screen that the user will see. As we saw earlier, this is wired to the data source through the **Items** property.
- From the browse screen, a "Details" button takes the user to the details screen. The button's **OnSelect** formula invokes the **Navigate** function to show the detail screen, and also passes the record to display as a context variable.  This record is taken from the **ThisItem** record of the gallery, reflecting the record that the user has selected.  - From the details screen, an "Edit" button takes the user to the edit screen.  This button's **OnSelect** formula also invokes the **Navigate** function to show the edit screen, and also passes the record to edit as a context variable.  
- With the controls on the edit screen, the user can make changes to the record.  When they are ready, a "Save" button invokes the **Patch** function to write the changes to the data source.  The **Errors** function can be used to detect and report on any problems before leaving this screen.  If all is well, you can use the **Navigate** function to return to the details or browse screen to see the result of the change.
- The user could also abandon a change to the record.  By using the "Cancel" button, **Back** is invoked which will return the user to the previous screen.  Since any changes are being abandoned, no record needs to be passed back to this screen.  
- There are a two more important paths.  First, the "New" button on the browse screen goes directly to the edit screen, using the result of the **Defaults** function as the record to edit.  When later used with the **Patch** function, a new record will be created.
- Second, the details screen offers a "Delete" button that invokes the **Remove** function to delete a record.  After deletion, you can **Navigate** the user back to the browse screen.

Note that the records passed between screens do not have a connection back to the data source.  They are stand alone records.  Which means you can manipulate them as records, such as placing them in context variables, using **Collect** to put them into a collection, or using **Patch** to merge records.  Each of the data functions such as **Patch** and **Remove** require an argument that is the data source to operate on, and this establishes the connection back to the data source.

Continuing our example, let's add a details screen and wire all three screens together.

1. Insert another screen.  Name it **DetailScreen**.
2. Insert a Card Gallery on the screen.
	- rename it **DetailGallery**  
	- Set its **Items** property to **Table( DetailRecord )**  
5. Add a section for each record property that the user will be able to view.
6. Insert an appropriate control for viewing data, such as a label control.  
	- Set its **Default** property to a column name of the data source (SharePoint list).
7. Insert a button outside the Card Gallery.  Name it "Edit" and set its **OnSelect** property to **Navigate( EditScreen, ScreenTransition!None, { EditRecord: DetailRecord } )**
8. Insert another button outside the Card Gallery.  Name it "Back" and set its **OnSelect** property to **Back()**.  This will return the user to the browse screen when they are done viewing the details.
8. Return to the Browser screen and change the "Edit" button into a "Detail" button and change its **OnSelect** property **Navigate( DetailScreen, ScreenTransition!None, { DetailRecord: ThisItem } )**.
8. Preview the app.  You should now be able to browse, view details, and edit records of the SharePoint list.  Changes are still observable on the SharePoint List too.

Two pieces of extra credit:

1. Add another button on the **BrowseScreen** and label it "New".  Set its **OnSelect** property to **Navigate( EditScreen, ScreenTransition!None, { EditRecord: Defaults( Customers ) }**.  This will pass a record to the **EditScreen**, that when used with **Patch**, will create a new record.
2. Add another button on the **DetailScreen** and label it "Delete".  Set its **OnSelect** property to **Remove( Customers, DetailRecord ); Back()**.  This will delete the current record and return the user to the browse screen. 
 
## Collections ##

Collections are a special kind of data source.  They are local to the app and not backed by a connection to a service.  They operate like any other data source, with a few exceptions:

- Collections can be created dynamically with the **Collect** function.  They do not need to be established ahead of time, as is done with connection based data sources.
- The columns of a collection can be modified at any time using the **Collect** function.
- Collections allow duplicate records.  More than one copy of the same record can exist in a collection.  Functions such as **Remove** will operate on the first match they find, unless the **All** argument is supplied. 
- You can use the **SaveData** and **LoadData** functions to save and reload a copy of the collection.  The information is stored in a private location that is not accessible by other users, apps, or devices. 

Collections are commonly used to hold global state for the app.  See [working with state](working-with-state.md) for the different options available for managing state.

<!-- TODO: lifetime of a collection -->

<!-- TODO: Static data sources -->
<!-- TODO: Refresh from local Excel file, Read only -->



