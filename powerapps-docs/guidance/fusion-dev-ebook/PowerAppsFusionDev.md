

Chapter 6: Using the Web API in the Power App
=============================================

Maria and Kiana are ready to combine the app with the Web API. However, before proceeding, they decide to consult with Preeti, the IT Operations Manager.

## Understanding the IT Operations Management Requirements for the Web API

Preeti is concerned that the app and the Web API must be secure because they provide access to sensitive data stored in the various databases. She wants assurances that she will be able to include authentication and authorization, to prevent unwarranted access to information. Preeti is also aware that the company is rapidly expanding, and the volume of data involved in managing customers, appointments, parts, and the knowledge base is likely to increase exponentially in the near term. Consequently, she wants the solution to be scalable.

Kiana explains to Preeti that the Web API is currently implemented as an Azure App Service. This service supports a number of authentication providers, which Preeti can configure using the Azure portal. Preeti is especially interested in Azure Active Directory because VanArsdel are looking to roll out this form of authentication to many of their other corporate systems in the near future:

![Azure App Service authentication configuration][100]

Azure App Service also provides horizontal and vertical scalability. If needed, Preeti can scale up the resources available to the Web API by upgrading the App Service Plan for the web app:

![Azure App Service scale up][101]

She can also arrange for the system to scale out by configuring autoscaling. Azure App Service enables an operations manager to define autoscale rules that determine the conditions under which the system should scale out across more instances when the load increases, or back in again as demand drops. She can also configure pre-emptive autoscaling to occur according to a schedule:

![Azure App Service scale out][102]

A key part of the role of an IT Operations Manager is to have an eye for how systems might evolve, and to ensure that the underlying support structures will handle future expansion and changes. Preeti knows that the Web API developed by Kiana might be extended, and reused by other VanArsdel systems in the future. She needs to be able to manage and control the way in which developers request use of the Web API, protect it as a valuable resource, and monitor its use. Therefore Preeti decides to protect the Web API behind the Azure API Management service (APIM).

APIM provides an extra layer of security to a Web API, as well as enabling detailed monitoring and control over which clients can access which operations. Using APIM, Preeti can manage resource utilization, and throttle the performance of low priority clients to ensure that critical higher priority apps are serviced more quickly.

> **NOTE:**
> For more details on the services that APIM provides, read **About API Management** at <https://aka.ms/AAbvfzn>.

## Creating an Azure API Management Service

Preeti created the API Management service through the Azure portal, using the following steps:

1.  Sign in to the Azure portal and, on the **Home** page, select **Create a resource**.

    ![Azure portal Home page][103]

2.  In the **Search the MarketPlace** text box, enter **API Management**, and press **Enter**.

3.  On the **API Management** page, select **Create**.

    ![Azure Create API Management Service page][104]

4.  On the **Create API Management** page, enter the following values, and then select **Review + create**:

    -   Subscription: Select your subscription
    -   Resource group: **webapi\_rg** (this is the same resource group that you created for the App Service)
    -   Region: Select your nearest region
    -   Resource name: Enter a unique name for the service
    -   Organization name: **VanArsdel**
    -   Administrator email: **itadmin\@vanarsdel.com**
    -   Pricing tier: **Developer (no SLA)**

    > **NOTE:**
    > Don't use the **Developer** pricing tier for a production system.

    ![New API Management Service page][105]

5.  On the validation page, select **Create**, and wait while the API Management service is created.

    > **NOTE:**
    > It can take 30 minutes or more for the API Management service to be provisioned, so be patient.

## Publishing the Web API through APIM

After the APIM service was created, Preeti published the Web API to make it accessible to other services and applications. She used the following steps:

1.  In the Azure portal, go to the APIM service.

2.  On the **API Management service** page, in the left pane, under **APIs**, select **APIs**:

    ![API Management Service page. Select APIs][106]

3.  In the **Add a new API** pane, select **OpenAPI**:

    ![API Management Service page. Select OpenAPI][107]

4.  In the **Create from OpenAPI specification** dialog box, enter the following values, and then select **Create**:

    -   OpenAPI specification: **https://*\<webapp name\>*.azurewebsites.net/swagger/v1/swagger.json**, where *\<webapp name\>* is the name of the App Service hosting your Web API
    -   Display name: **Field Engineer API**
    -   Name: **field-engineer-api**
    -   API URL suffix: Leave empty
    -   Base URL: Use the default URL

    ![Create API from OpenAPI specification][108]

5.  When the Field Engineer API has been created, select the **Settings** tab for the API, set the **Web Service URL** to **https://*\<webapp name\>*.azurewebsites.net**, and then select **Save**:

    ![Configure API settings][109]

6.  On the **Test** tab, select the **GET api/Appointments URI**, and then select **Send**:

    ![Test GetAppointments API][110]

7.  Verify that the request is successful (the HTTP return code is **200 OK**), and that it returns a result containing a list of appointments in the response body:

    ![Response from testing GetAppointments API][111]

## Connecting to APIM from the Power App

Kiana and Maria can now work together to connect the app to the Web API through the APIM service.

The first task is to create a custom connector that's used by the app to communicate with APIM. This involves exporting the API to the Power Apps environment used to create the app, which Kiana does as follows:

1.  In the Azure portal, go to the page for the APIM service that Preeti created.

2.  In the left pane, under **APIs**, select **APIs**.

3.  Click the ellipsis button for the **Field Engineer Ap**i, and then select **Export**:

    ![Export the Web API][112]

4.  In the **Export API** pane, select **Power Apps and Power Automate**:

    ![Export the Web API to Power Apps][113]

