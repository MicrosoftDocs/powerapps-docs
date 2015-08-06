<properties
	pageTitle="Show text, numbers, and dates in KratosApps"
	description="Show an individual piece of text, a numerical value, or a date by adding a label, or show related pieces of text (such as the headlines, the publication dates, and the copy for a set of articles) in a gallery."
	services="kratosapps"
	authors="AFTOwen"
 />
# Show text in KratosApps #

## Add, move, resize, and rename a label ##
1. On the **Insert** tab, click **Label**.

	*Screen shot*

	A label control appears near the upper-left corner of the screen. As with all controls, the label is selected by default, as indicated by the thick, gray box that surrounds it.

	*Screen shot*

	If you click outside the label, it's no longer selected, and the selection box disappears from the label. To select the label again, click it.

	**Important:** The label must be selected for any subsequent step in this procedure to work or for you to configure any other property of the label.

1. Move the label to the center of the screen by dragging the selection box itself (not a white square in an edge of the selection box or a white triangle in a corner of the selection box).
2. Double the width and height of the label by dragging a white square in the edge of the selection box or a white triangle in the corner of the selection box.

	*Screen shot*

1. On the **Home** tab, click **Label1**.

	*Screen shot*

2. Rename the label by typing **TestLabel** in the box that appears.

## Show text in a label ##
Show text in a label by setting the value of its **Text** property. You can set this property by typing directly into the label or by specifying an expression in the Function Bar. If you type directly into the label, it shows exactly what you type. If you specify an expression, the label shows the result of the expression.

1. Based on the steps in the previous procedure, add a label named **ShowText**.
2. In **ShowText**, double-click the default text to select it.

	*Screen shot*

4. Replace it by typing **This is my app** directly into **ShowText**.

	*Screen shot*

1. In the properties list, click **Text**, and then type or paste this expression in the Function Bar:

	**DateDiff(Today(), DateValue("01/01/2020"))**

	The label shows the number of days between today and January 1, 2020. This expression combines these functions:

	- **DateDiff**, which calculates the number of days, quarters, or years between two dates.
	- **Today**, which calculates the current day as a value.
	- **DateValue**, which converts a literal string, as shown between quotation marks, to a value on which calculations can be performed.

1. On the **Insert** tab, click **Text**, and then click **Input Text**.

	*Screen shot*

	An input-text box appears on the screen. Users can specify data by typing text into this box.

	*Screen shot*

1. Name the new box **Birthdate**.
2. Change the **Text** property of **ShowText** to this expression:

	**DateDiff(Today(), DateValue(Birthdate!Text))**

	This expression will show the number of days between today and whatever date the user types into **Birthdate**. When the user types a date into **Birthdate**, the **Text** property of that control is set to that value.

1. Double-click the default text in **Birthdate**, and then replace it by typing the date of your next birthday.

	**ShowText** shows the number of days between today and your next birthday.

## Format a label ##

1. With the label selected, click **Fill** on the **Home** tab, and then click a color in the list that appears.

	To follow this tutorial exactly, click the black option at the top of the leftmost column.

	*Screen shot*

	The fill of the label matches the color that you selected.

	*Screen shot*

2. On the **Home** tab, click **Color**, and then click a color in the list that appears.

	To follow this tutorial exactly, click the white option, which is second from the top of the leftmost column.

	*Screen shot*

	The text of the label matches the color that you selected.

	*Screen shot*

1. On the **Home** tab, click **Font Weight**, and then click **Bold**.

	*Screen shot*

	The text of the label appears in a bold font.

	*Screen shot*

1. On the **Home** tab, set the size of the font to **32**.

	*Screen shot*

1. On the **Home** tab, click **Align**, and then click **Center Alignment**.

	*Screen shot*

	The text appears in the horizontal center of the label.

	*Screen shot*

1. Click the **Label** tab to show options that are specific to labels.

	*Screen shot*

3. On the **Label** tab, click **VerticalAlign**, and then click **Middle**.

	*Screen shot*

	The text appears in the vertical center of the label.

	*Screen shot*

## Show text in a gallery ##
1. On the **Insert** tab, click **Gallery**, and then click a text gallery in landscape orientation.

	*Screen shot*

1. On the **File** menu, click **Data Sources** (or press Ctrl-D).

	*Screen shot*

1. Under **Add new source**, click **RSS Feed**.

	*Screen shot*

1. In the text box that appears, type or paste this URL, and then click **Import data**:

	**http://blogs.technet.com/b/projectsiena/rss.aspx**

	The RSS feed that you just added appears under **Existing Sources**, and a preview of its text appears in the pane to the right.

	*Screen shot*

1. Near the upper-left corner, click the Back button (or press Esc) to return to the default workspace.

	*Screen shot*

1. On the **Insert** tab, click **Gallery**, and then click a text gallery in landscape orientation.

	*Screen shot*

1. With the gallery selected and the properties list set to **Items**, type or paste **rss_1** in the Function Bar.

	*Screen shot*

	The gallery shows text from the RSS feed, but you probably want to change the kind of information that appears in each label, as the next procedure describes.

## Change the text that appears in each element of a gallery ##
1. Complete the steps in the previous procedure.
2. Select the **Heading1** label by clicking inside the leftmost item of the gallery, near the top.

	*Screen shot*

1. With the properties list set to **Text**, replace the default value with **ThisItem!title** in the Function Bar.

	*Screen shot*

	The first part of the title of each article appears near the top of the gallery.

	*Screen shot*

1. Set the size of the text to **11**, and make it bold.

	*Screen shot*

	The entire title of each article appears near the top of the gallery.

	**Note:** To avoid showing a partial item, widen the gallery to show more than one item, or shrink the gallery's width to show only one item.

	*Screen shot*

1. Select **Subtitle1** by clicking just under **Heading1** in the leftmost item of the gallery.

	*Screen shot*

1. With the properties list set to **Text**, replace the default value with **ThisItem!pubDate** in the Function Bar.

	*Screen shot*

	The publication date and time of each article appears under its title.

	*Screen shot*

1. Select the **Body1** label by clicking inside the leftmost item in the gallery, near the bottom.

	*Screen shot*

1. With the properties list set to **Text**, replace the default value with **ThisItem!description** in the Function Bar.

	*Screen shot*

	The body of each article appears with some HTML tags appearing as plain text. You can use an HTML label to render those tags properly, as the next procedure describes.

	*Screen shot*

## Show text in an HTML label ##
1. Follow the steps in the previous procedure.
2. Delete the **Body1** label by clicking the content of the article that appears in the leftmost item of the gallery and then pressing Delete.
3. Select the gallery template by clicking under the **Subtitle1** label in the leftmost item of the gallery.

	*Screen shot*

3. On the **Insert** tab, click **Text**, and then click **HTML Label**.

	*Screen shot*

	An HTML label appears in each item of the gallery.

1. In the leftmost item of the gallery, move and resize the HTML label to fit in the area that was taken by the label that you deleted.

	*Screen shot*

1. With the HTML label selected and the properties list showing **HtmlText**, replace the default value with **ThisItem!description** in the Function Bar.

	The HTML tags render properly.

	*Screen shot*