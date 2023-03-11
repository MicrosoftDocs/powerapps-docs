The capability to create rules in canvas apps for automated app modification based on specified criteria will be removed. This feature was retired in 2019 and will now be fully removed.

You'll have a few months to convert the rules into expressions using a converter. If there are any rules remaining in your canvas app that haven't been converted by the end of this period, the system will perform the conversion automatically.

** Important**

Effective October 14, 2019, the rules feature in canvas apps is deprecated. More information: [**<u>Blog: Canvas Rules feature deprecation</u>**](https://powerapps.microsoft.com/blog/canvas-rules-feature-deprecation/).

**Convert rules**

When you edit an app that has rules, you'll receive a prompt to convert them. The converter assists in migrating the rules within your app to a format that is compatible with future versions of Power Apps Studio. By utilizing the rules conditions in your app, the converter substitutes the references with corresponding inline expressions.

Follow these steps to convert rules in your app:

1.  Open your app for editing and go to the the Rules panel.

2.  On the warning message, select **Convert rules**.

![](media/image1.png)

3.  On the **Convert rules** dialog box, select **Convert now**.

4.  A dialog opens which shows all the rules which will be converted. The rule name is shown on the left, and its associated conditional expression is shown on the right.

![A dialog window which says Covert rules  Rules in canvas apps will be removed in a future release  Converting them to expressions will ensure they  39](media/ll work in the future. It also shows a table with two columns, &quot.png "This rule&quot")

5.  Select **Convert now**

6.  When the conversion is complete, a notification appears to alert you whether the conversion was successful.

![A green notification banner which reads Rules converted successfully  ](media/image3.png)

7.  Formulas that previously referenced rule names have been updated to directly use their associated conditional expression instead.

| ![The power Fx formula bar showing a formula using rules  The formula reads If Rule2 Color DarkSeaGreen If Rule1 Color DarkRed RGBA 56 96 178 1   ](media/image4.png) | ![The power Fx formula bar showing a formula no longer using rules  The formula reads  If Slider1 Value  gt](media/ 50,Color.DarkSeaGreen,If(Slider1.Value &gt.png " 20,Color.DarkRed,RGBA(56,96,178,1)))") |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Before the conversion, the Power Fx formula references rule names in the formula in place of their associated conditional expressions.                                                                                         | After the conversion, rule name references have been removed and replaced. In this example, *Rule2* was converted to*Slider1.Value &gt; 50.*                                                                                                                             |

**Reverting the conversion**

When the conversion is done, the rules are converted to the corresponding expression. During the conversion period, you can revert your changes to bring the rules back to your app for review and troubleshooting if necessary. While in the same session, you can use the Undo button or Ctrl-Z to revert the rule conversion. If you save the app, you can restore the previous version to revert the change. However, you will be prompted to convert the rules again the next time the app is opened for editing.

**Known Issues**

If your rules are in an error state or are empty, they will be replaced with the following formula: Boolean(Blank()). This formula preserves the behavior of rules in this state.
