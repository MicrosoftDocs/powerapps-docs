### Connect using the Plug-in Registration tool

1. Open the Plug-in Registration tool by executing the PAC CLI `pac tool prt` command.
1. Select **+Create new connection** to connect to your Dataverse environment.
1. Make sure **Office 365** is checked.
1. If you are connecting using a Microsoft account other than one you are currently using, select **Show Advanced** and enter your credentials. Otherwise, leave **Sign-in as current user** selected.
    > [!NOTE]
    > If your user account employs multifactor authentication (MFA), make sure the **Show Advanced** checkbox isn't checked.
1. If your Microsoft Account provides access to multiple environments, select **Display list of available organizations**.

    ![Logging in with the Plug-in registration tool.](../media/tutorial-write-plug-in-prt-login.png)

1. Select **Login**.
1. If you selected **Display list of available organizations**, select the organization you would like to connect to and select **Login**.
1. After you're connected, you'll see any existing registered plug-ins, custom workflow activities, and data providers.

    ![View existing plug-ins an custom workflow activities.](../media/tutorial-write-plug-in-view-existing-plug-ins.png)
