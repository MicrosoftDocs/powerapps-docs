# Compose a page

After adding the required webpages and managing their hierarchy in the sitemap, you can add various components. The WYSIWYG editor allows you to add and edit the required components on the canvas easily. You can add and edit the following portal components on the canvas:

-   Text

-   Image

-   IFrame

-   Form

-   List

-   Breadcrumb

## Use the WYSIWYG editor

1.  [Edit the portal](manage-existing-portals.md#edit) to open it in the maker experience.  

2.  Select the page on which you want to add the component.

3.  Select an editable element on the canvas.

    > [!NOTE]
    > The editable elements are demarcated by a boundary.

4.  Select **Components** ![components icon](media/components-icon.png "Components icon") from the toolbelt on the left side of the screen.  

5.  Select the component to be added.

    ![components pane](media/components-pane.png "Components pane")  

    The selected component is added to the canvas inside the editable element.

6.  To delete a component, select the component on the canvas and then select **Delete** on the component’s toolbar.

    ![delete component](media/delete-component.png "Delete component")  

### Add text box

1.  [Edit the portal](manage-existing-portals.md#edit) to open it in the maker experience.  

2.  Select the page on which you want to add the component.

3.  Select an editable element on the canvas.

4.  Select **Components** ![components icon](media/components-icon.png "Components icon") from the toolbelt on the left side of the screen.  

5.  Select **Text**.

6.  Enter the required text in the text box.

7.  To format the text, select the text to display the format options. Modify the font size and style as required.

    ![text component](media/text-component.png "Text component")  

### Add image

1.  [Edit the portal](manage-existing-portals.md#edit) to open it in the maker experience.  

2.  Select the page on which you want to add the component.

3.  Select an editable element on the canvas.

4.  Select **Components** ![components icon](media/components-icon.png "Components icon") from the toolbelt on the left side of the screen.  

5.  Select **Image**. The image placeholder is added to the canvas.

6.  In the **Properties** pane, enter the following information:

    - **Image**: Select this option if you would like to select an existing image or upload a new one. If you want to select a previously uploaded image, choose an image from the **Select image** list. To upload a new image, select **Upload file**.

    > [!NOTE]
    > You can upload only the images of type png, svg, jpg, and jpeg with the maximum size of 5 MB.

    ![image properties](media/image-props.png "Image properties")  

    - **External url**: Select this option if you would like to upload an image from an external URL. Enter the URL in the **External url** field. Only secured links are accepted—that is, https:// is mandatory. If you have images stored in your content delivery network, you can provide the link in this field.

    ![image external url](media/image-ext-url.png "Image external URL")  

    -   Formatting options

        - **Width**: Enter width of the image.

        - **Height**: Enter height of the image.

    > [!NOTE]
    > You can also select the image on the canvas and drag the handles to resize it.

### Add IFrame

1.  [Edit the portal](manage-existing-portals.md#edit) to open it in the maker experience.  

2.  Select the page on which you want to add the component.

3.  Select an editable element on the canvas.

4.  Select **Components** ![components icon](media/components-icon.png "Components icon") from the toolbelt on the left side of the screen.  

5.  Select **IFrame**. The IFrame placeholder is added to the canvas.

6.  In the **Properties** pane, enter the following information:

    1. **Width**: Enter the width of the IFrame.

    2. **Height**: Enter the height of the IFrame.

    3. **Link**: Enter the URL of the website to be displayed in the IFrame. Only secured links are accepted—that is, https:// is mandatory. By default, <https://www.bing.com> is available as the value.

    ![iframe properties](media/iframe-props.png "IFrame properties")  

    > [!NOTE]
    > You can also select the IFrame on the canvas and drag the handles to resize it.

### Add form

Form is a data-driven configuration that you use to add a form to collect data in the portal without the need for a developer to surface the form in the portal. [Forms are created in Common Data Service](https://docs.microsoft.com/en-us/powerapps/maker/model-driven-apps/form-designer-overview) and you can use them into webpages in the portal or in conjunction with lists to build out complete web applications.  

1.  [Edit the portal](manage-existing-portals.md#edit) to open it in the maker experience.  

2.  Select the page on which you want to add the component.

3.  Select an editable element on the canvas.

4.  Select **Components** ![components icon](media/components-icon.png "Components icon") from the toolbelt on the left side of the screen.  

5.  Select **Form**.

6.  In the **Properties** pane, enter information or make selection for the following:

    - **Entity name**: The name of the entity from which the form will be loaded.

    - **Forms**: The name of the form on the target entity in Common Data Service that is to be rendered.

    - **Mode**: Select one of the following options:

        - **Insert**: Indicates the form should insert a new record upon submission.

        - **Edit**: Indicates the form should edit an existing record.

        - **ReadOnly**: Indicates the form should display an existing record’s noneditable form.

        > [!NOTE]
        > The default option for **Edit** and **ReadOnly** modes is set as Query String Parameter Name passed as ID in URL. To change these values, you need to open Portal Management app and update the form properties.

    - **On success**: Select one of the following options:

        - **Show success message**: Requires a message to be displayed to the user on successful submission of the form. You can also select **Hide form on success** to hide the form upon successful submission.

        - **Redirect to webpage**: Redirects the user to the selected webpage in the portal. You must select a webpage from the **Redirect to webpage** list.

        - **Redirect to URL**: Redirects the user to the specified URL. You must enter a URL in the **Redirect to URL** field.

    - **Show captcha for anonymous users**: Displays captcha to anonymous users.

    - **Show captcha for authenticated users**: Displays captcha to authenticated users.

    - **Enable entity permissions**: Entity permissions to be considered for the form. By default, it is not selected. If selected, explicit permissions are required for any user to access the form. More information: [Entity permission](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/assign-entity-permissions)

    ![form properties](media/form-props.png "Form properties")

### Add list

List is a data-driven configuration that you use to add a webpage that will render a list of records without the need for a developer to surface the grid in the portal. Lists use [Common Data Service views](https://docs.microsoft.com/en-us/powerapps/maker/model-driven-apps/create-and-edit-views) to display records on the portal.  

1.  [Edit the portal](manage-existing-portals.md#edit) to open it in the maker experience.  

2.  Select the page on which you want to add the component.

3.  Select an editable element on the canvas.

4.  Select **Components** ![components icon](media/components-icon.png "Components icon") from the toolbelt on the left side of the screen.  

5.  Select **List**.

6.  In the **Properties** pane, enter information or make selection for the following:

    - **Entity name**: The name of the entity from which the views will be loaded.

    - **Views**: The list of views of the target entity that is to be rendered. You can select multiple views to display records in the list. The view selected first will be the default view.

    - **Enable create new record**: Allows a user to create a record. Select a webpage that contains a form to create a new record.

    - **Enable view details**: Allows a user to view details. Select a webpage that contains a form to display details.

    - **Enable edit record**: Allows a user to edit a record. Select a webpage that contains a form to edit the record.

    - **Enable delete record**: Allows a user to delete a record.

    - **Empty list message**: Message to be displayed when there are no records to be displayed.

    - **Number of records per page**: An integer value to specify the number of the records to display on a page.

    - **Enable search in entity list**: Allows a user to search records in the list.

    - **Enable entity permissions**: Entity permissions to be considered for the list. By default, it is not selected. If selected, explicit permissions are required for any user to access the form. More information: [Entity permission](https://docs.microsoft.com/en-us/dynamics365/customer-engagement/portals/assign-entity-permissions)  
    ![list properties](media/list-props.png "List properties")

### Add breadcrumb

1.  [Edit the portal](manage-existing-portals.md#edit) to open it in the maker experience.  

2.  Select the page on which you want to add the component.

3.  Select an editable element on the canvas.

4.  Select **Components** ![components icon](media/components-icon.png "Components icon") from the toolbelt on the left side of the screen.  

5.  Select **Breadcrumb**.

