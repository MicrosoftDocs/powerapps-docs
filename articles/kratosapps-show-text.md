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

	Important: The label must be selected for any subsequent step in this procedure to work or for you to configure any other property of the label.

1. Move the label to the center of the screen by dragging the selection box itself (not a white square in an edge of the selection box or a white triangle in a corner of the selection box).
2. Double the width and height of the label by dragging a white square in the edge of the selection box or a white triangle in the corner of the selection box.

	*Screen shot*

1. On the **Home** tab, click **Label1**.

	*Screen shot*

2. Rename the label by typing **TestLabel** in the box that appears.

## Show text in a label ##
Show words, numbers, dates, or currency values in a label by setting the value of its **Text** property. Set that value by typing directly into the label or by using the Function Bar. Specify the value of that property as literal string, which appears exactly as you type it, or to an expression. For example, use an expression to show data from another control.

1. Double-click the default text in the label, and then type **This is my app.**

	*Screen shot*

	You can change the text that a label shows by typing it directly in the label, as you just did, or by setting the **Text** property of the label, as you'll do throughout the rest of this procedure.

2. In the property list, click **Text**, and then type **"This is my new app."** (including the quotation marks) in the Function Bar.

	*Screen shot*

	The label shows only the text between the quotation marks, not the marks themselves. Quotation marks indicate a literal string, which means that the label shows exactly the text that you type between the quotation marks.

	*Screen shot*

1. In the Function Bar, type this expression:

	**"Seattle" & "," & "Washington"**

	*Screen shot*

	The expression contains three literal strings (the name of a city, a comma, and the name of a state) and two ampersands. The ampersands concatenate the name of the city, the comma, and the name of the state. That is, the ampersands show the three separate strings as a continuous piece of text.
1. In the Function Bar, type this string:

	 **"Now()"**

	*Screen shot*

1. In the Function Bar, remove the quotation marks.

	*Screen shot*

	The label shows the current date and time. Because you removed the quotation marks, the app interpreted the value as a function instead of a literal string. Use [functions in KratosApps]() to change how your app behaves.

1. In the Function Bar, type this expression:

	**Text(Value("123456"), "$#,#")**

	*Screen shot*

	The label shows the number in the quotation marks as a dollar value with a comma after the thousands digit. The expression combines the **Value** function with the **Text** function. The **Value** function converts the string between the quotation marks into a value, which KratosApps can format and use in mathematic operations. The **Text** function formats the value based on the symbols in the second set of quotation marks.

	**Note:** You could have gotten the same result by just typing **$123,456**. But labels often show input from other controls. For example, a user might specify a dollar value by using a slider. In that case, you could show the slider's value in a label but use the **Text** function to add the comma and the dollar sign.

## Show data from another control in a label ##
1. On the **Insert** tab, click **Text**, and then click **Input Text**.

	*Screen shot*

	An input-text box appears on the screen. Users can specify data by typing text into this box.

	*Screen shot*

1. Rename the new control **CityName**.

	*Screen shot*

2. Move **CityName** over **TestLabel**.

	*Screen shot*

3. Repeat the first three steps of this procedure, except name the control **StateName**.

	*Screen shot*

4. Set the **Text** property of **TestLabel** to this expression:

	**CityName!Text & StateName!Text**

	*Screen shot*

	This expression will concatenate the values of the **Text** properties of **CityName** and **StateName**.

1. Click **FirstNumber** to select it, double-click its default text, and then type a number, such as **46**.

	*Screen shot*

	In this step, you set the **Text** property of **FirstNumber**.

1. Set the **Text** property of **SecondNumber** to a number, such as **29**.

	**TestLabel** shows the sum of numbers that you specified in **FirstNumber** and **SecondNumber**
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

