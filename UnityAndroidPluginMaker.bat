echo off

SET FolderCY=D:\repo\MLDJClient\Version\Main\Project\Public\OtherTools\AndroidPlugin\360\CYMGChannelCY
SET FolderThird=D:\repo\MLDJClient\Version\Main\Project\Public\OtherTools\AndroidPlugin\360\CYMGChannelQihoo
SET FolderProject=D:\repo\MLDJClient\Version\Main\Project\Public\OtherTools\AndroidPlugin\360\MLDJ

SET FolderTarget="D:\repo\MLDJClient\Version\Main\Project\Client\AndroidPlugins\Android_360\"

:: clean target folder
IF EXIST %FolderTarget% RD /S/Q %FolderTarget%

:: copy res
XCOPY /Y/E/R %FolderCY%\res %FolderTarget%\res\
XCOPY /Y/E/R %FolderThird%\res %FolderTarget%\res\
XCOPY /Y/E/R %FolderProject%\res %FolderTarget%\res\

:: copy jar
XCOPY /Y/E/R %FolderCY%\libs %FolderTarget%
XCOPY /Y/E/R %FolderThird%\libs %FolderTarget%
XCOPY /Y/E/R %FolderProject%\libs %FolderTarget%
IF EXIST %FolderTarget%\unity-classes.jar DEL /S/Q %FolderTarget%\unity-classes.jar

:: generate jar file
IF EXIST %FolderProject%\plugin.jar DEL /S/Q %FolderProject%\plugin.jar
cd %FolderProject%\bin\classes
jar cvf %FolderProject%\plugin.jar *
XCOPY /Y/R %FolderProject%\plugin.jar %FolderTarget%
IF EXIST %FolderProject%\plugin.jar DEL /S/Q %FolderProject%\plugin.jar
ECHO %FolderProject%\plugin.jar

:: copy AndroidManifest.xml
XCOPY /Y/R %FolderProject%\AndroidManifest.xml %FolderTarget%

:: copy assets
XCOPY /Y/E/R %FolderProject%\assets %FolderTarget%\assets\

pause

