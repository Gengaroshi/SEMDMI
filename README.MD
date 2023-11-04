# SEModDownloader for Space Engineers - API

SEModDownloaderMod.io is a tool that allows you to download mods from Mod.io for the game Space Engineers. You need to add your API key to get started. Here are the steps:

1. **Create a Mod.io Profile**

   - First, you need to create a profile on the Mod.io website. Navigate to your profile settings, and under "Management" in the "API Access" section, you can generate your personal access key. Be sure to accept the terms and conditions.

2. **Add Your API Key**

   - Prior to using SEModDownloaderMod.io, you must insert your Mod.io API key into the `apikey.config` file. Follow these easy steps:
   
     - Open the `apikey.config` file.
     - Paste your Mod.io API key below the comment:
     
       ```
       # Paste your API key here
       YourApiKeyGoHere
       ```

3. **Running the Program**

   - Start the SEModDownloader program.

4. **Locate the Mod ID and Download**

   - After launching the program, you'll need to find the Mod ID of the mod you want to download.
   - Enter the Mod ID in the dedicated field.
   - Click the "Download Files" button.
   - The program will automatically download your selected mods to the "Downloaded Files" folder, situated within the application directory.

   - Alternatively, you can locate the mod's ID on the Mod's page. Examine your browser's URL; the ID is the number that appears at the end of the URL following "mods." For instance:

https://mod.io/spaceengineers/mods/123456

In this example, the mod's ID is 123456.

**Note:**

This program is designed to simplify mod downloads and can be customized to meet your specific requirements. If you need assistance with configurations or have any usage-related queries, please don't hesitate to reach out to us.

All informations by official api methods: https://docs.mod.io/?python#delete-mod
