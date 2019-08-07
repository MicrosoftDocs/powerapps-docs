Using an on-premises data gateway in Power Platform Dataflows
=============================================================

Install an on-premises data gateway to transfer data quickly and securely
between a Power Platform dataflow and a data source that isn't in the cloud,
such as an on-premises SQL Server database or an on-premises SharePoint site.
You can view all gateways for which you have administrative permissions and
manage permissions and connections for those gateways.

With a gateway, you can connect to on-premises data through these connections:

-   SharePoint

-   SQL Server

-   Oracle

-   Informix

-   Filesystem

-   DB2

Prerequisites
-------------

-   The user name and password that you used to [sign
    up](https://docs.microsoft.com/en-us/powerapps/maker/signup-for-powerapps)
    for PowerApps.

-   Administrative permissions on a gateway. ( these permissions are provided by
    default for gateways you install and administrators can grant other people
    permissions for gateways they administrate. .)

-   A license that supports accessing on-premises data using an on-premises
    gateway. For more information, see the “Connectivity” section of the
    [pricing page](https://powerapps.microsoft.com/pricing/).

-   Gateways and on-premises connections can only be created and used in the
    user's [default
    environment](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/working-with-environments).

Install a gateway
-----------------

1.  In the left navigation bar of
    [powerapps.com](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc),
    click or tap **Gateways**.

![](media/d27b236e197f4ccaf9aeb24de70e2c73.png)

>   Gateways in left navigation bar

1.  If you don't have administrative permissions for a gateway, click or tap
    [Install a gateway now](http://go.microsoft.com/fwlink/?LinkID=820931) (or
    **New Gateway** in the upper-right corner), and then follow the prompts in
    the wizard that appears.

![](media/01588429c0d458281245ea5c8adf9d69.png)

>   Gateways Install

>   For details about how to install a gateway, see [Understand on-premises data
>   gateways](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/gateway-reference).

Using an on-premises data source in a dataflow
----------------------------------------------

When creating a dataflow, select an on-premises data source from the data
sources list, as shown in the following image.

![Choose an on-premises data source](media/35c03d95dc48563f27e5771ae2ee887d.png)

Once you make your selection, you're prompted to provide the connection details
for the Enterprise Gateway that will be used to access the on-premises data. You
must select the gateway itself, and provide credentials for the selected
gateway. Only gateways for which the user is an administrator appear in the
drop-down list.

![Provide connection details](media/fa2fcba5390b4c5c752852bc2157cfa9.png)

You can change the Enterprise Gateway used for a given dataflow in the authoring
tool:

**From the authoring tool** – you can change the gateway assigned to all of your
queries using the dataflow authoring tool.

>   **Note**

>   The dataflow will try to find or create the required data sources using the
>   new gateway. If it cannot do so, you will not be able to change the gateway
>   until all needed dataflows are available from the selected gateway.

Limitations
-----------

There are a few known limitations to using Enterprise Gateways and dataflows:

-   Each dataflow may use only one gateway. As such, all queries should be
    configured using the same gateway.

-   Changing the gateway impact the entire dataflow.

-   If several gateways are needed, the best practice is to build several
    dataflows (one for each gateway) and use the compute or entity reference
    capabilities to unify the data.

-   Dataflows are only supported using enterprise gateways. Personal gateways
    will not be available for selection in the drop down lists and settings
    screens.

**View and manage gateway permissions**

1.  In the left navigation bar of
    [powerapps.com](https://web.powerapps.com/?utm_source=padocs&utm_medium=linkinadoc&utm_campaign=referralsfromdoc),
    click or tap **Gateways**, and then click or tap a gateway.

2.  Add a user to a gateway by clicking or tapping **Users**, specifying a user
    or group, and then specifying a permission level:

    -   **Can use**: Users who can create connections on the gateway to use for
        apps and flows, but cannot share the gateway. Use this permission for
        users who will run apps but not share them.

    -   **Can use + share**: Users who can create a connection on the gateway to
        use for apps and flows, and automatically share the gateway when sharing
        an app. Use this permission for users who need to share apps with other
        users or with the organization.

    -   **Admin**: Administrators who have full control of the gateway,
        including adding users, setting permissions, creating connections to all
        available data sources, and deleting the gateway.

For **Can use** and **Can use + share** permission levels, select the data
sources that the user can connect to over the gateway.

**View and manage gateway connections**

1.  In the left navigation bar of *powerapps.com*, click on **Gateways**, and
    then choose the appropriate gateway.

2.  Click on**Connections**, and then click on a connection to view its details,
    edit the settings, or delete it.

3.  To share a connection, click or tap **Share**, and then add or remove users.

>   **Note**

>   You can share only some types of connections, such as SQL Server. For more
>   information, see [Share app
>   resources](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/share-app-resources).

For more information about how to manage a connection, see [Manage your
connections](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/add-manage-connections).

**Troubleshooting and Advanced Configuration**

For more information on troubleshooting issues with gateways, or configuring the
gateway service for your network, see [Understand on-premises data
gateways](https://docs.microsoft.com/en-us/powerapps/maker/canvas-apps/gateway-reference).

**Next steps**

-   [Creating and using dataflows in
    PowerApps](https://go.microsoft.com/fwlink/?linkid=2100076)

-   [Add data to an entity in Common Data
    Service](https://go.microsoft.com/fwlink/?linkid=2100075)

-   [Connect Azure Data Lake Storage Gen2 for dataflow
    storage](https://go.microsoft.com/fwlink/?linkid=2099973)
