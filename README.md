# MCP Extensions Setup Guide

A step-by-step guide to install and configure MCP (Model Context Protocol) extensions in Claude Desktop, including File Systems, Windows-OS MCP, and Context7.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installing MCP Extensions](#installing-mcp-extensions)
- [Extension Setup](#extension-setup)
  - [File Systems Extension](#file-systems-extension)
  - [Windows-OS MCP Extension](#windows-os-mcp-extension)
  - [Context7 Extension](#context7-extension)
- [Managing Extensions](#managing-extensions)
- [Troubleshooting](#troubleshooting)
- [Usage Tips](#usage-tips)

## Overview

This guide walks you through installing MCP extensions in Claude Desktop application that enable:

- **File Systems**: Read, write, and manage files and directories on your computer
- **Windows-OS MCP**: Control Windows applications, automate UI interactions, and system operations
- **Context7**: Access up-to-date library documentation and coding resources

## Prerequisites

- **Claude Desktop Application** installed on your system
- **Windows OS** (required for Windows-MCP functionality)
- **Administrator privileges** (may be required for some extensions)

## Installing MCP Extensions

### Step 1: Open Claude Desktop Settings

1. Launch **Claude Desktop** application
2. Click on **File** in the menu bar
3. Select **Settings...** from the dropdown menu

   ![Settings Menu](images/settings-menu.png)

### Step 2: Navigate to Extensions

1. In the Settings window, click on the **Extensions** tab on the left sidebar
2. You'll see the Extensions browser interface

   ![Extensions Tab](images/extensions-tab.png)

### Step 3: Browse Available Extensions

1. The Extensions page will display available MCP extensions
2. You can browse by categories or search for specific extensions
3. Look for the following extensions:
   - **File Systems MCP**
   - **Windows-OS MCP** 
   - **Context7**

## Extension Setup

### File Systems Extension

#### Step 1: Install the Extension

1. In the Extensions browser, search for "**File Systems**" or "**Filesystem MCP**"
2. Click on the **File Systems MCP** extension card
3. Click the **Install** button
4. Wait for the installation to complete

#### Step 2: Configure File Access Permissions

1. After installation, click **Configure** next to the File Systems extension
2. Set up allowed directories:
   - Click **Add Directory** 
   - Browse and select folders you want Claude to access
   - Common choices:
     - `C:\Users\YourUsername\Documents`
     - `C:\Users\YourUsername\Desktop`
     - Your project folders
3. Set permissions:
   - ✅ **Read files** - Allow reading file contents
   - ✅ **Write files** - Allow creating and modifying files
   - ✅ **Create directories** - Allow folder creation
   - ⚠️ **Delete files** - Enable with caution
4. Click **Save Configuration**

#### Step 3: Test the Installation

1. Start a new conversation with Claude
2. Ask Claude to list files in one of your configured directories:
   ```
   Can you show me the files in my Documents folder?
   ```
3. Claude should now be able to access and display your files

### Windows-OS MCP Extension

#### Step 1: Install the Extension

1. Search for "**Windows MCP**" or "**Windows-OS**" in the Extensions browser
2. Click on the **Windows-OS MCP** extension
3. Click **Install**
4. You may be prompted to grant additional permissions - click **Allow**

#### Step 2: Configure Application Access

1. Click **Configure** for the Windows-OS MCP extension
2. Set up allowed applications:
   - Enable **Safe Mode** (recommended for beginners)
   - Add applications to the allowed list:
     - `notepad.exe`
     - `calc.exe` (Calculator)
     - `chrome.exe`
     - `firefox.exe`
     - Add other applications as needed
3. Configure automation settings:
   - ✅ **Launch Applications** - Allow starting programs
   - ✅ **UI Automation** - Allow clicking and typing
   - ✅ **Window Management** - Allow moving/resizing windows
   - ⚠️ **System Commands** - Enable with caution
4. Click **Save Configuration**

#### Step 3: Grant Windows Permissions

1. Windows may show a **User Account Control (UAC)** prompt
2. Click **Yes** to allow Claude to interact with Windows
3. You may need to add Claude Desktop to Windows Defender exceptions

#### Step 4: Test Windows Automation

1. Ask Claude to perform a simple task:
   ```
   Can you open Notepad and type "Hello World"?
   ```
2. Claude should be able to launch Notepad and type text

### Context7 Extension

#### Step 1: Install the Extension

1. Search for "**Context7**" in the Extensions browser
2. Click on the Context7 extension card
3. Click **Install**

#### Step 2: Set Up API Access

1. Click **Configure** for Context7
2. You'll need a Context7 API key:
   - Click **Get API Key** (this will open Context7 website)
   - Sign up for a free Context7 account
   - Copy your API key
3. Paste the API key in the configuration field
4. Configure settings:
   - **Token Limit**: 10000 (default)
   - **Cache Duration**: 1 hour
   - **Auto-resolve Libraries**: ✅ Enabled
5. Click **Save Configuration**

#### Step 3: Test Context7

1. Ask Claude about a programming library:
   ```
   Can you show me the latest React hooks documentation?
   ```
2. Claude should fetch and display current documentation from Context7

## Managing Extensions

### Viewing Installed Extensions

1. Go to **File** → **Settings** → **Extensions**
2. Click the **Installed** tab to see your active extensions
3. Each extension shows:
   - Status (Active/Inactive)
   - Version number
   - Last updated date

### Updating Extensions

1. In the **Installed** tab, look for extensions with update notifications
2. Click **Update** next to any extension that has available updates
3. Restart Claude Desktop if prompted

### Disabling/Enabling Extensions

1. In the **Installed** tab, find the extension you want to manage
2. Toggle the **Enable/Disable** switch
3. The extension will be activated or deactivated immediately

### Uninstalling Extensions

1. In the **Installed** tab, click on the extension you want to remove
2. Click **Uninstall**
3. Confirm the removal when prompted

## Troubleshooting

### Common Issues

#### Extensions Not Appearing

**Problem**: Can't see MCP extensions in the Extensions browser
**Solution**:
1. Check your internet connection
2. Restart Claude Desktop
3. Clear extension cache: **Settings** → **Advanced** → **Clear Extension Cache**

#### File Systems Extension Issues

**Problem**: "Permission denied" errors when accessing files
**Solution**:
1. Check your configured directories in extension settings
2. Ensure Claude Desktop has proper Windows permissions
3. Try running Claude Desktop as Administrator (temporarily)

**Problem**: Files not showing up
**Solution**:
1. Verify the folder path is correct
2. Check if the folder is in your allowed directories list
3. Refresh the extension: Disable and re-enable it

#### Windows-OS MCP Issues

**Problem**: Applications won't launch
**Solution**:
1. Add the application to your allowed list
2. Check if Windows Defender is blocking automation
3. Ensure UAC permissions were granted

**Problem**: UI automation not working
**Solution**:
1. Enable Safe Mode in extension settings
2. Make sure target applications are in focus
3. Try adding delays between actions

#### Context7 Issues

**Problem**: "Authentication failed" errors
**Solution**:
1. Verify your API key is correct
2. Check if your Context7 account is active
3. Try regenerating your API key

**Problem**: Library documentation not found
**Solution**:
1. Try different search terms for the library
2. Check if the library is supported by Context7
3. Clear Context7 cache in extension settings

### Getting Help

1. **Extension Logs**: **Settings** → **Advanced** → **View Extension Logs**
2. **Reset Extensions**: **Settings** → **Advanced** → **Reset All Extensions**
3. **Support**: Contact Claude support through the Help menu

## Usage Tips

### Best Practices

1. **Start Small**: Begin with simple tasks to test each extension
2. **Security First**: Only grant necessary permissions to extensions
3. **Regular Updates**: Keep extensions updated for best performance
4. **Monitor Usage**: Check extension logs if something isn't working

### Example Workflows

#### File Management Workflow
```
1. "Show me the files in my Desktop folder"
2. "Create a new folder called 'Projects' in Documents"
3. "Move the file 'report.txt' from Desktop to Documents/Projects"
```

#### Windows Automation Workflow
```
1. "Open Calculator"
2. "Calculate 15 * 24 using the calculator"
3. "Take a screenshot of the result"
```

#### Development Workflow
```
1. "Get the latest React documentation for useState hook"
2. "Create a new file called 'component.jsx' in my project folder"
3. "Write a React component using the useState examples"
```

### Performance Tips

- **Limit directory scope**: Only add folders you actually need
- **Use Safe Mode**: For Windows automation, especially when learning
- **Cache settings**: Adjust Context7 cache duration based on your needs
- **Regular cleanup**: Periodically review and remove unused extensions

## Changelog

### Latest Updates

- **File Systems v2.1**: Added support for symbolic links and improved error handling
- **Windows-OS MCP v1.8**: Enhanced UI automation and better application detection
- **Context7 v3.2**: Faster documentation retrieval and expanded library coverage

---

**Note**: Extension availability and features may vary based on your Claude Desktop version and subscription level. Some extensions may require premium access.
