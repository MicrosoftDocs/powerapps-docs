A literal string or a formula that evaluates to a string that appears on a control such as a text box or a button.

You can set the value of this property in multiple ways:

- Double-click the text that the control already shows (or triple-click the text if it contains spaces) and then type the exact text that you want.
- Select the control, select **Text** on the **Content** tab or in the properties list, and then type a literal string or a formula in the formula bar.
- Select the control, select **Advanced** on the **View** tab, and then type a literal string or a formula in the **Text** field (under **Data**) of the **Advanced** pane.

For example, you can type a literal string such as **"Hello, world!"** in the formula bar, and the control will show exactly what you typed between the quotation marks. As an alternative, you can type a formula such as **Today()** without quotation marks, and the control will show the result of the formula (in this case, the current date formatted as *mm*/*dd*/*yyyy*).

[Format dates, times, currency, and other strings](function-text.md).

In many cases, you'll set the **Text** property of a text box in a gallery to show data from a table column. For example, you might show address data in a gallery and set the **Text** property of a text box to **ThisItem.City** so that the control shows the name of the city for each address.