5.  In the **Export API to PowerApps** pane, select the PowerApps environment in which you created the prototype app (**Maria** in the image shown below), and then select **Export**:

    ![Export to Maria's Power Apps environment][114]

6.  After the API has been exported, select the **Field Engineer API**. On the **Settings** page, scroll down to the **Subscriptions** section, clear **Subscription required**, and then select **Save**:

    ![Deselect Subscription Required][115]

The prototype app used Excel spreadsheets for the data sources. Now the custom connector for the Web API is available, Maria performs the following steps to add the connector to the app:

1.  Sign in to Power Apps Studio at <http://make.powerapps.com>.

2.  In the left pane, expand **Data**, and select **Custom Connectors**. The **field-engineer-api** custom connector should be listed. Select **Create connection**:

    ![Create new custom connector][116]

3.  In the **field-engineer-api** dialog box, select **Create**:

    ![Create FieldEngineerAPI connector][117]

4.  When the connection has been created, verify that it appears in the list of available connections:

    ![Display available connections][118]

5.  In the left pane, select **Apps**, select **VanArsdelApp**, and then select **Edit**:

    ![Edit VanArsdel app][119]

6.  In the left pane, select the **Data** tab. Select **Add data**, select the ellipsis button for **Connectors**, and then select **Refresh**:

    ![Refresh data sources][120]

7.  In the list of connectors, select the **field-engineer-api** connector:

    ![View connectors][121]

8.  In the **field-engineer-api** dialog box, select the **field-engineer-api** connector:

    ![Add FieldEngineerAPI connection][122]

9.  In the **Data** pane, verify that the **FieldEngineerApi** connector is listed:

    ![FieldEngineerAPI connection added][123]

## Updating the App to use the Connector: Field Inventory Management

Now that the connection has been added to the Power App, Maria can modify the screens to use it to replace the Excel spreadsheets. This involves working through each screen methodically and changing the data source. No other changes should be necessary. She starts with the **BrowseParts** and **PartDetails** screens:

1.  On the **Home** screen of the Power App, select the **Parts** button. Set the **OnSelect** action property to the following formula:

    ```
    ClearCollect(partsCollection, FieldEngineerAPI.getapiboilerparts());
    
    Navigate(BrowseParts, ScreenTransition.Fade)
    ```

    The **ClearCollect** function creates a new collection named **partsCollection**, and populates it with the data that results from calling the **getboilerparts** operation in the **FieldEngineerAPI** connection.

    ![Create partsCollection variable][124]

    > **NOTE:**
    >  It's good practice to retrieve the data into a collection and reference that collection from any screens that need the information. This approach can save different screens from repeatedly running the same query and fetching the same data.

2.  Press **F5** to preview the app.

3.  On the **Home** screen, select **Parts**. This action will create the **partsCollection** collection. Close the preview window and return to Power Apps Studio.

    > **NOTE:**
    > The purpose of this step is to enable you to see the data while you edit the **BrowseParts** screen in the following steps.

4.  Select the **BrowseGallery1** control in the **BrowseParts** screen. In the formula for the **Items** property, replace the reference to the [\@Table1] data source to **partsCollection**.

    This change will result in some errors. This is because the field names in the original Excel spreadsheet used capitalization (**Name**, **CategoryID**, and **Overview**), whereas the properties returned in the body of the Web API response are named in lowercase. Change these references to use lowercase. The formula should look like this:

    ```
    SortByColumns(Search(FieldEngineerApi.getapiboilerparts(), TextSearchBox1.Text, "name", "categoryId", "overview"), "name", If(SortDescending1, Descending, Ascending))
    ```

    ![Update formula for Browse screen][125]

5.  In the **Tree view** pane, select the **IconRefresh1** control. Change the **OnSelect** action to the formula **ClearCollect(partsCollection, FieldEngineerAPI.getapiboilerparts())**.

    > **NOTE:**
    > The original formula for this action calls the **Refresh** function to repopulate the data using the connection to the original data source. You can't use **Refresh** with a connection that runs a function to retrieve the data, so it won't work with **FieldEngineerApi.getapiboilerparts()**. The solution in this step repopulates the **partsCollection** collection with the latest data.

6.  In the **Tree view** pane, expand the **BrowseGallery1** control, and select the **Body1** control. Change the **Text** property to **ThisItem.overview**.

7.  In the **Tree view** pane, select the **Subtitle1** control. Change the **Text** property to **ThisItem.categoryId**.

8.  In the **Tree view** pane, select the **Title** control. Change the **Text** property to **ThisItem.name**.

9.  In the **Tree view** pane, select the **DetailForm1** control in the **PartDetails** screen. Change the **DataSource** property from [\@Table1] to **partsCollection**.

10. In the **Tree view** pane, select the **Name\_DataCard1** control under **DetailForm1**. Change the **Default** property to **ThisItem.name**.

    ![Change Default for the Name data card][126]

11. Change the **Default** property of the **CategoryID\_DataCard1** control to **ThisItem.categoryId**.

12. Change the **Default** property of the **Overview\_DataCard1** control to **ThisItem.overview**.

13. Change the **Default** property of the **Price\_DataCard1** control to **ThisItem.price**.

14. Change the **Default** property of the **NumberInStock\_DataCard1** control to **ThisItem.numberInStock**.

15. Change the **Default** property of the **Image\_DataCard1** control to **ThisItem.imageUrl**.

16. In the left pane, on the **Data** tab, right-click the **Table1** data connection, and then select **Remove** to delete it from the Power App. This connection is no longer required.

    ![Remove the Table1 connection][127]

17. Save the Power Apps app.

    > **NOTE:**
    > You can quickly save the app without using the **File** menu by pressing **Ctrl + S**

18. Press **F5** to preview the app. The **Browse Parts** and **Part Details** screens should operate exactly as before, except this time they are retrieving data from the **InventoryDB** Azure SQL database through the Web API, rather than from a local spreadsheet.

19. Close the preview window and return to Power Apps Studio.

## Updating the App to use the Connector: Field Scheduling and Notes

Maria continues with the **BrowseAppointments**, **AppointmentDetails**, and **EditAppointment** screens. The data presented by these screens currently originates from the **Appointments** table in another Excel spreadsheet.

1.  On the **Home** screen of the Power App, set the **OnVisible** action to the following formula:

    ```
    ClearCollect(appointmentsCollection, Sort(Filter(FieldEngineerAPI.getapiappointments(), DateDiff(Today(), startDateTime) >= 0), startDateTime))
    ```

    This formula retrieves appointments data into the **appointmentsCollection** collection. The appointments are filtered to retrieve visits scheduled on or after the current date.

2.  Select the label control that displays the time of the next appointment. Set the **Text** property to **Text(First(appointmentsCollection).startDateTime, ShortTime24)**.

3.  Select the label control that displays the date for the next appointment. Set the **Text** property to **Text(First(appointmentsCollection).startDateTime, LongDate)**.

4.  Select the label control that displays the date for the next appointment. Set the **Text** property to **First(appointmentsCollection).customer.name**.

5.  Press **F5** to preview the app. On the **Home** screen, select **Appointments**. This action will create the **appointmentsCollection** collection. Close the preview window and return to Power Apps Studio.

6.  In the **Tree view** pane, select the **BrowseAppointmentsGallery** control in the **BrowseAppointments** screen. Change the formula in the **Items** property to the formula shown below:

    ```
    Sort(Filter(appointmentsCollection, StartsWith(customer.name, TextSearchBox1\_1.Text)), startDateTime)
    ```

    This formula filters the data displayed on the screen by customer name, enabling the user to enter the name of a customer. The appointments are displayed in date and time order.

7.  In the **Tree view** pane, expand the **BrowseAppointmentsGallery** control, and select the **Title1\_1** control. Change the **Text** property to:

    ```
    Text(ThisItem.startDateTime, LongDate)
    ```

    This formula displays the date part of the **startDateTime** field for the appointment.

8.  In the **Tree view** pane, expand the **BrowseAppointmentsGallery** control, and select the **Subtitle1\_1** control. Change the **Text** property to:

    ```
    Text(ThisItem.startDateTime, ShortTime24)
    ```

This formula displays the time element of the **startDateTime** field.

9.  In the **Tree view** pane, expand the **BrowseAppointmentsGallery** control, and select the **Body1\_1** control. Change the **Text** property to:

    ```
    ThisItem.customer.name
    ```

10. In the **Tree view** pane, select the **IconRefresh1\_1** control on the **BrowseAppointments** screen. Set the **OnSelect** action to the following formula:

    ```
    ClearCollect(appointmentsCollection, Sort(Filter(FieldEngineerAPI.getapiappointments(), DateDiff(Today(), startDateTime) >= 0), startDateTime));
    ```

11. In the **Tree view** pane, expand the **AppointmentDetails** screen, and select the **DetailForm1\_1** control. Set the **DataSource** property to **appointmentsCollection**.

12. In the **Tree view** pane, select the **IconEdit1** control. Modify the formula in the **DisplayMode** property to test the **appoinmentsCollection** collection:

    ```
    If(DataSourceInfo(**appointmentsCollection**, DataSourceInfo.EditPermission), DisplayMode.Edit, DisplayMode.Disabled)
    ```

13. In the **Tree view** pane, expand the **DetailForm1\_1** screen, and select the **Customer Name\_DataCard1** control. Change the **Default** property to **ThisItem.customer.name**.

14. Change the **Default** properties of the remaining data cards as follows:

    -   Customer Address\_DataCard1: **ThisItem.customer.address**
    -   Contact Number\_DataCard1: **ThisItem.customer.contactNumber**
    -   Problem Details\_DataCard1: **ThisItem.problemDetails**
    -   Status\_DataCard1: **ThisItem.appointmentStatus.statusName**
    -   Notes\_DataCard1: **ThisItem.notes**
    -   Image\_DataCard1\_1: **ThisItem.imageUrl**

15. In the **Tree view** pane, expand the **EditAppointment** screen, and select the **EditForm1** control. Set the **DataSource** property to **appointmentsCollection**.

16. In the **Tree view** pane, expand the **EditForm1** control, and select the **Customer Name\_DataCard3** control. Change the **Default** property to **ThisItem.customer.name**.

17. Change the **Default** properties of the remaining data cards as follows:

-   Contact Number\_DataCard2: **ThisItem.customer.contactNumber**; additionally, change the **MaxLength** property to **20**
-   Problem Details\_DataCard2: **ThisItem.problemDetails**
-   Status\_DataCard5: **ThisItem.appointmentStatus.statusName**
-   Notes\_DataCard3: **ThisItem.notes**
-   Image\_DataCard2: **ThisItem.imageUrl**

18. In the **Tree view** pane, expand the **Problem Details\_Card2** control. Rename the **DataCardValue*X*** (*X* will be a number) field under this control to **ProblemDetailsValue**. Repeat this process for the **DataCardValue*X*** controls in the following data cards:

    -   Status\_DataCard5: **StatusValue**
    -   Notes\_DataCard3: **NotesValue**

    > **NOTE:**
    > The Image control will be addressed in the next chapter.

19. Select the **ProblemDetailsValue**, and set the **MaxLength** property to **100**.

20. In the **Tree view** pane, select the **IconAccept1** control on the **EditAppointment** screen. Set the **OnSelect** action property to the following formula:

    ```
    FieldEngineerAPI.putapiappointmentsid(BrowseAppointmentsGallery.Selected.id, {problemDetails:ProblemDetailsValue.Text, statusName:StatusValue.Selected.Value, notes:NotesValue.Text, imageUrl:""});

    Remove(appointmentsCollection, First(Filter(appointmentsCollection, id=BrowseAppointmentsGallery.Selected.id)));

    Set(appointmentRec, FieldEngineerAPI.getapiappointmentsid(BrowseAppointmentsGallery.Selected.id));

    Collect(appointmentsCollection, appointmentRec);

    Navigate(AppointmentDetails, ScreenTransition.None);
    ```

    This formula calls the **PUT** operation for the Appointments controller in the Web API. It passes the appointment ID for the current appointment as the first parameter, followed by the details that the user might have modified on the screen. The details are passed as a JSON object. The Remove, Set, and Collect statements update the **appointmentsCollection** collection with the data saved to the database.

    > **NOTE:**
    > Don't use the **ClearCollect** function to delete and refresh the entire collection in situations such as this because it's wasteful if, for example, only one record has changed.

21. In the **Tree view** pane, select the **IconAccept1** control on the **EditAppointment** screen. Set the **OnSelect** action property to:

    ```
    ResetForm(EditForm1);

    Navigate(AppointmentDetails, ScreenTransition.None);
    ```

22. In the left pane, on the **Data** tab, right-click the **Appointments** data connection, and then select **Remove** to delete it from the Power App.

23. Save the Power Apps app.

24. Press **F5** to preview the app. From the **Home** screen, go to the **Appointments** screen, select and edit an appointment, then save the changes. Verify that the appointment is updated.

25. Close the preview window and return to Power Apps Studio.

## Creating the Azure Cognitive Search Service for the Field Knowledgebase

The Knowledgebase screen in the app is not currently attached to any data source. The Web API includes operations for querying and updating the **Tips**, **BoilerParts**, and **Engineers** tables in the **KnowledgeDB** database. However, the purpose of the **Query** screen in the app is to support searches through all of these tables. The volume of data in these tables is likely to increase quickly, so Maria, Kiana, and Preeti decide to deploy Azure Cognitive Search to support this feature. An app can submit queries and receive results from Azure Cognitive Search through a custom connector.

Azure Cognitive Search works best if the data to be searched is contained in a single database entity. Kiana creates a view in the **KnowledgeDB** database that presents a unified view of the **Tips**, **BoilerParts**, and **Engineers** tables, as follows:

1.  In the Azure portal, go to the **KnowledgeDB SQL Database** page.

2.  In the left pane, select **Query Editor** and sign in to the database as **sqladmin**, using the password **Pa55w.rd**.

    ![Sign in to Azure SQL Database][128]

3.  In the query window, enter the following statement, and then select **Run**:

    ```sql
    CREATE OR ALTER VIEW [dbo].[Knowledge] AS
    SELECT T.Id, T.Subject, T.Body, B.Name, B.Overview
    FROM [dbo].[Tips] T INNER JOIN [dbo].[BoilerParts] B
    ON B.Id=T.KnowledgeBaseBoilerPartId
    ```

    ![Create the "Knowledge" view][129]

    Verify that the view, **Knowledge**, is created successfully.

4.  In the left pane, select **Connection strings**. Make a note of the **ADO.NET** connection string; you'll need it when you configure **Azure Cognitive Search**:

    ![ADO.NET connection string for the KnowledgeDB database][130]

Working with Kiana, Preeti configures a new instance of the Azure Cognitive Search service to perform searches on rows in the **Knowledge** view:

1.  On the **Home** page, in the Azure portal, select **+ Create a resource**, type **Azure Cognitive Search**, press **Enter**, and then select **Create**:

    ![Create the Cognitive Search service][131]

2.  On the **New Search Service** page, enter the following settings, and then select **Review + create**:

    -   Subscription: Select your Azure subscription
    -   Resource group: **webapi\_rg**
    -   Service name: Enter a unique name for the service
    -   Location name: Select your nearest region
    -   Pricing tier: **Free**

3.  On the validation page, select **Create**, and wait while the service is provisioned.

4.  Go to the page for the new search service, select **Overview**, make a note of the **Url** (you'll need this later when you create the custom connector for Power Apps), and then select **Import Data**:

    ![Search Service Overview page][132]

5.  On the **Import data** page, in the Data Source drop-down list box, select **Azure SQL Database**:

    ![Select Azure SQL Database][133]

6.  On the **Connect to your data** page, specify the following settings:

    -   Data Source: **Azure SQL Database**
    -   Data source name: **knowledgebase**
    -   Connection string: Enter the Azure SQL Database connection string for the **KnowledgDB** database that you recorded earlier; in this string, make sure to set the password to **Pa55w.rd**
    -   Leave the **User Id** and **Password** fields at their default values; these items are retrieved from the connection string

7.  Select **Test connection**. Ensure that the test is successful, select the [Knowledge] view in the **Table/View** drop-down list box, and then select **Next: Add cognitive skills (Optional)**:

    ![Specify the search view][134]

8.  On the **Add cognitive skills (Optional)** page, select **Skip to: Customize target index**.

9.  On the **Customize target index** page, select **Retrievable** for all columns, and **Searchable** for **Subject**, **Body**, **Name**, and **Overview**. Select **Next: Create an indexer**:

    ![Customize the target index][135]

10. On the **Create an indexer** page, change the indexer **Name** to **knowledgebase-indexer**. For the **Schedule**, select **Hourly**, set the **High watermark column** to **Id**, and then select **Submit**:

    ![Create the indexer][136]

11. To test the indexer, on the **Overview** page for the search service, select **Search Explorer**:

    ![Select Search explorer][137]

12. In the **Query** **string** field, enter a word to search for in the knowledge base, and then select **Search**. The search service should generate a list of documents with a match in the **Subject**, **Body**, **Name**, or **Overview** fields, and display them in the **Results** pane. Make a note of the **Request URL** and the sample **Results**; you'll need these items later as an example request and response when you set up the Power Apps custom connector:

    ![Search query results][138]

## Creating the Custom Connector for the Azure Cognitive Search Service

Kiana can now create a custom connector that Power Apps uses to send search requests to the search service. She does this using Power Apps Studio:

1.  Sign in to Power Apps Studio at <http://make.powerapps.com>.

2.  In the left pane, expand **Data**, and select **Custom Connectors**. In the right pane, select **+ New custom connector**, and then select **Create from blank**:

    ![New custom connector][139]

3.  In the **Create from blank** dialog box, set the new connector name to **VanArsdelKBConnector**, and then select **Continue**:

    ![Create knowledgebase connector][140]

4.  On the **General information** page, enter a description and set the **Scheme** to **HTTPS**. In the **Hosts** box, enter the URL for your search service (you noted this URL earlier) but without the **https://** prefix, and then select **Security**:

    ![Search service connector General page][141]

5.  On the **Security** page, in the **Authentication** drop-down list box, select **API Key**. In the **Parameter label** field, enter **api-key**. In the **Parameter name** field, enter **api-key**. Select **Definition**:

    ![Search service connector Security page][142]

6.  On the **Definition** page, select **New action**. In the **Summary** field, enter **Query**. In the **Description** field, enter **Query the knowledgebase**. In the **Operation ID** field, enter **Query**. Under **Request**, select **+ Import from sample**:

    ![Search service connector Definition page][143]

7.  In the **Import from sample** dialog box, enter the following values, and then select **Import**:

    -   Verb: **GET**
    -   URL: Provide the example request URL that you noted when you tested the search service in Search Explorer earlier
    -   Headers: **Content-type**

    ![Import definition from sample request][144]

8.  Back on the **Definition** page, scroll down to the **Query** section, select the ellipsis button next to **search**, and then select **Edit**:

    ![Edit aearch request definition][145]

9.  On the edit screen, in the **Parameters** section, in the **Default value** field, enter an asterisk (**\***). Leave the other fields at their default values, and select **Back**:

    ![Set search default value][146]

10. On the **Definition** page, in the **Query** section, select the ellipsis button next to **api-version**, and then select **Edit**:

    ![Edit the API version][147]

11. On the edit screen, in the **Parameters** section, in the **Default value** field, enter **2020-06-30-Preview** (this is the version associated with the current version of Azure Cognitive Search; you can see the version in the request URL that you noted earlier). Set **Is required** to **Yes**, and set **Visibility** to **internal**. Leave the other fields at their default values, and then select **Back**:

    ![Set the API values for search parameters][148]

12. On the **Definition** page, scroll down to the **Response** section, and select **+ Add default response**:

    ![Add default response definition][149]

13. In the **Import from sample** dialog box, in the **Headers** field, enter the text **Content-type**. In the **Body** field, enter the example results that you recorded when testing the search service, and then select **Import**:

    ![Import the response message from a sample][150]

14. On the **Definition** page, select the **default** response:

    ![Select the default response][151]

15. In the **Description** field of the **Content-type** response, enter **application/json**, and then select **Back**:

    ![Set the response message header content][152]

    > **NOTE:**
    > The **Body** section on this page should display the fields of the response, such as **Body**, **Id**, **Name**, **Overview**, and **Subject** if it has been parsed successfully.

16. Select **Create connector**:

    ![Create Cognitive Search service connector][153]

    The connector should be created without reporting any errors or warnings.

## Updating the App to use Azure Cognitive Search: Field Knowledgebase

Maria can now use the custom connector in the Power App. But first, she requires a key that grants her the privileges required to connect to the Azure Cognitive Search service. Preeti obtains the key from the **Keys** page for the service in the Azure portal, and gives it to Maria:

![Search Service key in the Azure portal][154]

Maria edits the app in Power Apps Studio and performs the following tasks:

1.  Open the **VanArsdelApp** app for editing.

2.  On the **View** menu, select **Data sources**, and then select **Add data**:

    ![Add the data source to the app][155]

3.  In the **Search** box, under **Select a data source**, enter **Van**. The **VanArdelKBConnector** connector should be listed:

    ![Search for the Cognitive search service connector][156]

4.  Select the **VanArdelKBConnector** connector. In the **VanArdelKBConnector** pane, enter the key that Preeti provided for the search service, and then select **Connect**:

    ![Enter the API key][157]

5.  On the **File** menu, save and close the app, and then open it again. You may be prompted to authorize use of the custom connector when the app reopens.

    > **NOTE:**
    > This step is necessary to enable the custom connector.

6.  In the **Tree view** pane, expand the **Knowledgebase** screen, and select the **TextSearchBox2** control. Enter the following formula for the **OnChange** action:

    ```
    If(!IsBlank(TextSearchBox2.Text), ClearCollect(azResult, VanArsdelKBConnector.Query({search: TextSearchBox2.Text}).value))
    ```

    This formula calls the **Query** operation of the custom connector searching for items that match the term the user types into the search box. The results are stored in a collection named **azResult**.

7.  In the **Tree view** pane, under the **Knowledgebase** screen, select the **BrowseGallery2** control. Set the **Items** property to **azResult**.

8.  Expand the **BrowseGallery2** control and remove the **Image4** control.

9.  Select the **Title2** control. Set the following properties to the values specified:

    -   Text: **ThisItem.Subject**
    -   X: **24**
    -   Width: **Parent.TemplateWidth - 104**

10. Select the **Subtitle2** control. Set the **Text** property to **ThisItem.Body**.

11. Press **F5** to preview the app. On the **Knowledgebase** screen, enter a search term, and press **Enter**. Matching articles from the knowledge base should be displayed:

    ![Knowledgebase query in the app][158]

    > **NOTE:**
    > The details screen hasn't been created yet, so clicking the **\>** icon next to an article doesn't work.

12. Close the preview window and return to Power Apps Studio.

13. In the **Tree view** pane, right-click the **PartDetails** screen, and select **Duplicate screen**. This action will add another screen to the Power App, named **PartDetails\_1**:

    ![Duplicate the PartDetails screen][159]

14. In the **Tree view** pane, rename the **PartDetails\_1** screen as **KnowledgebaseDetails**.

    -   Select the **LblAppName*X*** control on the screen; set the **Text** property to **"Article Details"** (including the quotes)

15. In the **Tree view** pane, select the **DetailFormX** control on the screen. Set the following properties:

    -   DataSource: **azResult**
    -   Item: **BrowseGallery2.Selected **


    > **NOTE:**
    > **BrowseGallery2** is the browse gallery on the **Knowledgebase** screen. In your application, this gallery may have a different name.

16. In the **Tree view** pane, expand the **DetailForm*X*** form, then change the names of the following data card controls:

    -   Name\_DataCard1\_1: **Name\_DataCard**
    -   CategoryID\_DataCard1\_1: **Subject\_DataCard**
    -   Overview\_DataCard1\_1: **Overview\_DataCard**
    -   Price\_DataCard1\_1: **Body\_DataCard**

17. Delete the **NumberInStock\_DataCard1\_1**, and **Image\_DataCard1\_1** controls.

18. Select the **Name\_DataCard** control. Set the **Default** property to **ThisItem.Name**.

19. Select the **Subject\_DataCard** control. Set the following properties:

    -   DataField: **"Subject"**
    -   DisplayName: **"Subject"**
    -   Default: **ThisItem.Subject**

20. Select the **Overview\_DataCard** control. Set the **Default** property to **ThisItem.Overview**.

21. Select the **Body\_DataCard** control. Set the following properties:

    -   DataField: **"Body"**
    -   DisplayName: **"Body"**
    -   Default: **ThisItem.Body**

22. Select the **DataCardValue*X*** control in the **Body\_DataCard** control. Set the **Text** property to **Parent.Default**.

23. Resize each of the data card controls to spread them out down the screen:

    ![The ArticleDetails screen][160]

24. Select the back arrow icon in the screen header. Change the **OnSelect** action property to **Navigate(Knowledgebase, ScreenTransition.None)**.

25. In the **Tree view** pane, select the **Knowledgebase** screen, and then select the **BrowseGalleryX** control. Change the **OnSelect** action property to **Navigate(KnowledgebaseDetails, ScreenTransition.None)**. This action displays the details screen for the knowledge base article when the user selects the **\>** icon for an entry in the browse screen.

26. Save the Power Apps app.

27. Press **F5** to preview the app. On the **Knowledgebase** screen, enter a search term and press **Enter**. Select an article and verify that its details are displayed. Verify that the **Back** icon returns the user to the browse screen.

28. Close the preview window and return to Power Apps Studio.

Maria, Kiana, and Preeti have successfully incorporated the Web API and Azure Cognitive Search into the app.

Chapter 7: Adding Functionality to the App
==========================================

Kiana and Maria are excited to show the inventory management app to Caleb, the field technician. He likes it, but suggests adding some extra user interface functionality to make it easier to use. Specifically, Caleb would like to be able to:

-   Add a photograph of the work done on a boiler or air conditioning unit, and add it to the appointment details on the **Edit Appointment** screen. This image could prove useful as documentary evidence of repairs performed. The **Edit Appointment** screen currently enables the user to add an image to the appointment, but the image isn't saved as this feature hasn't been fully implemented yet. The reason for this omission is that Kiana and Preeti need to determine the best place to store image data. Caleb would like this functionality added as soon as possible.


-   View a complete appointment history for a customer, to track repairs requested for that customer and monitor any ongoing issues that may require repeated callouts.

-   Order parts from the **Part Details** screen.

    Additionally, the image control on the **Part Details** screen displays the images stored at a specified URL. Currently the URLs in the data are simply placeholders. Like the photographs for the appointment screen, Kiana and Preeti need to determine the best place to store images so they're available to the Power App.

## Adding a Photograph to an Appointment

Photographs need to be stored somewhere accessible by the Power App. For performance and security reasons, Preeti doesn't want photographs to be saved in OneDrive or in Azure SQL Database. Instead, she and Kiana decide to use Azure Blob Storage. Blob Storage is optimized for holding large binary objects, and is robust, with built-in security. Power Apps has a connector that allows access to Blob Storage. Maria suggests adding a new picture-taking screen, improving the user experience for Caleb.

> **NOTE:**
> For detailed information, visit the **Azure Blob Storage** page at <https://azure.microsoft.com/services/storage/blobs/>.

Preeti creates the Blob Storage account from the Azure portal:

1.  In the Azure portal, on the **Home** page, select **+ Create a resource**. In the **Search the Marketplace** box, enter **Storage account** and press **Enter**.

    ![Azure Marketplace search][161]

2.  On the **Storage account** page, select **Create**.

3.  On the **Create storage account** page, enter the following details, and then select **Review + create**:

    -   Subscription: Select your subscription
    -   Resource group: **webapi\_rg**
    -   Storage account name: Provide a globally unique name and make a note of it for later
    -   Location: Select your nearest location
    -   Performance: **Standard**
    -   Account kind: **BlobStorage**
    -   Replication: **RA-GRS**

    ![Create the Azure Storage account][162]

4.  On the validation page, select **Create** and wait for the storage account to be provisioned.

5.  Go to the page for the new storage account.

6.  On the **Overview** page, select **Containers**:

    ![Storage account Overview page][163]

7.  On the **Containers** page, select **+ Container**. Create a new container named **photos**, and then select **Create**. Change the public access level** to **Blob**:

    ![Create the Photos container][164]

8.  Back on the **Overview** page for the storage account, under settings, select **Access keys**. On the **Access keys** page, select **Show keys.** Make a note of the value of the key for **key1**:

    ![Storage account access keys][165]

Preeti gives the storage account name and key to Kiana, who uses this information to create a custom connector for the Power App:

1.  Sign in to Power Apps Studio at <http://make.powerapps.com>.

2.  In the left pane, expand **Data**, and select **Connections**. The existing connections used by the app should be listed. Select **+ New connection**:

    ![Power Apps connections page][166]

3.  On the **New connection** page, scroll down, select **Connections**, select **Azure Blob Storage**, and then select **Create**:

    ![Select Azure Blob Storage connector][167]

4.  In the **Azure Blob Storage** dialog box, enter the storage account name and access key that Preeti provided, and then select **Create**:

    ![Enter storage credentials][168]

5.  Wait while the new connection is created. It should appear on the list of connections.

Maria can use this connection to Azure Blob Storage in the app to save and retrieve photographic images. Her first task is to add the connection to the app:

1.  Open the **VanArsdelApp** app for editing in Power Apps Studio.

2.  In the **Data** pane, select **Add data**, search for the **Azure Blob Storage** connector, and then select this connector:

    ![Search for the Blob Storage connector][169]

3.  In the **Azure Blob Storage** dialog box, select the **Azure Blob Storage** connector to add it to your Power App:

    ![Add Blob Storage connection][170]

Maria's next task is to add a screen that enables a technician or engineer to save a photograph. Maria decides to add a new screen with a Picture control. When the app is run on a mobile device, this control can integrate with the camera to enable the technician to take a photograph. On other devices, this control prompts the user to upload an image file instead. She adds a link to this new screen from the **EditAppointment** screen:

1.  On the **Insert** menu, select **New screen**, and then select the **Scrollable** template:

    ![New screen from the Scrollable template][171]

2.  In the **Tree view** pane, select the new screen and rename it as **TakePhoto**.

3.  Change the **Text** property of the **LblAppName*X*** control on this screen to **Take a photograph**.

4.  Delete the **Canvas*X*** control from the screen.

5.  In the **Insert** menu, from the **Media** drop-down list, select **Add picture** to create a new picture control:

    ![Add a Picture control][172]

    > **NOTE:**
    > The picture control is actually a composite custom component that enables the user to add a picture to the screen and display the results.

6.  Resize and reposition the picture control to occupy the body of the screen.

7.  In the **Tree view** pane, select the **IconBackarrow*X*** control on the **AppointmentDetails** screen, and select **Copy**:

    ![Copy the Back Arrow control][173]

8.  In the **Tree view** menu, right-click the **TakePhoto** screen, and then select **Paste**. The **IconBackArrow*X*** control will be added to the screen:

    ![Paste the Back Arrow control in the TakePhoto screen][174]

9.  Move the **IconBackArrow*X*** control to the top left of the header bar.

10. In the **Tree view** pane, select the **IconBackArrow*X*** control on the **TakePhoto** screen. In the right pane, on the **Advanced** tab, modify the **OnSelect** action property to **Navigate(EditAppointment, ScreenTransition.None)**.

11. Add a new **Save** icon control to the top right of the header bar. Set the **Visible** property of this control to **If(IsBlank(AddMediaButton1.Media), false, true)**.

    This setting makes the **Save** icon invisible if the user hasn't selected an image.

    ![Add Save icon control][175]

12. Change the formula in the **OnSelect** action property of the **Save** icon control to:

    ```
    Set(ImageID, GUID() & ".jpg");

    AzureBlobStorage.CreateFile("photos", ImageID, AddMediaButton1.Media);

    Patch(appointmentsCollection, LookUp(appointmentsCollection,id=BrowseAppointmentsGallery.Selected.id), {imageUrl:"https://myappphotos.blob.core.windows.net/photos/" & ImageID});

    Navigate(EditAppointment,ScreenTransition.Cover);
    ```

    Replace **\<storage account name\>** with the name of the Azure storage account that Preeti created.

    This code uploads the image to the **photos** container in Azure Blob Storage. Each image is given a unique filename. The **Patch** function updates the **imageUrl** property in the appointments record with the URL of the image in Blob Storage.

13. In the **Tree view** pane, expand the **AddMediaWithImageX** control. Modify the **Image** property of the **UploadedImage*X*** control, and set it to **AppointmentImage**.

    AppointmentImage is a variable that will be populated with an image either uploaded by the user, or as the result of taking a photograph. You'll initialize this variable in the **EditAppointment** screen later.

14. In the **Tree view** pane, select the **AddMediaButton*X*** control. Set the **UseMobileCamera** property of this control to **true**. Set the **OnChange** action property of the control to:

    ```
    Set(AppointmentImage, AddMediaButton1.Media)
    ```

    This formula changes the **AppointmentImage** variable to reference the new image. The **UploadedImage*X*** control will display this image.

15. In the **Tree view** pane, select the **EditAppointment** screen.

16. Expand the **EditForm*X*** control. Under the **Image\_DataCardX** control, remove the **AddPictureX** control:

    ![Remove the AddPicture control][176]

17. Select the **Image*X*** control. Change the following properties:

    -   Image: **Parent.Default**
    -   X: **30**
    -   Y: **DataCardKey*X*.Y + DataCardKey*X*.Height + 150** (where **DataCardKey*X*** is the data card containing the **Image*X*** control)
    -   Width: **Parent.Width - 60**
    -   Height: **400**

    > **NOTE:**
    > The image control will drop down below the bottom of the screen, but a scroll bar will be added automatically to enable the image to be viewed.

18. Add a **Camera** icon to the data card then position it between the **Image** label and the **ImageX** control. Change the name of the control to **CameraIcon**:

    > **NOTE:**
    > Make sure you select the Camera Icon control, and **not** the Camera Media control.

    ![Add Camera icon][177]

19. Set the **OnSelect** action property of the **CameraIcon** control to:

    ```
    Set(AppointmentImage, SampleImage);

    Navigate(TakePhoto, ScreenTransition.None);
    ```

    When the user clicks this icon, they will go to the **TakePhoto** screen, to enable them to take a photo or upload an image. The initial image displayed will be the default sample image.

To test the app:

1.  In the **Tree view** pane, select the **Home** screen.

2.  Press **F5** to preview the app.

3.  On the **Home** screen, select **Appointments**.

4.  In the browse screen, select any appointment.

5.  On the details screen for the appointment, select the edit icon in the screen header.

6.  On the edit screen, select the **Camera** icon for the image.

7.  Verify that the **Take a photograph** screen appears.

8.  Select **Change Picture** and upload a picture of your choice (or take a photograph if you're running on a mobile device).

9.  Select **Save**. Verify that the image appears on the details page, and then select the tick icon to save the changes back to the database.

10. Close the preview window and return to Power Apps Studio.

## Displaying Images of Parts

Having determined that Azure Blob Storage is an ideal location for saving pictures associated with appointments, Preeti and Kiana decide that they should use the same approach for storing the images of parts. A key advantage of this approach is that it doesn't require any modifications to the Power Apps app. The app reuses the same storage account and the same connection. As a separate migration exercise, they can:

1.  Create a new Blob container.

2.  Upload the part images to this container.

3.  Change the **ImageUrl** references in the **Parts** table in the **InventoryDB** database to the URL of each image.

The app will pick up the new URL for each part image automatically, and the **Image** control on the **PartDetails** screen will display the image.

## Tracking Appointment History for a Customer

Maria thinks that being able to quickly view all the history from a customer's previous technician's visits could be added to the app by creating a custom component. Working with Caleb on what information they want to see, Maria sketches out a simple design comprising the notes and the date of each visit.

![Data for the customer appointment history][178]

Looking at the data, Maria believes that a gallery control is the best way to display the table data on a screen.

Maria creates the custom component as follows:

1.  Using Power Apps Studio, in the **Tree view** pane, select **Components**, and then select **+ New component**:

    ![Create a new component][179]

    A new blank component named **Component1** is created. Rename the component as **DateHistoryComponent**:

    ![Rename the component][180]

2.  On the **Insert** menu, select **Gallery**, and then choose the **Blank flexible height** gallery template:

    ![Add a Gallery control][181]

3.  Move the gallery control and resize it to fill the custom component.

4.  Select the **Add an item from the insert pane**, then select **Text label**.

    ![Add a Text label to the component][182]

5.  In the **Tree view** pane, rename the label control as **NotesLabel**. Set the **Overflow** property to **Overflow.Scroll**. This setting enables the control to display several lines of text and allow the user to scroll through it. Set the following properties so you can position and size the control:

    -   LineHeight: **2**
    -   X: **28**
    -   Y: **18**
    -   Width: **574**
    -   Height: **140**

6.  Add a second text label to the control. Rename this control as **DateLabel** and set the following properties:

    -   LineHeight: **2**
    -   X: **28**
    -   Y: **174**
    -   Width: **574**
    -   Height: **70**

7.  To see how the control will look when inserted into the app and using its theme, in the **Tree view** pane, select **DateHistoryComponent**. In the right pane, on the **Advanced** tab, select the **Fill** field and change the color to **RGBA(0, 0, 0, 1)**.

    ![View the component][183]

8.  From the **Insert** pane, expand **Shapes**, and add a **Rectangle** control to the custom component. Set the following properties for this control:

    -   X: **0**
    -   Y: **273**
    -   Width: **Parent.Width**
    -   Height: **2**

    This control acts as a separator between the records displayed in the gallery:

    ![Add a Rectangle control][184]

Maria is familiar with adding controls to screens and building Power Apps. However, reusable components don't work in quite the same way. Kiana described to Maria that to be able to use data in a custom component, she must add some additional custom input properties. Kiana also explained that Maria needs to provide example data for these properties, to allow her to reference the data fields in the controls in her component, as follows:

1.  In the **Tree view** pane, select **DateHistoryComponent**. In the right pane, on the **Properties** tab, select **New custom property**:

    ![New custom property][185]

2.  In the **New custom property** dialog box, specify the following values, and then select **Create**:

    -   Display name: **Data**
    -   Name: **Data**
    -   Description: **The table of appointments for a customer, showing the notes and dates**
    -   Property type: **Input**
    -   Data type: **Table**
    -   Raise OnReset when value changes: Leave blank

    ![New custom property properties][186]

3.  To change the sample data displayed by the control, select the new **Data** custom property. In the formula field, type **Table({Notes: "Example notes field text.", \'Appointment Date\': Text(Today())})**.

    ![Change the sample data][187]

4.  In the **Tree view** pane, select the **Gallery*X*** control in **DateHistoryComponent**, and rename it as **AppointmentHistory**.

5.  In the right pane, on the **Advanced** tab, set the **Items** property of the **AppointmentHistory** gallery control to **Parents.Data**.

    ![Update the Items property for the gallery control][188]

6.  Select the **NotesLabel** control. In the right pane on the **Advanced** tab, change the **Text** property to **ThisItem.Notes,** and change the **Size** property to **20**.

    > **NOTE:**
    > The **Size** property specifies the font size for the text displayed by the control.

7.  Select the **DateLabel** control to change the **Text** property to **ThisItem.\'Appointment Date\'** and change the **Size** property to **20**. The fields in the custom component should display the sample data:

    ![Custom component with sample data][189]

The custom component is complete. Maria creates a new screen to display the appointments history for a customer using this component:

1.  In the **Tree view** pane, select the **Screens** tab.

2.  Expand the **BrowseAppointments** screen, expand the **BrowseAppointmentsGallery** control, and select the **Body1\_1** control. On the **Insert** menu, select **Icons**, and then select the **Detail list** icon:

    ![Add Details list icon][190]

3.  Change the name of the icon control to **ViewAppointments**.

4.  In the **Tree view** menu, select the **BrowseAppointmentsGallery** control. In the right pane, on the **Advanced** tab, change the **TemplateSize** property to **220**. Increasing this property expands the space available in the gallery.

5.  Move the **ViewAppointments** icon into the empty space below the customer name:

    ![Amended appoinments gallery][191]

6.  Select the **ViewAppointments** icon control. Set the **OnSelect** action property to the following formula:

    ```
    ClearCollect(customerAppointmentsCollection, FieldEngineerAPI.getapicustomeridappointments(ThisItem.customerId));

    Navigate(AppointmentsHistoryScreen, ScreenTransition.Fade)
    ```

    This formula populates a collection named **customerAppointmentsCollection** with the appointments for the selected customer, and then moves to the **AppointmentHistoryScreen** to display them. You'll create this screen in the following steps.

7.  On the **Insert** menu, select **New screen**, and then select the **Scrollable** template:

    ![New screen based on the Scrollable template][192]

8.  Change the name of the new screen to **AppointmentHistoryScreen**.

9.  Delete the **Canvas*X*** control that was added to this screen:

    ![Delete the Canvas control][193]

10. Select the **LblAppName*X*** control on this screen. In the right pane, on the **Advanced** tab, change the **Text** property to:

    ```
    "Appointments History for " &  BrowseAppointmentsGallery.Selected.customer.name
    ```

11. Set the following properties for the **LblAppName*X*** control to adjust the position and size:

    -   X: **90**
    -   Y: **0**
    -   Width: **550**
    -   Height: **140**

12. Select the **RectQuickActionBar*X*** control, and set the **Height** property to **140**.

13. Add a **Left icon** control to the screen header, to the left of the title. Set the **OnSelect** action property for this control to **Navigate(BrowseAppointments, Transition.None)**.

    ![Empty AppointmentsHistory screen][194]

14. On the **Insert** menu, select **Custom**, and then select the **DateHistoryComponent**:

    ![Add DateHistory component][195]

15. Move and resize the component so that it occupies the body of the screen, below the heading:

    ![Resized component][196]

16. Set the following properties for this component:

    -   Data: **customerAppointmentsCollection**
    -   Appointment Date: **startDateTime**
    -   Notes: **notes**

17. Save the Power Apps app.

To test the Power Apps app:

1.  In the **Tree view** pane, select the **Home** screen.

2.  Press **F5** to preview app.

3.  On the **Home** screen, select **Appointments**.

4.  In the browse screen, select the **Detail list** icon for any appointment.

5.  Verify that the **Appointments History** screen for the selected customer appears.

6.  Close the preview window and return to Power Apps Studio.

## Ordering Parts

A key requirement of the system is to enable a technician to order any parts required while visiting a customer. If the parts are in stock, it should be possible to schedule another visit to complete the repair at the next convenient date for the customer. If the parts are currently out of stock and have to be ordered, the technician can tell the customer. Malik can then arrange an appointment with the customer when Maria receives notice that the parts have arrived in the warehouse.

The reservations part of the app uses the tables in the **InventoryDB** database shown in the diagram below. The **Orders** table holds information about orders placed for parts. The **Reservations** table lists the reservation requests that technicians and engineers have made for parts. The **Engineers** table provides the name and contact number for the engineer who made the reservation, in case of any queries by Maria, the inventory manager.

![The Reservations data model][197]

To support this feature, Kiana has to update the Web API with a method that fetches the number of reserved items for a specified part:

1.  Open the **FieldEngineerApi** Web API project in Visual Studio Code.

2.  Add a file named **Order.cs** to the **Models** folder. Add the following code to this file. The **Orders** class tracks the details of orders placed for parts.

    ```csharp
    using System;
    using System.ComponentModel.DataAnnotations;
    using System.ComponentModel.DataAnnotations.Schema;

    namespace FieldEngineerApi.Models
    {
        public class Order 
        {
            [Key]
            public long Id { get; set; }

            public long BoilerPartId { get; set; }

            public BoilerPart BoilerPart { get; set; }

            public long Quantity { get; set; }

            [Column(TypeName = "money")]
            public decimal TotalPrice { get; set; }

            [Display(Name = "OrderedDate")]
            [DataType(DataType.DateTime)]
            [DisplayFormat(DataFormatString = "{0:MM/dd/yyyy}")]
            public DateTime OrderedDateTime { get; set; }

            public bool Delivered { get; set; }

            [Display(Name = "DeliveredDate")]
            [DataType(DataType.DateTime)]
            [DisplayFormat(DataFormatString = "{0:MM/dd/yyyy}")]
            public DateTime? DeliveredDateTime { get; set; }
        }
    }
    ```

3.  Add another new file named **Reservation.cs** to the **Models** folder and add the code shown below to this file. The **Reservation** class contains information about the number of items for a given part that are currently reserved for other customers.

    ```csharp
    using System;
    using System.ComponentModel.DataAnnotations;

    namespace FieldEngineerApi.Models
    {
        public class Reservation
        {
            [Key]
            public long Id { get; set; }

            public long BoilerPartId { get; set; }

            public BoilerPart BoilerPart { get; set; }

            public int NumberToReserve { get; set; }

            public string EngineerId { get; set; }

            public InventoryEngineer Engineer { get; set; }
        }
    }
    ```

4.  Add one more file, named **InventoryEngineer.cs,** to the **Models** folder, with the following code. The **InventoryEngineer** class records which engineers have made which reservations:

    ```csharp
    using System.ComponentModel.DataAnnotations;
    using System.Collections.Generic;

    namespace FieldEngineerApi.Models
    {
        public class InventoryEngineer
        {
            [Key]
            public string Id { get; set; }

            [Required]
            public string Name { get; set; }

            public string ContactNumber { get; set; }

            public List<Reservation> Reservations { get; set; }
        }
    }
    ```

5.  Open the **InventoryContext.cs** file in the **Models** folder, and add the statements shown below to the **InventoryContext** class:

    ```csharp
    public class InventoryContext : DbContext
    {
        public InventoryContext(DbContextOptions\<InventoryContext\> options)
            : base(options)
        {

        }

        public DbSet<BoilerPart> BoilerParts { get; set; }
        public DbSet<InventoryEngineer> Engineers { get; set; }
        public DbSet<Order> Orders { get; set; }
        public DbSet<Reservation> Reservations { get; set; }
    }
    ```

6.  In the Terminal window in Visual Studio Code, run the following commands to build controllers for handling orders and reservations:

    ```shell
    dotnet aspnet-codegenerator controller ^
        -name OrdersController -async -api ^
        -m Order ^
        -dc InventoryContext -outDir Controllers

    dotnet aspnet-codegenerator controller ^
        -name ReservationsController -async -api ^
        -m Reservation ^
        -dc InventoryContext -outDir Controllers
    ```

7.  Open the **BoilerPartController.cs** file in the **Controllers** folder, and add the **GetTotalReservations** method, shown below, to the **BoilerPartsController** class:

    ```csharp
    public class BoilerPartsController : ControllerBase
    {
        private readonly InventoryContext _context;

        public BoilerPartsController(InventoryContext context)
        {
            _context = context;
        }

        ...
        
        // GET: api/BoilerParts/5/Reserved 
        [HttpGet("{id}/Reserved")]
        public async Task<ActionResult<object>> GetTotalReservations(long id)
        { 
            var reservations = await _context
                .Reservations
                .Where(r => r.BoilerPartId == id) 
                .ToListAsync();

            int totalReservations = 0; 

            foreach(Reservation reservation in reservations) 
            { 
                totalReservations += reservation.NumberToReserve; 
            } 

            return new {id, totalReservations}; 
        }
        ...
    }
    ```

8.  Edit the **OrdersController.cs** file, and modify the **PostOrder** method in the **OrdersController** class as shown below:

    ```csharp
    [HttpPost]
    public async Task<ActionResult<Order>> PostOrder(long boilerPartId, int quantity)
    {
        var part = await _context.BoilerParts.FindAsync(boilerPartId);

        Order order = new Order 
        {
            BoilerPartId = boilerPartId,
            Quantity = quantity,
            OrderedDateTime = DateTime.Now,
            TotalPrice = quantity * part.Price
        };

        _context.Orders.Add(order);
        await _context.SaveChangesAsync();

        return CreatedAtAction("GetOrder", new { id = order.Id }, order);
    }
    ```

9.  Edit the **ReservationsController.cs** file. Modify the **PostReservation** method in the **ReservationsController** class as follows:

    ```csharp
    [HttpPost]
    public async Task<ActionResult<Reservation>> PostReservation(long boilerPartId, string engineerId, int quantityToReserve)
    {
        Reservation reservation = new Reservation 
        {
            BoilerPartId = boilerPartId,
            EngineerId = engineerId,
            NumberToReserve = quantityToReserve
        };

        _context.Reservations.Add(reservation);
        await _context.SaveChangesAsync();

        return CreatedAtAction("GetReservation", new { id = reservation.Id }, reservation);
    }
    ```

10. In the Terminal window, run the following commands to build and publish the Web API ready for deployment:

    ```
    dotnet build
    dotnet publish -c Release -o ./publish
    ```

11. In Visual Studio Code, right-click the **publish** folder, and then select **Deploy to Web App**:

Preeti can now update the Azure API Management service used by the VanArsdel app to reflect the updated Web API. This is a non-breaking change; existing operations will continue to work, the differences being the new controllers and operations to make reservations and place orders. Preeti performs the following tasks:

> **NOTE:**
> Preeti could have chosen to delete the existing Field Engineer API and replace it with a new version, but this approach risks breaking any existing applications that may be currently using the API. It's better practice to leave the existing API in place and add the modifications as a revision.

1.  In the Azure portal, go to the APIM service.

2.  On the **API Management service** page, in the left pane, under **APIs**, select **APIs**:

3.  Select the **Field Engineer API**, select the ellipsis menu, and then select **Add revision**:

    ![Add a revision to the Field Engineer API][198]

4.  In the **Create a new revision of the Field Engineer API** dialog box, enter the description **Added GET operation and POST operations for part reservations and orders**, and then select **Create**:

    ![Create the revision][199]

5.  On the **REVISION 2** page, select **Design**:

    ![Design the revision][200]

6.  On the **Design** page, select **Add operation**. In the **FrontEnd** pane, set the following properties, and then select **Save**. This operation is used for retrieving the number of items reserved for a given boiler part:

    -   Display name: **api/BoilerParts/{id}/Reserved**
    -   Name: **api-boilerparts-id-reserved**
    -   URL: **GET** **api/BoilerParts/{id}/Reserved**

    ![Add the Reserved API operation][201]

7.  On the **Test** tab for the new operation, set the **id** parameter to a valid part number (the example in the image uses part 1), and then select **Send**:

    ![Test the Web API][202]

8.  Verify that the test is successful. The operation should complete with an HTTP 200 response, and a body that shows the number of reservations for the product:

    ![The test response][203]

9.  On the **Design** page, select **Add operation**. In the **FrontEnd** pane, set the following properties. This operation defines POST requests for creating new orders:

    -   Display name: **api/Orders - POST**
    -   Name: **api-orders-post**
    -   URL: **POST** **api/Orders**

10. On the **Query** tab, select **+ Add parameter**, add the following parameters, and then select **Save**:

    -   Name: **boilerPartId**, Descripion**: Boiler Part ID**, Type: **long**
    -   Name: **quantity**, Descripion**: Quantity**, Type : **integer**

    ![Add parameters to APIM query operation][204]

11. Select **Add operation** again In the **FrontEnd** pane, and set the following properties. This operation defines POST requests for creating new reservations:

    -   Display name: **api/Reservations - POST**
    -   Name: **api-reservations-post**
    -   URL: **POST** **api/Reservations**

12. On the **Query** tab, add the following parameters, and then select **Save**:

    -   Name: **boilerPartId**, Descripion: **Boiler Part ID**, Type: **long**
    -   Name: **engineerId**, Description: **Engineer ID**, Type: **string**
    -   Name: **quantityToReserve**, Descripion: **Quantity to reserve**, Type: **integer**

13. On the **Revisions** tab, select the new version. On the ellipsis menu for this version, select **Make current**:

    ![Set the current version for the revision][205]

14. In the **Make revision current** dialog box, select **Save**.

15. Open another page in your web browser and go to the URL **https://*\<APIM name\>*.azure-api.net/api/boilerparts/1/reserved** where **\<APIM name\>** is the name of your API service. Verify that you get a response similar to the following:

    ```js
    {"id":1,"totalReservations":5}
    ```

The updated Web API is now available. In theory, Kiana could create a new custom connector for the updated Web API and add it to the app. The app could then implement its own logic to determine how many items of the specified product are currently in stock, how many are reserved, compare the results to the number of items required, place an order for more stock if necessary, or reserve items from the existing stock. However, this kind of logic is better implemented in an Azure Logic App. The Power Apps app can call the Logic App through a custom connector when a technician wishes to reserve or order a part.

To create the Logic App, Kiana uses the following steps:

> **NOTE:**
> To keep things simple, the Logic App created in this example is non-transactional. It's possible that between checking the availability of a part and making a reservation, a concurrent user might make a conflicting reservation. You could implement transactional semantics by replacing some of the logic in this Logic App with a stored procedure in the **InventoryDB** database.

1.  In the Azure portal, on the **Home** page, select **+ Create a resource**.

2.  In the **Search the marketplace** box, type **Logic App**, and then press **Enter**.

3.  On the **Logic App** page, select **Create**.

    ![Create the Logic App][206]

4.  On the **Create a logic app** page, enter the following values, and then select **Review + create**.

    -   Subscription: Select your Azure subscription
    -   Resource group: **webapi\_rg**
    -   Logic App name: **FieldEngineerPartsOrdering**
    -   Region: Select the same location you used for the Web API
    -   Associate with integration service environment: Leave blank
    -   Enable log analytics: Leave blank

5.  On the verification page, select **Create**, and wait while the Logic App is deployed.

6.  When the deployment is complete, select **Go to resource**.

7.  On the **Logic Apps Designer** page, scroll down to the **Templates** section, and then select **Blank Logic App**:

    ![Select the Blank Logic App template][207]

8.  On the **All** tab, in the **Search connectors and triggers** text box, select **Request**:

    ![Select the Request trigger][208] 

9.  On the **Triggers** tab, select **When a HTTP request is received**:

    ![Trigger when an HTTP request is received][209]

10. In the **Request Body JSON Schema** box, enter the following schema, and then select **+ New step**:

    ```js
    {
        "type": "object",
        "properties": {
            "boilerPartId": {
                "type": "integer"
            },
            "numberToReserve": {
                "type": "integer"
            },
            "engineerId": {
                "type": "string"
            }
        }
    }
    ```

    ![Logic App request schema][210]

    This schema defines the content of the HTTP request that the Logic App is expecting. The request body comprises the ID of a boiler part, the number of items to reserve, and the ID of the engineer making the request. The Power Apps app will send this request when an engineer wants to reserve a part.

11. In the **Choose an operation** box, select **All**, and then select **HTTP**:

    ![SelectH tthe HTTP operation option][211]

    The Logic App will call the **BoilerParts{id}** operation of the Web API to retrieve information about the boiler part provided by the request from the Power Apps app.

12. In the **Actions** pane, select the **HTTP** action:

    ![Select the HTTP action option][212]

13. In the **HTTP** action box, on the ellipsis menu, select **Rename**, and change the name of the action to **CheckBoilerPart**:

    ![Rename the HTTP action][213]

14. Set the properties of the HTTP action as follows, and then select **+ New Step**:

    -   Method: **GET**
    -   URI: **https://*\<APIM name\>*.azure-api.net/api/boilerparts/**, where ***\<APIM name\>*** is the name of your APIM service. In the **Dynamic content** box for this URI, on the **Dynamic content** tab, select **boilerPartId**

    ![Specify dynamic content for HTTP action][214]

15. In the **Choose an operation** box, in the **Search connectors and actions** box, enter **Parse JSON**, and then select the **Parse JSON** action:

    ![Select the Parse JSON action][215]

16. Using the ellipsis menu for the **Parse JSON** action, rename the action as **ParseBoilerPart**.

17. In the **Content** box for the **ParseBoilerPart** action, in the **Dynamic Content** box, select **Body**. In the **Schema** box, enter the following JSON schema, and then select **+ New step**:

    ```js
    {
        "type": "object",
        "properties": {
            "id": {
                "type": "integer"
            },
            "name": {
                "type": "string"
            },
            "categoryId": {
                "type": "string"
            },
            "price": {
                "type": "number"
            },
            "overview": {
                "type": "string"
            },
            "numberInStock": {
                "type": "integer"
            },
            "imageUrl": {
                "type": "string"
            },
        }
    }
    ```

    ![Parsing the BoilerPart object][216]

    This action parses the response message returned by the **getBoilerParts/{id} request. The response contains the details of the boiler part, including the number currently in stock.

18. In the **Choose an operation** box for the new step, select the **HTTP** connector.

19. On the **Actions** tab, select the **HTTP** action.

20. Using the ellipsis menu for the operation, rename the operation as **CheckReservations**.

21. Set the following properties for this operation, and then select **+ New step**:

    -   Method: **GET**
    -   URI: **https://*\<APIM name\>*.azure-api.net/api/boilerparts/**. As before, in the **Dynamic content** box for this URI, on the **Dynamic content** tab, select **boilerPartId**. In the **URI** field, append the text **/reserved** after the **boilerPartId** placeholder

    ![The CheckReservations step][217]

22. In the **Choose an operation** box for the new action, in the **Search connectors and actions** box, enter **Parse JSON**, and then select the **Parse JSON** action.

23. Rename the operation as **ParseReservations**.

24. Set the **Content** property to **Body**.

25. Enter the following schema, and then select **+ New step**:

    ```js
    {
        "type": "object",
        "properties": {
            "id": {
                    "type": "integer"
            },
            "totalReservations": {
                    "type": "integer"
            }
        }
    }
    ```

    ![Parsing the Reservations data][218]

26. In the **Choose an operation** box for the new action, in the **Search connectors and actions** box, enter **Condition**, and then select the **Condition Control** action:

    ![Select the Condition control][219]

27. Rename the operation as **CompareStock**.

28. Select the **Choose a value** box. In the **Add dynamic content** box, on the **Expression** tab, enter the following expression, and then select **OK**:

    ```
    add(body('ParseReservations')?['totalReservations'], triggerBody()?['numberToReserve'])
    ```

    This expression calculates the sum of the number of items of the specified boiler part that are currently reserved, and the number requested by the engineer.

    ![The CompareStock condition][220]

29. In the condition drop-down list box, select **is greater than**.

30. In the remaining **Choose a value** box, in the **Dynamic content** box, on the **Dynamic content** tab, under **ParseBoilerPart**, select **numberInStock**:

    ![Compare total reservations to number of items in stock][221]

31. If the number of items required plus the number reserved is greater than the number in stock, then the app needs to place an order to replenish the inventory. In the **True** branch of the **CompareStock** action, select **Add an action**.

32. On the **All** tab for the new operation, select **HTTP**, and then select the **HTTP** action.

33. Rename the operation as **PostOrder**.

34. Set the following properties for the **PostOrder** operation:

    -   Method: **POST**
    -   URI: **https://*\<APIM name\>*.azure-api.net/api/orders**
    -   In the **Queries** table, in the first row, enter the key **boilerPartId**. For the value in the **Add dynamic content** box, on the **Dynamic content** tab, select **boilerPartId **
    -   In the second row of the **Queries** table, enter the key **quantity**. In the value field, enter **50**:

    ![Post a request to order more parts][222]

    The Logic App will automatically order 50 items of the specified part when stock is running low.

    > **NOTE:**
    > The Logic App assumes that the engineer will nor actually attempt to reserve more than 50 items of a specified part in a single request!

35. Leave the **False** branch of the **CompareStock** action empty.

36. Below the **CompareStock** action, select **+ New step**.

37. On the **All** tab for the new operation, select **HTTP**, and then select the **HTTP** action.

38. Rename the operation as **PostReservation**.

39. Set the following properties for the **PostReservation** operation:

-   Method: **POST**
-   URI: **https://*\<APIM name\>*.azure-api.net/api/reservations**
-   In the **Queries** table, in the first row, enter the key **boilerPartId**. For the value in the **Add dynamic content** box, on the **Dynamic content** tab, select **boilerPartId**.
-   In the second row, enter the key **engineerId**. For the value in the **Add dynamic content** box, on the **Dynamic content** tab, select **engineerId**
-   In the third row, enter the key **quantityToReserve**. For the value in the **Add dynamic content** box, on the **Dynamic content** tab, select **numberToReserve**

40. Select **+ New Step**. In the **Choose an operation** box, search for and select the **Response** action.

41. Set the following properties for the **Response** action:

    -   Status Code: **200**
    -   Headers: Key - **content-type**, Value - **application/json**
    -   Body: In the **Dynamic content** box, select the **Body** element from the **PostReservation** request. This is the body returned when the reservation is made:

    ![Response message sent by the Logic App][223]

42. In the top left of the **Logic Apps Designer** page, select **Save**. Verify that the Logic App saves without any errors.

To create the custom connector that the Power Apps app can use to trigger the Logic App, Kiana performs the following steps while still in the Azure portal:

1.  On the **Overview** page for the Logic App, select **Export**.

    ![Export the Logic App][224]

2.  In the **Export to Power Apps** pane, name the connector **PartsOrderingConnector**, select your Power Apps environment**,** and then select **OK**.

    ![Export the LOgic App to Power Apps][225]

3.  Sign in to Power Apps Studio at <http://make.powerapps.com>.

4.  In your environment, under **Data**, select **Custom Connectors** and verify that the **PartsOrderingConnector** is listed:

    ![Power Apps custom connectors][226]

Maria can now modify the VanArsdel app to enable a technician to order parts while attending a customer site. She adds an **Order** button to the **PartDetails** screen.

1.  Sign in to Power Apps Studio at <http://make.powerapps.com> (if not already signed in).

2.  Under **Apps**, select the **VanArsdelApp** app. On the ellipsis menu for the app, select **Edit**.

3.  In the **Data** pane, select **Add data**, search for the **PartsOrderingConnector** connector, and add a new connection using this connector:

    ![Add the PartsOrdering connector to the app][227]

4.  In the **Tree view** pane, expand the **PartDetails** screen, and then expand the **DetailForm1** form.

5.  In the **Properties** pane on the right, select **Edit fields**. In the **Fields** pane, on the ellipsis menu, select **Add a custom card**:

    ![Add a custom data card control to the app][228]

6.  In the **Tree view** pane, rename the new card from **DataCard1** to **ReserveCard**. In the **Design view** window, resize the card so that it occupies the lower part of the screen, below the **Image\_DataCard1** control:

    ![Rename and resize the data card control][229]

7.  On the **Insert** menu, from the **Input** sub menu, add a **Text Input** control, a **Button** control, and a **Label** control to the **ReserveCard** control.

8.  Resize and position the controls so that they're adjacent, with the **Button** control to the right of the **Text Input** control, and the **Label** underneath the **Button** control.

9.  In the **Properties** pane for the **Text Input** control, clear the **Default** property.

10. In the **Properties** pane for the **Button** control, set the **Text** property to **Reserve**.

    ![The layout of the ParttDetails screen][230]

11. Rename the **Text Input** control as **NumberToReserve**, rename the **Button** control as **Reserve**, and rename the **Label** control as **Message**.

12. In the **Properties** pane for the **Message** control, set the **Text** property to **Parts Reserved**, and set the **Visible** property to **MessageIsVisible**.


    > **NOTE:**
    > **MessageIsVisible** is a variable that you will initialize to **false** when the screen is displayed, but is changed to **true** if the user hits the **Reserve** button.

13. Set the **OnSelect** property for the **Reserve** button control to the following formula:

    ```
    FieldEngineerPartsOrdering.manualinvoke({boilerPartId:ThisItem.id, engineerId:"ab9f4790-05f2-4cc3-9f01-8dfa7d848179", numberToReserve:NumberToReserve.Text});

    Set(MessageIsVisible, true);
    ```


    > **NOTE:**
    > This formula uses a hard-coded engineer ID to represent the technician currently running the app. Chapter 8 describes how to retrieve the ID for the logged-on user.
    >
    > Additionally, the app performs no error checking; it assumes that the request to reserve parts always succeeds. For more information on error handling, read **Errors function in Power Apps** at <https://docs.microsoft.com/powerapps/maker/canvas-apps/functions/function-errors>.

14. Set the **OnVisible** property for the **PartDetails** screen to **Set(MessageIsVisible, false)**.

To test the app:

1.  In the **Tree view** pane, select the **Home** screen.

2.  Press **F5** to preview the app.

3.  On the **Home** screen, select **Parts**.

4.  In the browse screen, select any part.

5.  On the **Part Details** screen, scroll down to the reservations section, enter a positive integer value, and then select **Reserve**. Verify that the **Parts reserved** message appears:

    ![The PartDetails screen with the Reserve function enabled][231]

6.  Close the preview window and return to Power Apps Studio.

7.  In the Azure portal, go to the page for the **InventoryDB** Azure SQL Database.

8.  Select the **Query editor**, and sign in as **sqladmin** with your password.

9.  In the **Query 1** pane, enter the following query, and then select Run. Verify that the reservation you made in the VanArsdel app appears:

    ```sql
    SELECT * FROM [dbo].[Reservations]
    ```

    ![The query results in Azure SQL Database][232]

Chapter 8: Protecting and Deploying the App
===========================================

The app is now functionally complete, but Preeti and Kiana want to ensure that the solution is safe to deploy, and that they have a mechanism for maintaining it as requirements change in the future.

## Protecting the App and Resources

When you first sign in to Power Apps, you're required to authenticate yourself, typically by providing your email address and password. Office 365 utilizes its own Azure AD domain; each organization has its own domain. Your credentials are checked against your organization's domain for Office 365. A Power Apps app can only access the Office 365 resources to which you've been granted the appropriate authority. Authorization is managed by your Office 365 Administrator (Preeti in the VanArsdel scenario). For more information, read **Securing the app and data** at <https://aka.ms/AAbvtkm>.

The Azure resources that an app accesses are also subject to authorization. Services such as Azure Storage require an application to provide an access key. Additionally, many services can be protected through role-based access control (RBAC), which describes the operations that individual users and groups can perform. The IT Operations Manager (Preeti, again) can set the authorization policy that defines which accounts and machines can connect to services such as Azure SQL Database, Azure Blob Storage, Azure API Management, and Azure App Services. Some services also enable you to restrict the endpoints from which authenticated users can request access. For example, you can configure a firewall for Azure SQL Database to deny access to requests emanating from unexpected IP addresses.

Azure helps to protect data in-flight by using transport layer security to encrypt it. This feature is vital for ensuring the integrity and privacy for any distributed system that transmits data over a network such as the public internet. In the case of VanArsdel, technicians will be running the app on mobile devices, utilizing roaming network connections that are outside the organization's control. Preeti is keen to ensure that unauthorized users cannot view or compromise sensitive data.

Data at rest, in storage accounts, databases, and other services in Azure, can also be encrypted. This provides an additional layer of privacy should the datacenter housing this information be breached. For a full list of the security features provided by Azure, read *Introduction to Azure security* at <https://aka.ms/AAbvtkn>.

## Personalizing the App

When someone runs a Power Apps app, it can retrieve information about the user from the Office365 environment. This information can be used to personalize the app. For example, currently the app that Maria and Kiana have developed doesn't distinguish between the different users; they all have access to the same data. Ideally, the app should be personalized to display the information most relevant to the engineer who uses it. Power Apps provides a function named **User** that enables the app to retrieve the email and full name of the current user. This app also requires the user ID (a unique Guid assigned to each user). The rationale behind this requirement is that usernames can be changed, but the ID cannot. The user ID is accessible using the features provided by the **Office365** connector. The steps below illustrate how to add this connector to the app:

1.  Using Power Apps Studio, in the **Tree view** pane, select the **Home** screen.

2.  On the **Insert** menu, from the **Text** drop-down list, add a **Label** control to the screen.

3.  Rename the **Label** control as **UserName**.

4.  Move the control so that it appears below the details showing the next appointment:

    ![Modify the layout of the Home screen][233]

5.  In the **Data** pane, select **Add data**. In the search box, enter **Office 365 Users**. Add the **Office 365 Users** connection to the app:

    ![Add the Office 365 Users connectore][234]

6.  In the **Tree view** pane, select the **UserName** label, and set the **Text** property to the following formula:

    ```
    Office365Users.MyProfileV2().displayName
    ```

    This formula uses the **Office365Users** connection to retrieve identity information about the current user. The **displayName** property of the **MyProfileV2** function contains the user's logged-on name.

    ![Home screen with the user name displayed][235]


> **NOTE:**
> Feel free to style the **UserName** control to make it stand out more.

Office365 runs in an Azure AD domain, but you can also extend this security domain with your own Azure AD installation. If your organization authenticates users through your own Azure AD domain, you can obtain user information by using the **Azure AD** connector instead of **Office365Users**:

![Add the Azure AD connector][236]

In this case, set the **Text** property of the **UserName** label to:

```
AzureAD.GetUser(User().Email).displayName
```

To personalize the appointments list requires calling a different Web API function in the **FieldEngineerAPI** connector. Currently, the **OnVisible** property of the **Home** screen contains the following formula:

```
ClearCollect(appointmentsCollection, Sort(Filter(FieldEngineerAPI.getapiappointments(), DateDiff(Today(), startDateTime) >= 0), startDateTime));
```

The Web API provides an alternative function that retrieves the appointments for a specified technician; you provide the ID of the technician as a parameter. You can use the Office365 user ID for this purpose. Update the **OnVisible** property as shown below:

```
Set(id, Office365Users.MyProfileV2().id);

ClearCollect(appointmentsCollection, Sort(Filter(FieldEngineerAPI.getapischeduleengineeridappointments(id), DateDiff(Today(), startDateTime) >= 0), startDateTime);
```

If you're authenticating with Azure AD, use this formula instead:

```
Set(id, AzureAD.GetUser(User().Email).id);

ClearCollect(appointmentsCollection, Filter(FieldEngineerAPI.getapischeduleengineeridappointments(id), DateDiff(Today(), startDateTime) >= 0), startDateTime);
```

> **NOTE**:
> This modification requires that the **EngineerId** column in the **Appointments** table is populated with the user's ID. This ID is a GUID, but is stored as a string in the database. The image below shows a few rows of sample data:

![Sample engineer data with IDs as GUIDs][237]

The **Engineers** table must also contain an Engineer with the corresponding ID:

![The Engineers table in the database][238]

The app is now ready to deploy and roll out.

## Deploying the App

The simplest way to deploy an app is to publish it to your Office 365 domain. All users who have the **Can use** permission can run the app, either from Power Apps Studio, or by using the Microsoft **Power Apps** app, available in the Windows Store at <https://aka.ms/AAbvtko>. Power Apps can be run on mobile devices like tablets and phones as soon as they're published; users only need find the Power Apps app in their devices' app store.

To publish an app:

1.  In Power Apps Studio, on the **File** menu, select **Save**. Save the app if you've made any changes. When you save the app, the **Publish** button appears.

2.  Select **Publish**. In the **Publish** dialog box, the **Edit details** option enables you to select settings, such as the name of the app, an icon for the app, and a description. You can also change the screen size and orientation used by the app. Select **Publish this version** to make the app available to other Power Apps users in your organization.

    ![Publish the app][239]

You can track the deployment history and app usage from the **Apps** tab on the **Administrators** page in Power Apps Studio, at <https://make.powerapps.com>. Select the app then, on the ellipses menu, select **Details**:

![Select the Details pane for an app][240]

On the **Details** pane, the **Versions** tab shows the version history for the app. The options on the ellipses menu for an app enable you to restore a previous version if you need to roll back a recent publication.

![Restore a previous version of an app ][241]

## Maintaining the App

The Power Platform admin center allows you to manage the environments in which Power Apps apps reside. The suggested approach is to create and publish your apps through Dataverse environments. You use separate environments for development and production.

Dataverse provides four types of environments: 

1.  **Sandbox**: Ideal for your development.  

2.  **Production**: Where the app should be deployed for use. 

3.  **Developer**: Assets created in here can\'t be shared. As a single user environment, you could use it for learning and exploring the capabilities of Power Apps apps.  

4.  **Default**: An environment that's automatically created for each tenant. Microsoft doesn\'t recommend you use this for apps because everyone in your tenant could then access those apps.  

You create environments using the Power Platform admin center at [https://admin.powerplatform.microsoft.com/](https://admin.powerplatform.microsoft.com/). On the **Environments** tab, select the **New** option in the menu bar. Specify the type of environment:

![Create a new Power Apps environment][242]

A good approach to application lifecycle management (ALM) is to start in a new sandbox environment, allowing you to safely develop and test your app in isolation from the production environment. Share and test your app as it\'s being developed. When your app is ready for real use, deploy it to a production environment and publish it from there. You can automate much of this process by using the Microsoft Power Platform Build Tools, described at <https://aka.ms/AAbvfzw>

For detailed information about ALM with Power Apps as it applies to VanArsdel, go to the **Scenario 1: Citizen Development** page at <https://aka.ms/AAbvfzx>

Chapter 9: Conclusions
======================

Fusion development is not a strict methodology; rather, it's an approach and philosophy that encourages rapid software development.

Fusion development combines the technical and business skills of an organization's employees to design and build applications. This approach values the insights and abilities of the different members of the team. It utilizes their specific insights into the business requirements and technical challenges required to implement a solution. The synergy afforded by fusion development enables efficient communication between different team members and enables them to iterate quickly to produce a functional system.

In this guide, you've seen how the staff at VanArsdel followed a fusion development approach. They produced an app that meets the expectations of the users represented by Caleb, the technician, Maria, the inventory manager, and Malik, who schedules engineers. Preeti is also satisfied that the system is safe and maintainable. The project was completed in record time - from the initial discussions between Caleb and Maria, to the rollout to all technicians.

The VanArsdel team has now experienced how fusion development teams work and is excited to keep collaborating on future projects.

  [https://www.microsoft.com]: https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.microsoft.com%2F&data=04%7C01%7Cshboyer%40microsoft.com%7Cb1396d7184b84ff63cae08d8fa682a21%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637534672631280414%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=rlcRH4u6zmBvIiC5IVCPgqbq%2FimkpV7QHQ2eW9Jd%2BmA%3D&reserved=0
    
  [1]: media/image1.png 
  [2]: media/image2.png 
  [3]: media/image3.png 
  [4]: media/image4.png 
  [5]: media/image5.png 
  [6]: media/image6.png 
  [7]: media/image7.png 
  [8]: media/image8.png 
  [9]: media/image9.png 
  [10]: media/image10.png 
  [11]: media/image11.png 
  [12]: media/image12.png 
  [13]: media/image13.png 
  [14]: media/image14.png 
  [15]: media/image15.png 
  [16]: media/image16.png 
  [17]: media/image17.png 
  [18]: media/image18.png 
  [19]: media/image19.png 
  [20]: media/image20.png 
  [21]: media/image21.png 
  [22]: media/image22.png 
  [23]: media/image23.png 
  [24]: media/image24.png 
  [25]: media/image25.png 
  [26]: media/image26.png 
  [27]: media/image27.png 
  [28]: media/image28.png 
  [29]: media/image29.png 
  [30]: media/image30.png 
  [31]: media/image31.png 
  [32]: media/image32.png 
  [33]: media/image33.png 
  [34]: media/image34.png 
  [35]: media/image35.png 
  [36]: media/image36.png 
  [37]: media/image37.png 
  [38]: media/image38.png 
  [39]: media/image39.png 
  [40]: media/image40.png 
  [41]: media/image41.png 
  [42]: media/image42.png 
  [43]: media/image43.png 
  [44]: media/image44.png 
  [45]: media/image45.png 
  [46]: media/image46.png 
  [47]: media/image47.png 
  [48]: media/image48.png 
  [49]: media/image49.png 
  [50]: media/image50.png 
  [51]: media/image51.png 
  [52]: media/image52.png 
  [53]: media/image53.png 
  [54]: media/image54.png 
  [55]: media/image55.png 
  [56]: media/image56.png 
  [57]: media/image57.png 
  [58]: media/image58.png 
  [59]: media/image59.png 
  [60]: media/image60.png 
  [61]: media/image61.png 
  [62]: media/image62.png 
  [63]: media/image63.png 
  [64]: media/image64.png 
  [65]: media/image65.png 
  [66]: media/image66.png 
  [67]: media/image67.png 
  [68]: media/image68.png 
  [69]: media/image69.png 
  [70]: media/image70.png 
  [71]: media/image71.png 
  [72]: media/image72.png 
  [73]: media/image73.png 
  [74]: media/image74.png 
  [75]: media/image75.png 
  [76]: media/image76.png 
  [77]: media/image77.png 
  [78]: media/image78.png 
  [79]: media/image79.png 
  [80]: media/image80.png 
  [81]: media/image81.png 
  [82]: media/image82.png 
  [83]: media/image83.png 
  [84]: media/image84.png 
  [85]: media/image85.png 
  [86]: media/image86.png 
  [87]: media/image87.png 
  [88]: media/image88.png 
  [89]: media/image89.png 
  [90]: media/image90.png 
  [91]: media/image91.png 
  [92]: media/image92.png 
  [93]: media/image93.png 
  [94]: media/image94.png 
  [95]: media/image95.png 
  [96]: media/image96.png 
  [97]: media/image97.png 
  [98]: media/image98.png 
  [99]: media/image99.png 
  [100]: media/image100.png 
  [101]: media/image101.png 
  [102]: media/image102.png 
  [103]: media/image103.png 
  [104]: media/image104.png 
  [105]: media/image105.png 
  [106]: media/image106.png 
  [107]: media/image107.png 
  [108]: media/image108.png 
  [109]: media/image109.png 
  [110]: media/image110.png 
  [111]: media/image111.png 
  [112]: media/image112.png 
  [113]: media/image113.png 
  [114]: media/image114.png 
  [115]: media/image115.png 
  [116]: media/image116.png 
  [117]: media/image117.png 
  [118]: media/image118.png 
  [119]: media/image119.png 
  [120]: media/image120.png 
  [121]: media/image121.png 
  [122]: media/image122.png 
  [123]: media/image123.png 
  [124]: media/image124.png 
  [125]: media/image125.png 
  [126]: media/image126.png 
  [127]: media/image127.png 
  [128]: media/image128.png 
  [129]: media/image129.png 
  [130]: media/image130.png 
  [131]: media/image131.png 
  [132]: media/image132.png 
  [133]: media/image133.png 
  [134]: media/image134.png 
  [135]: media/image135.png 
  [136]: media/image136.png 
  [137]: media/image137.png 
  [138]: media/image138.png 
  [139]: media/image139.png 
  [140]: media/image140.png 
  [141]: media/image141.png 
  [142]: media/image142.png 
  [143]: media/image143.png 
  [144]: media/image144.png 
  [145]: media/image145.png 
  [146]: media/image146.png 
  [147]: media/image147.png 
  [148]: media/image148.png 
  [149]: media/image149.png 
  [150]: media/image150.png 
  [151]: media/image151.png 
  [152]: media/image152.png 
  [153]: media/image153.png 
  [154]: media/image154.png 
  [155]: media/image155.png 
  [156]: media/image156.png 
  [157]: media/image157.png 
  [158]: media/image158.png 
  [159]: media/image159.png 
  [160]: media/image160.png 
  [161]: media/image161.png 
  [162]: media/image162.png 
  [163]: media/image163.png 
  [164]: media/image164.png 
  [165]: media/image165.png 
  [166]: media/image166.png 
  [167]: media/image167.png 
  [168]: media/image168.png 
  [169]: media/image169.png 
  [170]: media/image170.png 
  [171]: media/image171.png 
  [172]: media/image172.png 
  [173]: media/image173.png 
  [174]: media/image174.png 
  [175]: media/image175.png 
  [176]: media/image176.png 
  [177]: media/image177.png 
  [178]: media/image178.emf 
  [179]: media/image179.png 
  [180]: media/image180.png 
  [181]: media/image181.png 
  [182]: media/image182.png 
  [183]: media/image183.png 
  [184]: media/image184.png 
  [185]: media/image185.png 
  [186]: media/image186.png 
  [187]: media/image187.png 
  [188]: media/image188.png 
  [189]: media/image189.png 
  [190]: media/image190.png 
  [191]: media/image191.png 
  [192]: media/image192.png 
  [193]: media/image193.png 
  [194]: media/image194.png 
  [195]: media/image195.png 
  [196]: media/image196.png 
  [197]: media/image197.png 
  [198]: media/image198.png 
  [199]: media/image199.png 
  [200]: media/image200.png 
  [201]: media/image201.png 
  [202]: media/image202.png 
  [203]: media/image203.png 
  [204]: media/image204.png 
  [205]: media/image205.png 
  [206]: media/image206.png 
  [207]: media/image207.png 
  [208]: media/image208.png 
  [209]: media/image209.png 
  [210]: media/image210.png 
  [211]: media/image211.png 
  [212]: media/image212.png 
  [213]: media/image213.png 
  [214]: media/image214.png 
  [215]: media/image215.png 
  [216]: media/image216.png 
  [217]: media/image217.png 
  [218]: media/image218.png 
  [219]: media/image219.png 
  [220]: media/image220.png 
  [221]: media/image221.png 
  [222]: media/image222.png 
  [223]: media/image223.png 
  [224]: media/image224.png 
  [225]: media/image225.png 
  [226]: media/image226.png 
  [227]: media/image227.png 
  [228]: media/image228.png 
  [229]: media/image229.png 
  [230]: media/image230.png 
  [231]: media/image231.png 
  [232]: media/image232.png 
  [233]: media/image233.png 
  [234]: media/image234.png 
  [235]: media/image235.png 
  [236]: media/image236.png 
  [237]: media/image237.png 
  [238]: media/image238.png 
  [239]: media/image239.png 
  [240]: media/image240.png 
  [241]: media/image241.png 
  [242]: media/image242.png 
