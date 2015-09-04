<properties
	pageTitle="KratosApps tutorial: Create an app from a blank screen"
	description="Create an app from scratch by importing a set of sample data, filtering the data, adding items to a custom list, specifying a quantity for each item, and calculating the total cost."
	services="kratosapps"
	authors="AFTOwen"
 />

# Create an app from a blank screen in KratosApps #
Create an app that shows sample data about tablets, laptops, and desktop computers from various manufacturers. Import text and images from an Excel file, show a list from which users can choose one or more devices, and dynamically update the total cost based on a variable quantity for each device.

The first screen of this app shows icons for device categories along the top and manufacturers (OEMs) along the left edge. Users can click these icons to filter the list of devices in the middle of the screen. Users create a list of devices that interest them by selecting the check box for each device. To show the list on the next screen, users click **View Device Mix**.

![Fully configured MainScreen](./media/gs-pcselector/main-screen.jpg)

The second screen of this app shows a list of the devices that the user specified on the first screen. Users can specify a quantity for each device, and the app shows the total cost.

![Summary screen](./media/gs-pcselector/summary-screen.jpg)

**Prerequisites**

- Download and install [KratosApps](https://www.kratosapps.com/downloads).

## Install sample data
In this procedure, you'll download an Excel file and three sets of graphics. The Excel file contains these tables:

- **PcCategory**, which contains a name and a link to a graphic for each category
- **OEM**, which contains a name and a link to a graphic for each manufacturer
- **Devices**, which contains a name, a link to a graphic, and other information for each device

After you install the sample data, you'll configure the folder that contains the data so that KratosApps can find it.

1. Download [this file](), and then double-click it to install the sample data in this folder:

	**C:\\Users\\Public\\Public Pictures\\SienaAssets\\PcSelector**
1. In **C:\\Users\\Public\\Pictures**, right-click **SienaAssets**, point to **Include in library**, and then click **Pictures**.

	![Including the SienaAssets in a library](./media/gs-pcselector/include-library.jpg)

1. (optional) Open the Excel file to understand how the tables are structured.

	For example, the **OEM** table has a column for the name of each manufacturer and a column for links to each logo:

	![The OEM table, with names and links to logos](./media/gs-pcselector/oem-table.jpg)

##Import sample data##

2. Open KratosApps, and then press Alt-D (or open the **File** menu, and then click **Data Sources**).

	![File menu](./media/gs-pcselector/file-menu.jpg)

4. In the list of data sources, click **Excel**.

	![List of data sources, including Excel](./media/gs-pcselector/add-excel-data.jpg)

5. Browse to the Excel file that you installed at the start of this procedure, and then click that file.

	![Sample data, including the Excel file](./media/gs-pcselector/win8devices.jpg)

6. Click **Open**, confirm that all three checkboxes are selected, and then click **Import Data**.

	![A checkbox for each table in Excel that you can import](./media/gs-pcselector/select-tables.jpg)

	The three tables in the Excel file appear under **Existing sources**.

	![A list of the tables that you imported from Excel](./media/gs-pcselector/existing-sources.jpg)

1. (optional) Click each table to display a preview of the data that it contains.

	For example, the **OEM** table shows the name and a logo for each manufacturer. The logos will appear along the left edge of the first screen of the app.

	![A preview of the OEM table](./media/gs-pcselector/oem-preview.jpg)

7. Return to the default workspace by pressing Esc (or by clicking the Back arrow in the upper-left corner of the screen).

	![Back arrow from the list of data sources](./media/gs-pcselector/back-arrow.jpg)

## Create a banner ##
In this procedure, you'll add a rectangle to the first screen of your app, and then you'll configure the **Fill** color, location, and size of the rectangle.

2. On the ribbon, click the **Insert** tab.

	![Insert tab in the ribbon](./media/gs-pcselector/insert-tab.jpg)

3. On the **Insert** tab, click **Shapes**, and then click the rectangle to add it to the first screen of your app.

	![The shapes that you can add to a screen in your app](./media/gs-pcselector/add-rectangle.jpg)

	The rectangle appears near the upper-left corner of the screen.

	![The shapes that you can add to a screen in your app](./media/gs-pcselector/default-rectangle.jpg)

	By default, a thick, gray box surrounds the rectangle to indicate that it's selected by default.

	**Important:** If you click away from the rectangle, it's no longer selected, and you can't configure it. To modify the rectangle (or any other control or screen), click it to select it, and then you can change any of its properties, such as its **Fill** color.

4. On the **Home** tab of the ribbon, click **Fill**, and then click a color in the list that appears.

	To follow this tutorial exactly, click the orange option in the middle of the leftmost column.

	![The Fill item on the Home tab of the ribbon](./media/gs-pcselector/fill-menu.jpg)

5. Move the rectangle to the upper-left corner of the screen by dragging the selection box around it up and to the left.

6. In the right side of the same selection box, drag the white square to the right edge of the screen, so that the rectangle becomes a banner.

	The thumbnail view of your screen, near its left edge, reflects your changes.

	![A thumbnail of a blank screen with an orange banner](./media/gs-pcselector/banner-thumbnail.jpg)
## Show the device categories ##
In this procedure, you'll add a gallery that shows an icon for each device category. A gallery is a UI element that contains other UI elements. By adding and configuring a gallery, you can show a set of related data more easily than by adding and configuring individual elements.

1. On the **Insert** tab, click **Gallery**, and then click the horizontal **Image Only** gallery to add it to your screen.

	![Gallery tab with the horizontal Image Only gallery selected](./media/gs-pcselector/add-category-gallery.jpg)

1. Confirm that **Items** appears in the properties list, which is near the upper-left corner of the screen.

	**Tip:** You can configure some properties of a control, such as its size and location, by clicking, dragging, or typing in the control itself. You can change other properties, such as **Fill**, by clicking options in the ribbon. But all properties appear alphabetically in the properties list, so you can always find a property by looking for its name in that list.

3. Set the **Items** property of the gallery by typing **PcCategory** in the Function Bar, which is to the right of the function button.

	**PcCategory** is the name of a table in the Excel file that you imported. That table contains links to icons that the gallery should show.

	![Property list showing Items and Function Bar showing PcCategory](./media/gs-pcselector/items-pccategory.jpg)

2. Move the gallery to the center of the orange banner, and resize the gallery to fit inside the banner.

	![Orange banner with a icon for each type of device](./media/gs-pcselector/category-gallery.jpg)

## Rename a screen and a gallery
In this procedure, you'll rename the default screen and the gallery that you added. You can more easily develop an app if you rename, for example, screens from the default names of **Screen1**, **Screen2**, and so forth.

4. Select the gallery by clicking the icon for the **Laptop** or the **All-in-one** category.

	![Selecting the PcCategory gallery](./media/gs-pcselector/select-pccategory-gallery.jpg)

6. On the **Home** tab, click **Gallery1**, and then type **CategoryGallery**.

	**Note:** If you've added and deleted a gallery before you added this one, the name of the gallery will end with a number that's greater than 1.

	![Renaming the PcCategory gallery](./media/gs-pcselector/rename-gallery.jpg)

7. Click an empty area of the screen to select it, click **Screen1** on the **Home** tab, and then type **MainScreen**.

	![Renaming the first screen](./media/gs-pcselector/rename-screen.jpg)

8. Save your changes by pressing Ctrl-S (or by opening the **File** menu and then clicking **Save**).

## Show the OEM logos ##
In this procedure, you'll add another gallery and then configure it to show the logo of each OEM. You'll also update the template for that gallery, which will automatically update every item in the gallery to match.

6. On the **Insert** tab, click **Gallery**, and then click the vertical **Image Only** gallery.

	![Gallery tab with the vertical Image Only gallery selected](./media/gs-pcselector/add-oem-gallery.jpg)

8. Name the gallery that you just added **OemGallery**, and set its **Items** property to **OEM**.
7. Move the **OemGallery** to the left edge of the screen (under the orange banner), and resize the gallery so that it shows most of four logos.

	![OEM gallery with four truncated logos](./media/gs-pcselector/four-logos.jpg)

8. Click the first the image in the gallery to update the gallery template.

	![OEM gallery with gallery selected](./media/gs-pcselector/oem-gallery-template.jpg)

9. On the **Image** tab, click **ImagePosition**, and then click **ImagePosition!Fit**.

	![Image Position menu on Image tab](./media/gs-pcselector/image-position.jpg)

	Each logo appears entirely in the gallery.

	![OEM gallery](./media/gs-pcselector/oem-gallery.jpg)

## Show the devices ##
In this procedure, you'll add a third gallery, which will show an image of each device, its manufacturer, and its category. In the last step, you'll configure the gallery to show the price of each device instead of its category.

1. On the **Insert** tab, click **Gallery**, and then click the horizontal **Image With Text** gallery.

	![Add Image gallery with text](./media/gs-pcselector/add-device-gallery.jpg)

2. Name the newest gallery **DevicesGallery**, and set its **Items** property to **Devices**.

	![Image gallery with text set to show devices](./media/gs-pcselector/device-gallery-default.jpg)

2. Position the **DevicesGallery** so that it touches the right edge of the **OemGallery**, near the vertical center.
3. 4. Just as you did for the **OemGallery**, set the **ImagePosition** property for images in the **DevicesGallery** to **Fit**.
4. Under the first image in the **DevicesGallery**, click the bottom label, and then set its **Text** property to this expression, so that the price of each device appears with a dollar sign:

	**"$" & ThisItem!Price**

	![Device gallery showing price](./media/gs-pcselector/device-price.jpg)

	**Note:** The price expression contains two elements and an ampersand:

	- The first element (the dollar sign) is a literal string, which means that it will appear exactly as you type it. To specify a literal string in an expression, you surround the string with quotation marks.
	- The ampersand concatenates whatever elements precede and follow it, so that they appear as a continuous element.
	- The last element is a placeholder for the price of the device. The element is automatically replaced with whatever value is in the **Price** column of the table that the gallery shows.

## Filter the devices ##
In this procedure, you'll configure the **DeviceGallery** so that users can filter it by both category and manufacturer. You'll also test the filter in Preview, with which you can verify that your app works exactly as you expect.

1. Set the **Items** property of the **DevicesGallery** to this expression:

	**Filter(Devices, MFR = OemGallery!Selected!MFR && DeviceType = CategoryGallery!Selected!PcCategory)**

	[More information]() about **Filter** and other functions

2. Press F5 to open Preview.

3. Click a category and an OEM logo to show only devices in that category from that manufacturer.

4. Return to the default workspace by pressing Esc.

## Highlight devices by price##
In this procedure, you'll highlight less expensive devices by using a conditional statement. For the **If** function, you specify a condition that is either true or false and a result if the condition is true. You can also specify a result if the condition is false.

In this case, you'll specify that, if the price of the device is less than $700, the **Fill** color of the price label will be light green. If the price is $700 or more, the **Fill** color will be light gray. You'll also change the text in that label to a black bold font.

1. Under the first image in the **DevicesGallery**, click the bottom label, and then set its **Fill** property to this expression:

	**If(Price<700,LightGreen,LightGray)**

	[More information]() about **If** and other functions

2. Set the **Color** property of the same label to **Black**, and set its **FontWeight** property to **Bold**.
3. (optional) Find a device that costs less than $700, and verify that its price appears in a green, not gray, box.

	![Devices that are less than $700 are highlighted in green](./media/gs-pcselector/price-highlight.jpg)

## Create a custom list ##
In this procedure, you'll add a checkbox to each item in the **DevicesGallery**. Users can select or clear the checkbox for one or more devices to add them to a custom list or to remove them from the list.

1. In the **DevicesGallery**, click any item except the first one, and then click the pencil icon in the upper-left corner of the gallery.

	![Select a gallery template](./media/gs-pcselector/select-gallery-template.jpg)

	You've selected the gallery template, instead of a specific element in the template.

	![The template for the DevicesGallery is selected](./media/gs-pcselector/device-gallery-template.jpg)

1. On the **Insert** tab, click **Controls**, and then click **Checkbox**.

	![Add a checkbox](./media/gs-pcselector/insert-checkbox.jpg)

1. Shrink the height of the image element, and then move the checkbox under it.

	![Move a checkbox under image](./media/gs-pcselector/checkbox-under-image.jpg)

1. In the first item of the gallery change the checkbox's text by double-clicking **Option** and then typing **Save**.

1. Ensure that the checkbox element is still selected.

	![The checkbox element, not the checkbox itself, is selected](./media/gs-pcselector/checkbox-element-selected.jpg)

3. On the **Behavior** tab, click **OnCheck**.

	![Setting the OnCheck behavior property](./media/gs-pcselector/behavior-oncheck.jpg)

	**OnCheck** and other behavior properties determine how your app responds when an event that you specify occurs. In this case, you're specifying what happens when the user adds a checkmark to the checkbox.

1. Click **Collect**, click the down arrow for the lower list, and then click **ThisItem**.

	![Create a collection](./media/gs-pcselector/create-collection.jpg)

	The properties list shows **OnCheck**, and the Function Bar shows the expression for adding the selected item to a collection named **Collection1**.

	![OnCheck in the properties list and the Collect function in the Function Bar](./media/gs-pcselector/collect-property-function.jpg)

	[More information]() about collections

1. With the checkbox control still selected, click **OnUncheck** on the **Behavior** tab.

	![Setting the OnUncheck behavior property](./media/gs-pcselector/behavior-onuncheck.jpg)

1. Click **Remove**, click the down arrow for the lower list, and then click **ThisItem**.

	![Remove ThisItem from Collection1](./media/gs-pcselector/remove-thisitem.jpg)

## Add a screen and navigation##
In this procedure, you'll add the SummaryScreen. On the MainScreen, you'll add a button that users can click to show the SummaryScreen. On the SummaryScreen, you'll add a back arrow that users can click to show the MainScreen.

1. On the **Home** tab, click **New Screen**.

	![Add a screen](./media/gs-pcselector/add-screen.jpg)

1. Name the new screen **SummaryScreen**, and then return to the **MainScreen** by clicking it in the left navigation bar.
2. On the **Insert** tab, click **Button**.

	![Add a button](./media/gs-pcselector/add-button.jpg)

1. Move the button near the right edge of the banner, change its text to **View Device Mix**, and change its fill to black.

	![Move button and change its text and color](./media/gs-pcselector/configure-button.jpg)

1. With the button still selected, click the **Behavior** tab, and then click **Navigate**.

	![Add Navigate behavior to button](./media/gs-pcselector/navigate-button.jpg)

	The properties list automatically shows the **OnSelect** property, which determines how the app responds when users click the button. The Function Bar shows the expression for showing the **SummaryScreen** with a fade transition:

	**Navigate(SummaryScreen, ScreenTransition!Fade)**

	[More information]() about how to navigate between screens

1. Show the **SummaryScreen** by clicking it in the left navigation bar.

	![Choose the SummaryScreen in the left navigation bar](./media/gs-pcselector/navigate-summary.jpg)

2. On the **Insert** tab, click **Shapes**, and then click the back arrow to add it to the screen.

	![Add a back arrow](./media/gs-pcselector/add-back-arrow.jpg)

1. With the arrow still selected, click the **Behavior** tab, and then click **Navigate**.

	The properties list shows the **OnSelect** property, and the Function Bar shows the expression for navigating to the **MainScreen** with a fade transition:

	**Navigate(MainScreen, ScreenTransition!Fade)**

1. (optional) Test navigation:
	1. Press F5 to open Preview.
	2. Show each screen by clicking the button on the **MainScreen** and the back arrow on the **SummaryScreen**.
	3. Press Esc to return to the default workspace.

## Show the custom list ##
In this procedure, you'll add items to a custom list and then show it in a gallery. To keep this procedure short, you'll copy the gallery from the **MainScreen**, paste it into the **SummaryScreen**. Then you'll change the gallery's data source to the custom list that you create in **Collection1**.

1. From the **MainScreen**, press F5 to open Preview.

2. Select the checkbox for more than one device, and then press Esc to return to the default workspace.

2. Click the orange banner, and then hold down Ctrl as you click any item in the **DevicesGallery** except the first one.

	A selection box appears around both the banner and the **DevicesGallery**.

	![Select both the banner and the DevicesGallery](./media/gs-pcselector/select-banner-gallery.jpg)

3. Press Ctrl-C to copy those two controls to the Clipboard, show the **SummaryScreen**, and then press Ctrl-V to paste them onto that screen.

1. Rename the gallery that you pasted to **SelectedDevicesGallery**, and set its **Items** property to **Collection1**.

4. Click the banner, click **Reorder** on the **Home** tab, and then click **Send to Back**.

	![Send banner to back to show arrow](./media/gs-pcselector/send-to-back.jpg)

	The back arrow appears in front of the banner.

6. Change the **Fill** property of the back arrow to white, and move it to the closer to the left edge of the banner, near the vertical center.

	![Show the custom list, the banner, and the back arrow](./media/gs-pcselector/custom-list.jpg)

##Specify a quantity for each device ##
In this procedure, you'll replace the checkbox in each item of the gallery with a slider and add a label for clarity. Users will adjust the slider for each device to specify a quantity for that device.

1. In the first item of the **SelectedDevicesGallery**, click the checkbox, and then press Delete.

2. Select the template for the **SelectedDevicesGallery** by clicking any item *except* the first one and then clicking the pencil icon in the upper-left corner of the gallery.

	![Select the template for the SelectedDevicesGallery](./media/gs-pcselector/select-template.jpg)

3. On the **Insert** tab, click **Controls**, and then click **Slider**.

	![Add a slider](./media/gs-pcselector/add-slider.jpg)

4. Rename the slider **QuantitySlider**, and move it below the image in the template.

	![Move slider under device image](./media/gs-pcselector/slider-under-image.jpg)

1. With the template still selected, click **Label** on the **Insert** tab.

	![Add a label](./media/gs-pcselector/add-label.jpg)

2. Double-click the label, and then type **QTY:** to change its text.
3. Move the label near the left edge of the slider.

	![Configure the text of the label and move it](./media/gs-pcselector/qty-label.jpg)

## Show total cost ##
In this procedure, you'll add a label and configure it with an expression that calculates the overall cost of all devices in the custom list. The expression combines the following:

- A literal string, surrounded by quotation marks, to explain what the value is and precede it with a dollar sign
- An ampersand to concatenate the literal string and the value
- A **Sum** function that multiplies the per-unit price of each device in the list by the quantity that you specify with the slider for that device

[More information]() about functions such as **Sum**

1.  On the **SummaryScreen**, add a label, and move it near the right edge of the banner.

3. With the label still selected, click **Text** in the properties list, and then replace the default text with this expression:

	**"Total Cost: $" & Sum(SelectedDevicesGallery!AllItems, Price * QuantitySlider!Value)**

	After you add the expression, the label will resemble this graphic, though the actual value will depend on which devices you selected and which quantities you specified.

	![Summary screen](./media/gs-pcselector/summary-screen.jpg)

1. (optional) Press F5 to open Preview, adjust the sliders to verify that the total cost updates to reflect your changes, and then press Esc to return to the default workspace.

## Publish the app ##
1. On the **File** menu, click **Publish**.

	![The Publish option on the File menu](./media/gs-pcselector/file-publish.jpg)

2. In the text box, type a name for the app, and then click **Publish**.

	![Specify a name for the app](./media/gs-pcselector/name-app.jpg)

	If you sign in to the product website, the app will appear under **My apps**.

3. (optional) To allow others to use or modify your app:
	1. Type their email addresses in the **To:** text box.
	2. In the drop-down list, click **Can view** to allow them to run the app, or click **Can edit** to allow them to run or modify the app.
	3. Customize the **Subject** and **Message** text if you want, and then click **Share**.

	![Mail template for sharing an app](./media/gs-pcselector/share-app.jpg)

	If any of the users that you specified sign in to the product website, the app will appear under **My apps**.

1. Press Esc (or click the back arrow in the upper-left corner) to return to the default workspace.
## Next Steps ##

- [Save your custom list]() When you close this app, the information in your custom list will be lost unless you save it on your local device.
