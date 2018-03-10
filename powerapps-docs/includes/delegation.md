## Delegation
When possible, PowerApps will delegate filter and sort operations to the data source and page through the results on demand. For example, when you start an app that shows a **[Gallery](../maker/canvas-apps/controls/control-gallery.md)** control filled with data, only the first set of records will be initially brought to the device. As the user scrolls, additional data is brought down from the data source. The result is a faster start time for the app and access to very large data sets.

However, delegation may not always be possible. Data sources vary on what functions and operators they support with delegation. If complete delegation of a formula isn't possible, the authoring environment will flag the portion that can't be delegated with a warning. When possible, consider changing the formula to avoid functions and operators that can't be delegated.  The [delegation list](../maker/canvas-apps/delegation-list.md) details which data sources and operations can be delegated.

If delegation is not possible, PowerApps will pull down only a small set of records to work on locally. Filter and sort functions will operate on a reduced set of records. What is available in the **[Gallery](../maker/canvas-apps/controls/control-gallery.md)** may not be the complete story, which could be confusing to users. 

See the [delegation overview](../maker/canvas-apps/delegation-overview.md) for more information.

